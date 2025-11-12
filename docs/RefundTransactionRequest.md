# RefundTransactionRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** |  | [optional] 
**amount** | **str** | Optional custom amount to refund. If not provided, the full amount of the transaction will be refunded. | [optional] 
**context** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.refund_transaction_request import RefundTransactionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RefundTransactionRequest from a JSON string
refund_transaction_request_instance = RefundTransactionRequest.from_json(json)
# print the JSON string representation of the object
print(RefundTransactionRequest.to_json())

# convert the object into a dict
refund_transaction_request_dict = refund_transaction_request_instance.to_dict()
# create an instance of RefundTransactionRequest from a dict
refund_transaction_request_from_dict = RefundTransactionRequest.from_dict(refund_transaction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


