# ActivationResumeAfterDelay



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Activation identifier | [optional] 
**schedule_id** | **str** | Activation schedule identifier | [optional] 
**schedule_date** | **datetime** | Activation schedule due date | [optional] 
**payload** | **object** | Activation payload | [optional] 
**automation** | **object** | Activation Automation | [optional] 
**scheduled_action_id** | **str** | Scheduled action identifier - with the intent to execute that action&#39;s post actions | [optional] 
**external_entity_id** | **str** | Optional - external entity id that this activation is related to | [optional] 

## Example

```python
from openapi_client.models.activation_resume_after_delay import ActivationResumeAfterDelay

# TODO update the JSON string below
json = "{}"
# create an instance of ActivationResumeAfterDelay from a JSON string
activation_resume_after_delay_instance = ActivationResumeAfterDelay.from_json(json)
# print the JSON string representation of the object
print(ActivationResumeAfterDelay.to_json())

# convert the object into a dict
activation_resume_after_delay_dict = activation_resume_after_delay_instance.to_dict()
# create an instance of ActivationResumeAfterDelay from a dict
activation_resume_after_delay_from_dict = ActivationResumeAfterDelay.from_dict(activation_resume_after_delay_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


