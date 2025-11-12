# GiftCardInfo

Information about the Gift Card associated with a Wallet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Gift Card Code | [optional] [readonly] 
**balance** | **str** | Current Gift Card Balance | [optional] [readonly] 
**currency** | **str** | Gift Card Currency | [optional] [readonly] 
**code_suffix** | **str** | Gift Card Code Suffix | [optional] [readonly] 

## Example

```python
from openapi_client.models.gift_card_info import GiftCardInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GiftCardInfo from a JSON string
gift_card_info_instance = GiftCardInfo.from_json(json)
# print the JSON string representation of the object
print(GiftCardInfo.to_json())

# convert the object into a dict
gift_card_info_dict = gift_card_info_instance.to_dict()
# create an instance of GiftCardInfo from a dict
gift_card_info_from_dict = GiftCardInfo.from_dict(gift_card_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


