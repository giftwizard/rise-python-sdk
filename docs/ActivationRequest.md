# ActivationRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activation_id** | **str** | Activation&#39;s ID. | [optional] 
**configuration_id** | **str** | Configuration&#39;s ID. | [optional] 
**configuration_correlation_id** | **str** |  | [optional] 
**event_name** | **str** | Received event name. | [optional] 
**event_slug** | **str** | Received event slug. | [optional] 
**event_payload** | **str** | Received event payload. | [optional] 
**actions** | **List[object]** | List of action data. | [optional] 
**external_id** | **str** | External ID. | [optional] 
**source** | **object** | The source of this activation | [optional] 
**actions_map** | **object** | Actions tree | [optional] 
**automation** | **object** | Automation V2. Used for reporting domain event until activation request will be deprecated. | [optional] 
**trigger_schema** | **object** | Trigger entity for the activation, available for v2 and v3 automations only | [optional] 

## Example

```python
from openapi_client.models.activation_request import ActivationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActivationRequest from a JSON string
activation_request_instance = ActivationRequest.from_json(json)
# print the JSON string representation of the object
print(ActivationRequest.to_json())

# convert the object into a dict
activation_request_dict = activation_request_instance.to_dict()
# create an instance of ActivationRequest from a dict
activation_request_from_dict = ActivationRequest.from_dict(activation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


