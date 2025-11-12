# GiftCard

GiftCard is the main entity of GiftCardService. It contains basic information such as gift card code, balance, and expiration date, as well as information about the source of the gift card (e.g., purchase, migration, etc.).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of the Gift Card. | [optional] [readonly] 
**code** | **str** | Gift Card code for redemption. | [optional] 
**initial_value** | **str** | Initial value of the Gift Card. | [optional] 
**balance** | **str** | Current balance of the Gift Card. | [optional] [readonly] 
**source_info** | **object** | Information about the source of the gift card. | [optional] 
**revision** | **str** | Gift Card revision. | [optional] [readonly] 
**currency** | **str** | Gift Card currency. | [optional] 
**expiration_date** | **datetime** | Gift Card expiration date. | [optional] 
**created_date** | **datetime** | Gift Card creation date. | [optional] [readonly] 
**updated_date** | **datetime** | Gift Card last update date. | [optional] [readonly] 
**last_transaction_id** | **str** | ID of the last transaction that modified the gift card balance. | [optional] [readonly] 
**disable_date** | **datetime** | Gift Card disable date, if the gift card was disabled. | [optional] [readonly] 
**idempotency_key** | **str** | Gift Card idempotency key, to prevent duplicate creation. | [optional] 
**code_suffix** | **str** | Last 4 characters of the gift card code for easier reference and searching. | [optional] [readonly] 
**transaction_details** | **object** | Transaction details related to the gift card. | [optional] [readonly] 

## Example

```python
from openapi_client.models.gift_card import GiftCard

# TODO update the JSON string below
json = "{}"
# create an instance of GiftCard from a JSON string
gift_card_instance = GiftCard.from_json(json)
# print the JSON string representation of the object
print(GiftCard.to_json())

# convert the object into a dict
gift_card_dict = gift_card_instance.to_dict()
# create an instance of GiftCard from a dict
gift_card_from_dict = GiftCard.from_dict(gift_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


