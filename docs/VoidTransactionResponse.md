# VoidTransactionResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction** | **object** |  | [optional] 
**balance** | **str** | GiftCard balance after transaction. | [optional] 
**currency** | **str** | GiftCard Currency. | [optional] 

## Example

```python
from openapi_client.models.void_transaction_response import VoidTransactionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VoidTransactionResponse from a JSON string
void_transaction_response_instance = VoidTransactionResponse.from_json(json)
# print the JSON string representation of the object
print(VoidTransactionResponse.to_json())

# convert the object into a dict
void_transaction_response_dict = void_transaction_response_instance.to_dict()
# create an instance of VoidTransactionResponse from a dict
void_transaction_response_from_dict = VoidTransactionResponse.from_dict(void_transaction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


