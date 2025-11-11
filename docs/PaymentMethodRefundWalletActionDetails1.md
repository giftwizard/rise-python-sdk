# PaymentMethodRefundWalletActionDetails1

Optional details for the refund that is based of a specific store credit.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_action_id** | **str** |  | [optional] 
**funding_transaction_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.payment_method_refund_wallet_action_details1 import PaymentMethodRefundWalletActionDetails1

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodRefundWalletActionDetails1 from a JSON string
payment_method_refund_wallet_action_details1_instance = PaymentMethodRefundWalletActionDetails1.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodRefundWalletActionDetails1.to_json())

# convert the object into a dict
payment_method_refund_wallet_action_details1_dict = payment_method_refund_wallet_action_details1_instance.to_dict()
# create an instance of PaymentMethodRefundWalletActionDetails1 from a dict
payment_method_refund_wallet_action_details1_from_dict = PaymentMethodRefundWalletActionDetails1.from_dict(payment_method_refund_wallet_action_details1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


