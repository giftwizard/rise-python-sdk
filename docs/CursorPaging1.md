# CursorPaging1

Cursor token pointing to a page of results. Not used in the first request. Following requests use the cursor token and not `filter` or `sort`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | Number of items to load. | [optional] 
**cursor** | **str** | Pointer to the next or previous page in the list of results.  You can get the relevant cursor token from the &#x60;pagingMetadata&#x60; object in the previous call&#39;s response. Not relevant for the first request. | [optional] 

## Example

```python
from openapi_client.models.cursor_paging1 import CursorPaging1

# TODO update the JSON string below
json = "{}"
# create an instance of CursorPaging1 from a JSON string
cursor_paging1_instance = CursorPaging1.from_json(json)
# print the JSON string representation of the object
print(CursorPaging1.to_json())

# convert the object into a dict
cursor_paging1_dict = cursor_paging1_instance.to_dict()
# create an instance of CursorPaging1 from a dict
cursor_paging1_from_dict = CursorPaging1.from_dict(cursor_paging1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


