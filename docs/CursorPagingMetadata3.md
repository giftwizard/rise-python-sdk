# CursorPagingMetadata3

Paging metadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of items returned in the response. | [optional] 
**cursors** | [**Cursors5**](Cursors5.md) |  | [optional] 
**has_next** | **bool** | Indicates if there are more results after the current page. If &#x60;true&#x60;, another page of results can be retrieved. If &#x60;false&#x60;, this is the last page. | [optional] 

## Example

```python
from openapi_client.models.cursor_paging_metadata3 import CursorPagingMetadata3

# TODO update the JSON string below
json = "{}"
# create an instance of CursorPagingMetadata3 from a JSON string
cursor_paging_metadata3_instance = CursorPagingMetadata3.from_json(json)
# print the JSON string representation of the object
print(CursorPagingMetadata3.to_json())

# convert the object into a dict
cursor_paging_metadata3_dict = cursor_paging_metadata3_instance.to_dict()
# create an instance of CursorPagingMetadata3 from a dict
cursor_paging_metadata3_from_dict = CursorPagingMetadata3.from_dict(cursor_paging_metadata3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


