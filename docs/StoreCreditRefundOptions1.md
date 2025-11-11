# StoreCreditRefundOptions1

Information about a transaction whose source is a store credit refund. (**Deprecated**: Use `wallet_action_start_options` instead.)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**store_credit_refund_options** | [**StoreCreditRefundOptions1**](StoreCreditRefundOptions1.md) |  | [optional] 

## Example

```python
from openapi_client.models.store_credit_refund_options1 import StoreCreditRefundOptions1

# TODO update the JSON string below
json = "{}"
# create an instance of StoreCreditRefundOptions1 from a JSON string
store_credit_refund_options1_instance = StoreCreditRefundOptions1.from_json(json)
# print the JSON string representation of the object
print(StoreCreditRefundOptions1.to_json())

# convert the object into a dict
store_credit_refund_options1_dict = store_credit_refund_options1_instance.to_dict()
# create an instance of StoreCreditRefundOptions1 from a dict
store_credit_refund_options1_from_dict = StoreCreditRefundOptions1.from_dict(store_credit_refund_options1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


