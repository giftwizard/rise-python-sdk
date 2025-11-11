# QueryTransactionsInternalResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transactions** | **List[object]** | The retrieved Transactions. | [optional] 
**paging_metadata** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.query_transactions_internal_response import QueryTransactionsInternalResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QueryTransactionsInternalResponse from a JSON string
query_transactions_internal_response_instance = QueryTransactionsInternalResponse.from_json(json)
# print the JSON string representation of the object
print(QueryTransactionsInternalResponse.to_json())

# convert the object into a dict
query_transactions_internal_response_dict = query_transactions_internal_response_instance.to_dict()
# create an instance of QueryTransactionsInternalResponse from a dict
query_transactions_internal_response_from_dict = QueryTransactionsInternalResponse.from_dict(query_transactions_internal_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


