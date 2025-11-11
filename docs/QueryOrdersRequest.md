# QueryOrdersRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **object** | API Query Language expression. | [optional] 

## Example

```python
from openapi_client.models.query_orders_request import QueryOrdersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QueryOrdersRequest from a JSON string
query_orders_request_instance = QueryOrdersRequest.from_json(json)
# print the JSON string representation of the object
print(QueryOrdersRequest.to_json())

# convert the object into a dict
query_orders_request_dict = query_orders_request_instance.to_dict()
# create an instance of QueryOrdersRequest from a dict
query_orders_request_from_dict = QueryOrdersRequest.from_dict(query_orders_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


