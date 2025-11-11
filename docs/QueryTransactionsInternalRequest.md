# QueryTransactionsInternalRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **object** | WQL expression. | [optional] 

## Example

```python
from openapi_client.models.query_transactions_internal_request import QueryTransactionsInternalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QueryTransactionsInternalRequest from a JSON string
query_transactions_internal_request_instance = QueryTransactionsInternalRequest.from_json(json)
# print the JSON string representation of the object
print(QueryTransactionsInternalRequest.to_json())

# convert the object into a dict
query_transactions_internal_request_dict = query_transactions_internal_request_instance.to_dict()
# create an instance of QueryTransactionsInternalRequest from a dict
query_transactions_internal_request_from_dict = QueryTransactionsInternalRequest.from_dict(query_transactions_internal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


