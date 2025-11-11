# PaymentMethodRefundWalletActionDetails



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_action_id** | **str** |  | [optional] 
**funding_transaction_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.payment_method_refund_wallet_action_details import PaymentMethodRefundWalletActionDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodRefundWalletActionDetails from a JSON string
payment_method_refund_wallet_action_details_instance = PaymentMethodRefundWalletActionDetails.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodRefundWalletActionDetails.to_json())

# convert the object into a dict
payment_method_refund_wallet_action_details_dict = payment_method_refund_wallet_action_details_instance.to_dict()
# create an instance of PaymentMethodRefundWalletActionDetails from a dict
payment_method_refund_wallet_action_details_from_dict = PaymentMethodRefundWalletActionDetails.from_dict(payment_method_refund_wallet_action_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


