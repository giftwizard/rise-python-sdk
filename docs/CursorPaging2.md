# CursorPaging2

Cursor token pointing to a page of results. Not used in the first request. Following requests use the cursor token and not `filter` or `sort`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor_paging** | [**CursorPaging2**](CursorPaging2.md) |  | [optional] 

## Example

```python
from openapi_client.models.cursor_paging2 import CursorPaging2

# TODO update the JSON string below
json = "{}"
# create an instance of CursorPaging2 from a JSON string
cursor_paging2_instance = CursorPaging2.from_json(json)
# print the JSON string representation of the object
print(CursorPaging2.to_json())

# convert the object into a dict
cursor_paging2_dict = cursor_paging2_instance.to_dict()
# create an instance of CursorPaging2 from a dict
cursor_paging2_from_dict = CursorPaging2.from_dict(cursor_paging2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


