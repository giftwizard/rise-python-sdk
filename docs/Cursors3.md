# Cursors3

Cursors to navigate through the result pages using `next` and `prev`. Returned if cursor paging is used.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Cursor pointing to next page in the list of results. | [optional] 
**prev** | **str** | Cursor pointing to previous page in the list of results. | [optional] 

## Example

```python
from openapi_client.models.cursors3 import Cursors3

# TODO update the JSON string below
json = "{}"
# create an instance of Cursors3 from a JSON string
cursors3_instance = Cursors3.from_json(json)
# print the JSON string representation of the object
print(Cursors3.to_json())

# convert the object into a dict
cursors3_dict = cursors3_instance.to_dict()
# create an instance of Cursors3 from a dict
cursors3_from_dict = Cursors3.from_dict(cursors3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


