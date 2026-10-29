from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone
from types import SimpleNamespace
from typing import Any, Dict, Tuple
from unittest import mock

import pytest
from com.xebialabs.xlrelease.api.v1.activity_logs_api import ActivityLogsApi
from com.xebialabs.xlrelease.api.v1.application_api import ApplicationApi
from com.xebialabs.xlrelease.api.v1.archive_api import ArchiveApi
from com.xebialabs.xlrelease.api.v1.attachment_api import AttachmentApi
from com.xebialabs.xlrelease.api.v1.category_api import CategoryApi
from com.xebialabs.xlrelease.api.v1.configuration_api import ConfigurationApi
from com.xebialabs.xlrelease.api.v1.delivery_api import DeliveryApi
from com.xebialabs.xlrelease.api.v1.delivery_pattern_api import DeliveryPatternApi
from com.xebialabs.xlrelease.api.v1.dsl_api import DslApi
from com.xebialabs.xlrelease.api.v1.environment_api import EnvironmentApi
from com.xebialabs.xlrelease.api.v1.environment_label_api import EnvironmentLabelApi
from com.xebialabs.xlrelease.api.v1.environment_reservation_api import EnvironmentReservationApi
from com.xebialabs.xlrelease.api.v1.environment_stage_api import EnvironmentStageApi
from com.xebialabs.xlrelease.api.v1.folder_api import FolderApi
from com.xebialabs.xlrelease.api.v1.folder_versioning_api import FolderVersioningApi
from com.xebialabs.xlrelease.api.v1.permissions_api import PermissionsApi
from com.xebialabs.xlrelease.api.v1.phase_api import PhaseApi
from com.xebialabs.xlrelease.api.v1.release_api import ReleaseApi
from com.xebialabs.xlrelease.api.v1.report_api import ReportApi
from com.xebialabs.xlrelease.api.v1.risk_api import RiskApi
from com.xebialabs.xlrelease.api.v1.roles_api import RolesApi
from com.xebialabs.xlrelease.api.v1.search_api import SearchApi
from com.xebialabs.xlrelease.api.v1.settings_api import SettingsApi
from com.xebialabs.xlrelease.api.v1.task_api import TaskApi
from com.xebialabs.xlrelease.api.v1.task_reporting_api import TaskReportingApi
from com.xebialabs.xlrelease.api.v1.team_api import TeamApi
from com.xebialabs.xlrelease.api.v1.template_api import TemplateApi
from com.xebialabs.xlrelease.api.v1.triggers_api import TriggersApi
from com.xebialabs.xlrelease.api.v1.user_api import UserApi
from com.xebialabs.xlrelease.api.v1.variable_api import VariableApi
from com.xebialabs.xlrelease.domain.variable import ValueProvider, Variable

from digitalai.release.integration import base_task
from digitalai.release.integration.api_base_task import ApiBaseTask
from digitalai.release.integration.input_context import AutomatedTaskAsUserContext, ReleaseContext
from tests.support import FOLDER_ID, PHASE_ID, RELEASE_ID, SERVER_URL, TASK_ID

# Every ApiBaseTask property and the API wrapper class it must return.
API_PROPERTIES = {
    "activityLogsApi": ActivityLogsApi,
    "applicationApi": ApplicationApi,
    "archiveApi": ArchiveApi,
    "attachmentApi": AttachmentApi,
    "categoryApi": CategoryApi,
    "configurationApi": ConfigurationApi,
    "deliveryApi": DeliveryApi,
    "deliveryPatternApi": DeliveryPatternApi,
    "dslApi": DslApi,
    "environmentApi": EnvironmentApi,
    "environmentLabelApi": EnvironmentLabelApi,
    "environmentReservationApi": EnvironmentReservationApi,
    "environmentStageApi": EnvironmentStageApi,
    "folderApi": FolderApi,
    "folderVersioningApi": FolderVersioningApi,
    "permissionsApi": PermissionsApi,
    "phaseApi": PhaseApi,
    "releaseApi": ReleaseApi,
    "reportApi": ReportApi,
    "riskApi": RiskApi,
    "rolesApi": RolesApi,
    "searchApi": SearchApi,
    "settingsApi": SettingsApi,
    "taskApi": TaskApi,
    "taskReportingApi": TaskReportingApi,
    "teamApi": TeamApi,
    "templateApi": TemplateApi,
    "triggersApi": TriggersApi,
    "userApi": UserApi,
    "variableApi": VariableApi,
}


