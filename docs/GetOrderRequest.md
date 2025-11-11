# GetOrderRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | ID of the Order to retrieve. | [optional] 

## Example

```python
from openapi_client.models.get_order_request import GetOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrderRequest from a JSON string
get_order_request_instance = GetOrderRequest.from_json(json)
# print the JSON string representation of the object
print(GetOrderRequest.to_json())

# convert the object into a dict
get_order_request_dict = get_order_request_instance.to_dict()
# create an instance of GetOrderRequest from a dict
get_order_request_from_dict = GetOrderRequest.from_dict(get_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


