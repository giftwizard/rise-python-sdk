# GiftCardOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_options** | **object** | Detailed information about a Gift Card issued from an order. | [optional] 
**campaign_options** | **object** | Bulk Options (deprecated) | [optional] 
**migration_options** | **object** | Detailed information about a Gift Card or Gift Card Transaction whose source is a migration from Rise V1 or another platform. | [optional] 
**store_credit_options** | **object** | Detailed information about a Gift Card that belongs to a Store Credit Wallet. | [optional] 
**workflow_options** | **object** | Detailed information about a Gift Card issued from a workflow. | [optional] 
**bulk_options** | **object** | Detailed information about a Gift Card or Gift Card transaction issued from a bulk. | [optional] 
**manual_options** | **object** | Detailed information about a Gift Card that was created manually. | [optional] 

## Example

```python
from openapi_client.models.gift_card_options import GiftCardOptions

# TODO update the JSON string below
json = "{}"
# create an instance of GiftCardOptions from a JSON string
gift_card_options_instance = GiftCardOptions.from_json(json)
# print the JSON string representation of the object
print(GiftCardOptions.to_json())

# convert the object into a dict
gift_card_options_dict = gift_card_options_instance.to_dict()
# create an instance of GiftCardOptions from a dict
gift_card_options_from_dict = GiftCardOptions.from_dict(gift_card_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


