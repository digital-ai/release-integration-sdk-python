"""
Live integration tests for :class:`ApiBaseTask`.

These tests run against a *real* Digital.ai Release server (by default the
developer instance on ``localhost:5516`` with ``admin``/``admin``). They build
an ``ApiBaseTask`` wired exactly the way the Release runtime wires it -- a task
context carrying the release id, the task id and the "Run as user" credentials
-- and then exercise the convenience helpers (``getCurrent*``, ``get*ByTitle``,
the variable getters/setters and ``getVersion``) end to end.

The suite is fully self-contained:

* ``setUpClass`` first verifies the server is reachable, authentication works
  and the API responds within a bounded timeout. If any of those checks fail
  the whole suite is skipped (CI has no Release server).
* It then creates every prerequisite object -- a folder, a template (moved into
  that folder), a phase, a task, and release/folder/global variables -- and
  spins up a release from the template so the task context points at real ids.
* ``tearDownClass`` removes everything again; deleting the folder cascades to
  the release and template, so the server is returned to its original state.
"""

import socket
import unittest
import uuid

from digitalai.release.release_api_client import ReleaseAPIClient
from digitalai.release.integration.api_base_task import ApiBaseTask
from digitalai.release.integration.input_context import (
    AutomatedTaskAsUserContext,
    ReleaseContext,
)

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


# Live server connection details. Locally this is the developer's instance;
# CI has no such server, so the suite skips itself when it is not reachable.
LIVE_SERVER_HOST = "localhost"
LIVE_SERVER_PORT = 5516
LIVE_SERVER_URL = f"http://{LIVE_SERVER_HOST}:{LIVE_SERVER_PORT}"
LIVE_SERVER_USER = "admin"
LIVE_SERVER_PASSWORD = "admin"

# Bounded timeout (connect, read) so an unresponsive server skips rather than
# hangs the suite.
LIVE_SERVER_TIMEOUT = (3.05, 10)


def _server_reachable(host: str, port: int, timeout: float = 0.5) -> bool:
    """Return True if a TCP connection to host:port succeeds within the timeout."""
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except OSError:
        return False


class _LiveApiTask(ApiBaseTask):
    """Concrete ApiBaseTask used to drive the helpers against the live server."""

    def execute(self) -> None:  # pragma: no cover - never executed by the tests
        pass


