# ActivationContinuedAfterSchedule



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Activation identifier | [optional] 
**automation** | **object** | Activation Automation | [optional] 

## Example

```python
from openapi_client.models.activation_continued_after_schedule import ActivationContinuedAfterSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of ActivationContinuedAfterSchedule from a JSON string
activation_continued_after_schedule_instance = ActivationContinuedAfterSchedule.from_json(json)
# print the JSON string representation of the object
print(ActivationContinuedAfterSchedule.to_json())

# convert the object into a dict
activation_continued_after_schedule_dict = activation_continued_after_schedule_instance.to_dict()
# create an instance of ActivationContinuedAfterSchedule from a dict
activation_continued_after_schedule_from_dict = ActivationContinuedAfterSchedule.from_dict(activation_continued_after_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