class SampleApiTask(ApiBaseTask):
    def execute(self) -> None:
        pass


@pytest.fixture
def task():
    task = SampleApiTask()
    task.task_id = TASK_ID
    task.release_server_url = SERVER_URL
    task.release_context = ReleaseContext(
        id=RELEASE_ID,
        automated_task_as_user=AutomatedTaskAsUserContext(username="admin", password="admin"),
    )
    return task


@pytest.fixture
def client_class(monkeypatch):
    """Replaces ReleaseAPIClient so no client is built; returns the stand-in class."""
    fake = mock.Mock(name="ReleaseAPIClient", side_effect=lambda *a, **kw: mock.Mock(name="client"))
    monkeypatch.setattr(base_task, "ReleaseAPIClient", fake)
    return fake


@pytest.fixture
def apis(task):
    """
    Signature-checked stand-ins for the APIs the helpers use, placed in the
    task's API cache so the helpers pick them up instead of building real ones.
    """
    instances = {cls: mock.create_autospec(cls, instance=True)
                 for cls in (ReleaseApi, TaskApi, PhaseApi, FolderApi, ConfigurationApi, SettingsApi)}
    task._api_instances.update(instances)
    return SimpleNamespace(release=instances[ReleaseApi], task=instances[TaskApi], phase=instances[PhaseApi],
                           folder=instances[FolderApi], configuration=instances[ConfigurationApi],
                           settings=instances[SettingsApi])


def variable(key, value, vtype="xlrelease.StringVariable", **extra):
    return Variable(id=f"{RELEASE_ID}/Variable_{key}", key=key, value=value, type=vtype, **extra)


# -- client and API instances ----------------------------------------------

def test_api_client_is_built_from_the_task_context_on_first_use(task, client_class):
    client_class.assert_not_called()

    client = task.apiClient

    client_class.assert_called_once_with(SERVER_URL, "admin", "admin", timeout=None)
    assert task.apiClient is client


@pytest.mark.parametrize("name, api_class", API_PROPERTIES.items(), ids=list(API_PROPERTIES))
def test_api_property_returns_a_cached_wrapper_on_the_shared_client(task, client_class, name, api_class):
    api = getattr(task, name)

    assert isinstance(api, api_class)
    assert getattr(task, name) is api
    assert api.api is task.apiClient


def test_all_api_properties_share_one_client(task, client_class):
    for name in API_PROPERTIES:
        getattr(task, name)

    client_class.assert_called_once()


def test_reset_api_clients_rebuilds_the_client_and_wrappers(task, client_class):
    old_client, old_release_api = task.apiClient, task.releaseApi

    task.reset_api_clients()

    assert task.apiClient is not old_client
    assert task.releaseApi is not old_release_api
    assert task.releaseApi.api is task.apiClient


# -- current-context helpers -----------------------------------------------

@pytest.mark.parametrize("helper, api, method, expected_id", [
    ("getCurrentTask", "task", "getTask", TASK_ID),
    ("getCurrentPhase", "phase", "getPhase", PHASE_ID),
    ("getCurrentRelease", "release", "getRelease", RELEASE_ID),
    ("getCurrentFolder", "folder", "getFolder", FOLDER_ID),
])
def test_get_current_object_fetches_it_by_the_derived_id(task, apis, helper, api, method, expected_id):
    api_method = getattr(getattr(apis, api), method)

    result = getattr(task, helper)()

    api_method.assert_called_once_with(expected_id)
    assert result is api_method.return_value


