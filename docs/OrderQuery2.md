# OrderQuery2

Order ID or Source Identifiers of the Order whose status is to be updated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Order ID. | [optional] 
**source_info** | [**OrderSourceInfoSourceInfo**](OrderSourceInfoSourceInfo.md) |  | [optional] 

## Example

```python
from openapi_client.models.order_query2 import OrderQuery2

# TODO update the JSON string below
json = "{}"
# create an instance of OrderQuery2 from a JSON string
order_query2_instance = OrderQuery2.from_json(json)
# print the JSON string representation of the object
print(OrderQuery2.to_json())

# convert the object into a dict
order_query2_dict = order_query2_instance.to_dict()
# create an instance of OrderQuery2 from a dict
order_query2_from_dict = OrderQuery2.from_dict(order_query2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


