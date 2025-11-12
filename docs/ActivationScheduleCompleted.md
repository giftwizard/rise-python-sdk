# ActivationScheduleCompleted



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Activation identifier | [optional] 
**schedule_id** | **str** | Activation schedule identifier | [optional] 
**schedule_date** | **datetime** | Activation schedule due date | [optional] 
**payload** | **object** | Activation payload | [optional] 
**automation** | **object** | Activation Automation | [optional] 
**external_entity_id** | **str** | Optional - external entity id that this activation is related to | [optional] 

## Example

```python
from openapi_client.models.activation_schedule_completed import ActivationScheduleCompleted

# TODO update the JSON string below
json = "{}"
# create an instance of ActivationScheduleCompleted from a JSON string
activation_schedule_completed_instance = ActivationScheduleCompleted.from_json(json)
# print the JSON string representation of the object
print(ActivationScheduleCompleted.to_json())

# convert the object into a dict
activation_schedule_completed_dict = activation_schedule_completed_instance.to_dict()
# create an instance of ActivationScheduleCompleted from a dict
activation_schedule_completed_from_dict = ActivationScheduleCompleted.from_dict(activation_schedule_completed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


