# UpdateOrderResponse1



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | [**GiftCardOrder2**](GiftCardOrder2.md) |  | [optional] 

## Example

```python
from openapi_client.models.update_order_response1 import UpdateOrderResponse1

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOrderResponse1 from a JSON string
update_order_response1_instance = UpdateOrderResponse1.from_json(json)
# print the JSON string representation of the object
print(UpdateOrderResponse1.to_json())

# convert the object into a dict
update_order_response1_dict = update_order_response1_instance.to_dict()
# create an instance of UpdateOrderResponse1 from a dict
update_order_response1_from_dict = UpdateOrderResponse1.from_dict(update_order_response1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


