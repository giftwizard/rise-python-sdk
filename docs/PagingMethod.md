# PagingMethod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor_paging** | [**PagingMethodCursorPaging**](PagingMethodCursorPaging.md) |  | [optional] 

## Example

```python
from openapi_client.models.paging_method import PagingMethod

# TODO update the JSON string below
json = "{}"
# create an instance of PagingMethod from a JSON string
paging_method_instance = PagingMethod.from_json(json)
# print the JSON string representation of the object
print(PagingMethod.to_json())

# convert the object into a dict
paging_method_dict = paging_method_instance.to_dict()
# create an instance of PagingMethod from a dict
paging_method_from_dict = PagingMethod.from_dict(paging_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