@unittest.skipUnless(
    _server_reachable(LIVE_SERVER_HOST, LIVE_SERVER_PORT),
    f"live Release server not available on {LIVE_SERVER_HOST}:{LIVE_SERVER_PORT}",
)
class TestApiBaseTaskLive(unittest.TestCase):
    """Live integration tests for the ApiBaseTask convenience helpers."""

    # Populated by setUpClass; defaults keep tearDownClass safe if setup aborts.
    client = None
    uid = None
    folder_id = None
    folder_title = None
    template_id = None
    release_id = None
    release_title = None
    task_id = None
    global_var_id = None
    global_var_name = None
    # Global variables created by the "create when missing" tests; tracked here so
    # _cleanup can delete them (they live outside the folder, so the folder-delete
    # cascade does not remove them).
    created_global_var_ids = []
    task = None

    # -- lifecycle ----------------------------------------------------------

    @classmethod
    def setUpClass(cls):
        uid = uuid.uuid4().hex[:10]
        cls.uid = uid
        cls.created_global_var_ids = []
        cls.client = ReleaseAPIClient(
            LIVE_SERVER_URL,
            LIVE_SERVER_USER,
            LIVE_SERVER_PASSWORD,
            timeout=LIVE_SERVER_TIMEOUT,
        )

        # Skip gate: verify authentication works and the API responds. Any
        # failure here (auth error, timeout, unreachable) skips the whole suite.
        folder_api = FolderApi(cls.client)
        try:
            root_folders = folder_api.listRoot()
            if not root_folders:
                raise unittest.SkipTest("No root folders available on the server.")
        except unittest.SkipTest:
            raise
        except Exception as exc:  # noqa: BLE001 - any failure means "skip"
            raise unittest.SkipTest(
                f"Release server authentication/API check failed: {exc}"
            )

        try:
            cls._create_test_data(uid, root_folders[0].id)
        except Exception:
            # Clean up whatever was created before re-raising; unittest does not
            # call tearDownClass when setUpClass fails.
            cls._cleanup()
            raise

        # Build the ApiBaseTask exactly as the Release runtime would: server URL
        # + "Run as user" credentials + the real release and task ids.
        cls.task = _LiveApiTask()
        cls.task.release_server_url = LIVE_SERVER_URL
        cls.task.release_context = ReleaseContext(
            id=cls.release_id,
            automated_task_as_user=AutomatedTaskAsUserContext(
                username=LIVE_SERVER_USER, password=LIVE_SERVER_PASSWORD
            ),
        )
        cls.task.task_id = cls.task_id
        print(f"Live ApiBaseTask wired to release {cls.release_id}")

    @classmethod
    def _create_test_data(cls, uid: str, root_id: str):
        """Create the folder/template/release/variables the helpers operate on."""
        template_api = TemplateApi(cls.client)
        folder_api = FolderApi(cls.client)
        phase_api = PhaseApi(cls.client)
        task_api = TaskApi(cls.client)
        config_api = ConfigurationApi(cls.client)

        # Folder (under root) that will contain the release.
        cls.folder_title = f"AbtLiveFolder_{uid}"
        folder = folder_api.addFolder(root_id, Folder(title=cls.folder_title))
        cls.folder_id = folder.id
        print(f"Created folder: {cls.folder_id}")

        # Template at root with a phase, a manual task and a release variable.
        template_title = f"AbtLiveTemplate_{uid}"
        payload = {
            "id": f"Applications/Release_abt_live_{uid}",
            "title": template_title,
            "type": "xlrelease.Release",
            "status": "TEMPLATE",
            "scheduledStartDate": "2026-06-01T00:00:00+00:00",
            "dueDate": "2026-07-01T00:00:00+00:00",
        }
        response = cls.client.post("/api/v1/templates", json=payload)
        response.raise_for_status()
        root_template = Release.from_dict(response.json())

        phase = phase_api.addPhase(
            root_template.id, Phase(title="Test Phase", type="xlrelease.Phase")
        )
        task_api.addTask(phase.id, Task(title="Manual Task", type="xlrelease.Task"))
        template_api.createVariable(
            root_template.id,
            Variable(
                type="xlrelease.StringVariable",
                key="relVar",
                value="release-value",
                requiresValue=False,
                showOnReleaseStart=False,
            ),
        )
        # A set (set-of-string) release variable; its value round-trips as a list.
        template_api.createVariable(
            root_template.id,
            Variable(
                type="xlrelease.SetStringVariable",
                key="relSetVar",
                value=["Apples", "Pears"],
                requiresValue=False,
                showOnReleaseStart=False,
            ),
        )
        # A key/value-map release variable; its value round-trips as a dict.
        template_api.createVariable(
            root_template.id,
            Variable(
                type="xlrelease.MapStringStringVariable",
                key="relMapVar",
                value={"env": "dev", "region": "us"},
                requiresValue=False,
                showOnReleaseStart=False,
            ),
        )
        # A reference release variable. It holds no literal value -- the server
        # resolves it from a value provider -- so getReleaseVariable must read
        # its value from the server-resolved value map rather than `.value`.
        template_api.createVariable(
            root_template.id,
            Variable(
                type="xlrelease.ReferenceVariable",
                key="relRefVar",
                referencedType="xlrelease.StringVariable",
                requiresValue=False,
                showOnReleaseStart=False,
            ),
        )

        # Move the template into the folder so releases created from it live
        # inside the folder (required for getCurrentFolder to resolve).
        folder_api.moveTemplate(cls.folder_id, root_template.id)
        moved = [
            t for t in folder_api.getTemplates(cls.folder_id)
            if t.title == template_title
        ]
        if not moved:
            raise RuntimeError("Template not found in folder after move.")
        cls.template_id = moved[0].id
        print(f"Created template in folder: {cls.template_id}")

        # A folder-owned variable.
        folder_api.createVariable(
            cls.folder_id,
            Variable(
                type="xlrelease.StringVariable",
                key="folder.folderVar",
                value="folder-value",
                requiresValue=False,
                showOnReleaseStart=False,
            ),
        )

        # A global variable (lives outside the folder; deleted explicitly later).
        cls.global_var_name = f"abtLiveGlobal_{uid}"
        global_var = config_api.addGlobalVariable(
            Variable(
                type="xlrelease.StringVariable",
                key=f"global.{cls.global_var_name}",
                value="global-value",
                requiresValue=False,
                showOnReleaseStart=False,
            )
        )
        cls.global_var_id = global_var.id
        print(f"Created global variable: {cls.global_var_id}")

        # Create the release from the template; it inherits the phase, task and
        # release variable, and lives inside the folder.
        cls.release_title = f"AbtLiveRelease_{uid}"
        release = template_api.create(
            cls.template_id, CreateRelease(releaseTitle=cls.release_title)
        )
        cls.release_id = release.id
        print(f"Created release: {cls.release_id}")

        # Resolve the task id of the release's manual task -> the task context.
        tasks = task_api.searchTasksByTitle("Manual Task", cls.release_id)
        if not tasks:
            raise RuntimeError("Manual Task not found in created release.")
        cls.task_id = tasks[0].id
        print(f"Resolved task id: {cls.task_id}")

    @classmethod
    def _cleanup(cls):
        """Best-effort removal of every object created by the suite."""
        client = cls.client
        if client is None:
            return

        if cls.release_id:
            release_api = ReleaseApi(client)
            try:
                release_api.abort(cls.release_id, "Aborting for test cleanup")
            except Exception:
                pass
            try:
                release_api.delete(cls.release_id)
            except Exception:
                pass

        if cls.template_id:
            try:
                TemplateApi(client).deleteTemplate(cls.template_id)
            except Exception:
                pass

        if cls.global_var_id:
            try:
                ConfigurationApi(client).deleteGlobalVariable(cls.global_var_id)
            except Exception:
                pass

        # Global variables created by the "create when missing" tests.
        for var_id in cls.created_global_var_ids:
            try:
                ConfigurationApi(client).deleteGlobalVariable(var_id)
            except Exception:
                pass

        # Deleting the folder cascades to anything still inside it (release,
        # template), so this is the catch-all that restores the server state.
        if cls.folder_id:
            try:
                FolderApi(client).delete(cls.folder_id)
            except Exception:
                pass

    @classmethod
    def tearDownClass(cls):
        cls._cleanup()

    # -- getVersion ---------------------------------------------------------

    def test_01_get_version(self):
        """getVersion returns the server's version string."""
        version = self.task.getVersion()
        self.assertIsInstance(version, str)
        self.assertTrue(version)
        print(f"getVersion -> {version}")

    # -- getCurrent* --------------------------------------------------------

    def test_02_get_current_release(self):
        """getCurrentRelease returns the release the task belongs to."""
        release = self.task.getCurrentRelease()
        self.assertEqual(release.id, self.release_id)
        self.assertEqual(release.title, self.release_title)
        print(f"getCurrentRelease -> {release.title}")

    def test_03_get_current_task(self):
        """getCurrentTask returns the task running the code."""
        task = self.task.getCurrentTask()
        self.assertEqual(task.id, self.task_id)
        self.assertEqual(task.title, "Manual Task")
        print(f"getCurrentTask -> {task.title}")

    def test_04_get_current_phase(self):
        """getCurrentPhase returns the phase that contains the task."""
        phase = self.task.getCurrentPhase()
        self.assertEqual(phase.id, self.task.get_phase_id())
        self.assertEqual(phase.title, "Test Phase")
        print(f"getCurrentPhase -> {phase.title}")

    def test_05_get_current_folder(self):
        """getCurrentFolder returns the folder that contains the release."""
        folder = self.task.getCurrentFolder()
        self.assertEqual(folder.id, self.folder_id)
        self.assertEqual(folder.title, self.folder_title)
        print(f"getCurrentFolder -> {folder.title}")

    # -- release variables --------------------------------------------------

    def test_06_get_release_variable(self):
        """getReleaseVariable returns the value of a current-release variable."""
        value = self.task.getReleaseVariable("relVar")
        self.assertEqual(value, "release-value")
        print(f"getReleaseVariable('relVar') -> {value}")

    def test_07_set_release_variable(self):
        """setReleaseVariable persists a new value, readable back via the getter."""
        updated = self.task.setReleaseVariable("relVar", "release-value-updated")
        self.assertEqual(updated.value, "release-value-updated")
        self.assertEqual(
            self.task.getReleaseVariable("relVar"), "release-value-updated"
        )
        print("setReleaseVariable('relVar') -> release-value-updated")

    def test_08_get_release_variable_missing_raises(self):
        """getReleaseVariable raises KeyError for an unknown variable name."""
        with self.assertRaises(KeyError):
            self.task.getReleaseVariable("doesNotExist")
        print("getReleaseVariable(unknown) correctly raised KeyError")

    # -- release variables: set (set-of-string) -----------------------------

    def test_08a_get_release_set_variable(self):
        """getReleaseVariable returns a set variable's value as a list."""
        value = self.task.getReleaseVariable("relSetVar")
        # A set is unordered on the server, so compare membership, not order.
        self.assertEqual(set(value), {"Apples", "Pears"})
        print(f"getReleaseVariable('relSetVar') -> {value}")

    def test_08b_set_release_set_variable(self):
        """setReleaseVariable persists a new set value, readable back via the getter."""
        new_value = ["Oranges", "Bananas", "Grapes"]
        updated = self.task.setReleaseVariable("relSetVar", new_value)
        self.assertEqual(set(updated.value), set(new_value))
        self.assertEqual(
            set(self.task.getReleaseVariable("relSetVar")), set(new_value)
        )
        print(f"setReleaseVariable('relSetVar') -> {new_value}")

    # -- release variables: key/value map -----------------------------------

    def test_08c_get_release_map_variable(self):
        """getReleaseVariable returns a key/value-map variable's value as a dict."""
        value = self.task.getReleaseVariable("relMapVar")
        self.assertEqual(value, {"env": "dev", "region": "us"})
        print(f"getReleaseVariable('relMapVar') -> {value}")

    def test_08d_set_release_map_variable(self):
        """setReleaseVariable persists a new map value, readable back via the getter."""
        new_value = {"env": "prod", "region": "eu", "tier": "gold"}
        updated = self.task.setReleaseVariable("relMapVar", new_value)
        self.assertEqual(updated.value, new_value)
        self.assertEqual(self.task.getReleaseVariable("relMapVar"), new_value)
        print(f"setReleaseVariable('relMapVar') -> {new_value}")

    # -- release variables: reference ---------------------------------------

    def test_08h_get_release_reference_variable(self):
        """getReleaseVariable returns a reference variable's server-resolved value.

        A reference variable carries no literal value (``.value`` is empty); the
        getter must read it from the resolved value map. The reference here has
        no real provider target, so it resolves to an empty string -- but the
        getter must return exactly what the resolved map holds for ``${key}``,
        proving it delegates resolution to the server rather than returning the
        raw (empty) ``.value``.
        """
        resolved = self.task.releaseApi.getVariableValues(self.release_id)
        expected = resolved.get("${relRefVar}")
        self.assertIsNotNone(expected, "reference variable missing from value map")
        self.assertEqual(self.task.getReleaseVariable("relRefVar"), expected)
        print(f"getReleaseVariable('relRefVar') -> {expected!r} (server-resolved)")

    # -- release variables: create when missing -----------------------------

    def test_08e_set_release_variable_creates_when_missing(self):
        """setReleaseVariable creates a string variable when the key is unknown."""
        created = self.task.setReleaseVariable("relNewVar", "created-value")
        self.assertEqual(created.key, "relNewVar")
        self.assertEqual(created.type, "xlrelease.StringVariable")
        self.assertEqual(created.value, "created-value")
        self.assertEqual(self.task.getReleaseVariable("relNewVar"), "created-value")
        print("setReleaseVariable('relNewVar') created -> created-value")

    def test_08f_set_release_set_variable_creates_when_missing(self):
        """setReleaseVariable creates a set variable when the key is unknown."""
        new_value = ["red", "green", "blue"]
        created = self.task.setReleaseVariable("relNewSetVar", new_value)
        self.assertEqual(created.type, "xlrelease.SetStringVariable")
        self.assertEqual(set(created.value), set(new_value))
        self.assertEqual(
            set(self.task.getReleaseVariable("relNewSetVar")), set(new_value)
        )
        print(f"setReleaseVariable('relNewSetVar') created -> {new_value}")

    def test_08g_set_release_map_variable_creates_when_missing(self):
        """setReleaseVariable creates a map variable when the key is unknown."""
        new_value = {"stage": "qa", "owner": "team-a"}
        created = self.task.setReleaseVariable("relNewMapVar", new_value)
        self.assertEqual(created.type, "xlrelease.MapStringStringVariable")
        self.assertEqual(created.value, new_value)
        self.assertEqual(self.task.getReleaseVariable("relNewMapVar"), new_value)
        print(f"setReleaseVariable('relNewMapVar') created -> {new_value}")

    # -- folder variables ---------------------------------------------------

    def test_09_get_folder_variable(self):
        """getFolderVariable resolves a folder variable by its prefixed name."""
        self.assertEqual(
            self.task.getFolderVariable("folder.folderVar"), "folder-value"
        )
        print("getFolderVariable('folder.folderVar') -> folder-value")

    def test_09a_get_folder_variable_requires_prefix(self):
        """getFolderVariable raises ValueError when the folder. prefix is missing."""
        with self.assertRaises(ValueError):
            self.task.getFolderVariable("folderVar")
        print("getFolderVariable('folderVar') correctly raised ValueError")

    def test_10_set_folder_variable(self):
        """setFolderVariable persists a new value on the folder-owned variable."""
        updated = self.task.setFolderVariable(
            "folder.folderVar", "folder-value-updated"
        )
        self.assertEqual(updated.value, "folder-value-updated")
        self.assertEqual(
            self.task.getFolderVariable("folder.folderVar"), "folder-value-updated"
        )
        print("setFolderVariable('folder.folderVar') -> folder-value-updated")

    def test_10_set_folder_variable_requires_prefix(self):
        """setFolderVariable raises ValueError when the folder. prefix is missing."""
        with self.assertRaises(ValueError):
            self.task.setFolderVariable("folderVar", "nope")
        print("setFolderVariable('folderVar') correctly raised ValueError")

    # -- folder variables: create when missing ------------------------------

    def test_10a_set_folder_variable_creates_when_missing(self):
        """setFolderVariable creates a folder-owned variable when the key is unknown."""
        created = self.task.setFolderVariable("folder.folderNewVar", "folder-created")
        self.assertEqual(created.key, "folder.folderNewVar")
        self.assertEqual(created.type, "xlrelease.StringVariable")
        self.assertEqual(created.value, "folder-created")
        self.assertEqual(
            self.task.getFolderVariable("folder.folderNewVar"), "folder-created"
        )
        print("setFolderVariable('folder.folderNewVar') created -> folder-created")

    def test_10b_set_folder_set_variable_creates_when_missing(self):
        """setFolderVariable creates a set variable when the key is unknown."""
        new_value = ["alpha", "beta"]
        created = self.task.setFolderVariable("folder.folderNewSetVar", new_value)
        self.assertEqual(created.type, "xlrelease.SetStringVariable")
        self.assertEqual(set(created.value), set(new_value))
        self.assertEqual(
            set(self.task.getFolderVariable("folder.folderNewSetVar")), set(new_value)
        )
        print(f"setFolderVariable('folder.folderNewSetVar') created -> {new_value}")

    def test_10c_set_folder_map_variable_creates_when_missing(self):
        """setFolderVariable creates a map variable when the key is unknown."""
        new_value = {"team": "infra", "tier": "silver"}
        created = self.task.setFolderVariable("folder.folderNewMapVar", new_value)
        self.assertEqual(created.type, "xlrelease.MapStringStringVariable")
        self.assertEqual(created.value, new_value)
        self.assertEqual(
            self.task.getFolderVariable("folder.folderNewMapVar"), new_value
        )
        print(f"setFolderVariable('folder.folderNewMapVar') created -> {new_value}")

    # -- global variables ---------------------------------------------------

    def test_11_get_global_variable(self):
        """getGlobalVariable resolves a global variable by its prefixed name."""
        self.assertEqual(
            self.task.getGlobalVariable(f"global.{self.global_var_name}"),
            "global-value",
        )
        print(f"getGlobalVariable('global.{self.global_var_name}') -> global-value")

    def test_11a_get_global_variable_requires_prefix(self):
        """getGlobalVariable raises ValueError when the global. prefix is missing."""
        with self.assertRaises(ValueError):
            self.task.getGlobalVariable(self.global_var_name)
        print("getGlobalVariable(unprefixed) correctly raised ValueError")

    def test_12_set_global_variable(self):
        """setGlobalVariable persists a new value on the global variable."""
        key = f"global.{self.global_var_name}"
        updated = self.task.setGlobalVariable(key, "global-value-updated")
        self.assertEqual(updated.value, "global-value-updated")
        self.assertEqual(self.task.getGlobalVariable(key), "global-value-updated")
        print(f"setGlobalVariable('{key}') -> global-value-updated")

    def test_12_set_global_variable_requires_prefix(self):
        """setGlobalVariable raises ValueError when the global. prefix is missing."""
        with self.assertRaises(ValueError):
            self.task.setGlobalVariable(self.global_var_name, "nope")
        print("setGlobalVariable(unprefixed) correctly raised ValueError")

    # -- global variables: create when missing ------------------------------

    def test_12a_set_global_variable_creates_when_missing(self):
        """setGlobalVariable creates a global variable when the key is unknown."""
        name = f"global.abtLiveGlobalNew_{self.uid}"
        created = self.task.setGlobalVariable(name, "global-created")
        self.created_global_var_ids.append(created.id)
        self.assertEqual(created.key, name)
        self.assertEqual(created.type, "xlrelease.StringVariable")
        self.assertEqual(created.value, "global-created")
        self.assertEqual(self.task.getGlobalVariable(name), "global-created")
        print(f"setGlobalVariable('{name}') created -> global-created")

    def test_12b_set_global_set_variable_creates_when_missing(self):
        """setGlobalVariable creates a set variable when the key is unknown."""
        name = f"global.abtLiveGlobalNewSet_{self.uid}"
        new_value = ["x", "y", "z"]
        created = self.task.setGlobalVariable(name, new_value)
        self.created_global_var_ids.append(created.id)
        self.assertEqual(created.type, "xlrelease.SetStringVariable")
        self.assertEqual(set(created.value), set(new_value))
        self.assertEqual(set(self.task.getGlobalVariable(name)), set(new_value))
        print(f"setGlobalVariable('{name}') created -> {new_value}")

    def test_12c_set_global_map_variable_creates_when_missing(self):
        """setGlobalVariable creates a map variable when the key is unknown."""
        name = f"global.abtLiveGlobalNewMap_{self.uid}"
        new_value = {"region": "ap", "tier": "bronze"}
        created = self.task.setGlobalVariable(name, new_value)
        self.created_global_var_ids.append(created.id)
        self.assertEqual(created.type, "xlrelease.MapStringStringVariable")
        self.assertEqual(created.value, new_value)
        self.assertEqual(self.task.getGlobalVariable(name), new_value)
        print(f"setGlobalVariable('{name}') created -> {new_value}")

    # -- ...ByTitle ---------------------------------------------------------

    def test_13_get_phases_by_title(self):
        """getPhasesByTitle finds the phase by title in the current release."""
        phases = self.task.getPhasesByTitle("Test Phase")
        self.assertGreaterEqual(len(phases), 1)
        self.assertTrue(all(p.title == "Test Phase" for p in phases))
        print(f"getPhasesByTitle('Test Phase') -> {len(phases)} phase(s)")

    def test_14_get_tasks_by_title(self):
        """getTasksByTitle finds the task by title, optionally scoped to a phase."""
        tasks = self.task.getTasksByTitle("Manual Task")
        self.assertGreaterEqual(len(tasks), 1)
        self.assertTrue(any(t.id == self.task_id for t in tasks))

        scoped = self.task.getTasksByTitle("Manual Task", "Test Phase")
        self.assertGreaterEqual(len(scoped), 1)
        print(
            f"getTasksByTitle('Manual Task') -> {len(tasks)} task(s), "
            f"scoped to phase -> {len(scoped)} task(s)"
        )

    def test_15_get_releases_by_title(self):
        """getReleasesByTitle finds the current release by its title."""
        releases = self.task.getReleasesByTitle(self.release_title)
        self.assertGreaterEqual(len(releases), 1)
        self.assertTrue(any(r.id == self.release_id for r in releases))
        print(f"getReleasesByTitle('{self.release_title}') -> {len(releases)} release(s)")


if __name__ == "__main__":
    unittest.main()
