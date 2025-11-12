# VoidOptionsVoidOptions

Information about a transaction that comes to void a previous transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | ID of the transaction being voided. | [optional] 

## Example

```python
from openapi_client.models.void_options_void_options import VoidOptionsVoidOptions

# TODO update the JSON string below
json = "{}"
# create an instance of VoidOptionsVoidOptions from a JSON string
void_options_void_options_instance = VoidOptionsVoidOptions.from_json(json)
# print the JSON string representation of the object
print(VoidOptionsVoidOptions.to_json())

# convert the object into a dict
void_options_void_options_dict = void_options_void_options_instance.to_dict()
# create an instance of VoidOptionsVoidOptions from a dict
void_options_void_options_from_dict = VoidOptionsVoidOptions.from_dict(void_options_void_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


