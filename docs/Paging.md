# Paging



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | Number of items to load. | [optional] 
**offset** | **int** | Number of items to skip in the current sort order. | [optional] 

## Example

```python
from openapi_client.models.paging import Paging

# TODO update the JSON string below
json = "{}"
# create an instance of Paging from a JSON string
paging_instance = Paging.from_json(json)
# print the JSON string representation of the object
print(Paging.to_json())

# convert the object into a dict
paging_dict = paging_instance.to_dict()
# create an instance of Paging from a dict
paging_from_dict = Paging.from_dict(paging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


