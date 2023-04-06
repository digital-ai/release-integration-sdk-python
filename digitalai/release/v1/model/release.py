"""
    Digital.ai Release API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from digitalai.release.v1.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from digitalai.release.v1.exceptions import ApiAttributeError


def lazy_import():
    from digitalai.release.v1.model.attachment import Attachment
    from digitalai.release.v1.model.flag_status import FlagStatus
    from digitalai.release.v1.model.folder_variables import FolderVariables
    from digitalai.release.v1.model.gate_task import GateTask
    from digitalai.release.v1.model.global_variables import GlobalVariables
    from digitalai.release.v1.model.phase import Phase
    from digitalai.release.v1.model.plan_item import PlanItem
    from digitalai.release.v1.model.release_extension import ReleaseExtension
    from digitalai.release.v1.model.release_status import ReleaseStatus
    from digitalai.release.v1.model.release_trigger import ReleaseTrigger
    from digitalai.release.v1.model.task import Task
    from digitalai.release.v1.model.team import Team
    from digitalai.release.v1.model.usage_point import UsagePoint
    from digitalai.release.v1.model.user_input_task import UserInputTask
    from digitalai.release.v1.model.value_with_interpolation import ValueWithInterpolation
    from digitalai.release.v1.model.variable import Variable
    globals()['Attachment'] = Attachment
    globals()['FlagStatus'] = FlagStatus
    globals()['FolderVariables'] = FolderVariables
    globals()['GateTask'] = GateTask
    globals()['GlobalVariables'] = GlobalVariables
    globals()['Phase'] = Phase
    globals()['PlanItem'] = PlanItem
    globals()['ReleaseExtension'] = ReleaseExtension
    globals()['ReleaseStatus'] = ReleaseStatus
    globals()['ReleaseTrigger'] = ReleaseTrigger
    globals()['Task'] = Task
    globals()['Team'] = Team
    globals()['UsagePoint'] = UsagePoint
    globals()['UserInputTask'] = UserInputTask
    globals()['ValueWithInterpolation'] = ValueWithInterpolation
    globals()['Variable'] = Variable


class Release(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
        ('variables_keys_in_non_interpolatable_variable_values',): {
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'id': (str,),  # noqa: E501
            'type': (str,),  # noqa: E501
            'start_date': (datetime,),  # noqa: E501
            'scheduled_start_date': (datetime,),  # noqa: E501
            'end_date': (datetime,),  # noqa: E501
            'due_date': (datetime,),  # noqa: E501
            'title': (str,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'owner': (str,),  # noqa: E501
            'planned_duration': (int,),  # noqa: E501
            'flag_status': (FlagStatus,),  # noqa: E501
            'flag_comment': (str,),  # noqa: E501
            'overdue_notified': (bool,),  # noqa: E501
            'flagged': (bool,),  # noqa: E501
            'start_or_scheduled_date': (datetime,),  # noqa: E501
            'end_or_due_date': (datetime,),  # noqa: E501
            'overdue': (bool,),  # noqa: E501
            'or_calculate_due_date': (str, none_type,),  # noqa: E501
            'computed_planned_duration': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'actual_duration': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'root_release_id': (str,),  # noqa: E501
            'max_concurrent_releases': (int,),  # noqa: E501
            'release_triggers': ([ReleaseTrigger],),  # noqa: E501
            'teams': ([Team],),  # noqa: E501
            'member_viewers': ([str],),  # noqa: E501
            'role_viewers': ([str],),  # noqa: E501
            'attachments': ([Attachment],),  # noqa: E501
            'phases': ([Phase],),  # noqa: E501
            'queryable_start_date': (datetime,),  # noqa: E501
            'queryable_end_date': (datetime,),  # noqa: E501
            'real_flag_status': (FlagStatus,),  # noqa: E501
            'status': (ReleaseStatus,),  # noqa: E501
            'tags': ([str],),  # noqa: E501
            'variables': ([Variable],),  # noqa: E501
            'calendar_link_token': (str,),  # noqa: E501
            'calendar_published': (bool,),  # noqa: E501
            'tutorial': (bool,),  # noqa: E501
            'abort_on_failure': (bool,),  # noqa: E501
            'archive_release': (bool,),  # noqa: E501
            'allow_passwords_in_all_fields': (bool,),  # noqa: E501
            'disable_notifications': (bool,),  # noqa: E501
            'allow_concurrent_releases_from_trigger': (bool,),  # noqa: E501
            'origin_template_id': (str,),  # noqa: E501
            'created_from_trigger': (bool,),  # noqa: E501
            'script_username': (str,),  # noqa: E501
            'script_user_password': (str,),  # noqa: E501
            'extensions': ([ReleaseExtension],),  # noqa: E501
            'started_from_task_id': (str,),  # noqa: E501
            'auto_start': (bool,),  # noqa: E501
            'automated_resume_count': (int,),  # noqa: E501
            'max_automated_resumes': (int,),  # noqa: E501
            'abort_comment': (str,),  # noqa: E501
            'variable_mapping': ({str: (str,)},),  # noqa: E501
            'risk_profile': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'metadata': ({str: (dict,)},),  # noqa: E501
            'archived': (bool,),  # noqa: E501
            'ci_uid': (int,),  # noqa: E501
            'variable_values': ({str: ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},)},),  # noqa: E501
            'password_variable_values': ({str: ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},)},),  # noqa: E501
            'ci_property_variables': ([Variable],),  # noqa: E501
            'all_string_variable_values': ({str: (str,)},),  # noqa: E501
            'all_release_global_and_folder_variables': ([Variable],),  # noqa: E501
            'all_variable_values_as_strings_with_interpolation_info': ({str: (ValueWithInterpolation,)},),  # noqa: E501
            'variables_keys_in_non_interpolatable_variable_values': ([str],),  # noqa: E501
            'variables_by_keys': ({str: (Variable,)},),  # noqa: E501
            'all_variables': ([Variable],),  # noqa: E501
            'global_variables': (GlobalVariables,),  # noqa: E501
            'folder_variables': (FolderVariables,),  # noqa: E501
            'admin_team': (Team,),  # noqa: E501
            'release_attachments': ([Attachment],),  # noqa: E501
            'current_phase': (Phase,),  # noqa: E501
            'current_task': (Task,),  # noqa: E501
            'all_tasks': ([Task],),  # noqa: E501
            'all_gates': ([GateTask],),  # noqa: E501
            'all_user_input_tasks': ([UserInputTask],),  # noqa: E501
            'done': (bool,),  # noqa: E501
            'planned_or_active': (bool,),  # noqa: E501
            'active': (bool,),  # noqa: E501
            'defunct': (bool,),  # noqa: E501
            'updatable': (bool,),  # noqa: E501
            'aborted': (bool,),  # noqa: E501
            'failing': (bool,),  # noqa: E501
            'failed': (bool,),  # noqa: E501
            'paused': (bool,),  # noqa: E501
            'template': (bool,),  # noqa: E501
            'planned': (bool,),  # noqa: E501
            'in_progress': (bool,),  # noqa: E501
            'release': (Release,),  # noqa: E501
            'release_uid': (int,),  # noqa: E501
            'display_path': (str,),  # noqa: E501
            'children': ([PlanItem],),  # noqa: E501
            'all_plan_items': ([PlanItem],),  # noqa: E501
            'url': (str,),  # noqa: E501
            'active_tasks': ([Task],),  # noqa: E501
            'variable_usages': ([UsagePoint],),  # noqa: E501
            'pending': (bool,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'type': 'type',  # noqa: E501
        'start_date': 'startDate',  # noqa: E501
        'scheduled_start_date': 'scheduledStartDate',  # noqa: E501
        'end_date': 'endDate',  # noqa: E501
        'due_date': 'dueDate',  # noqa: E501
        'title': 'title',  # noqa: E501
        'description': 'description',  # noqa: E501
        'owner': 'owner',  # noqa: E501
        'planned_duration': 'plannedDuration',  # noqa: E501
        'flag_status': 'flagStatus',  # noqa: E501
        'flag_comment': 'flagComment',  # noqa: E501
        'overdue_notified': 'overdueNotified',  # noqa: E501
        'flagged': 'flagged',  # noqa: E501
        'start_or_scheduled_date': 'startOrScheduledDate',  # noqa: E501
        'end_or_due_date': 'endOrDueDate',  # noqa: E501
        'overdue': 'overdue',  # noqa: E501
        'or_calculate_due_date': 'orCalculateDueDate',  # noqa: E501
        'computed_planned_duration': 'computedPlannedDuration',  # noqa: E501
        'actual_duration': 'actualDuration',  # noqa: E501
        'root_release_id': 'rootReleaseId',  # noqa: E501
        'max_concurrent_releases': 'maxConcurrentReleases',  # noqa: E501
        'release_triggers': 'releaseTriggers',  # noqa: E501
        'teams': 'teams',  # noqa: E501
        'member_viewers': 'memberViewers',  # noqa: E501
        'role_viewers': 'roleViewers',  # noqa: E501
        'attachments': 'attachments',  # noqa: E501
        'phases': 'phases',  # noqa: E501
        'queryable_start_date': 'queryableStartDate',  # noqa: E501
        'queryable_end_date': 'queryableEndDate',  # noqa: E501
        'real_flag_status': 'realFlagStatus',  # noqa: E501
        'status': 'status',  # noqa: E501
        'tags': 'tags',  # noqa: E501
        'variables': 'variables',  # noqa: E501
        'calendar_link_token': 'calendarLinkToken',  # noqa: E501
        'calendar_published': 'calendarPublished',  # noqa: E501
        'tutorial': 'tutorial',  # noqa: E501
        'abort_on_failure': 'abortOnFailure',  # noqa: E501
        'archive_release': 'archiveRelease',  # noqa: E501
        'allow_passwords_in_all_fields': 'allowPasswordsInAllFields',  # noqa: E501
        'disable_notifications': 'disableNotifications',  # noqa: E501
        'allow_concurrent_releases_from_trigger': 'allowConcurrentReleasesFromTrigger',  # noqa: E501
        'origin_template_id': 'originTemplateId',  # noqa: E501
        'created_from_trigger': 'createdFromTrigger',  # noqa: E501
        'script_username': 'scriptUsername',  # noqa: E501
        'script_user_password': 'scriptUserPassword',  # noqa: E501
        'extensions': 'extensions',  # noqa: E501
        'started_from_task_id': 'startedFromTaskId',  # noqa: E501
        'auto_start': 'autoStart',  # noqa: E501
        'automated_resume_count': 'automatedResumeCount',  # noqa: E501
        'max_automated_resumes': 'maxAutomatedResumes',  # noqa: E501
        'abort_comment': 'abortComment',  # noqa: E501
        'variable_mapping': 'variableMapping',  # noqa: E501
        'risk_profile': 'riskProfile',  # noqa: E501
        'metadata': '$metadata',  # noqa: E501
        'archived': 'archived',  # noqa: E501
        'ci_uid': 'ciUid',  # noqa: E501
        'variable_values': 'variableValues',  # noqa: E501
        'password_variable_values': 'passwordVariableValues',  # noqa: E501
        'ci_property_variables': 'ciPropertyVariables',  # noqa: E501
        'all_string_variable_values': 'allStringVariableValues',  # noqa: E501
        'all_release_global_and_folder_variables': 'allReleaseGlobalAndFolderVariables',  # noqa: E501
        'all_variable_values_as_strings_with_interpolation_info': 'allVariableValuesAsStringsWithInterpolationInfo',  # noqa: E501
        'variables_keys_in_non_interpolatable_variable_values': 'variablesKeysInNonInterpolatableVariableValues',  # noqa: E501
        'variables_by_keys': 'variablesByKeys',  # noqa: E501
        'all_variables': 'allVariables',  # noqa: E501
        'global_variables': 'globalVariables',  # noqa: E501
        'folder_variables': 'folderVariables',  # noqa: E501
        'admin_team': 'adminTeam',  # noqa: E501
        'release_attachments': 'releaseAttachments',  # noqa: E501
        'current_phase': 'currentPhase',  # noqa: E501
        'current_task': 'currentTask',  # noqa: E501
        'all_tasks': 'allTasks',  # noqa: E501
        'all_gates': 'allGates',  # noqa: E501
        'all_user_input_tasks': 'allUserInputTasks',  # noqa: E501
        'done': 'done',  # noqa: E501
        'planned_or_active': 'plannedOrActive',  # noqa: E501
        'active': 'active',  # noqa: E501
        'defunct': 'defunct',  # noqa: E501
        'updatable': 'updatable',  # noqa: E501
        'aborted': 'aborted',  # noqa: E501
        'failing': 'failing',  # noqa: E501
        'failed': 'failed',  # noqa: E501
        'paused': 'paused',  # noqa: E501
        'template': 'template',  # noqa: E501
        'planned': 'planned',  # noqa: E501
        'in_progress': 'inProgress',  # noqa: E501
        'release': 'release',  # noqa: E501
        'release_uid': 'releaseUid',  # noqa: E501
        'display_path': 'displayPath',  # noqa: E501
        'children': 'children',  # noqa: E501
        'all_plan_items': 'allPlanItems',  # noqa: E501
        'url': 'url',  # noqa: E501
        'active_tasks': 'activeTasks',  # noqa: E501
        'variable_usages': 'variableUsages',  # noqa: E501
        'pending': 'pending',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Release - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            id (str): [optional]  # noqa: E501
            type (str): [optional]  # noqa: E501
            start_date (datetime): [optional]  # noqa: E501
            scheduled_start_date (datetime): [optional]  # noqa: E501
            end_date (datetime): [optional]  # noqa: E501
            due_date (datetime): [optional]  # noqa: E501
            title (str): [optional]  # noqa: E501
            description (str): [optional]  # noqa: E501
            owner (str): [optional]  # noqa: E501
            planned_duration (int): [optional]  # noqa: E501
            flag_status (FlagStatus): [optional]  # noqa: E501
            flag_comment (str): [optional]  # noqa: E501
            overdue_notified (bool): [optional]  # noqa: E501
            flagged (bool): [optional]  # noqa: E501
            start_or_scheduled_date (datetime): [optional]  # noqa: E501
            end_or_due_date (datetime): [optional]  # noqa: E501
            overdue (bool): [optional]  # noqa: E501
            or_calculate_due_date (str, none_type): [optional]  # noqa: E501
            computed_planned_duration ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): [optional]  # noqa: E501
            actual_duration ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): [optional]  # noqa: E501
            root_release_id (str): [optional]  # noqa: E501
            max_concurrent_releases (int): [optional]  # noqa: E501
            release_triggers ([ReleaseTrigger]): [optional]  # noqa: E501
            teams ([Team]): [optional]  # noqa: E501
            member_viewers ([str]): [optional]  # noqa: E501
            role_viewers ([str]): [optional]  # noqa: E501
            attachments ([Attachment]): [optional]  # noqa: E501
            phases ([Phase]): [optional]  # noqa: E501
            queryable_start_date (datetime): [optional]  # noqa: E501
            queryable_end_date (datetime): [optional]  # noqa: E501
            real_flag_status (FlagStatus): [optional]  # noqa: E501
            status (ReleaseStatus): [optional]  # noqa: E501
            tags ([str]): [optional]  # noqa: E501
            variables ([Variable]): [optional]  # noqa: E501
            calendar_link_token (str): [optional]  # noqa: E501
            calendar_published (bool): [optional]  # noqa: E501
            tutorial (bool): [optional]  # noqa: E501
            abort_on_failure (bool): [optional]  # noqa: E501
            archive_release (bool): [optional]  # noqa: E501
            allow_passwords_in_all_fields (bool): [optional]  # noqa: E501
            disable_notifications (bool): [optional]  # noqa: E501
            allow_concurrent_releases_from_trigger (bool): [optional]  # noqa: E501
            origin_template_id (str): [optional]  # noqa: E501
            created_from_trigger (bool): [optional]  # noqa: E501
            script_username (str): [optional]  # noqa: E501
            script_user_password (str): [optional]  # noqa: E501
            extensions ([ReleaseExtension]): [optional]  # noqa: E501
            started_from_task_id (str): [optional]  # noqa: E501
            auto_start (bool): [optional]  # noqa: E501
            automated_resume_count (int): [optional]  # noqa: E501
            max_automated_resumes (int): [optional]  # noqa: E501
            abort_comment (str): [optional]  # noqa: E501
            variable_mapping ({str: (str,)}): [optional]  # noqa: E501
            risk_profile (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            metadata ({str: (dict,)}): [optional]  # noqa: E501
            archived (bool): [optional]  # noqa: E501
            ci_uid (int): [optional]  # noqa: E501
            variable_values ({str: ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},)}): [optional]  # noqa: E501
            password_variable_values ({str: ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},)}): [optional]  # noqa: E501
            ci_property_variables ([Variable]): [optional]  # noqa: E501
            all_string_variable_values ({str: (str,)}): [optional]  # noqa: E501
            all_release_global_and_folder_variables ([Variable]): [optional]  # noqa: E501
            all_variable_values_as_strings_with_interpolation_info ({str: (ValueWithInterpolation,)}): [optional]  # noqa: E501
            variables_keys_in_non_interpolatable_variable_values ([str]): [optional]  # noqa: E501
            variables_by_keys ({str: (Variable,)}): [optional]  # noqa: E501
            all_variables ([Variable]): [optional]  # noqa: E501
            global_variables (GlobalVariables): [optional]  # noqa: E501
            folder_variables (FolderVariables): [optional]  # noqa: E501
            admin_team (Team): [optional]  # noqa: E501
            release_attachments ([Attachment]): [optional]  # noqa: E501
            current_phase (Phase): [optional]  # noqa: E501
            current_task (Task): [optional]  # noqa: E501
            all_tasks ([Task]): [optional]  # noqa: E501
            all_gates ([GateTask]): [optional]  # noqa: E501
            all_user_input_tasks ([UserInputTask]): [optional]  # noqa: E501
            done (bool): [optional]  # noqa: E501
            planned_or_active (bool): [optional]  # noqa: E501
            active (bool): [optional]  # noqa: E501
            defunct (bool): [optional]  # noqa: E501
            updatable (bool): [optional]  # noqa: E501
            aborted (bool): [optional]  # noqa: E501
            failing (bool): [optional]  # noqa: E501
            failed (bool): [optional]  # noqa: E501
            paused (bool): [optional]  # noqa: E501
            template (bool): [optional]  # noqa: E501
            planned (bool): [optional]  # noqa: E501
            in_progress (bool): [optional]  # noqa: E501
            release (Release): [optional]  # noqa: E501
            release_uid (int): [optional]  # noqa: E501
            display_path (str): [optional]  # noqa: E501
            children ([PlanItem]): [optional]  # noqa: E501
            all_plan_items ([PlanItem]): [optional]  # noqa: E501
            url (str): [optional]  # noqa: E501
            active_tasks ([Task]): [optional]  # noqa: E501
            variable_usages ([UsagePoint]): [optional]  # noqa: E501
            pending (bool): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """Release - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            id (str): [optional]  # noqa: E501
            type (str): [optional]  # noqa: E501
            start_date (datetime): [optional]  # noqa: E501
            scheduled_start_date (datetime): [optional]  # noqa: E501
            end_date (datetime): [optional]  # noqa: E501
            due_date (datetime): [optional]  # noqa: E501
            title (str): [optional]  # noqa: E501
            description (str): [optional]  # noqa: E501
            owner (str): [optional]  # noqa: E501
            planned_duration (int): [optional]  # noqa: E501
            flag_status (FlagStatus): [optional]  # noqa: E501
            flag_comment (str): [optional]  # noqa: E501
            overdue_notified (bool): [optional]  # noqa: E501
            flagged (bool): [optional]  # noqa: E501
            start_or_scheduled_date (datetime): [optional]  # noqa: E501
            end_or_due_date (datetime): [optional]  # noqa: E501
            overdue (bool): [optional]  # noqa: E501
            or_calculate_due_date (str, none_type): [optional]  # noqa: E501
            computed_planned_duration ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): [optional]  # noqa: E501
            actual_duration ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): [optional]  # noqa: E501
            root_release_id (str): [optional]  # noqa: E501
            max_concurrent_releases (int): [optional]  # noqa: E501
            release_triggers ([ReleaseTrigger]): [optional]  # noqa: E501
            teams ([Team]): [optional]  # noqa: E501
            member_viewers ([str]): [optional]  # noqa: E501
            role_viewers ([str]): [optional]  # noqa: E501
            attachments ([Attachment]): [optional]  # noqa: E501
            phases ([Phase]): [optional]  # noqa: E501
            queryable_start_date (datetime): [optional]  # noqa: E501
            queryable_end_date (datetime): [optional]  # noqa: E501
            real_flag_status (FlagStatus): [optional]  # noqa: E501
            status (ReleaseStatus): [optional]  # noqa: E501
            tags ([str]): [optional]  # noqa: E501
            variables ([Variable]): [optional]  # noqa: E501
            calendar_link_token (str): [optional]  # noqa: E501
            calendar_published (bool): [optional]  # noqa: E501
            tutorial (bool): [optional]  # noqa: E501
            abort_on_failure (bool): [optional]  # noqa: E501
            archive_release (bool): [optional]  # noqa: E501
            allow_passwords_in_all_fields (bool): [optional]  # noqa: E501
            disable_notifications (bool): [optional]  # noqa: E501
            allow_concurrent_releases_from_trigger (bool): [optional]  # noqa: E501
            origin_template_id (str): [optional]  # noqa: E501
            created_from_trigger (bool): [optional]  # noqa: E501
            script_username (str): [optional]  # noqa: E501
            script_user_password (str): [optional]  # noqa: E501
            extensions ([ReleaseExtension]): [optional]  # noqa: E501
            started_from_task_id (str): [optional]  # noqa: E501
            auto_start (bool): [optional]  # noqa: E501
            automated_resume_count (int): [optional]  # noqa: E501
            max_automated_resumes (int): [optional]  # noqa: E501
            abort_comment (str): [optional]  # noqa: E501
            variable_mapping ({str: (str,)}): [optional]  # noqa: E501
            risk_profile (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            metadata ({str: (dict,)}): [optional]  # noqa: E501
            archived (bool): [optional]  # noqa: E501
            ci_uid (int): [optional]  # noqa: E501
            variable_values ({str: ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},)}): [optional]  # noqa: E501
            password_variable_values ({str: ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},)}): [optional]  # noqa: E501
            ci_property_variables ([Variable]): [optional]  # noqa: E501
            all_string_variable_values ({str: (str,)}): [optional]  # noqa: E501
            all_release_global_and_folder_variables ([Variable]): [optional]  # noqa: E501
            all_variable_values_as_strings_with_interpolation_info ({str: (ValueWithInterpolation,)}): [optional]  # noqa: E501
            variables_keys_in_non_interpolatable_variable_values ([str]): [optional]  # noqa: E501
            variables_by_keys ({str: (Variable,)}): [optional]  # noqa: E501
            all_variables ([Variable]): [optional]  # noqa: E501
            global_variables (GlobalVariables): [optional]  # noqa: E501
            folder_variables (FolderVariables): [optional]  # noqa: E501
            admin_team (Team): [optional]  # noqa: E501
            release_attachments ([Attachment]): [optional]  # noqa: E501
            current_phase (Phase): [optional]  # noqa: E501
            current_task (Task): [optional]  # noqa: E501
            all_tasks ([Task]): [optional]  # noqa: E501
            all_gates ([GateTask]): [optional]  # noqa: E501
            all_user_input_tasks ([UserInputTask]): [optional]  # noqa: E501
            done (bool): [optional]  # noqa: E501
            planned_or_active (bool): [optional]  # noqa: E501
            active (bool): [optional]  # noqa: E501
            defunct (bool): [optional]  # noqa: E501
            updatable (bool): [optional]  # noqa: E501
            aborted (bool): [optional]  # noqa: E501
            failing (bool): [optional]  # noqa: E501
            failed (bool): [optional]  # noqa: E501
            paused (bool): [optional]  # noqa: E501
            template (bool): [optional]  # noqa: E501
            planned (bool): [optional]  # noqa: E501
            in_progress (bool): [optional]  # noqa: E501
            release (Release): [optional]  # noqa: E501
            release_uid (int): [optional]  # noqa: E501
            display_path (str): [optional]  # noqa: E501
            children ([PlanItem]): [optional]  # noqa: E501
            all_plan_items ([PlanItem]): [optional]  # noqa: E501
            url (str): [optional]  # noqa: E501
            active_tasks ([Task]): [optional]  # noqa: E501
            variable_usages ([UsagePoint]): [optional]  # noqa: E501
            pending (bool): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
