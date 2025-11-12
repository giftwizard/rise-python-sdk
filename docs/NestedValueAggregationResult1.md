# NestedValueAggregationResult1



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Value of the field. | [optional] 
**nested_results** | [**NestedAggregationResults1**](NestedAggregationResults1.md) |  | [optional] 

## Example

```python
from openapi_client.models.nested_value_aggregation_result1 import NestedValueAggregationResult1

# TODO update the JSON string below
json = "{}"
# create an instance of NestedValueAggregationResult1 from a JSON string
nested_value_aggregation_result1_instance = NestedValueAggregationResult1.from_json(json)
# print the JSON string representation of the object
print(NestedValueAggregationResult1.to_json())

# convert the object into a dict
nested_value_aggregation_result1_dict = nested_value_aggregation_result1_instance.to_dict()
# create an instance of NestedValueAggregationResult1 from a dict
nested_value_aggregation_result1_from_dict = NestedValueAggregationResult1.from_dict(nested_value_aggregation_result1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


