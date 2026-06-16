from typing import Dict, Type, TypeVar

from digitalai.release.integration.base_task import BaseTask

from com.xebialabs.xlrelease.release_api_client import ReleaseAPIClient
from com.xebialabs.xlrelease.domain.folder import Folder
from com.xebialabs.xlrelease.domain.phase import Phase
from com.xebialabs.xlrelease.domain.release import Release
from com.xebialabs.xlrelease.domain.task import Task

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

T = TypeVar("T")


class ApiBaseTask(BaseTask):
    """
    Base class for Release container tasks that need the v1 REST API.

    Subclass this instead of :class:`BaseTask` to get a ready-to-use, lazily
    created instance of every ``com.xebialabs.xlrelease.api.v1`` wrapper as a
    property (``releaseApi``, ``phaseApi``, ``taskApi``, ...). All wrappers
    share a single, pre-configured :class:`ReleaseAPIClient` built from the
    task's "Run as user" context (credentials + server URL), so the client and
    each API object are created only once and only when first accessed.

    Example::

        class MyTask(ApiBaseTask):
            def execute(self) -> None:
                release = self.releaseApi.getRelease(self.get_release_id())
                self.add_comment(f"Working on {release.title}")
    """

    def __init__(self):
        super().__init__()
        self._api_client: ReleaseAPIClient = None
        self._api_instances: Dict[Type, object] = {}

    # -- client / instance management ---------------------------------------

    @property
    def apiClient(self) -> ReleaseAPIClient:
        """The shared :class:`ReleaseAPIClient`, created on first access."""
        if self._api_client is None:
            self._api_client = self.get_release_api_client()
        return self._api_client

    def _api(self, api_class: Type[T]) -> T:
        """Return a cached instance of ``api_class``, creating it on first use."""
        instance = self._api_instances.get(api_class)
        if instance is None:
            instance = api_class(self.apiClient)
            self._api_instances[api_class] = instance
        return instance

    def reset_api_clients(self) -> None:
        """Drop the cached client and API instances (e.g. to re-authenticate)."""
        self._api_client = None
        self._api_instances = {}

    # -- API wrappers -------------------------------------------------------

    @property
    def activityLogsApi(self) -> ActivityLogsApi:
        return self._api(ActivityLogsApi)

    @property
    def applicationApi(self) -> ApplicationApi:
        return self._api(ApplicationApi)

    @property
    def archiveApi(self) -> ArchiveApi:
        return self._api(ArchiveApi)

    @property
    def attachmentApi(self) -> AttachmentApi:
        return self._api(AttachmentApi)

    @property
    def categoryApi(self) -> CategoryApi:
        return self._api(CategoryApi)

    @property
    def configurationApi(self) -> ConfigurationApi:
        return self._api(ConfigurationApi)

    @property
    def deliveryApi(self) -> DeliveryApi:
        return self._api(DeliveryApi)

    @property
    def deliveryPatternApi(self) -> DeliveryPatternApi:
        return self._api(DeliveryPatternApi)

    @property
    def dslApi(self) -> DslApi:
        return self._api(DslApi)

    @property
    def environmentApi(self) -> EnvironmentApi:
        return self._api(EnvironmentApi)

    @property
    def environmentLabelApi(self) -> EnvironmentLabelApi:
        return self._api(EnvironmentLabelApi)

    @property
    def environmentReservationApi(self) -> EnvironmentReservationApi:
        return self._api(EnvironmentReservationApi)

    @property
    def environmentStageApi(self) -> EnvironmentStageApi:
        return self._api(EnvironmentStageApi)

    @property
    def folderApi(self) -> FolderApi:
        return self._api(FolderApi)

    @property
    def folderVersioningApi(self) -> FolderVersioningApi:
        return self._api(FolderVersioningApi)

    @property
    def permissionsApi(self) -> PermissionsApi:
        return self._api(PermissionsApi)

    @property
    def phaseApi(self) -> PhaseApi:
        return self._api(PhaseApi)

    @property
    def releaseApi(self) -> ReleaseApi:
        return self._api(ReleaseApi)

    @property
    def reportApi(self) -> ReportApi:
        return self._api(ReportApi)

    @property
    def riskApi(self) -> RiskApi:
        return self._api(RiskApi)

    @property
    def rolesApi(self) -> RolesApi:
        return self._api(RolesApi)

    @property
    def searchApi(self) -> SearchApi:
        return self._api(SearchApi)

    @property
    def settingsApi(self) -> SettingsApi:
        return self._api(SettingsApi)

    @property
    def taskApi(self) -> TaskApi:
        return self._api(TaskApi)

    @property
    def taskReportingApi(self) -> TaskReportingApi:
        return self._api(TaskReportingApi)

    @property
    def teamApi(self) -> TeamApi:
        return self._api(TeamApi)

    @property
    def templateApi(self) -> TemplateApi:
        return self._api(TemplateApi)

    @property
    def triggersApi(self) -> TriggersApi:
        return self._api(TriggersApi)

    @property
    def userApi(self) -> UserApi:
        return self._api(UserApi)

    @property
    def variableApi(self) -> VariableApi:
        return self._api(VariableApi)

    # -- current-context helpers --------------------------------------------
    # Convenience methods that resolve the release object the task is running
    # in, mirroring the helpers the Jython script API offers on the server
    # (XLReleaseApi.py). Each derives the relevant id from the task's context
    # and fetches the object through the matching API wrapper above.

    def getCurrentTask(self) -> Task:
        """
        Return the task that is running this code.

        Fetches the task via ``taskApi`` using the task's own id.
        """
        return self.taskApi.getTask(self.get_task_id())

    def getCurrentPhase(self) -> Phase:
        """
        Return the phase that contains this task.

        The phase id is derived from the task id, then fetched via ``phaseApi``.
        """
        return self.phaseApi.getPhase(self.get_phase_id())

    def getCurrentRelease(self) -> Release:
        """
        Return the release this task belongs to.

        Fetches the release via ``releaseApi`` using the task's release id, so
        the caller does not need to know or substitute the id itself.
        """
        return self.releaseApi.getRelease(self.get_release_id())

    def getCurrentFolder(self) -> Folder:
        """
        Return the folder that contains the current release.

        The folder id is derived from the release id, then fetched via
        ``folderApi``.
        """
        return self.folderApi.getFolder(self.get_folder_id())

    def getTasksByTitle(self, taskTitle: str, phaseTitle: str | None = None,
                        releaseId: str | None = None) -> list[Task]:
        """
        Find tasks by title.

        :param taskTitle: the task title to search for.
        :param phaseTitle: optional phase title to scope the search; searches the
            whole release when omitted.
        :param releaseId: optional release to search; the current release when
            omitted.
        :return: the matching tasks.
        """
        return self.taskApi.searchTasksByTitle(
            taskTitle, releaseId or self.get_release_id(), phaseTitle)

    def getPhasesByTitle(self, phaseTitle: str,
                         releaseId: str | None = None) -> list[Phase]:
        """
        Find phases by title.

        :param phaseTitle: the phase title to search for.
        :param releaseId: optional release to search; the current release when
            omitted.
        :return: the matching phases.
        """
        return self.phaseApi.searchPhasesByTitle(
            phaseTitle, releaseId or self.get_release_id())

    def getReleasesByTitle(self, releaseTitle: str) -> list[Release]:
        """
        Find releases by title.

        :param releaseTitle: the release title to search for.
        :return: the matching releases.
        """
        return self.releaseApi.searchReleasesByTitle(releaseTitle)

    def getVersion(self) -> str | None:
        """
        Return the version of this Digital.ai Release instance.
        """
        return self.settingsApi.getInstanceInformation().get('version')