def test_get_tasks_by_title_searches_the_current_release(task, apis):
    result = task.getTasksByTitle("Deploy")

    apis.task.searchTasksByTitle.assert_called_once_with("Deploy", RELEASE_ID, None)
    assert result is apis.task.searchTasksByTitle.return_value


def test_get_tasks_by_title_honours_phase_and_release(task, apis):
    task.getTasksByTitle("Deploy", "Prod", "Applications/Release2")

    apis.task.searchTasksByTitle.assert_called_once_with("Deploy", "Applications/Release2", "Prod")


@pytest.mark.parametrize("release_id, expected", [(None, RELEASE_ID), ("Applications/Release2", "Applications/Release2")])
def test_get_phases_by_title_defaults_to_the_current_release(task, apis, release_id, expected):
    task.getPhasesByTitle("Prod", release_id)

    apis.phase.searchPhasesByTitle.assert_called_once_with("Prod", expected)


def test_get_releases_by_title_searches_all_releases(task, apis):
    result = task.getReleasesByTitle("Nightly")

    apis.release.searchReleasesByTitle.assert_called_once_with("Nightly")
    assert result is apis.release.searchReleasesByTitle.return_value


@pytest.mark.parametrize("info, expected", [({"version": "25.3.0", "edition": "enterprise"}, "25.3.0"), ({}, None)])
def test_get_version_reads_the_instance_information(task, apis, info, expected):
    apis.settings.getInstanceInformation.return_value = info

    assert task.getVersion() == expected


# -- variable getters and setters ------------------------------------------

@dataclass(frozen=True)
class Scope:
    """How one variable scope maps onto ApiBaseTask helpers and API calls."""
    name: str                       # variable name as a task author passes it
    get: str                        # ApiBaseTask getter
    set: str                        # ApiBaseTask setter
    api: str                        # attribute of the `apis` fixture
    list_variables: str             # API method listing the scope's variables
    get_list_args: Tuple            # its arguments when reading
    set_list_args: Tuple            # ... and when writing
    set_list_kwargs: Dict[str, Any]
    list_values: str                # API method returning the ${key} -> value map
    create: str
    create_args: Tuple              # arguments before the new Variable
    update: str
    update_args: Tuple              # arguments before the variable id


SCOPES = {
    "release": Scope("relVar", "getReleaseVariable", "setReleaseVariable", "release",
                     "getVariables", (RELEASE_ID,), (RELEASE_ID,), {}, "getVariableValues",
                     "createVariable", (RELEASE_ID,), "updateVariable", ()),
    "folder": Scope("folder.myVar", "getFolderVariable", "setFolderVariable", "folder",
                    "listVariables", (FOLDER_ID,), (FOLDER_ID,), {"folderOnly": True}, "listVariableValues",
                    "createVariable", (FOLDER_ID,), "updateVariable", (FOLDER_ID,)),
    "global": Scope("global.myVar", "getGlobalVariable", "setGlobalVariable", "configuration",
                    "getGlobalVariables", (), (), {}, "getGlobalVariableValues",
                    "addGlobalVariable", (), "updateGlobalVariable", ()),
}

scopes = pytest.mark.parametrize("scope", SCOPES.values(), ids=list(SCOPES))


def scope_api(apis, scope):
    return getattr(apis, scope.api)


def stored(apis, scope, *variables):
    getattr(scope_api(apis, scope), scope.list_variables).return_value = list(variables)


@scopes
def test_getter_returns_the_stored_value(task, apis, scope):
    stored(apis, scope, variable("other", "x"), variable(scope.name, "value"))

    assert getattr(task, scope.get)(scope.name) == "value"

    getattr(scope_api(apis, scope), scope.list_variables).assert_called_once_with(*scope.get_list_args)
    getattr(scope_api(apis, scope), scope.list_values).assert_not_called()


