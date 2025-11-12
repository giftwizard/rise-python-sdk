# RunAutomationRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** | App of the automation trigger | [optional] 
**trigger_key** | **str** | Trigger key of the action | [optional] 
**trigger_payload** | **object** | Payload of the triggered event | [optional] 
**automation_id** | **str** | Specific automation id to run | [optional] 
**trigger_schema** | **object** | Schema of the trigger | [optional] 
**skip_retry** | **bool** | Skip retry mechanism. If set to true, we will not retry the automations actions in case of a retryable error. | [optional] 

## Example

```python
from openapi_client.models.run_automation_request import RunAutomationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RunAutomationRequest from a JSON string
run_automation_request_instance = RunAutomationRequest.from_json(json)
# print the JSON string representation of the object
print(RunAutomationRequest.to_json())

# convert the object into a dict
run_automation_request_dict = run_automation_request_instance.to_dict()
# create an instance of RunAutomationRequest from a dict
run_automation_request_from_dict = RunAutomationRequest.from_dict(run_automation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


