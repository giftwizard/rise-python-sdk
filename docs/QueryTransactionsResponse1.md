# QueryTransactionsResponse1



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transactions** | [**List[Transaction1]**](Transaction1.md) | The retrieved Transactions. | [optional] 
**paging_metadata** | [**PagingMetadataV21**](PagingMetadataV21.md) |  | [optional] 

## Example

```python
from openapi_client.models.query_transactions_response1 import QueryTransactionsResponse1

# TODO update the JSON string below
json = "{}"
# create an instance of QueryTransactionsResponse1 from a JSON string
query_transactions_response1_instance = QueryTransactionsResponse1.from_json(json)
# print the JSON string representation of the object
print(QueryTransactionsResponse1.to_json())

# convert the object into a dict
query_transactions_response1_dict = query_transactions_response1_instance.to_dict()
# create an instance of QueryTransactionsResponse1 from a dict
query_transactions_response1_from_dict = QueryTransactionsResponse1.from_dict(query_transactions_response1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


