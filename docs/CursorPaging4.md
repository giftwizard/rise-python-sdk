# CursorPaging4

Cursor paging options.  Learn more about [cursor paging](https://dev.wix.com/docs/rest/articles/getting-started/api-query-language#cursor-paging).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | Maximum number of items to return in the results. | [optional] 
**cursor** | **str** | Pointer to the next or previous page in the list of results.  Pass the relevant cursor token from the &#x60;pagingMetadata&#x60; object in the previous call&#39;s response. Not relevant for the first request. | [optional] 

## Example

```python
from openapi_client.models.cursor_paging4 import CursorPaging4

# TODO update the JSON string below
json = "{}"
# create an instance of CursorPaging4 from a JSON string
cursor_paging4_instance = CursorPaging4.from_json(json)
# print the JSON string representation of the object
print(CursorPaging4.to_json())

# convert the object into a dict
cursor_paging4_dict = cursor_paging4_instance.to_dict()
# create an instance of CursorPaging4 from a dict
cursor_paging4_from_dict = CursorPaging4.from_dict(cursor_paging4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


