# DeleteOrderRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | ID of the Order to delete. | [optional] 

## Example

```python
from openapi_client.models.delete_order_request import DeleteOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteOrderRequest from a JSON string
delete_order_request_instance = DeleteOrderRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteOrderRequest.to_json())

# convert the object into a dict
delete_order_request_dict = delete_order_request_instance.to_dict()
# create an instance of DeleteOrderRequest from a dict
delete_order_request_from_dict = DeleteOrderRequest.from_dict(delete_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


