# VoidOptions1

Information about a transaction that comes to void a previous transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**void_options** | [**VoidOptions1**](VoidOptions1.md) |  | [optional] 

## Example

```python
from openapi_client.models.void_options1 import VoidOptions1

# TODO update the JSON string below
json = "{}"
# create an instance of VoidOptions1 from a JSON string
void_options1_instance = VoidOptions1.from_json(json)
# print the JSON string representation of the object
print(VoidOptions1.to_json())

# convert the object into a dict
void_options1_dict = void_options1_instance.to_dict()
# create an instance of VoidOptions1 from a dict
void_options1_from_dict = VoidOptions1.from_dict(void_options1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


