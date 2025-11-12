# ActionSettings



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permanent_action_ids** | **List[str]** | List of actions that cannot be deleted. Default: Empty. All actions are deletable by default. | [optional] 
**readonly_action_ids** | **List[str]** | List of actions that cannot be edited. Default: Empty. All actions are editable by default. | [optional] 
**disable_delay_addition** | **bool** | Whether the option to add a delay is disabled for the automation. | [optional] 
**disable_condition_addition** | **bool** | Whether the option to add a condition is disabled for the automation. | [optional] 

## Example

```python
from openapi_client.models.action_settings import ActionSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ActionSettings from a JSON string
action_settings_instance = ActionSettings.from_json(json)
# print the JSON string representation of the object
print(ActionSettings.to_json())

# convert the object into a dict
action_settings_dict = action_settings_instance.to_dict()
# create an instance of ActionSettings from a dict
action_settings_from_dict = ActionSettings.from_dict(action_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


