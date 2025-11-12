# NestedValueAggregationResult



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Value of the field. | [optional] 
**nested_results** | **object** | Nested aggregations. | [optional] 

## Example

```python
from openapi_client.models.nested_value_aggregation_result import NestedValueAggregationResult

# TODO update the JSON string below
json = "{}"
# create an instance of NestedValueAggregationResult from a JSON string
nested_value_aggregation_result_instance = NestedValueAggregationResult.from_json(json)
# print the JSON string representation of the object
print(NestedValueAggregationResult.to_json())

# convert the object into a dict
nested_value_aggregation_result_dict = nested_value_aggregation_result_instance.to_dict()
# create an instance of NestedValueAggregationResult from a dict
nested_value_aggregation_result_from_dict = NestedValueAggregationResult.from_dict(nested_value_aggregation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


