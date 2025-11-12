# BuyerInfo

Information about the buyer of a GiftCard Order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | The buyer&#39;s first name. | [optional] 
**last_name** | **str** | The buyer&#39;s last name. | [optional] 
**email** | **str** | The buyer&#39;s email address. | [optional] 
**billing_address** | **str** | deprecated | [optional] 
**source_customer_id** | **str** | The buyer&#39;s customer ID in the source sales channel (if it exists). | [optional] 
**billing_info** | **object** | Billing information of the buyer. | [optional] 

## Example

```python
from openapi_client.models.buyer_info import BuyerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BuyerInfo from a JSON string
buyer_info_instance = BuyerInfo.from_json(json)
# print the JSON string representation of the object
print(BuyerInfo.to_json())

# convert the object into a dict
buyer_info_dict = buyer_info_instance.to_dict()
# create an instance of BuyerInfo from a dict
buyer_info_from_dict = BuyerInfo.from_dict(buyer_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


