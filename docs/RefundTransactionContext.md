# RefundTransactionContext



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_tenant_id** | **str** |  | [optional] 
**source_channel_id** | **str** |  | [optional] 
**source_location_id** | **str** |  | [optional] 
**source_order_id** | **str** |  | [optional] 
**source_order_number** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.refund_transaction_context import RefundTransactionContext

# TODO update the JSON string below
json = "{}"
# create an instance of RefundTransactionContext from a JSON string
refund_transaction_context_instance = RefundTransactionContext.from_json(json)
# print the JSON string representation of the object
print(RefundTransactionContext.to_json())

# convert the object into a dict
refund_transaction_context_dict = refund_transaction_context_instance.to_dict()
# create an instance of RefundTransactionContext from a dict
refund_transaction_context_from_dict = RefundTransactionContext.from_dict(refund_transaction_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


