# OrderOptions1

Detailed information about a Gift Card issued from an order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_options** | [**OrderOptions1**](OrderOptions1.md) |  | [optional] 

## Example

```python
from openapi_client.models.order_options1 import OrderOptions1

# TODO update the JSON string below
json = "{}"
# create an instance of OrderOptions1 from a JSON string
order_options1_instance = OrderOptions1.from_json(json)
# print the JSON string representation of the object
print(OrderOptions1.to_json())

# convert the object into a dict
order_options1_dict = order_options1_instance.to_dict()
# create an instance of OrderOptions1 from a dict
order_options1_from_dict = OrderOptions1.from_dict(order_options1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


