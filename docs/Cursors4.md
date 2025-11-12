# Cursors4

Cursor strings that point to the next page, previous page, or both.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Cursor string pointing to the next page in the list of results. | [optional] 
**prev** | **str** | Cursor pointing to the previous page in the list of results. | [optional] 

## Example

```python
from openapi_client.models.cursors4 import Cursors4

# TODO update the JSON string below
json = "{}"
# create an instance of Cursors4 from a JSON string
cursors4_instance = Cursors4.from_json(json)
# print the JSON string representation of the object
print(Cursors4.to_json())

# convert the object into a dict
cursors4_dict = cursors4_instance.to_dict()
# create an instance of Cursors4 from a dict
cursors4_from_dict = Cursors4.from_dict(cursors4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


