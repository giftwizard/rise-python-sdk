# BuyerInfo1

Information about the buyer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | The buyer&#39;s first name. | [optional] 
**last_name** | **str** | The buyer&#39;s last name. | [optional] 
**email** | **str** | The buyer&#39;s email address. | [optional] 
**billing_address** | **str** | deprecated (**Deprecated**: Use &#x60;billing_info&#x60; instead.) | [optional] 
**source_customer_id** | **str** | The buyer&#39;s customer ID in the source sales channel (if it exists). | [optional] 
**billing_info** | [**BillingInfo1**](BillingInfo1.md) |  | [optional] 

## Example

```python
from openapi_client.models.buyer_info1 import BuyerInfo1

# TODO update the JSON string below
json = "{}"
# create an instance of BuyerInfo1 from a JSON string
buyer_info1_instance = BuyerInfo1.from_json(json)
# print the JSON string representation of the object
print(BuyerInfo1.to_json())

# convert the object into a dict
buyer_info1_dict = buyer_info1_instance.to_dict()
# create an instance of BuyerInfo1 from a dict
buyer_info1_from_dict = BuyerInfo1.from_dict(buyer_info1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


