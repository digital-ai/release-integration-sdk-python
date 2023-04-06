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
    from digitalai.release.v1.model.blackout_metadata import BlackoutMetadata
    from digitalai.release.v1.model.comment import Comment
    from digitalai.release.v1.model.dependency import Dependency
    from digitalai.release.v1.model.facet import Facet
    from digitalai.release.v1.model.flag_status import FlagStatus
    from digitalai.release.v1.model.gate_condition import GateCondition
    from digitalai.release.v1.model.phase import Phase
    from digitalai.release.v1.model.plan_item import PlanItem
    from digitalai.release.v1.model.release import Release
    from digitalai.release.v1.model.task import Task
    from digitalai.release.v1.model.task_container import TaskContainer
    from digitalai.release.v1.model.task_recover_op import TaskRecoverOp
    from digitalai.release.v1.model.task_status import TaskStatus
    from digitalai.release.v1.model.usage_point import UsagePoint
    from digitalai.release.v1.model.variable import Variable
    globals()['Attachment'] = Attachment
    globals()['BlackoutMetadata'] = BlackoutMetadata
    globals()['Comment'] = Comment
    globals()['Dependency'] = Dependency
    globals()['Facet'] = Facet
    globals()['FlagStatus'] = FlagStatus
    globals()['GateCondition'] = GateCondition
    globals()['Phase'] = Phase
    globals()['PlanItem'] = PlanItem
    globals()['Release'] = Release
    globals()['Task'] = Task
    globals()['TaskContainer'] = TaskContainer
    globals()['TaskRecoverOp'] = TaskRecoverOp
    globals()['TaskStatus'] = TaskStatus
    globals()['UsagePoint'] = UsagePoint
    globals()['Variable'] = Variable


