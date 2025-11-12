# QueryOrdersResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**orders** | **List[object]** | List of the retrieved Orders. | [optional] 
**paging_metadata** | **object** | Paging metadata | [optional] 

## Example

```python
from openapi_client.models.query_orders_response import QueryOrdersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QueryOrdersResponse from a JSON string
query_orders_response_instance = QueryOrdersResponse.from_json(json)
# print the JSON string representation of the object
print(QueryOrdersResponse.to_json())

# convert the object into a dict
query_orders_response_dict = query_orders_response_instance.to_dict()
# create an instance of QueryOrdersResponse from a dict
query_orders_response_from_dict = QueryOrdersResponse.from_dict(query_orders_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