@scopes
def test_getter_resolves_a_reference_variable_on_the_server(task, apis, scope):
    stored(apis, scope, variable(scope.name, None, "xlrelease.ReferenceVariable"))
    values = getattr(scope_api(apis, scope), scope.list_values)
    values.return_value = {f"${{{scope.name}}}": "resolved"}

    assert getattr(task, scope.get)(scope.name) == "resolved"

    values.assert_called_once_with(*scope.get_list_args)


@scopes
def test_getter_falls_back_to_the_stored_value_when_reference_is_unresolved(task, apis, scope):
    stored(apis, scope, variable(scope.name, "stored", "xlrelease.ReferenceVariable"))
    getattr(scope_api(apis, scope), scope.list_values).return_value = {}

    assert getattr(task, scope.get)(scope.name) == "stored"


@scopes
def test_getter_raises_key_error_listing_available_names(task, apis, scope):
    stored(apis, scope, variable("b", 1), variable("a", 2))

    with pytest.raises(KeyError, match=r"\['a', 'b'\]"):
        getattr(task, scope.get)(scope.name)


@scopes
def test_setter_updates_an_existing_variable(task, apis, scope):
    existing = variable(scope.name, "old")
    stored(apis, scope, existing)
    update = getattr(scope_api(apis, scope), scope.update)

    result = getattr(task, scope.set)(scope.name, "new")

    getattr(scope_api(apis, scope), scope.list_variables).assert_called_once_with(
        *scope.set_list_args, **scope.set_list_kwargs)
    update.assert_called_once_with(*scope.update_args, existing.id, existing)
    assert existing.value == "new"
    assert result is update.return_value


@scopes
def test_setter_creates_a_missing_variable_with_an_inferred_type(task, apis, scope):
    stored(apis, scope, variable("other", "x"))
    create = getattr(scope_api(apis, scope), scope.create)

    result = getattr(task, scope.set)(scope.name, {"b", "a"})

    (*args, created), _ = create.call_args
    assert tuple(args) == scope.create_args
    assert (created.key, created.type, sorted(created.value)) == (scope.name, "xlrelease.SetStringVariable",
                                                                  ["a", "b"])
    assert (created.requiresValue, created.showOnReleaseStart) == (False, False)
    getattr(scope_api(apis, scope), scope.update).assert_not_called()
    assert result is create.return_value


@scopes
def test_setter_rejects_a_value_of_the_wrong_type(task, apis, scope):
    stored(apis, scope, variable(scope.name, ["a"], "xlrelease.SetStringVariable"))

    with pytest.raises(TypeError, match="Cannot assign str"):
        getattr(task, scope.set)(scope.name, "not-a-set")

    getattr(scope_api(apis, scope), scope.update).assert_not_called()


@scopes
def test_setter_leaves_reference_variables_to_the_server(task, apis, scope):
    stored(apis, scope, variable(scope.name, None, "xlrelease.ReferenceVariable"))

    getattr(task, scope.set)(scope.name, 42)

    getattr(scope_api(apis, scope), scope.update).assert_called_once()


@pytest.mark.parametrize("helper, args", [
    ("getFolderVariable", ("myVar",)),
    ("setFolderVariable", ("myVar", "x")),
    ("getGlobalVariable", ("myVar",)),
    ("setGlobalVariable", ("myVar", "x")),
    ("getFolderVariable", ("global.myVar",)),
    ("getGlobalVariable", ("folder.myVar",)),
])
def test_folder_and_global_helpers_require_the_scope_prefix(task, apis, helper, args):
    with pytest.raises(ValueError, match="prefix"):
        getattr(task, helper)(*args)

    apis.folder.listVariables.assert_not_called()
    apis.configuration.getGlobalVariables.assert_not_called()


