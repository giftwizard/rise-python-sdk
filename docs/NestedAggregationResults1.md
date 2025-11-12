# NestedAggregationResults1

Nested aggregations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Unique, caller-defined aggregation name, identifiable by the requested aggregation &#x60;name&#x60;. | [optional] 
**type** | **str** | Aggregation type. | [optional] 
**field_path** | **str** | Field which the data was aggregated by. | [optional] 
**values** | [**ValueResultsValues**](ValueResultsValues.md) |  | [optional] 
**ranges** | [**RangeResultsRanges**](RangeResultsRanges.md) |  | [optional] 
**scalar** | [**NestedAggregationResults1OneOf2Scalar**](NestedAggregationResults1OneOf2Scalar.md) |  | [optional] 
**grouped_by_value** | **object** | Circular reference to #/components/schemas/wix.common.AggregationData.AggregationResults.GroupByValueResults (simplified) | [optional] 
**date_histogram** | [**NestedAggregationResults1OneOf4DateHistogram**](NestedAggregationResults1OneOf4DateHistogram.md) |  | [optional] 
**nested** | [**NestedAggregationResults1OneOf5Nested**](NestedAggregationResults1OneOf5Nested.md) |  | [optional] 

## Example

```python
from openapi_client.models.nested_aggregation_results1 import NestedAggregationResults1

# TODO update the JSON string below
json = "{}"
# create an instance of NestedAggregationResults1 from a JSON string
nested_aggregation_results1_instance = NestedAggregationResults1.from_json(json)
# print the JSON string representation of the object
print(NestedAggregationResults1.to_json())

# convert the object into a dict
nested_aggregation_results1_dict = nested_aggregation_results1_instance.to_dict()
# create an instance of NestedAggregationResults1 from a dict
nested_aggregation_results1_from_dict = NestedAggregationResults1.from_dict(nested_aggregation_results1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


