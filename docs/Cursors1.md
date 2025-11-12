# Cursors1

Offset that was requested.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Cursor pointing to next page in the list of results. | [optional] 
**prev** | **str** | Cursor pointing to previous page in the list of results. | [optional] 

## Example

```python
from openapi_client.models.cursors1 import Cursors1

# TODO update the JSON string below
json = "{}"
# create an instance of Cursors1 from a JSON string
cursors1_instance = Cursors1.from_json(json)
# print the JSON string representation of the object
print(Cursors1.to_json())

# convert the object into a dict
cursors1_dict = cursors1_instance.to_dict()
# create an instance of Cursors1 from a dict
cursors1_from_dict = Cursors1.from_dict(cursors1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


