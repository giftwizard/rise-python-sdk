# PaymentMethodRefundOptions1

Information about a transaction whose source is a refunding a payment method.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_method_refund_options** | [**PaymentMethodRefundOptions1**](PaymentMethodRefundOptions1.md) |  | [optional] 

## Example

```python
from openapi_client.models.payment_method_refund_options1 import PaymentMethodRefundOptions1

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodRefundOptions1 from a JSON string
payment_method_refund_options1_instance = PaymentMethodRefundOptions1.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodRefundOptions1.to_json())

# convert the object into a dict
payment_method_refund_options1_dict = payment_method_refund_options1_instance.to_dict()
# create an instance of PaymentMethodRefundOptions1 from a dict
payment_method_refund_options1_from_dict = PaymentMethodRefundOptions1.from_dict(payment_method_refund_options1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


