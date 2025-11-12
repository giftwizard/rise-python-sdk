# PagingMethodCursorPaging

Cursor token pointing to a page of results. Not used in the first request. Following requests use the cursor token and not `filter` or `sort`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | Number of items to load. | [optional] 
**cursor** | **str** | Pointer to the next or previous page in the list of results.  You can get the relevant cursor token from the &#x60;pagingMetadata&#x60; object in the previous call&#39;s response. Not relevant for the first request. | [optional] 

## Example

```python
from openapi_client.models.paging_method_cursor_paging import PagingMethodCursorPaging

# TODO update the JSON string below
json = "{}"
# create an instance of PagingMethodCursorPaging from a JSON string
paging_method_cursor_paging_instance = PagingMethodCursorPaging.from_json(json)
# print the JSON string representation of the object
print(PagingMethodCursorPaging.to_json())

# convert the object into a dict
paging_method_cursor_paging_dict = paging_method_cursor_paging_instance.to_dict()
# create an instance of PagingMethodCursorPaging from a dict
paging_method_cursor_paging_from_dict = PagingMethodCursorPaging.from_dict(paging_method_cursor_paging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


