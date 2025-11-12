# OrderOptionsOrderOptions

Detailed information about a Gift Card issued from an order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | ID of the gift card order. | [optional] 
**liability** | **bool** | Indicates whether the gift card order is a liability. | [optional] 
**order_number** | **str** | Order number of the gift card order. | [optional] 

## Example

```python
from openapi_client.models.order_options_order_options import OrderOptionsOrderOptions

# TODO update the JSON string below
json = "{}"
# create an instance of OrderOptionsOrderOptions from a JSON string
order_options_order_options_instance = OrderOptionsOrderOptions.from_json(json)
# print the JSON string representation of the object
print(OrderOptionsOrderOptions.to_json())

# convert the object into a dict
order_options_order_options_dict = order_options_order_options_instance.to_dict()
# create an instance of OrderOptionsOrderOptions from a dict
order_options_order_options_from_dict = OrderOptionsOrderOptions.from_dict(order_options_order_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


