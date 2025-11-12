# TypeInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_defined_action_info** | **object** | APP DEFINED action additional info | [optional] 
**condition_action_info** | **object** | Condition action additional info | [optional] 
**rate_limit_action_info** | **object** | Rate limit action additional info | [optional] 
**delay_action_info** | **object** | Delay action additional info | [optional] 
**set_variables_action_info** | **object** | Set Variables action additional info | [optional] 

## Example

```python
from openapi_client.models.type_info import TypeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TypeInfo from a JSON string
type_info_instance = TypeInfo.from_json(json)
# print the JSON string representation of the object
print(TypeInfo.to_json())

# convert the object into a dict
type_info_dict = type_info_instance.to_dict()
# create an instance of TypeInfo from a dict
type_info_from_dict = TypeInfo.from_dict(type_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


