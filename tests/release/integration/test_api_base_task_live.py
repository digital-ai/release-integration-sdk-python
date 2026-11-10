"""
ApiBaseTask helpers against a real Digital.ai Release server.

The server defaults to the developer instance on localhost:5516 with
admin/admin; override with RELEASE_LIVE_URL, RELEASE_LIVE_USER and
RELEASE_LIVE_PASSWORD. The module is skipped when the server is unreachable or
rejects the credentials, so CI (which has no server) skips it.

A module-scoped fixture creates a folder, a template with a phase and a task,
release/folder/global variables, and a release from the template, then deletes
them afterwards. Tests that read a variable and tests that write one use
different variables, so the tests do not depend on each other's order.
"""
import os
import socket
import uuid
from datetime import datetime, timezone
from types import SimpleNamespace
from urllib.parse import urlparse

import pytest
from com.xebialabs.xlrelease.api.v1.configuration_api import ConfigurationApi
from com.xebialabs.xlrelease.api.v1.folder_api import FolderApi
from com.xebialabs.xlrelease.api.v1.phase_api import PhaseApi
from com.xebialabs.xlrelease.api.v1.release_api import ReleaseApi
from com.xebialabs.xlrelease.api.v1.task_api import TaskApi
from com.xebialabs.xlrelease.api.v1.template_api import TemplateApi
from com.xebialabs.xlrelease.domain.folder import Folder
from com.xebialabs.xlrelease.domain.forms import CreateRelease
from com.xebialabs.xlrelease.domain.phase import Phase
from com.xebialabs.xlrelease.domain.release import Release
from com.xebialabs.xlrelease.domain.task import Task
from com.xebialabs.xlrelease.domain.variable import Variable

from digitalai.release.integration.api_base_task import ApiBaseTask
from digitalai.release.integration.input_context import AutomatedTaskAsUserContext, ReleaseContext
from digitalai.release.release_api_client import ReleaseAPIClient

pytestmark = pytest.mark.live

SERVER_URL = os.getenv("RELEASE_LIVE_URL", "http://localhost:5516")
USERNAME = os.getenv("RELEASE_LIVE_USER", "admin")
PASSWORD = os.getenv("RELEASE_LIVE_PASSWORD", "admin")
# (connect, read) seconds, so an unresponsive server fails fast instead of hanging.
TIMEOUT = (3.05, 10)

PHASE_TITLE = "Test Phase"
TASK_TITLE = "Manual Task"


def server_reachable() -> bool:
    url = urlparse(SERVER_URL)
    port = url.port or (443 if url.scheme == "https" else 80)
    try:
        with socket.create_connection((url.hostname, port), timeout=0.5):
            return True
    except OSError:
        return False


if not server_reachable():
    pytest.skip(f"no Release server reachable at {SERVER_URL}", allow_module_level=True)


class LiveApiTask(ApiBaseTask):
    def execute(self) -> None:
        pass


def as_instant(value) -> datetime:
    """A date variable value as an aware datetime; the server may format it with 'Z' or its own offset."""
    return datetime.fromisoformat(str(value).replace("Z", "+00:00"))


def same_value(actual, expected) -> bool:
    """Compares variable values; a set variable comes back as a list in server order."""
    if isinstance(expected, list):
        return set(actual) == set(expected)
    return actual == expected


def new_variable(vtype, key, value=None, **extra):
    return Variable(type=vtype, key=key, value=value, requiresValue=False, showOnReleaseStart=False, **extra)


