# GiftCardLineItem1

The details of an order line item that is a Gift Card.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Line Item ID in Rise. | [optional] [readonly] 
**source_line_item_id** | **str** | Line Item ID in Source Channel. | [optional] 
**source_variant_id** | **str** | Product Variant ID in Source Channel. | [optional] 
**gifting_info** | [**GiftingInfo1**](GiftingInfo1.md) |  | [optional] 
**quantity** | **int** | Number of Gift Cards to create for this Line Item. | [optional] 
**fulfilled_quantity** | **int** | Number of Gift Cards that were already fulfilled for this Line Item. | [optional] [readonly] 
**price** | **str** | Price of the Line Item. | [optional] 
**gift_card_initial_value** | **str** | The initial value to apply to the Gift Card. | [optional] 
**updated_date** | **datetime** | Date and time the Line Item was last updated. | [optional] [readonly] 
**fulfilled_data** | [**FulfilledData1**](FulfilledData1.md) |  | [optional] 
**gift_card_expiration** | [**Expiration1**](Expiration1.md) |  | [optional] 
**side_effects** | [**SideEffects1**](SideEffects1.md) |  | [optional] 
**gift_card_encrypted_code** | **str** | The encrypted code to create the Gift Card with. | [optional] 

## Example

```python
from openapi_client.models.gift_card_line_item1 import GiftCardLineItem1

# TODO update the JSON string below
json = "{}"
# create an instance of GiftCardLineItem1 from a JSON string
gift_card_line_item1_instance = GiftCardLineItem1.from_json(json)
# print the JSON string representation of the object
print(GiftCardLineItem1.to_json())

# convert the object into a dict
gift_card_line_item1_dict = gift_card_line_item1_instance.to_dict()
# create an instance of GiftCardLineItem1 from a dict
gift_card_line_item1_from_dict = GiftCardLineItem1.from_dict(gift_card_line_item1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