class GateTask(ModelNormal):
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
        ('watchers',): {
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
            'scheduled_start_date': (datetime,),  # noqa: E501
            'flag_status': (FlagStatus,),  # noqa: E501
            'title': (str,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'owner': (str,),  # noqa: E501
            'due_date': (datetime,),  # noqa: E501
            'start_date': (datetime,),  # noqa: E501
            'end_date': (datetime,),  # noqa: E501
            'planned_duration': (int,),  # noqa: E501
            'flag_comment': (str,),  # noqa: E501
            'overdue_notified': (bool,),  # noqa: E501
            'flagged': (bool,),  # noqa: E501
            'start_or_scheduled_date': (datetime,),  # noqa: E501
            'end_or_due_date': (datetime,),  # noqa: E501
            'overdue': (bool,),  # noqa: E501
            'or_calculate_due_date': (str, none_type,),  # noqa: E501
            'computed_planned_duration': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'actual_duration': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'release_uid': (int,),  # noqa: E501
            'ci_uid': (int,),  # noqa: E501
            'comments': ([Comment],),  # noqa: E501
            'container': (TaskContainer,),  # noqa: E501
            'facets': ([Facet],),  # noqa: E501
            'attachments': ([Attachment],),  # noqa: E501
            'status': (TaskStatus,),  # noqa: E501
            'team': (str,),  # noqa: E501
            'watchers': ([str],),  # noqa: E501
            'wait_for_scheduled_start_date': (bool,),  # noqa: E501
            'delay_during_blackout': (bool,),  # noqa: E501
            'postponed_due_to_blackout': (bool,),  # noqa: E501
            'postponed_until_environments_are_reserved': (bool,),  # noqa: E501
            'original_scheduled_start_date': (datetime,),  # noqa: E501
            'has_been_flagged': (bool,),  # noqa: E501
            'has_been_delayed': (bool,),  # noqa: E501
            'precondition': (str,),  # noqa: E501
            'failure_handler': (str,),  # noqa: E501
            'task_failure_handler_enabled': (bool,),  # noqa: E501
            'task_recover_op': (TaskRecoverOp,),  # noqa: E501
            'failures_count': (int,),  # noqa: E501
            'execution_id': (str,),  # noqa: E501
            'variable_mapping': ({str: (str,)},),  # noqa: E501
            'external_variable_mapping': ({str: (str,)},),  # noqa: E501
            'max_comment_size': (int,),  # noqa: E501
            'tags': ([str],),  # noqa: E501
            'configuration_uri': (str,),  # noqa: E501
            'due_soon_notified': (bool,),  # noqa: E501
            'locked': (bool,),  # noqa: E501
            'check_attributes': (bool,),  # noqa: E501
            'abort_script': (str,),  # noqa: E501
            'phase': (Phase,),  # noqa: E501
            'blackout_metadata': (BlackoutMetadata,),  # noqa: E501
            'flagged_count': (int,),  # noqa: E501
            'delayed_count': (int,),  # noqa: E501
            'done': (bool,),  # noqa: E501
            'done_in_advance': (bool,),  # noqa: E501
            'defunct': (bool,),  # noqa: E501
            'updatable': (bool,),  # noqa: E501
            'aborted': (bool,),  # noqa: E501
            'not_yet_reached': (bool,),  # noqa: E501
            'planned': (bool,),  # noqa: E501
            'active': (bool,),  # noqa: E501
            'in_progress': (bool,),  # noqa: E501
            'pending': (bool,),  # noqa: E501
            'waiting_for_input': (bool,),  # noqa: E501
            'failed': (bool,),  # noqa: E501
            'failing': (bool,),  # noqa: E501
            'completed_in_advance': (bool,),  # noqa: E501
            'skipped': (bool,),  # noqa: E501
            'skipped_in_advance': (bool,),  # noqa: E501
            'precondition_in_progress': (bool,),  # noqa: E501
            'failure_handler_in_progress': (bool,),  # noqa: E501
            'abort_script_in_progress': (bool,),  # noqa: E501
            'facet_in_progress': (bool,),  # noqa: E501
            'movable': (bool,),  # noqa: E501
            'gate': (bool,),  # noqa: E501
            'task_group': (bool,),  # noqa: E501
            'parallel_group': (bool,),  # noqa: E501
            'precondition_enabled': (bool,),  # noqa: E501
            'failure_handler_enabled': (bool,),  # noqa: E501
            'release': (Release,),  # noqa: E501
            'display_path': (str,),  # noqa: E501
            'release_owner': (str,),  # noqa: E501
            'all_tasks': ([Task],),  # noqa: E501
            'children': ([PlanItem],),  # noqa: E501
            'input_variables': ([Variable],),  # noqa: E501
            'referenced_variables': ([Variable],),  # noqa: E501
            'unbound_required_variables': ([str],),  # noqa: E501
            'automated': (bool,),  # noqa: E501
            'task_type': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'due_soon': (bool,),  # noqa: E501
            'elapsed_duration_fraction': (float,),  # noqa: E501
            'url': (str,),  # noqa: E501
            'conditions': ([GateCondition],),  # noqa: E501
            'dependencies': ([Dependency],),  # noqa: E501
            'open': (bool,),  # noqa: E501
            'open_in_advance': (bool,),  # noqa: E501
            'completable': (bool,),  # noqa: E501
            'aborted_dependency_titles': (str,),  # noqa: E501
            'variable_usages': ([UsagePoint],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'type': 'type',  # noqa: E501
        'scheduled_start_date': 'scheduledStartDate',  # noqa: E501
        'flag_status': 'flagStatus',  # noqa: E501
        'title': 'title',  # noqa: E501
        'description': 'description',  # noqa: E501
        'owner': 'owner',  # noqa: E501
        'due_date': 'dueDate',  # noqa: E501
        'start_date': 'startDate',  # noqa: E501
        'end_date': 'endDate',  # noqa: E501
        'planned_duration': 'plannedDuration',  # noqa: E501
        'flag_comment': 'flagComment',  # noqa: E501
        'overdue_notified': 'overdueNotified',  # noqa: E501
        'flagged': 'flagged',  # noqa: E501
        'start_or_scheduled_date': 'startOrScheduledDate',  # noqa: E501
        'end_or_due_date': 'endOrDueDate',  # noqa: E501
        'overdue': 'overdue',  # noqa: E501
        'or_calculate_due_date': 'orCalculateDueDate',  # noqa: E501
        'computed_planned_duration': 'computedPlannedDuration',  # noqa: E501
        'actual_duration': 'actualDuration',  # noqa: E501
        'release_uid': 'releaseUid',  # noqa: E501
        'ci_uid': 'ciUid',  # noqa: E501
        'comments': 'comments',  # noqa: E501
        'container': 'container',  # noqa: E501
        'facets': 'facets',  # noqa: E501
        'attachments': 'attachments',  # noqa: E501
        'status': 'status',  # noqa: E501
        'team': 'team',  # noqa: E501
        'watchers': 'watchers',  # noqa: E501
        'wait_for_scheduled_start_date': 'waitForScheduledStartDate',  # noqa: E501
        'delay_during_blackout': 'delayDuringBlackout',  # noqa: E501
        'postponed_due_to_blackout': 'postponedDueToBlackout',  # noqa: E501
        'postponed_until_environments_are_reserved': 'postponedUntilEnvironmentsAreReserved',  # noqa: E501
        'original_scheduled_start_date': 'originalScheduledStartDate',  # noqa: E501
        'has_been_flagged': 'hasBeenFlagged',  # noqa: E501
        'has_been_delayed': 'hasBeenDelayed',  # noqa: E501
        'precondition': 'precondition',  # noqa: E501
        'failure_handler': 'failureHandler',  # noqa: E501
        'task_failure_handler_enabled': 'taskFailureHandlerEnabled',  # noqa: E501
        'task_recover_op': 'taskRecoverOp',  # noqa: E501
        'failures_count': 'failuresCount',  # noqa: E501
        'execution_id': 'executionId',  # noqa: E501
        'variable_mapping': 'variableMapping',  # noqa: E501
        'external_variable_mapping': 'externalVariableMapping',  # noqa: E501
        'max_comment_size': 'maxCommentSize',  # noqa: E501
        'tags': 'tags',  # noqa: E501
        'configuration_uri': 'configurationUri',  # noqa: E501
        'due_soon_notified': 'dueSoonNotified',  # noqa: E501
        'locked': 'locked',  # noqa: E501
        'check_attributes': 'checkAttributes',  # noqa: E501
        'abort_script': 'abortScript',  # noqa: E501
        'phase': 'phase',  # noqa: E501
        'blackout_metadata': 'blackoutMetadata',  # noqa: E501
        'flagged_count': 'flaggedCount',  # noqa: E501
        'delayed_count': 'delayedCount',  # noqa: E501
        'done': 'done',  # noqa: E501
        'done_in_advance': 'doneInAdvance',  # noqa: E501
        'defunct': 'defunct',  # noqa: E501
        'updatable': 'updatable',  # noqa: E501
        'aborted': 'aborted',  # noqa: E501
        'not_yet_reached': 'notYetReached',  # noqa: E501
        'planned': 'planned',  # noqa: E501
        'active': 'active',  # noqa: E501
        'in_progress': 'inProgress',  # noqa: E501
        'pending': 'pending',  # noqa: E501
        'waiting_for_input': 'waitingForInput',  # noqa: E501
        'failed': 'failed',  # noqa: E501
        'failing': 'failing',  # noqa: E501
        'completed_in_advance': 'completedInAdvance',  # noqa: E501
        'skipped': 'skipped',  # noqa: E501
        'skipped_in_advance': 'skippedInAdvance',  # noqa: E501
        'precondition_in_progress': 'preconditionInProgress',  # noqa: E501
        'failure_handler_in_progress': 'failureHandlerInProgress',  # noqa: E501
        'abort_script_in_progress': 'abortScriptInProgress',  # noqa: E501
        'facet_in_progress': 'facetInProgress',  # noqa: E501
        'movable': 'movable',  # noqa: E501
        'gate': 'gate',  # noqa: E501
        'task_group': 'taskGroup',  # noqa: E501
        'parallel_group': 'parallelGroup',  # noqa: E501
        'precondition_enabled': 'preconditionEnabled',  # noqa: E501
        'failure_handler_enabled': 'failureHandlerEnabled',  # noqa: E501
        'release': 'release',  # noqa: E501
        'display_path': 'displayPath',  # noqa: E501
        'release_owner': 'releaseOwner',  # noqa: E501
        'all_tasks': 'allTasks',  # noqa: E501
        'children': 'children',  # noqa: E501
        'input_variables': 'inputVariables',  # noqa: E501
        'referenced_variables': 'referencedVariables',  # noqa: E501
        'unbound_required_variables': 'unboundRequiredVariables',  # noqa: E501
        'automated': 'automated',  # noqa: E501
        'task_type': 'taskType',  # noqa: E501
        'due_soon': 'dueSoon',  # noqa: E501
        'elapsed_duration_fraction': 'elapsedDurationFraction',  # noqa: E501
        'url': 'url',  # noqa: E501
        'conditions': 'conditions',  # noqa: E501
        'dependencies': 'dependencies',  # noqa: E501
        'open': 'open',  # noqa: E501
        'open_in_advance': 'openInAdvance',  # noqa: E501
        'completable': 'completable',  # noqa: E501
        'aborted_dependency_titles': 'abortedDependencyTitles',  # noqa: E501
        'variable_usages': 'variableUsages',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """GateTask - a model defined in OpenAPI

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
            scheduled_start_date (datetime): [optional]  # noqa: E501
            flag_status (FlagStatus): [optional]  # noqa: E501
            title (str): [optional]  # noqa: E501
            description (str): [optional]  # noqa: E501
            owner (str): [optional]  # noqa: E501
            due_date (datetime): [optional]  # noqa: E501
            start_date (datetime): [optional]  # noqa: E501
            end_date (datetime): [optional]  # noqa: E501
            planned_duration (int): [optional]  # noqa: E501
            flag_comment (str): [optional]  # noqa: E501
            overdue_notified (bool): [optional]  # noqa: E501
            flagged (bool): [optional]  # noqa: E501
            start_or_scheduled_date (datetime): [optional]  # noqa: E501
            end_or_due_date (datetime): [optional]  # noqa: E501
            overdue (bool): [optional]  # noqa: E501
            or_calculate_due_date (str, none_type): [optional]  # noqa: E501
            computed_planned_duration ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): [optional]  # noqa: E501
            actual_duration ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): [optional]  # noqa: E501
            release_uid (int): [optional]  # noqa: E501
            ci_uid (int): [optional]  # noqa: E501
            comments ([Comment]): [optional]  # noqa: E501
            container (TaskContainer): [optional]  # noqa: E501
            facets ([Facet]): [optional]  # noqa: E501
            attachments ([Attachment]): [optional]  # noqa: E501
            status (TaskStatus): [optional]  # noqa: E501
            team (str): [optional]  # noqa: E501
            watchers ([str]): [optional]  # noqa: E501
            wait_for_scheduled_start_date (bool): [optional]  # noqa: E501
            delay_during_blackout (bool): [optional]  # noqa: E501
            postponed_due_to_blackout (bool): [optional]  # noqa: E501
            postponed_until_environments_are_reserved (bool): [optional]  # noqa: E501
            original_scheduled_start_date (datetime): [optional]  # noqa: E501
            has_been_flagged (bool): [optional]  # noqa: E501
            has_been_delayed (bool): [optional]  # noqa: E501
            precondition (str): [optional]  # noqa: E501
            failure_handler (str): [optional]  # noqa: E501
            task_failure_handler_enabled (bool): [optional]  # noqa: E501
            task_recover_op (TaskRecoverOp): [optional]  # noqa: E501
            failures_count (int): [optional]  # noqa: E501
            execution_id (str): [optional]  # noqa: E501
            variable_mapping ({str: (str,)}): [optional]  # noqa: E501
            external_variable_mapping ({str: (str,)}): [optional]  # noqa: E501
            max_comment_size (int): [optional]  # noqa: E501
            tags ([str]): [optional]  # noqa: E501
            configuration_uri (str): [optional]  # noqa: E501
            due_soon_notified (bool): [optional]  # noqa: E501
            locked (bool): [optional]  # noqa: E501
            check_attributes (bool): [optional]  # noqa: E501
            abort_script (str): [optional]  # noqa: E501
            phase (Phase): [optional]  # noqa: E501
            blackout_metadata (BlackoutMetadata): [optional]  # noqa: E501
            flagged_count (int): [optional]  # noqa: E501
            delayed_count (int): [optional]  # noqa: E501
            done (bool): [optional]  # noqa: E501
            done_in_advance (bool): [optional]  # noqa: E501
            defunct (bool): [optional]  # noqa: E501
            updatable (bool): [optional]  # noqa: E501
            aborted (bool): [optional]  # noqa: E501
            not_yet_reached (bool): [optional]  # noqa: E501
            planned (bool): [optional]  # noqa: E501
            active (bool): [optional]  # noqa: E501
            in_progress (bool): [optional]  # noqa: E501
            pending (bool): [optional]  # noqa: E501
            waiting_for_input (bool): [optional]  # noqa: E501
            failed (bool): [optional]  # noqa: E501
            failing (bool): [optional]  # noqa: E501
            completed_in_advance (bool): [optional]  # noqa: E501
            skipped (bool): [optional]  # noqa: E501
            skipped_in_advance (bool): [optional]  # noqa: E501
            precondition_in_progress (bool): [optional]  # noqa: E501
            failure_handler_in_progress (bool): [optional]  # noqa: E501
            abort_script_in_progress (bool): [optional]  # noqa: E501
            facet_in_progress (bool): [optional]  # noqa: E501
            movable (bool): [optional]  # noqa: E501
            gate (bool): [optional]  # noqa: E501
            task_group (bool): [optional]  # noqa: E501
            parallel_group (bool): [optional]  # noqa: E501
            precondition_enabled (bool): [optional]  # noqa: E501
            failure_handler_enabled (bool): [optional]  # noqa: E501
            release (Release): [optional]  # noqa: E501
            display_path (str): [optional]  # noqa: E501
            release_owner (str): [optional]  # noqa: E501
            all_tasks ([Task]): [optional]  # noqa: E501
            children ([PlanItem]): [optional]  # noqa: E501
            input_variables ([Variable]): [optional]  # noqa: E501
            referenced_variables ([Variable]): [optional]  # noqa: E501
            unbound_required_variables ([str]): [optional]  # noqa: E501
            automated (bool): [optional]  # noqa: E501
            task_type ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): [optional]  # noqa: E501
            due_soon (bool): [optional]  # noqa: E501
            elapsed_duration_fraction (float): [optional]  # noqa: E501
            url (str): [optional]  # noqa: E501
            conditions ([GateCondition]): [optional]  # noqa: E501
            dependencies ([Dependency]): [optional]  # noqa: E501
            open (bool): [optional]  # noqa: E501
            open_in_advance (bool): [optional]  # noqa: E501
            completable (bool): [optional]  # noqa: E501
            aborted_dependency_titles (str): [optional]  # noqa: E501
            variable_usages ([UsagePoint]): [optional]  # noqa: E501
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
        """GateTask - a model defined in OpenAPI

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
            scheduled_start_date (datetime): [optional]  # noqa: E501
            flag_status (FlagStatus): [optional]  # noqa: E501
            title (str): [optional]  # noqa: E501
            description (str): [optional]  # noqa: E501
            owner (str): [optional]  # noqa: E501
            due_date (datetime): [optional]  # noqa: E501
            start_date (datetime): [optional]  # noqa: E501
            end_date (datetime): [optional]  # noqa: E501
            planned_duration (int): [optional]  # noqa: E501
            flag_comment (str): [optional]  # noqa: E501
            overdue_notified (bool): [optional]  # noqa: E501
            flagged (bool): [optional]  # noqa: E501
            start_or_scheduled_date (datetime): [optional]  # noqa: E501
            end_or_due_date (datetime): [optional]  # noqa: E501
            overdue (bool): [optional]  # noqa: E501
            or_calculate_due_date (str, none_type): [optional]  # noqa: E501
            computed_planned_duration ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): [optional]  # noqa: E501
            actual_duration ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): [optional]  # noqa: E501
            release_uid (int): [optional]  # noqa: E501
            ci_uid (int): [optional]  # noqa: E501
            comments ([Comment]): [optional]  # noqa: E501
            container (TaskContainer): [optional]  # noqa: E501
            facets ([Facet]): [optional]  # noqa: E501
            attachments ([Attachment]): [optional]  # noqa: E501
            status (TaskStatus): [optional]  # noqa: E501
            team (str): [optional]  # noqa: E501
            watchers ([str]): [optional]  # noqa: E501
            wait_for_scheduled_start_date (bool): [optional]  # noqa: E501
            delay_during_blackout (bool): [optional]  # noqa: E501
            postponed_due_to_blackout (bool): [optional]  # noqa: E501
            postponed_until_environments_are_reserved (bool): [optional]  # noqa: E501
            original_scheduled_start_date (datetime): [optional]  # noqa: E501
            has_been_flagged (bool): [optional]  # noqa: E501
            has_been_delayed (bool): [optional]  # noqa: E501
            precondition (str): [optional]  # noqa: E501
            failure_handler (str): [optional]  # noqa: E501
            task_failure_handler_enabled (bool): [optional]  # noqa: E501
            task_recover_op (TaskRecoverOp): [optional]  # noqa: E501
            failures_count (int): [optional]  # noqa: E501
            execution_id (str): [optional]  # noqa: E501
            variable_mapping ({str: (str,)}): [optional]  # noqa: E501
            external_variable_mapping ({str: (str,)}): [optional]  # noqa: E501
            max_comment_size (int): [optional]  # noqa: E501
            tags ([str]): [optional]  # noqa: E501
            configuration_uri (str): [optional]  # noqa: E501
            due_soon_notified (bool): [optional]  # noqa: E501
            locked (bool): [optional]  # noqa: E501
            check_attributes (bool): [optional]  # noqa: E501
            abort_script (str): [optional]  # noqa: E501
            phase (Phase): [optional]  # noqa: E501
            blackout_metadata (BlackoutMetadata): [optional]  # noqa: E501
            flagged_count (int): [optional]  # noqa: E501
            delayed_count (int): [optional]  # noqa: E501
            done (bool): [optional]  # noqa: E501
            done_in_advance (bool): [optional]  # noqa: E501
            defunct (bool): [optional]  # noqa: E501
            updatable (bool): [optional]  # noqa: E501
            aborted (bool): [optional]  # noqa: E501
            not_yet_reached (bool): [optional]  # noqa: E501
            planned (bool): [optional]  # noqa: E501
            active (bool): [optional]  # noqa: E501
            in_progress (bool): [optional]  # noqa: E501
            pending (bool): [optional]  # noqa: E501
            waiting_for_input (bool): [optional]  # noqa: E501
            failed (bool): [optional]  # noqa: E501
            failing (bool): [optional]  # noqa: E501
            completed_in_advance (bool): [optional]  # noqa: E501
            skipped (bool): [optional]  # noqa: E501
            skipped_in_advance (bool): [optional]  # noqa: E501
            precondition_in_progress (bool): [optional]  # noqa: E501
            failure_handler_in_progress (bool): [optional]  # noqa: E501
            abort_script_in_progress (bool): [optional]  # noqa: E501
            facet_in_progress (bool): [optional]  # noqa: E501
            movable (bool): [optional]  # noqa: E501
            gate (bool): [optional]  # noqa: E501
            task_group (bool): [optional]  # noqa: E501
            parallel_group (bool): [optional]  # noqa: E501
            precondition_enabled (bool): [optional]  # noqa: E501
            failure_handler_enabled (bool): [optional]  # noqa: E501
            release (Release): [optional]  # noqa: E501
            display_path (str): [optional]  # noqa: E501
            release_owner (str): [optional]  # noqa: E501
            all_tasks ([Task]): [optional]  # noqa: E501
            children ([PlanItem]): [optional]  # noqa: E501
            input_variables ([Variable]): [optional]  # noqa: E501
            referenced_variables ([Variable]): [optional]  # noqa: E501
            unbound_required_variables ([str]): [optional]  # noqa: E501
            automated (bool): [optional]  # noqa: E501
            task_type ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): [optional]  # noqa: E501
            due_soon (bool): [optional]  # noqa: E501
            elapsed_duration_fraction (float): [optional]  # noqa: E501
            url (str): [optional]  # noqa: E501
            conditions ([GateCondition]): [optional]  # noqa: E501
            dependencies ([Dependency]): [optional]  # noqa: E501
            open (bool): [optional]  # noqa: E501
            open_in_advance (bool): [optional]  # noqa: E501
            completable (bool): [optional]  # noqa: E501
            aborted_dependency_titles (str): [optional]  # noqa: E501
            variable_usages ([UsagePoint]): [optional]  # noqa: E501
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
