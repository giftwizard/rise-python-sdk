# Value1



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**null_value** | **str** |  | [optional] 
**number_value** | **float** |  | [optional] 
**string_value** | **str** |  | [optional] 
**bool_value** | **bool** |  | [optional] 
**struct_value** | **object** | Circular reference to #/components/schemas/google.protobuf.Struct (simplified) | [optional] 
**list_value** | [**ListValueListValue**](ListValueListValue.md) |  | [optional] 

## Example

```python
from openapi_client.models.value1 import Value1

# TODO update the JSON string below
json = "{}"
# create an instance of Value1 from a JSON string
value1_instance = Value1.from_json(json)
# print the JSON string representation of the object
print(Value1.to_json())

# convert the object into a dict
value1_dict = value1_instance.to_dict()
# create an instance of Value1 from a dict
value1_from_dict = Value1.from_dict(value1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


