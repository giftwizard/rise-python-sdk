# GiftCard1

The created GiftCard.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of the Gift Card. | [optional] [readonly] 
**code** | **str** | Gift Card code for redemption. | [optional] 
**initial_value** | **str** | Initial value of the Gift Card. | [optional] 
**balance** | **str** | Current balance of the Gift Card. | [optional] [readonly] 
**source_info** | [**GiftCardSourceInfo1**](GiftCardSourceInfo1.md) |  | [optional] 
**revision** | **str** | Gift Card revision. | [optional] [readonly] 
**currency** | **str** | Gift Card currency. | [optional] 
**expiration_date** | **datetime** | Gift Card expiration date. | [optional] 
**created_date** | **datetime** | Gift Card creation date. | [optional] [readonly] 
**updated_date** | **datetime** | Gift Card last update date. | [optional] [readonly] 
**last_transaction_id** | **str** | ID of the last transaction that modified the gift card balance. (**Deprecated**: Use &#x60;id&#x60; instead.) | [optional] [readonly] 
**disable_date** | **datetime** | Gift Card disable date, if the gift card was disabled. | [optional] [readonly] 
**idempotency_key** | **str** | Gift Card idempotency key, to prevent duplicate creation. | [optional] 
**code_suffix** | **str** | Last 4 characters of the gift card code for easier reference and searching. | [optional] [readonly] 
**transaction_details** | [**TransactionDetails1**](TransactionDetails1.md) |  | [optional] 

## Example

```python
from openapi_client.models.gift_card1 import GiftCard1

# TODO update the JSON string below
json = "{}"
# create an instance of GiftCard1 from a JSON string
gift_card1_instance = GiftCard1.from_json(json)
# print the JSON string representation of the object
print(GiftCard1.to_json())

# convert the object into a dict
gift_card1_dict = gift_card1_instance.to_dict()
# create an instance of GiftCard1 from a dict
gift_card1_from_dict = GiftCard1.from_dict(gift_card1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


