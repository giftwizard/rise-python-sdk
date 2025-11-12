# QueryOrdersResponse1



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**orders** | [**List[GiftCardOrder3]**](GiftCardOrder3.md) | List of the retrieved Orders. | [optional] 
**paging_metadata** | [**CursorPagingMetadata3**](CursorPagingMetadata3.md) |  | [optional] 

## Example

```python
from openapi_client.models.query_orders_response1 import QueryOrdersResponse1

# TODO update the JSON string below
json = "{}"
# create an instance of QueryOrdersResponse1 from a JSON string
query_orders_response1_instance = QueryOrdersResponse1.from_json(json)
# print the JSON string representation of the object
print(QueryOrdersResponse1.to_json())

# convert the object into a dict
query_orders_response1_dict = query_orders_response1_instance.to_dict()
# create an instance of QueryOrdersResponse1 from a dict
query_orders_response1_from_dict = QueryOrdersResponse1.from_dict(query_orders_response1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


