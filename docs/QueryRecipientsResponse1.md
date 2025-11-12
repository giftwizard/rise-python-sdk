# QueryRecipientsResponse1



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipients** | [**List[Recipient3]**](Recipient3.md) | List of Recipients. | [optional] 
**paging_metadata** | [**CursorPagingMetadata1**](CursorPagingMetadata1.md) |  | [optional] 

## Example

```python
from openapi_client.models.query_recipients_response1 import QueryRecipientsResponse1

# TODO update the JSON string below
json = "{}"
# create an instance of QueryRecipientsResponse1 from a JSON string
query_recipients_response1_instance = QueryRecipientsResponse1.from_json(json)
# print the JSON string representation of the object
print(QueryRecipientsResponse1.to_json())

# convert the object into a dict
query_recipients_response1_dict = query_recipients_response1_instance.to_dict()
# create an instance of QueryRecipientsResponse1 from a dict
query_recipients_response1_from_dict = QueryRecipientsResponse1.from_dict(query_recipients_response1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


