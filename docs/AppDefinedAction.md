# AppDefinedAction



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** | ID of the app that defines the action. | [optional] 
**action_key** | **str** | Action key. | [optional] 
**input_mapping** | **object** | Action input mapping. | [optional] 
**skip_condition_or_expression_groups** | **List[object]** | Array of conditions determining whether to skip the action in the automation flow. The action will be skipped if any of the expression groups evaluate to &#x60;true&#x60;. Actions following a skipped action will still run. | [optional] 
**post_action_ids** | **List[str]** | List of IDs of actions to run in parallel once the action completes. | [optional] 
**override_output_schema** | **object** | Optional output schema of the action. It will be used instead the action schema in case it&#39;s provided. | [optional] 

## Example

```python
from openapi_client.models.app_defined_action import AppDefinedAction

# TODO update the JSON string below
json = "{}"
# create an instance of AppDefinedAction from a JSON string
app_defined_action_instance = AppDefinedAction.from_json(json)
# print the JSON string representation of the object
print(AppDefinedAction.to_json())

# convert the object into a dict
app_defined_action_dict = app_defined_action_instance.to_dict()
# create an instance of AppDefinedAction from a dict
app_defined_action_from_dict = AppDefinedAction.from_dict(app_defined_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