# Release variables seeded on the template: key -> (type, value).
RELEASE_VARIABLES = {
    "relVar": ("xlrelease.StringVariable", "release-value"),
    "relSetVar": ("xlrelease.SetStringVariable", ["Apples", "Pears"]),
    "relListVar": ("xlrelease.ListStringVariable", ["second", "first"]),
    "relMapVar": ("xlrelease.MapStringStringVariable", {"env": "dev", "region": "us"}),
    "relDateVar": ("xlrelease.DateVariable", "2026-01-02T03:04:05+00:00"),
    # Written by the setter tests; never read by the getter tests.
    "relVarRw": ("xlrelease.StringVariable", "initial"),
    "relSetVarRw": ("xlrelease.SetStringVariable", ["initial"]),
    "relListVarRw": ("xlrelease.ListStringVariable", ["initial"]),
    "relMapVarRw": ("xlrelease.MapStringStringVariable", {"initial": "yes"}),
    "relDateVarRw": ("xlrelease.DateVariable", "2026-01-02T03:04:05+00:00"),
}


class Cleanup:
    """Deletes what the fixture created, best effort, in reverse dependency order."""

    def __init__(self, client):
        self.client = client
        self.release_id = None
        self.template_id = None
        self.folder_id = None
        self.global_variable_ids = []

    def run(self):
        steps = []
        if self.release_id:
            steps += [lambda: ReleaseApi(self.client).abort(self.release_id, "Test cleanup"),
                      lambda: ReleaseApi(self.client).delete(self.release_id)]
        if self.template_id:
            steps.append(lambda: TemplateApi(self.client).deleteTemplate(self.template_id))
        steps += [lambda v=v: ConfigurationApi(self.client).deleteGlobalVariable(v) for v in self.global_variable_ids]
        if self.folder_id:
            # Deleting the folder also removes anything still inside it.
            steps.append(lambda: FolderApi(self.client).delete(self.folder_id))
        for step in steps:
            try:
                step()
            except Exception:  # noqa: BLE001 - keep cleaning up
                pass


@pytest.fixture(scope="module")
def live():
    client = ReleaseAPIClient(SERVER_URL, USERNAME, PASSWORD, timeout=TIMEOUT)
    try:
        root_folders = FolderApi(client).listRoot()
    except Exception as exc:  # noqa: BLE001 - any failure here means "no usable server"
        client.close()
        pytest.skip(f"Release server at {SERVER_URL} rejected the API check: {exc}")
    if not root_folders:
        client.close()
        pytest.skip("Release server has no root folder to create test data in")

    uid = uuid.uuid4().hex[:10]
    cleanup = Cleanup(client)
    try:
        yield create_test_data(client, cleanup, uid, root_folders[0].id)
    finally:
        cleanup.run()
        client.close()


def create_test_data(client, cleanup, uid, root_folder_id):
    folder_api, template_api = FolderApi(client), TemplateApi(client)
    config_api = ConfigurationApi(client)

    folder_title = f"AbtLiveFolder_{uid}"
    folder_id = folder_api.addFolder(root_folder_id, Folder(title=folder_title)).id
    cleanup.folder_id = folder_id

    template_title = f"AbtLiveTemplate_{uid}"
    response = client.post("/api/v1/templates", json={
        "id": f"Applications/Release_abt_live_{uid}",
        "title": template_title,
        "type": "xlrelease.Release",
        "status": "TEMPLATE",
        "scheduledStartDate": "2026-06-01T00:00:00+00:00",
        "dueDate": "2026-07-01T00:00:00+00:00",
    })
    response.raise_for_status()
    root_template_id = Release.from_dict(response.json()).id
    cleanup.template_id = root_template_id

    phase = PhaseApi(client).addPhase(root_template_id, Phase(title=PHASE_TITLE, type="xlrelease.Phase"))
    TaskApi(client).addTask(phase.id, Task(title=TASK_TITLE, type="xlrelease.Task"))
    for key, (vtype, value) in RELEASE_VARIABLES.items():
        template_api.createVariable(root_template_id, new_variable(vtype, key, value))
    # A reference variable holds no literal value: the server resolves it from a value provider.
    template_api.createVariable(root_template_id, new_variable(
        "xlrelease.ReferenceVariable", "relRefVar", referencedType="xlrelease.StringVariable"))

    # Releases created from a template inside the folder live in that folder.
    folder_api.moveTemplate(folder_id, root_template_id)
    template_id = next(t.id for t in folder_api.getTemplates(folder_id) if t.title == template_title)
    cleanup.template_id = template_id

    for key, value in (("folder.folderVar", "folder-value"), ("folder.folderVarRw", "initial")):
        folder_api.createVariable(folder_id, new_variable("xlrelease.StringVariable", key, value))

    global_names = {}
    for name, value in (("read", "global-value"), ("rw", "initial")):
        key = f"global.abtLive_{name}_{uid}"
        created = config_api.addGlobalVariable(new_variable("xlrelease.StringVariable", key, value))
        cleanup.global_variable_ids.append(created.id)
        global_names[name] = key

    release_title = f"AbtLiveRelease_{uid}"
    release_id = template_api.create(template_id, CreateRelease(releaseTitle=release_title)).id
    cleanup.release_id = release_id
    task_id = TaskApi(client).searchTasksByTitle(TASK_TITLE, release_id)[0].id

    task = LiveApiTask()
    task.release_server_url = SERVER_URL
    task.release_context = ReleaseContext(
        id=release_id, automated_task_as_user=AutomatedTaskAsUserContext(username=USERNAME, password=PASSWORD))
    task.task_id = task_id

    return SimpleNamespace(task=task, uid=uid, folder_id=folder_id, folder_title=folder_title,
                           release_id=release_id, release_title=release_title, task_id=task_id,
                           global_read=global_names["read"], global_rw=global_names["rw"], cleanup=cleanup)


