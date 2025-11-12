# PaymentMethodRefundOptionsPaymentMethodRefundOptions

Information about a transaction whose source is a refunding a payment method.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | ID of the order associated with the refund. | [optional] 
**liability** | **bool** | Indicates whether the payment method refund is a liability. | [optional] 
**order_number** | **str** | Order number associated with the refund. | [optional] 
**active_funding_transaction** | [**PaymentMethodRefundWalletActionDetails1**](PaymentMethodRefundWalletActionDetails1.md) |  | [optional] 

## Example

```python
from openapi_client.models.payment_method_refund_options_payment_method_refund_options import PaymentMethodRefundOptionsPaymentMethodRefundOptions

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodRefundOptionsPaymentMethodRefundOptions from a JSON string
payment_method_refund_options_payment_method_refund_options_instance = PaymentMethodRefundOptionsPaymentMethodRefundOptions.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodRefundOptionsPaymentMethodRefundOptions.to_json())

# convert the object into a dict
payment_method_refund_options_payment_method_refund_options_dict = payment_method_refund_options_payment_method_refund_options_instance.to_dict()
# create an instance of PaymentMethodRefundOptionsPaymentMethodRefundOptions from a dict
payment_method_refund_options_payment_method_refund_options_from_dict = PaymentMethodRefundOptionsPaymentMethodRefundOptions.from_dict(payment_method_refund_options_payment_method_refund_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


