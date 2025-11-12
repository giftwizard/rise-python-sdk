# PaymentMethodRefundOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_method_refund_options** | [**PaymentMethodRefundOptionsPaymentMethodRefundOptions**](PaymentMethodRefundOptionsPaymentMethodRefundOptions.md) |  | [optional] 

## Example

```python
from openapi_client.models.payment_method_refund_options import PaymentMethodRefundOptions

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodRefundOptions from a JSON string
payment_method_refund_options_instance = PaymentMethodRefundOptions.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodRefundOptions.to_json())

# convert the object into a dict
payment_method_refund_options_dict = payment_method_refund_options_instance.to_dict()
# create an instance of PaymentMethodRefundOptions from a dict
payment_method_refund_options_from_dict = PaymentMethodRefundOptions.from_dict(payment_method_refund_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


