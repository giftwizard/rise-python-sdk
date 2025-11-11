# PagingMethod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**paging** | **object** | Paging options to limit and skip the number of items. | [optional] 
**cursor_paging** | **object** | Cursor token pointing to a page of results. Not used in the first request. Following requests use the cursor token and not &#x60;filter&#x60; or &#x60;sort&#x60;. | [optional] 

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


