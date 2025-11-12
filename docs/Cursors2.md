# Cursors2

Cursors to navigate through the result pages using `next` and `prev`. Returned if cursor paging is used.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Cursor string pointing to the next page in the list of results. | [optional] 
**prev** | **str** | Cursor pointing to the previous page in the list of results. | [optional] 

## Example

```python
from openapi_client.models.cursors2 import Cursors2

# TODO update the JSON string below
json = "{}"
# create an instance of Cursors2 from a JSON string
cursors2_instance = Cursors2.from_json(json)
# print the JSON string representation of the object
print(Cursors2.to_json())

# convert the object into a dict
cursors2_dict = cursors2_instance.to_dict()
# create an instance of Cursors2 from a dict
cursors2_from_dict = Cursors2.from_dict(cursors2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


