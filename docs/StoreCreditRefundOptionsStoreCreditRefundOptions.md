# StoreCreditRefundOptionsStoreCreditRefundOptions

Information about a transaction whose source is a store credit refund. (**Deprecated**: Use `wallet_action_start_options` instead.)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_action_id** | **str** | ID of the wallet action (store credit) given as a refund. | [optional] 
**liability** | **bool** | Indicates whether the store credit refund is a liability. | [optional] 

## Example

```python
from openapi_client.models.store_credit_refund_options_store_credit_refund_options import StoreCreditRefundOptionsStoreCreditRefundOptions

# TODO update the JSON string below
json = "{}"
# create an instance of StoreCreditRefundOptionsStoreCreditRefundOptions from a JSON string
store_credit_refund_options_store_credit_refund_options_instance = StoreCreditRefundOptionsStoreCreditRefundOptions.from_json(json)
# print the JSON string representation of the object
print(StoreCreditRefundOptionsStoreCreditRefundOptions.to_json())

# convert the object into a dict
store_credit_refund_options_store_credit_refund_options_dict = store_credit_refund_options_store_credit_refund_options_instance.to_dict()
# create an instance of StoreCreditRefundOptionsStoreCreditRefundOptions from a dict
store_credit_refund_options_store_credit_refund_options_from_dict = StoreCreditRefundOptionsStoreCreditRefundOptions.from_dict(store_credit_refund_options_store_credit_refund_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