# -- server and current context --------------------------------------------

def test_get_version_returns_the_server_version(live):
    version = live.task.getVersion()

    assert isinstance(version, str) and version


def test_get_current_release(live):
    release = live.task.getCurrentRelease()

    assert (release.id, release.title) == (live.release_id, live.release_title)


def test_get_current_task(live):
    task = live.task.getCurrentTask()

    assert (task.id, task.title) == (live.task_id, TASK_TITLE)


def test_get_current_phase(live):
    phase = live.task.getCurrentPhase()

    assert (phase.id, phase.title) == (live.task.get_phase_id(), PHASE_TITLE)


def test_get_current_folder(live):
    folder = live.task.getCurrentFolder()

    assert (folder.id, folder.title) == (live.folder_id, live.folder_title)


# -- release variables -----------------------------------------------------

@pytest.mark.parametrize("key, expected", [
    ("relVar", "release-value"),
    ("relListVar", ["second", "first"]),
    ("relMapVar", {"env": "dev", "region": "us"}),
])
def test_get_release_variable(live, key, expected):
    assert live.task.getReleaseVariable(key) == expected


def test_get_release_set_variable_returns_its_members(live):
    assert set(live.task.getReleaseVariable("relSetVar")) == {"Apples", "Pears"}


def test_get_release_date_variable_returns_the_stored_instant(live):
    assert as_instant(live.task.getReleaseVariable("relDateVar")) == datetime(2026, 1, 2, 3, 4, 5,
                                                                               tzinfo=timezone.utc)


def test_get_release_reference_variable_returns_the_server_resolved_value(live):
    resolved = live.task.releaseApi.getVariableValues(live.release_id)

    assert "${relRefVar}" in resolved
    assert live.task.getReleaseVariable("relRefVar") == resolved["${relRefVar}"]


def test_get_release_variable_raises_for_an_unknown_name(live):
    with pytest.raises(KeyError):
        live.task.getReleaseVariable("doesNotExist")


@pytest.mark.parametrize("key, value", [
    ("relVarRw", "updated"),
    ("relListVarRw", ["b", "a", "b"]),  # a list keeps its order and duplicates
    ("relMapVarRw", {"env": "prod", "tier": "gold"}),
])
def test_set_release_variable_persists_the_value(live, key, value):
    updated = live.task.setReleaseVariable(key, value)

    assert updated.value == value
    assert live.task.getReleaseVariable(key) == value


def test_set_release_set_variable_persists_the_members(live):
    members = ["Oranges", "Bananas", "Grapes"]

    updated = live.task.setReleaseVariable("relSetVarRw", members)

    assert set(updated.value) == set(members)
    assert set(live.task.getReleaseVariable("relSetVarRw")) == set(members)


