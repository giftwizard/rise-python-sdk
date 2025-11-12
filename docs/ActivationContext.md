# ActivationContext



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activation_id** | **str** | Activation ID | [optional] 
**action_id** | **str** | Action ID | [optional] 
**configuration_id** | **str** | Configuration ID | [optional] 
**configuration_correlation_id** | **str** | Configuration Correlation ID | [optional] 
**event_name** | **str** | name of the event. intended to keep backwards compatibility, probably not in use. | [optional] 
**event_slug** | **str** | Event slug, also probably not in use | [optional] 
**enriched_event_payload** | **str** | Enriched event payload | [optional] 
**raw_event_payload** | **str** | Raw event payload | [optional] 
**actions** | **List[object]** | Actions | [optional] 
**activation_status** | **str** | Activation status | [optional] 
**external_id** | **str** | External ID | [optional] 
**automation_v2** | **object** | Automation | [optional] 
**output** | **str** | Output | [optional] 

## Example

```python
from openapi_client.models.activation_context import ActivationContext

# TODO update the JSON string below
json = "{}"
# create an instance of ActivationContext from a JSON string
activation_context_instance = ActivationContext.from_json(json)
# print the JSON string representation of the object
print(ActivationContext.to_json())

# convert the object into a dict
activation_context_dict = activation_context_instance.to_dict()
# create an instance of ActivationContext from a dict
activation_context_from_dict = ActivationContext.from_dict(activation_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


