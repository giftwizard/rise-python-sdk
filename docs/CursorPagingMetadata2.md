# CursorPagingMetadata2

Paging metadata. Contains cursor which can be used in next query.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of items returned in current page. | [optional] 
**cursors** | [**Cursors4**](Cursors4.md) |  | [optional] 
**has_next** | **bool** | Whether there are more pages to retrieve following the current page.  + &#x60;true&#x60;: Another page of results can be retrieved. + &#x60;false&#x60;: This is the last page. | [optional] 

## Example

```python
from openapi_client.models.cursor_paging_metadata2 import CursorPagingMetadata2

# TODO update the JSON string below
json = "{}"
# create an instance of CursorPagingMetadata2 from a JSON string
cursor_paging_metadata2_instance = CursorPagingMetadata2.from_json(json)
# print the JSON string representation of the object
print(CursorPagingMetadata2.to_json())

# convert the object into a dict
cursor_paging_metadata2_dict = cursor_paging_metadata2_instance.to_dict()
# create an instance of CursorPagingMetadata2 from a dict
cursor_paging_metadata2_from_dict = CursorPagingMetadata2.from_dict(cursor_paging_metadata2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


