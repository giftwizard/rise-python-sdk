# SearchDetails



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** | Search mode. Defines the search logic for combining multiple terms in the &#x60;expression&#x60;. | [optional] 
**expression** | **str** | Search term or expression. | [optional] 
**fields** | **List[str]** | Fields to search in. If the array is empty, all searchable fields are searched. Use dot notation to specify a JSON path. For example, &#x60;order.address.streetName&#x60;. | [optional] 
**fuzzy** | **bool** | Whether to enable the search function to use an algorithm to automatically find results that are close to the search expression, such as typos and declensions. | [optional] 

## Example

```python
from openapi_client.models.search_details import SearchDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SearchDetails from a JSON string
search_details_instance = SearchDetails.from_json(json)
# print the JSON string representation of the object
print(SearchDetails.to_json())

# convert the object into a dict
search_details_dict = search_details_instance.to_dict()
# create an instance of SearchDetails from a dict
search_details_from_dict = SearchDetails.from_dict(search_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


