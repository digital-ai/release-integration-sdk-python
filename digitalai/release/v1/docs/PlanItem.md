# PlanItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**owner** | **str** |  | [optional] 
**scheduled_start_date** | **datetime** |  | [optional] 
**due_date** | **datetime** |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**planned_duration** | **int** |  | [optional] 
**flag_status** | [**FlagStatus**](FlagStatus.md) |  | [optional] 
**flag_comment** | **str** |  | [optional] 
**overdue_notified** | **bool** |  | [optional] 
**flagged** | **bool** |  | [optional] 
**start_or_scheduled_date** | **datetime** |  | [optional] 
**end_or_due_date** | **datetime** |  | [optional] 
**children** | [**[PlanItem]**](PlanItem.md) |  | [optional] 
**overdue** | **bool** |  | [optional] 
**done** | **bool** |  | [optional] 
**release** | [**Release**](Release.md) |  | [optional] 
**release_uid** | **int** |  | [optional] 
**updatable** | **bool** |  | [optional] 
**display_path** | **str** |  | [optional] 
**aborted** | **bool** |  | [optional] 
**active** | **bool** |  | [optional] 
**variable_usages** | [**[UsagePoint]**](UsagePoint.md) |  | [optional] 
**or_calculate_due_date** | **str, none_type** |  | [optional] 
**computed_planned_duration** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**actual_duration** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


