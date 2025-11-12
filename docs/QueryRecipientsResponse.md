# QueryRecipientsResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipients** | **List[object]** | List of Recipients. | [optional] 
**paging_metadata** | **object** | Paging metadata | [optional] 

## Example

```python
from openapi_client.models.query_recipients_response import QueryRecipientsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QueryRecipientsResponse from a JSON string
query_recipients_response_instance = QueryRecipientsResponse.from_json(json)
# print the JSON string representation of the object
print(QueryRecipientsResponse.to_json())

# convert the object into a dict
query_recipients_response_dict = query_recipients_response_instance.to_dict()
# create an instance of QueryRecipientsResponse from a dict
query_recipients_response_from_dict = QueryRecipientsResponse.from_dict(query_recipients_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


