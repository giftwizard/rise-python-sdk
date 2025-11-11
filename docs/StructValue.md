# StructValue

Circular reference to #/components/schemas/google.protobuf.Struct (simplified)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**struct_value** | **object** | Circular reference to #/components/schemas/google.protobuf.Struct (simplified) | [optional] 

## Example

```python
from openapi_client.models.struct_value import StructValue

# TODO update the JSON string below
json = "{}"
# create an instance of StructValue from a JSON string
struct_value_instance = StructValue.from_json(json)
# print the JSON string representation of the object
print(StructValue.to_json())

# convert the object into a dict
struct_value_dict = struct_value_instance.to_dict()
# create an instance of StructValue from a dict
struct_value_from_dict = StructValue.from_dict(struct_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


