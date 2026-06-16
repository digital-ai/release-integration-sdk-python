import unittest
from types import SimpleNamespace
from unittest.mock import MagicMock

from digitalai.release.integration.input_context import (
    AutomatedTaskAsUserContext,
    ReleaseContext,
)
from digitalai.release.integration.api_base_task import ApiBaseTask

from com.xebialabs.xlrelease.release_api_client import ReleaseAPIClient
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
from com.xebialabs.xlrelease.api.v1.environment_reservation_api import (
    EnvironmentReservationApi,
)
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


# Mapping of every ApiBaseTask property name to the wrapper class it must return.
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


class _SampleApiTask(ApiBaseTask):
    """Concrete ApiBaseTask used to exercise the base behaviour in tests."""

    def execute(self) -> None:  # pragma: no cover - never executed by the tests
        pass


class TestApiBaseTask(unittest.TestCase):
    """Integration tests for the ApiBaseTask base class."""

    def setUp(self):
        # Configure the task context the way the Release runtime would, so that
        # get_release_api_client() builds a client from the "Run as user" details.
        self.task = _SampleApiTask()
        self.task.release_server_url = "http://localhost:5516"
        self.task.release_context = ReleaseContext(
            id="Applications/Release0000000000000000000000000000",
            automated_task_as_user=AutomatedTaskAsUserContext(
                username="admin", password="admin"
            ),
        )

    def test_api_client_is_lazy_and_cached(self):
        """apiClient is built on first access and the same instance is reused."""
        self.assertIsNone(self.task._api_client)
        client = self.task.apiClient
        self.assertIsInstance(client, ReleaseAPIClient)
        self.assertIs(self.task.apiClient, client)

    def test_all_api_properties_return_correct_type(self):
        """Every API property returns an instance of its wrapper class."""
        for name, api_class in API_PROPERTIES.items():
            with self.subTest(api=name):
                instance = getattr(self.task, name)
                self.assertIsInstance(instance, api_class)

    def test_api_properties_are_cached(self):
        """Accessing a property twice returns the very same cached instance."""
        for name in API_PROPERTIES:
            with self.subTest(api=name):
                first = getattr(self.task, name)
                second = getattr(self.task, name)
                self.assertIs(first, second)

    def test_all_apis_share_single_client(self):
        """All wrappers are built on the one shared apiClient."""
        client = self.task.apiClient
        for name in API_PROPERTIES:
            with self.subTest(api=name):
                self.assertIs(getattr(self.task, name).api, client)

    def test_reset_api_clients_clears_caches(self):
        """reset_api_clients drops the client and forces fresh instances."""
        old_client = self.task.apiClient
        old_release_api = self.task.releaseApi

        self.task.reset_api_clients()
        self.assertIsNone(self.task._api_client)
        self.assertEqual(self.task._api_instances, {})

        self.assertIsNot(self.task.apiClient, old_client)
        self.assertIsNot(self.task.releaseApi, old_release_api)

    def test_wired_client_performs_live_call(self):
        """A property built by ApiBaseTask can talk to the live server."""
        info = self.task.settingsApi.getInstanceInformation()
        self.assertIsInstance(info, dict)
        self.assertIn("version", info)
        print(f"ApiBaseTask wired client instance information: {info}")


# Realistic ids, matching the documented sample input context. The phase and
# folder ids are substrings the helpers derive from the task / release ids.
FOLDER_ID = "Applications/Folder1f65c7220b394afbb941154342fd9fc6"
RELEASE_ID = f"{FOLDER_ID}/Release31de09e95c8e4ebb95aaed29a8082d0b"
PHASE_ID = f"{RELEASE_ID}/Phase723a601c78804f7dbcaa8b05b83708f5"
TASK_ID = f"{PHASE_ID}/Task3a35b67b42b6428b854857fba470b39a"


class TestApiBaseTaskContextHelpers(unittest.TestCase):
    """Tests for the getCurrent*/...ByTitle/getVersion convenience helpers."""

    def _stub_task(self, release_id=RELEASE_ID, task_id=TASK_ID):
        """Build an ApiBaseTask with every API wrapper replaced by a MagicMock.

        Returns the task plus the dict of stub APIs keyed by property name. The
        class-level property overrides are removed again after the test.
        """
        task = _SampleApiTask()
        task.task_id = task_id
        task.release_context = SimpleNamespace(id=release_id)
        task._api_instances = {}

        apis = {name: MagicMock(name=name) for name in (
            "releaseApi", "taskApi", "phaseApi", "folderApi", "settingsApi")}
        for name, stub in apis.items():
            setattr(type(task), name, property(lambda self, s=stub: s))
        self.addCleanup(
            lambda: [delattr(type(task), name) for name in apis])
        return task, apis

    def test_get_current_release_and_task(self):
        task, apis = self._stub_task()
        apis["releaseApi"].getRelease.return_value = SimpleNamespace(title="My Release")
        apis["taskApi"].getTask.return_value = SimpleNamespace(title="My Task")

        self.assertEqual(task.getCurrentRelease().title, "My Release")
        self.assertEqual(task.getCurrentTask().title, "My Task")
        apis["releaseApi"].getRelease.assert_called_once_with(RELEASE_ID)
        apis["taskApi"].getTask.assert_called_once_with(TASK_ID)

    def test_get_current_phase_and_folder_derive_ids(self):
        task, apis = self._stub_task()
        apis["phaseApi"].getPhase.return_value = SimpleNamespace(title="My Phase")
        apis["folderApi"].getFolder.return_value = SimpleNamespace(title="My Folder")

        self.assertEqual(task.getCurrentPhase().title, "My Phase")
        self.assertEqual(task.getCurrentFolder().title, "My Folder")
        apis["phaseApi"].getPhase.assert_called_once_with(PHASE_ID)
        apis["folderApi"].getFolder.assert_called_once_with(FOLDER_ID)

    def test_search_helpers_default_to_current_release(self):
        task, apis = self._stub_task()
        apis["taskApi"].searchTasksByTitle.return_value = ["t"]
        apis["phaseApi"].searchPhasesByTitle.return_value = ["p"]
        apis["releaseApi"].searchReleasesByTitle.return_value = ["r"]

        self.assertEqual(task.getTasksByTitle("Deploy"), ["t"])
        self.assertEqual(task.getPhasesByTitle("Prod"), ["p"])
        self.assertEqual(task.getReleasesByTitle("Nightly"), ["r"])
        # taskApi signature is (taskTitle, releaseId, phaseTitle).
        apis["taskApi"].searchTasksByTitle.assert_called_once_with("Deploy", RELEASE_ID, None)
        apis["phaseApi"].searchPhasesByTitle.assert_called_once_with("Prod", RELEASE_ID)
        apis["releaseApi"].searchReleasesByTitle.assert_called_once_with("Nightly")

    def test_search_helpers_honor_explicit_arguments(self):
        task, apis = self._stub_task()
        apis["taskApi"].searchTasksByTitle.return_value = []

        task.getTasksByTitle("Deploy", "Prod", "Release/Other")

        apis["taskApi"].searchTasksByTitle.assert_called_once_with(
            "Deploy", "Release/Other", "Prod")

    def test_get_version(self):
        task, apis = self._stub_task()
        apis["settingsApi"].getInstanceInformation.return_value = {
            "product": "Digital.ai Release", "edition": "enterprise", "version": "25.3.0"}

        self.assertEqual(task.getVersion(), "25.3.0")


if __name__ == "__main__":
    unittest.main()
