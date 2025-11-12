# AutomationSettings



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hidden** | **bool** | Whether the automation is hidden from users. Default: &#x60;false&#x60; | [optional] 
**readonly** | **bool** | Whether the automation is read-only. Default: &#x60;false&#x60; | [optional] 
**disable_delete** | **bool** | Whether the option to delete the automation from the site is disabled. Default: &#x60;false&#x60; | [optional] 
**disable_status_change** | **bool** | Whether the option to change the automation status (from active to inactive and vice versa) is disabled. Default: &#x60;false&#x60; | [optional] 
**action_settings** | **object** | Automation action settings. | [optional] 

## Example

```python
from openapi_client.models.automation_settings import AutomationSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AutomationSettings from a JSON string
automation_settings_instance = AutomationSettings.from_json(json)
# print the JSON string representation of the object
print(AutomationSettings.to_json())

# convert the object into a dict
automation_settings_dict = automation_settings_instance.to_dict()
# create an instance of AutomationSettings from a dict
automation_settings_from_dict = AutomationSettings.from_dict(automation_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


