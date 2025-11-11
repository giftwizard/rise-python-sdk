# CursorPaging



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | Number of items to load. | [optional] 
**cursor** | **str** | Pointer to the next or previous page in the list of results.  You can get the relevant cursor token from the &#x60;pagingMetadata&#x60; object in the previous call&#39;s response. Not relevant for the first request. | [optional] 

## Example

```python
from openapi_client.models.cursor_paging import CursorPaging

# TODO update the JSON string below
json = "{}"
# create an instance of CursorPaging from a JSON string
cursor_paging_instance = CursorPaging.from_json(json)
# print the JSON string representation of the object
print(CursorPaging.to_json())

# convert the object into a dict
cursor_paging_dict = cursor_paging_instance.to_dict()
# create an instance of CursorPaging from a dict
cursor_paging_from_dict = CursorPaging.from_dict(cursor_paging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


