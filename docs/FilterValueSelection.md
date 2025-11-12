# FilterValueSelection



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected_filter_values** | **List[str]** | Values that can help the user filter certain automations, values will look like \&quot;&lt;filter_id&gt;__&lt;selected_value&gt;\&quot; | [optional] 

## Example

```python
from openapi_client.models.filter_value_selection import FilterValueSelection

# TODO update the JSON string below
json = "{}"
# create an instance of FilterValueSelection from a JSON string
filter_value_selection_instance = FilterValueSelection.from_json(json)
# print the JSON string representation of the object
print(FilterValueSelection.to_json())

# convert the object into a dict
filter_value_selection_dict = filter_value_selection_instance.to_dict()
# create an instance of FilterValueSelection from a dict
filter_value_selection_from_dict = FilterValueSelection.from_dict(filter_value_selection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