@pytest.mark.parametrize("value", [
    datetime(2027, 7, 8, 9, 10, 11, tzinfo=timezone.utc),
    datetime.now(timezone.utc).replace(microsecond=0),
], ids=["fixed", "now"])
def test_set_release_date_variable_persists_the_instant(live, value):
    updated = live.task.setReleaseVariable("relDateVarRw", value)

    assert as_instant(updated.value) == value
    assert as_instant(live.task.getReleaseVariable("relDateVarRw")) == value


@pytest.mark.parametrize("value, vtype", [
    ("created-value", "xlrelease.StringVariable"),
    (["red", "green"], "xlrelease.SetStringVariable"),
    ({"stage": "qa"}, "xlrelease.MapStringStringVariable"),
], ids=["string", "set", "map"])
def test_set_release_variable_creates_a_missing_variable(live, value, vtype):
    key = f"relNew_{vtype.split('.')[1]}"

    created = live.task.setReleaseVariable(key, value)

    assert (created.key, created.type) == (key, vtype)
    assert same_value(live.task.getReleaseVariable(key), value)


# -- folder variables ------------------------------------------------------

def test_get_folder_variable(live):
    assert live.task.getFolderVariable("folder.folderVar") == "folder-value"


def test_set_folder_variable_persists_the_value(live):
    updated = live.task.setFolderVariable("folder.folderVarRw", "updated")

    assert updated.value == "updated"
    assert live.task.getFolderVariable("folder.folderVarRw") == "updated"


@pytest.mark.parametrize("value, vtype", [
    ("folder-created", "xlrelease.StringVariable"),
    (["alpha", "beta"], "xlrelease.SetStringVariable"),
    ({"team": "infra"}, "xlrelease.MapStringStringVariable"),
], ids=["string", "set", "map"])
def test_set_folder_variable_creates_a_missing_variable(live, value, vtype):
    key = f"folder.new_{vtype.split('.')[1]}"

    created = live.task.setFolderVariable(key, value)

    assert (created.key, created.type) == (key, vtype)
    assert same_value(live.task.getFolderVariable(key), value)


# -- global variables ------------------------------------------------------

def test_get_global_variable(live):
    assert live.task.getGlobalVariable(live.global_read) == "global-value"


def test_set_global_variable_persists_the_value(live):
    updated = live.task.setGlobalVariable(live.global_rw, "updated")

    assert updated.value == "updated"
    assert live.task.getGlobalVariable(live.global_rw) == "updated"


@pytest.mark.parametrize("value, vtype", [
    ("global-created", "xlrelease.StringVariable"),
    (["x", "y"], "xlrelease.SetStringVariable"),
    ({"region": "ap"}, "xlrelease.MapStringStringVariable"),
], ids=["string", "set", "map"])
def test_set_global_variable_creates_a_missing_variable(live, value, vtype):
    key = f"global.abtLiveNew_{vtype.split('.')[1]}_{live.uid}"

    created = live.task.setGlobalVariable(key, value)
    live.cleanup.global_variable_ids.append(created.id)

    assert (created.key, created.type) == (key, vtype)
    assert same_value(live.task.getGlobalVariable(key), value)


# -- search by title -------------------------------------------------------

def test_get_phases_by_title_searches_the_current_release(live):
    phases = live.task.getPhasesByTitle(PHASE_TITLE)

    assert phases and all(p.title == PHASE_TITLE for p in phases)


@pytest.mark.parametrize("phase_title", [None, PHASE_TITLE], ids=["release-wide", "in-phase"])
def test_get_tasks_by_title_finds_the_current_task(live, phase_title):
    tasks = live.task.getTasksByTitle(TASK_TITLE, phase_title)

    assert live.task_id in [t.id for t in tasks]


def test_get_releases_by_title_finds_the_current_release(live):
    releases = live.task.getReleasesByTitle(live.release_title)

    assert live.release_id in [r.id for r in releases]

