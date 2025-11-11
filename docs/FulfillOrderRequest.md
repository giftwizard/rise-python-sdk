# FulfillOrderRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **object** | Order ID or Source Identifiers of the Order to fulfill. | [optional] 

## Example

```python
from openapi_client.models.fulfill_order_request import FulfillOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FulfillOrderRequest from a JSON string
fulfill_order_request_instance = FulfillOrderRequest.from_json(json)
# print the JSON string representation of the object
print(FulfillOrderRequest.to_json())

# convert the object into a dict
fulfill_order_request_dict = fulfill_order_request_instance.to_dict()
# create an instance of FulfillOrderRequest from a dict
fulfill_order_request_from_dict = FulfillOrderRequest.from_dict(fulfill_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


