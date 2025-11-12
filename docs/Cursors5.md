# Cursors5

Offset that was requested.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Cursor pointing to next page in the list of results. | [optional] 
**prev** | **str** | Cursor pointing to previous page in the list of results. | [optional] 

## Example

```python
from openapi_client.models.cursors5 import Cursors5

# TODO update the JSON string below
json = "{}"
# create an instance of Cursors5 from a JSON string
cursors5_instance = Cursors5.from_json(json)
# print the JSON string representation of the object
print(Cursors5.to_json())

# convert the object into a dict
cursors5_dict = cursors5_instance.to_dict()
# create an instance of Cursors5 from a dict
cursors5_from_dict = Cursors5.from_dict(cursors5_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


