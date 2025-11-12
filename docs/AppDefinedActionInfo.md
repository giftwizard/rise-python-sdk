# AppDefinedActionInfo



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** | Action app ID | [optional] 
**action_key** | **str** | Action key | [optional] 

## Example

```python
from openapi_client.models.app_defined_action_info import AppDefinedActionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppDefinedActionInfo from a JSON string
app_defined_action_info_instance = AppDefinedActionInfo.from_json(json)
# print the JSON string representation of the object
print(AppDefinedActionInfo.to_json())

# convert the object into a dict
app_defined_action_info_dict = app_defined_action_info_instance.to_dict()
# create an instance of AppDefinedActionInfo from a dict
app_defined_action_info_from_dict = AppDefinedActionInfo.from_dict(app_defined_action_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


