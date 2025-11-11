# ScheduleActivationRequested



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Activation identifier | [optional] 
**external_entity_id** | **str** | Optional - external entity id that this activation is related to | [optional] 
**payload** | **object** | Activation payload | [optional] 
**automation** | **object** | Activation Automation | [optional] 
**schedule_date** | **datetime** | Activation schedule date | [optional] 

## Example

```python
from openapi_client.models.schedule_activation_requested import ScheduleActivationRequested

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleActivationRequested from a JSON string
schedule_activation_requested_instance = ScheduleActivationRequested.from_json(json)
# print the JSON string representation of the object
print(ScheduleActivationRequested.to_json())

# convert the object into a dict
schedule_activation_requested_dict = schedule_activation_requested_instance.to_dict()
# create an instance of ScheduleActivationRequested from a dict
schedule_activation_requested_from_dict = ScheduleActivationRequested.from_dict(schedule_activation_requested_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


