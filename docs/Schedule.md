# Schedule



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**identifier** | **str** | doesn&#39;t have to be unique. example: triggerName+entityId | [optional] 
**configuration_correlation_id** | **str** |  | [optional] 
**activation_id** | **str** |  | [optional] 
**scheduled_action** | **object** |  | [optional] 
**event_payload** | **str** | Raw domain event, not enriched | [optional] 
**schedule_status** | **str** |  | [optional] [readonly] 
**schedule_date** | **datetime** |  | [optional] [readonly] 
**created_date** | **datetime** |  | [optional] [readonly] 
**updated_date** | **datetime** |  | [optional] [readonly] 
**overrideable** | **bool** |  | [optional] 
**trigger_info** | **object** |  | [optional] 
**automation** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.schedule import Schedule

# TODO update the JSON string below
json = "{}"
# create an instance of Schedule from a JSON string
schedule_instance = Schedule.from_json(json)
# print the JSON string representation of the object
print(Schedule.to_json())

# convert the object into a dict
schedule_dict = schedule_instance.to_dict()
# create an instance of Schedule from a dict
schedule_from_dict = Schedule.from_dict(schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


