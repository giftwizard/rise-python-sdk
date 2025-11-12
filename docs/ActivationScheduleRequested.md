# ActivationScheduleRequested



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Activation identifier | [optional] 
**requested_date** | **datetime** | Activation schedule request date | [optional] 
**schedule_date** | **datetime** | Activation schedule due date | [optional] 
**payload** | **object** | Activation payload | [optional] 
**automation** | **object** | Activation Automation | [optional] 
**external_entity_id** | **str** | Optional - external entity id that this activation is related to | [optional] 

## Example

```python
from openapi_client.models.activation_schedule_requested import ActivationScheduleRequested

# TODO update the JSON string below
json = "{}"
# create an instance of ActivationScheduleRequested from a JSON string
activation_schedule_requested_instance = ActivationScheduleRequested.from_json(json)
# print the JSON string representation of the object
print(ActivationScheduleRequested.to_json())

# convert the object into a dict
activation_schedule_requested_dict = activation_schedule_requested_instance.to_dict()
# create an instance of ActivationScheduleRequested from a dict
activation_schedule_requested_from_dict = ActivationScheduleRequested.from_dict(activation_schedule_requested_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


