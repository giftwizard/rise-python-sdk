# CursorPagingMetadata



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of items returned in the response. | [optional] 
**cursors** | **object** | Offset that was requested. | [optional] 
**has_next** | **bool** | Indicates if there are more results after the current page. If &#x60;true&#x60;, another page of results can be retrieved. If &#x60;false&#x60;, this is the last page. | [optional] 

## Example

```python
from openapi_client.models.cursor_paging_metadata import CursorPagingMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of CursorPagingMetadata from a JSON string
cursor_paging_metadata_instance = CursorPagingMetadata.from_json(json)
# print the JSON string representation of the object
print(CursorPagingMetadata.to_json())

# convert the object into a dict
cursor_paging_metadata_dict = cursor_paging_metadata_instance.to_dict()
# create an instance of CursorPagingMetadata from a dict
cursor_paging_metadata_from_dict = CursorPagingMetadata.from_dict(cursor_paging_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


