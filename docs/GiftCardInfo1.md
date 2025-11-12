# GiftCardInfo1

Information about the Gift Card associated with this Wallet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Gift Card Code | [optional] [readonly] 
**balance** | **str** | Current Gift Card Balance | [optional] [readonly] 
**currency** | **str** | Gift Card Currency | [optional] [readonly] 
**code_suffix** | **str** | Gift Card Code Suffix | [optional] [readonly] 

## Example

```python
from openapi_client.models.gift_card_info1 import GiftCardInfo1

# TODO update the JSON string below
json = "{}"
# create an instance of GiftCardInfo1 from a JSON string
gift_card_info1_instance = GiftCardInfo1.from_json(json)
# print the JSON string representation of the object
print(GiftCardInfo1.to_json())

# convert the object into a dict
gift_card_info1_dict = gift_card_info1_instance.to_dict()
# create an instance of GiftCardInfo1 from a dict
gift_card_info1_from_dict = GiftCardInfo1.from_dict(gift_card_info1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


