# OrderSourceInfoSourceInfo

Source Identifiers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_channel_id** | **str** | Source channel, i.e. Shopify. | [optional] 
**source_tenant_id** | **str** | Tenant ID in Source, i.e. shop ID. | [optional] 
**source_order_id** | **str** | Order ID in Source. | [optional] 

## Example

```python
from openapi_client.models.order_source_info_source_info import OrderSourceInfoSourceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OrderSourceInfoSourceInfo from a JSON string
order_source_info_source_info_instance = OrderSourceInfoSourceInfo.from_json(json)
# print the JSON string representation of the object
print(OrderSourceInfoSourceInfo.to_json())

# convert the object into a dict
order_source_info_source_info_dict = order_source_info_source_info_instance.to_dict()
# create an instance of OrderSourceInfoSourceInfo from a dict
order_source_info_source_info_from_dict = OrderSourceInfoSourceInfo.from_dict(order_source_info_source_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


