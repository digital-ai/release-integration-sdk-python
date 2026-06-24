from datetime import date
from typing import Any, Dict, Type, TypeVar

from digitalai.release.integration.base_task import BaseTask

from digitalai.release.release_api_client import ReleaseAPIClient
from com.xebialabs.xlrelease.domain.folder import Folder
from com.xebialabs.xlrelease.domain.phase import Phase
from com.xebialabs.xlrelease.domain.release import Release
from com.xebialabs.xlrelease.domain.task import Task
from com.xebialabs.xlrelease.domain.variable import Variable

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

    def getReleaseVariable(self, name: str) -> Any:
        """
        Return the value of a variable in the current release by name.

        The Python3 equivalent of the Jython script global
        ``releaseVariables[name]``. Pass the bare variable name (e.g.
        ``"JenkinsBuildNumber"``). The variable is looked up by its ``key`` via
        ``releaseApi.getVariables`` and its stored value returned as-is.

        A reference variable holds no literal value -- the server resolves it
        from its value provider -- so its value is read from the server-resolved
        value map (``releaseApi.getVariableValues``) instead, matching Jython.

        Password variables never return their secret: the server masks the value
        as ``********``.

        :param name: the variable name (e.g. ``"JenkinsBuildNumber"``).
        :return: the variable's value (masked as ``********`` for password variables).
        :raises KeyError: if the release has no variable with that name.
        """
        release_id = self.get_release_id()
        variables = self.releaseApi.getVariables(release_id)
        variable = next((v for v in variables if v.key == name), None)
        if variable is None:
            raise KeyError(
                f"No variable named {name} in the current release; "
                f"available: {sorted(v.key for v in variables)}")
        if self._is_reference_variable(variable):
            return self._resolve_from_values(
                variable, self.releaseApi.getVariableValues(release_id))
        return variable.value

    def setReleaseVariable(self, name: str, value: Any) -> Variable:
        """
        Set the value of a variable in the current release by name.

        The Python3 equivalent of the Jython script assignment
        ``releaseVariables[name] = value``. Pass the bare variable name (e.g.
        ``"JenkinsBuildNumber"``). The variable is looked up by its ``key`` in
        the current release; if it exists its value is persisted via
        ``releaseApi.updateVariable``, otherwise a new variable is created via
        ``releaseApi.createVariable``. The new variable's type is inferred from
        ``value`` (see :meth:`_variable_type_for_value`).

        For a date variable, pass a timezone-aware ``datetime`` so the stored
        ISO-8601 value carries an explicit offset (see :meth:`_coerce_value`).

        :param name: the variable name (e.g. ``"JenkinsBuildNumber"``).
        :param value: the new value to assign.
        :return: the updated (or newly created) variable.
        :raises TypeError: if ``value`` is incompatible with the type of an
            existing variable (see :meth:`_check_value_type`).
        """
        release_id = self.get_release_id()
        variables = self.releaseApi.getVariables(release_id)
        variable = next((v for v in variables if v.key == name), None)
        if variable is None:
            return self.releaseApi.createVariable(
                release_id, self._new_variable(name, value))
        self._check_value_type(variable, value)
        variable.value = self._coerce_value(value)
        return self.releaseApi.updateVariable(variable.id, variable)

    def getFolderVariable(self, name: str) -> Any:
        """
        Return the value of a variable in the current folder by name.

        Like :meth:`getReleaseVariable`, but scoped to the folder that contains
        the current release. Inherited variables (from parent folders and global
        variables) are included, mirroring what a release actually resolves.

        Folder variables are stored with a ``folder.`` prefix, which is
        required here: pass the fully qualified name (e.g. ``"folder.foo"``).

        :param name: the variable name, including the ``folder.`` prefix.
        :return: the variable's value.
        Password variables never return their secret: the server masks the value
        as ``********``.

        :raises ValueError: if ``name`` does not start with ``folder.``.
        :raises KeyError: if no such variable is visible to the folder.
        """
        key = self._folder_key(name)
        folder_id = self.get_folder_id()
        variables = self.folderApi.listVariables(folder_id)
        variable = next((v for v in variables if v.key == key), None)
        if variable is None:
            raise KeyError(
                f"No variable named {key} visible to the current folder; "
                f"available: {sorted(v.key for v in variables)}")
        if self._is_reference_variable(variable):
            return self._resolve_from_values(
                variable, self.folderApi.listVariableValues(folder_id))
        return variable.value

    def setFolderVariable(self, name: str, value: Any) -> Variable:
        """
        Set the value of a variable owned by the current folder by name.

        Only variables the folder owns are matched: an inherited variable
        (defined on a parent folder or as a global variable) is not. If the
        folder owns the variable its value is persisted via
        ``folderApi.updateVariable``; otherwise a new folder-owned variable is
        created via ``folderApi.createVariable``. The new variable's type is
        inferred from ``value`` (see :meth:`_variable_type_for_value`). Creating
        a variable whose name matches an inherited one yields a folder-owned
        variable that shadows the inherited value.

        The ``folder.`` prefix is required (see :meth:`getFolderVariable`).

        :param name: the variable name, including the ``folder.`` prefix.
        :param value: the new value to assign.
        :return: the updated (or newly created) variable.
        :raises ValueError: if ``name`` does not start with ``folder.``.
        :raises TypeError: if ``value`` is incompatible with the type of an
            existing variable (see :meth:`_check_value_type`).
        """
        folder_id = self.get_folder_id()
        key = self._folder_key(name)
        variables = self.folderApi.listVariables(folder_id, folderOnly=True)
        variable = next((v for v in variables if v.key == key), None)
        if variable is None:
            return self.folderApi.createVariable(
                folder_id, self._new_variable(key, value))
        self._check_value_type(variable, value)
        variable.value = self._coerce_value(value)
        return self.folderApi.updateVariable(folder_id, variable.id, variable)

    def getGlobalVariable(self, name: str) -> Any:
        """
        Return the value of a global variable by name.

        Global variables are stored with a ``global.`` prefix, which is
        required here: pass the fully qualified name (e.g. ``"global.foo"``).

        Password variables never return their secret: the server masks the value
        as ``********``.

        :param name: the global variable name, including the ``global.`` prefix.
        :return: the variable's value (masked as ``********`` for password variables).
        :raises ValueError: if ``name`` does not start with ``global.``.
        :raises KeyError: if no global variable with that name exists.
        """
        key = self._global_key(name)
        variables = self.configurationApi.getGlobalVariables()
        variable = next((v for v in variables if v.key == key), None)
        if variable is None:
            raise KeyError(
                f"No global variable named {key}; "
                f"available: {sorted(v.key for v in variables)}")
        if self._is_reference_variable(variable):
            return self._resolve_from_values(
                variable, self.configurationApi.getGlobalVariableValues())
        return variable.value

    def setGlobalVariable(self, name: str, value: Any) -> Variable:
        """
        Set the value of a global variable by name.

        The ``global.`` prefix is required (see :meth:`getGlobalVariable`). If
        the variable exists its value is persisted via
        ``configurationApi.updateGlobalVariable``; otherwise a new global
        variable is created via ``configurationApi.addGlobalVariable``, with its
        type inferred from ``value`` (see :meth:`_variable_type_for_value`). The
        task's run-as user must hold the permission to edit global variables.

        :param name: the global variable name, including the ``global.`` prefix.
        :param value: the new value to assign.
        :return: the updated (or newly created) variable.
        :raises ValueError: if ``name`` does not start with ``global.``.
        :raises TypeError: if ``value`` is incompatible with the type of an
            existing variable (see :meth:`_check_value_type`).
        """
        key = self._global_key(name)
        variables = self.configurationApi.getGlobalVariables()
        variable = next((v for v in variables if v.key == key), None)
        if variable is None:
            return self.configurationApi.addGlobalVariable(
                self._new_variable(key, value))
        self._check_value_type(variable, value)
        variable.value = self._coerce_value(value)
        return self.configurationApi.updateGlobalVariable(variable.id, variable)

    @staticmethod
    def _is_reference_variable(variable: Variable) -> bool:
        """
        Return ``True`` if ``variable`` is a reference variable.

        A reference variable (``xlrelease.ReferenceVariable``) does not store a
        literal value; the server resolves it from a value provider, so its
        ``value`` comes back empty and the resolved value must be read from the
        scope's variable-value map instead. Detected by type, with the presence
        of a ``valueProvider`` as a fallback signal.
        """
        vtype = getattr(variable, "type", None) or ""
        return (vtype.endswith("ReferenceVariable")
                or getattr(variable, "valueProvider", None) is not None)

    @staticmethod
    def _resolve_from_values(variable: Variable, values: Dict[str, Any]) -> Any:
        """
        Return ``variable``'s server-resolved value from a ``${key}: value`` map.

        The variable-value endpoints key entries by the interpolation token
        ``${key}``. Falls back to the variable's stored ``value`` when the token
        is absent from the map.
        """
        return values.get(f"${{{variable.key}}}", variable.value)

    @staticmethod
    def _global_key(name: str) -> str:
        """
        Validate and return the stored ``key`` of a global variable.

        The ``global.`` prefix is required: ``name`` is returned unchanged, but
        a :class:`ValueError` is raised when it is missing.
        """
        if not name.startswith("global."):
            raise ValueError(
                f"Global variable name must include the 'global.' prefix; "
                f"got {name!r}.")
        return name

    @staticmethod
    def _folder_key(name: str) -> str:
        """
        Validate and return the stored ``key`` of a folder variable.

        The ``folder.`` prefix is required: ``name`` is returned unchanged, but
        a :class:`ValueError` is raised when it is missing.
        """
        if not name.startswith("folder."):
            raise ValueError(
                f"Folder variable name must include the 'folder.' prefix; "
                f"got {name!r}.")
        return name

    @staticmethod
    def _coerce_value(value: Any) -> Any:
        """
        Return ``value`` in a JSON-serializable form for a variable payload.

        Sets and tuples (natural Python types for a set-of-string variable) are
        converted to lists; ``date``/``datetime`` values (for a date variable)
        are formatted as an ISO-8601 string, which the server parses back into a
        date; everything else is passed through unchanged.

        Prefer a timezone-aware ``datetime``: its ISO-8601 form carries an
        explicit offset (e.g. ``2026-04-07T08:22:28+00:00``), matching the
        format the REST API uses. A naive ``datetime`` has no offset, so the
        server interprets it in its own timezone, which can shift the instant.
        """
        if isinstance(value, (set, tuple)):
            return list(value)
        # datetime is a subclass of date; isoformat() covers both.
        if isinstance(value, date):
            return value.isoformat()
        return value

    @staticmethod
    def _variable_type_for_value(value: Any) -> str:
        """
        Infer the Release variable ``type`` to use for a new variable from the
        Python type of ``value``.

        ====================  ======================================
        Python value          Variable type
        ====================  ======================================
        ``bool``              ``xlrelease.BooleanVariable``
        ``int``               ``xlrelease.IntegerVariable``
        ``date``/``datetime`` ``xlrelease.DateVariable``
        ``dict``              ``xlrelease.MapStringStringVariable``
        ``list``/``set``/     ``xlrelease.SetStringVariable``
        ``tuple``
        anything else         ``xlrelease.StringVariable``
        ====================  ======================================

        ``bool`` is checked before ``int`` because ``bool`` is a subclass of
        ``int`` in Python.
        """
        if isinstance(value, bool):
            return "xlrelease.BooleanVariable"
        if isinstance(value, int):
            return "xlrelease.IntegerVariable"
        # datetime is a subclass of date, so this covers both.
        if isinstance(value, date):
            return "xlrelease.DateVariable"
        if isinstance(value, dict):
            return "xlrelease.MapStringStringVariable"
        if isinstance(value, (list, set, tuple)):
            return "xlrelease.SetStringVariable"
        return "xlrelease.StringVariable"

    @staticmethod
    def _value_matches_type(vtype: str, value: Any) -> bool:
        """
        Return ``True`` if ``value`` is a valid Python value for an existing
        Release variable of type ``vtype``.

        The accepted Python types mirror :meth:`_variable_type_for_value`.
        ``vtype`` is matched by suffix so subtypes are treated as their base
        kind (e.g. ``PasswordStringVariable`` is a string). More specific
        suffixes are tested first because ``SetStringVariable`` and
        ``MapStringStringVariable`` also end in ``StringVariable``. A type the
        SDK does not recognise returns ``True`` -- it is left for the server to
        validate rather than blocked here.
        """
        if vtype.endswith("BooleanVariable"):
            return isinstance(value, bool)
        if vtype.endswith("IntegerVariable"):
            # bool is a subclass of int; an IntegerVariable must not accept it.
            return isinstance(value, int) and not isinstance(value, bool)
        if vtype.endswith("DateVariable"):
            # A date/datetime, or an ISO-8601 string the server parses to a date.
            return isinstance(value, (date, str))
        if vtype.endswith("MapStringStringVariable"):
            return isinstance(value, dict)
        if vtype.endswith("SetStringVariable"):
            return isinstance(value, (list, set, tuple))
        if vtype.endswith("StringVariable"):
            return isinstance(value, str)
        return True

    @classmethod
    def _check_value_type(cls, variable: Variable, value: Any) -> None:
        """
        Raise :class:`TypeError` when ``value`` is incompatible with the type
        of an existing ``variable`` being updated.

        The variable setters preserve an existing variable's ``type`` and only
        replace its value (the type is inferred from the value only when a new
        variable is created). Without this guard a value of the wrong Python
        type -- e.g. a ``str`` assigned to a ``SetStringVariable`` -- would be
        forwarded to the server as a mismatched payload. Reference variables
        and types the SDK does not recognise (see :meth:`_value_matches_type`)
        are not checked.
        """
        if cls._is_reference_variable(variable):
            return
        vtype = getattr(variable, "type", None) or ""
        if not cls._value_matches_type(vtype, value):
            raise TypeError(
                f"Cannot assign {type(value).__name__} value {value!r} to "
                f"variable {variable.key!r} of type {vtype!r}.")

    @classmethod
    def _new_variable(cls, key: str, value: Any) -> Variable:
        """
        Build a :class:`Variable` to create for ``key``/``value``, inferring the
        ``type`` from ``value`` and coercing the value to a serializable form.
        """
        return Variable(
            type=cls._variable_type_for_value(value),
            key=key,
            value=cls._coerce_value(value),
            requiresValue=False,
            showOnReleaseStart=False,
        )

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