def test_set_release_variable_sends_a_datetime_as_iso_8601(task, apis):
    existing = variable("when", None, "xlrelease.DateVariable")
    stored(apis, SCOPES["release"], existing)

    task.setReleaseVariable("when", datetime(2026, 6, 24, 10, 30, tzinfo=timezone.utc))

    assert existing.value == "2026-06-24T10:30:00+00:00"


# -- value typing rules ----------------------------------------------------

@pytest.mark.parametrize("value, expected", [
    (True, "xlrelease.BooleanVariable"),
    (0, "xlrelease.IntegerVariable"),
    (date(2026, 1, 1), "xlrelease.DateVariable"),
    (datetime(2026, 1, 1, tzinfo=timezone.utc), "xlrelease.DateVariable"),
    ({"k": "v"}, "xlrelease.MapStringStringVariable"),
    (["a"], "xlrelease.SetStringVariable"),
    ({"a"}, "xlrelease.SetStringVariable"),
    (("a",), "xlrelease.SetStringVariable"),
    ("text", "xlrelease.StringVariable"),
    (1.5, "xlrelease.StringVariable"),
], ids=["bool", "int", "date", "datetime", "dict", "list", "set", "tuple", "str", "float"])
def test_new_variable_type_is_inferred_from_the_value(value, expected):
    assert ApiBaseTask._variable_type_for_value(value) == expected


@pytest.mark.parametrize("vtype, value", [
    ("xlrelease.BooleanVariable", False),
    ("xlrelease.IntegerVariable", 3),
    ("xlrelease.DateVariable", date(2026, 1, 1)),
    ("xlrelease.DateVariable", "2026-01-01T00:00:00Z"),
    ("xlrelease.MapStringStringVariable", {"k": "v"}),
    ("xlrelease.SetStringVariable", ("a",)),
    ("xlrelease.StringVariable", "text"),
    ("xlrelease.PasswordStringVariable", "secret"),
    ("custom.UnknownVariable", object()),
])
def test_value_matching_the_variable_type_is_accepted(vtype, value):
    assert ApiBaseTask._value_matches_type(vtype, value) is True


@pytest.mark.parametrize("vtype, value", [
    ("xlrelease.BooleanVariable", 1),
    ("xlrelease.IntegerVariable", True),
    ("xlrelease.IntegerVariable", "3"),
    ("xlrelease.DateVariable", 12345),
    ("xlrelease.MapStringStringVariable", [("k", "v")]),
    ("xlrelease.SetStringVariable", "a"),
    ("xlrelease.StringVariable", 42),
    ("xlrelease.PasswordStringVariable", None),
])
def test_value_not_matching_the_variable_type_is_rejected(vtype, value):
    assert ApiBaseTask._value_matches_type(vtype, value) is False


@pytest.mark.parametrize("value, expected", [
    ({"a"}, ["a"]),
    (("a", "b"), ["a", "b"]),
    (date(2026, 6, 24), "2026-06-24"),
    (datetime(2026, 6, 24, 10, 30, tzinfo=timezone(timedelta(hours=2))), "2026-06-24T10:30:00+02:00"),
    (["a"], ["a"]),
    ({"k": "v"}, {"k": "v"}),
    ("text", "text"),
])
def test_values_are_coerced_to_a_json_form(value, expected):
    assert ApiBaseTask._coerce_value(value) == expected


@pytest.mark.parametrize("candidate, expected", [
    (variable("v", None, "xlrelease.ReferenceVariable"), True),
    (variable("v", None, "xlrelease.StringVariable", valueProvider=ValueProvider()), True),
    (variable("v", "x", "xlrelease.StringVariable"), False),
    (variable("v", "x", None), False),
], ids=["by-type", "by-value-provider", "plain", "untyped"])
def test_reference_variables_are_detected(candidate, expected):
    assert ApiBaseTask._is_reference_variable(candidate) is expected
