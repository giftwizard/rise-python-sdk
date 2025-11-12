# GiftCardOrder1

The created Order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Order ID. | [optional] [readonly] 
**revision** | **str** | Revision number, which increments by 1 each time the Order is updated. To prevent conflicting changes, the current revision must be passed when updating the Order.  Ignored when creating a Order. | [optional] [readonly] 
**created_date** | **datetime** | Date and time the Order was created. | [optional] [readonly] 
**updated_date** | **datetime** | Date and time the Order was last updated. | [optional] [readonly] 
**source_channel_id** | **str** | Source sales channel, i.e. Shopify. | [optional] 
**source_tenant_id** | **str** | Tenant ID in source sales channel, i.e. shop ID. | [optional] 
**source_order_id** | **str** | Order ID in source sales channel. | [optional] 
**source_order_number** | **str** | The order number in source sales channel. | [optional] 
**total_amount** | **str** | The total amount of the order that contains the Gift Card. | [optional] 
**currency** | **str** | The order&#39;s currency. | [optional] 
**note** | **str** | Note to be added to the order. | [optional] 
**payment_status** | **str** | The payment status of the order. | [optional] 
**fulfillment_status** | **str** | Fulfillment status of the order in Rise. | [optional] 
**status** | **str** | Status of the order in Rise. | [optional] 
**buyer_info** | [**BuyerInfo1**](BuyerInfo1.md) |  | [optional] 
**schedule_fulfill_at** | **datetime** | Date and time to fulfill the order by creating Gift Cards. Default is now. | [optional] 
**rise_fulfilled_at** | **datetime** | Date and time the order was fulfilled in Rise by creating Gift Cards. | [optional] [readonly] 
**source_fulfilled_at** | **datetime** | Date and time the order was marked fulfilled in the Source sales channel. | [optional] 
**line_items** | [**List[GiftCardLineItem1]**](GiftCardLineItem1.md) | The line items in the order that are Gift Cards. | [optional] 
**fraud_message** | **str** | The fraud message. | [optional] 
**fraud_type** | **str** | The fraud logic type. | [optional] 
**source_location_id** | **str** | Location ID in Source. | [optional] 

## Example

```python
from openapi_client.models.gift_card_order1 import GiftCardOrder1

# TODO update the JSON string below
json = "{}"
# create an instance of GiftCardOrder1 from a JSON string
gift_card_order1_instance = GiftCardOrder1.from_json(json)
# print the JSON string representation of the object
print(GiftCardOrder1.to_json())

# convert the object into a dict
gift_card_order1_dict = gift_card_order1_instance.to_dict()
# create an instance of GiftCardOrder1 from a dict
gift_card_order1_from_dict = GiftCardOrder1.from_dict(gift_card_order1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


