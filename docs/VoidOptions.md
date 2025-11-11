# VoidOptions



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | ID of the transaction being voided. | [optional] 

## Example

```python
from openapi_client.models.void_options import VoidOptions

# TODO update the JSON string below
json = "{}"
# create an instance of VoidOptions from a JSON string
void_options_instance = VoidOptions.from_json(json)
# print the JSON string representation of the object
print(VoidOptions.to_json())

# convert the object into a dict
void_options_dict = void_options_instance.to_dict()
# create an instance of VoidOptions from a dict
void_options_from_dict = VoidOptions.from_dict(void_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


