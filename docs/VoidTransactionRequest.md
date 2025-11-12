# VoidTransactionRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** |  | [optional] 
**source_tenant_id** | **str** |  | [optional] 
**source_channel_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.void_transaction_request import VoidTransactionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VoidTransactionRequest from a JSON string
void_transaction_request_instance = VoidTransactionRequest.from_json(json)
# print the JSON string representation of the object
print(VoidTransactionRequest.to_json())

# convert the object into a dict
void_transaction_request_dict = void_transaction_request_instance.to_dict()
# create an instance of VoidTransactionRequest from a dict
void_transaction_request_from_dict = VoidTransactionRequest.from_dict(void_transaction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


