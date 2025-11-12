# AutomationConfiguration

Automation runtime configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Status of the automation on the site. | [optional] 
**trigger** | **object** | Automation trigger configuration. | [optional] 
**root_action_ids** | **List[str]** | List of IDs of root actions. Root actions are the first actions to run after the trigger. The actions in the list run in parallel. | [optional] 
**actions** | [**Actions**](Actions.md) |  | [optional] 

## Example

```python
from openapi_client.models.automation_configuration import AutomationConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of AutomationConfiguration from a JSON string
automation_configuration_instance = AutomationConfiguration.from_json(json)
# print the JSON string representation of the object
print(AutomationConfiguration.to_json())

# convert the object into a dict
automation_configuration_dict = automation_configuration_instance.to_dict()
# create an instance of AutomationConfiguration from a dict
automation_configuration_from_dict = AutomationConfiguration.from_dict(automation_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


