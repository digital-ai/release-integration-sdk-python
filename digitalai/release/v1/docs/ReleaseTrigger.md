# ReleaseTrigger


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**script** | **str** |  | [optional] 
**abort_script** | **str** |  | [optional] 
**ci_uid** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**trigger_state** | **str** |  | [optional] 
**folder_id** | **str** |  | [optional] 
**allow_parallel_execution** | **bool** |  | [optional] 
**last_run_date** | **datetime** |  | [optional] 
**last_run_status** | [**TriggerExecutionStatus**](TriggerExecutionStatus.md) |  | [optional] 
**poll_type** | [**PollType**](PollType.md) |  | [optional] 
**periodicity** | **str** |  | [optional] 
**initial_fire** | **bool** |  | [optional] 
**release_title** | **str** |  | [optional] 
**execution_id** | **str** |  | [optional] 
**variables** | [**[Variable]**](Variable.md) |  | [optional] 
**template** | **str** |  | [optional] 
**tags** | **[str]** |  | [optional] 
**release_folder** | **str** |  | [optional] 
**internal_properties** | **[str]** |  | [optional] 
**template_variables** | **{str: (str,)}** |  | [optional] 
**template_password_variables** | **{str: (str,)}** |  | [optional] 
**trigger_state_from_results** | **str** |  | [optional] 
**script_variable_names** | **[str]** |  | [optional] 
**script_variables_from_results** | **{str: ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},)}** |  | [optional] 
**string_script_variable_values** | **{str: (str,)}** |  | [optional] 
**script_variable_values** | **{str: ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},)}** |  | [optional] 
**variables_by_keys** | [**{str: (Variable,)}**](Variable.md) |  | [optional] 
**container_id** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


