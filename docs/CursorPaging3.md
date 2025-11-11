# CursorPaging3

Cursor token pointing to a page of results. Not used in the first request. Following requests use the cursor token and not `filter` or `sort`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor_paging** | [**CursorPaging3**](CursorPaging3.md) |  | [optional] 

## Example

```python
from openapi_client.models.cursor_paging3 import CursorPaging3

# TODO update the JSON string below
json = "{}"
# create an instance of CursorPaging3 from a JSON string
cursor_paging3_instance = CursorPaging3.from_json(json)
# print the JSON string representation of the object
print(CursorPaging3.to_json())

# convert the object into a dict
cursor_paging3_dict = cursor_paging3_instance.to_dict()
# create an instance of CursorPaging3 from a dict
cursor_paging3_from_dict = CursorPaging3.from_dict(cursor_paging3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


