# Cursors



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Cursor pointing to next page in the list of results. | [optional] 
**prev** | **str** | Cursor pointing to previous page in the list of results. | [optional] 

## Example

```python
from openapi_client.models.cursors import Cursors

# TODO update the JSON string below
json = "{}"
# create an instance of Cursors from a JSON string
cursors_instance = Cursors.from_json(json)
# print the JSON string representation of the object
print(Cursors.to_json())

# convert the object into a dict
cursors_dict = cursors_instance.to_dict()
# create an instance of Cursors from a dict
cursors_from_dict = Cursors.from_dict(cursors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


