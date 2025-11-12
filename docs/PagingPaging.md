# PagingPaging

Paging options to limit and skip the number of items.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | Number of items to load. | [optional] 
**offset** | **int** | Number of items to skip in the current sort order. | [optional] 

## Example

```python
from openapi_client.models.paging_paging import PagingPaging

# TODO update the JSON string below
json = "{}"
# create an instance of PagingPaging from a JSON string
paging_paging_instance = PagingPaging.from_json(json)
# print the JSON string representation of the object
print(PagingPaging.to_json())

# convert the object into a dict
paging_paging_dict = paging_paging_instance.to_dict()
# create an instance of PagingPaging from a dict
paging_paging_from_dict = PagingPaging.from_dict(paging_paging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


