# NestedResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nested** | [**NestedAggregationResults1OneOf5Nested**](NestedAggregationResults1OneOf5Nested.md) |  | [optional] 

## Example

```python
from openapi_client.models.nested_results import NestedResults

# TODO update the JSON string below
json = "{}"
# create an instance of NestedResults from a JSON string
nested_results_instance = NestedResults.from_json(json)
# print the JSON string representation of the object
print(NestedResults.to_json())

# convert the object into a dict
nested_results_dict = nested_results_instance.to_dict()
# create an instance of NestedResults from a dict
nested_results_from_dict = NestedResults.from_dict(nested_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


