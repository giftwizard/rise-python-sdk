# QueryTransactionsRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **object** | WQL expression. | [optional] 

## Example

```python
from openapi_client.models.query_transactions_request import QueryTransactionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QueryTransactionsRequest from a JSON string
query_transactions_request_instance = QueryTransactionsRequest.from_json(json)
# print the JSON string representation of the object
print(QueryTransactionsRequest.to_json())

# convert the object into a dict
query_transactions_request_dict = query_transactions_request_instance.to_dict()
# create an instance of QueryTransactionsRequest from a dict
query_transactions_request_from_dict = QueryTransactionsRequest.from_dict(query_transactions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


