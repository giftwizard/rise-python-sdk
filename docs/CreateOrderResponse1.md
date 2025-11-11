# CreateOrderResponse1



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | [**GiftCardOrder1**](GiftCardOrder1.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_order_response1 import CreateOrderResponse1

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrderResponse1 from a JSON string
create_order_response1_instance = CreateOrderResponse1.from_json(json)
# print the JSON string representation of the object
print(CreateOrderResponse1.to_json())

# convert the object into a dict
create_order_response1_dict = create_order_response1_instance.to_dict()
# create an instance of CreateOrderResponse1 from a dict
create_order_response1_from_dict = CreateOrderResponse1.from_dict(create_order_response1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


