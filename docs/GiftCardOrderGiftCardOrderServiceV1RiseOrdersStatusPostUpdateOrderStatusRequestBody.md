# GiftCardOrderGiftCardOrderServiceV1RiseOrdersStatusPostUpdateOrderStatusRequestBody



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | [**OrderQuery2**](OrderQuery2.md) |  | 
**payment_status** | **str** | The new payment status of the order. | 
**skip_auto_fulfillment** | **bool** | Skip auto fulfillment of the gift card. Default is false. | [optional] 

## Example

```python
from openapi_client.models.gift_card_order_gift_card_order_service_v1_rise_orders_status_post_update_order_status_request_body import GiftCardOrderGiftCardOrderServiceV1RiseOrdersStatusPostUpdateOrderStatusRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of GiftCardOrderGiftCardOrderServiceV1RiseOrdersStatusPostUpdateOrderStatusRequestBody from a JSON string
gift_card_order_gift_card_order_service_v1_rise_orders_status_post_update_order_status_request_body_instance = GiftCardOrderGiftCardOrderServiceV1RiseOrdersStatusPostUpdateOrderStatusRequestBody.from_json(json)
# print the JSON string representation of the object
print(GiftCardOrderGiftCardOrderServiceV1RiseOrdersStatusPostUpdateOrderStatusRequestBody.to_json())

# convert the object into a dict
gift_card_order_gift_card_order_service_v1_rise_orders_status_post_update_order_status_request_body_dict = gift_card_order_gift_card_order_service_v1_rise_orders_status_post_update_order_status_request_body_instance.to_dict()
# create an instance of GiftCardOrderGiftCardOrderServiceV1RiseOrdersStatusPostUpdateOrderStatusRequestBody from a dict
gift_card_order_gift_card_order_service_v1_rise_orders_status_post_update_order_status_request_body_from_dict = GiftCardOrderGiftCardOrderServiceV1RiseOrdersStatusPostUpdateOrderStatusRequestBody.from_dict(gift_card_order_gift_card_order_service_v1_rise_orders_status_post_update_order_status_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


