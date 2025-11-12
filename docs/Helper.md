# Helper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**if_filter** | **object** |  | [optional] 
**switch_filter** | **object** |  | [optional] 
**delay** | **object** |  | [optional] 
**rate_limiting** | **object** |  | [optional] 
**condition_filter** | **object** |  | [optional] 
**output** | **object** |  | [optional] 
**set_variables** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.helper import Helper

# TODO update the JSON string below
json = "{}"
# create an instance of Helper from a JSON string
helper_instance = Helper.from_json(json)
# print the JSON string representation of the object
print(Helper.to_json())

# convert the object into a dict
helper_dict = helper_instance.to_dict()
# create an instance of Helper from a dict
helper_from_dict = Helper.from_dict(helper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


