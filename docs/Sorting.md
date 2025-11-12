# Sorting



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_name** | **str** | Name of the field to sort by. | [optional] 
**order** | **str** | Sort order. | [optional] 

## Example

```python
from openapi_client.models.sorting import Sorting

# TODO update the JSON string below
json = "{}"
# create an instance of Sorting from a JSON string
sorting_instance = Sorting.from_json(json)
# print the JSON string representation of the object
print(Sorting.to_json())

# convert the object into a dict
sorting_dict = sorting_instance.to_dict()
# create an instance of Sorting from a dict
sorting_from_dict = Sorting.from_dict(sorting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


