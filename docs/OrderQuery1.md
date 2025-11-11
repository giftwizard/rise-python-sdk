# OrderQuery1

Order ID or Source Identifiers of the Order to fulfill.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Order ID. | [optional] 
**source_info** | [**OrderSourceInfo1**](OrderSourceInfo1.md) |  | [optional] 

## Example

```python
from openapi_client.models.order_query1 import OrderQuery1

# TODO update the JSON string below
json = "{}"
# create an instance of OrderQuery1 from a JSON string
order_query1_instance = OrderQuery1.from_json(json)
# print the JSON string representation of the object
print(OrderQuery1.to_json())

# convert the object into a dict
order_query1_dict = order_query1_instance.to_dict()
# create an instance of OrderQuery1 from a dict
order_query1_from_dict = OrderQuery1.from_dict(order_query1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


