# AggregationResults1



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Aggregation name, returned in &#x60;aggregations.results.name&#x60;. | [optional] 
**type** | **str** | Aggregation type. Must align with the corresponding aggregation field. | [optional] 
**field_path** | **str** | Field to aggregate by. Use dot notation to specify a JSON path. For example, &#x60;order.address.streetName&#x60;. | [optional] 
**values** | [**ValueResultsValues**](ValueResultsValues.md) |  | [optional] 
**ranges** | [**RangeResultsRanges**](RangeResultsRanges.md) |  | [optional] 
**scalar** | [**NestedAggregationResults1OneOf2Scalar**](NestedAggregationResults1OneOf2Scalar.md) |  | [optional] 
**grouped_by_value** | [**GroupByValueResultsGroupedByValue**](GroupByValueResultsGroupedByValue.md) |  | [optional] 
**date_histogram** | [**NestedAggregationResults1OneOf4DateHistogram**](NestedAggregationResults1OneOf4DateHistogram.md) |  | [optional] 
**nested** | [**NestedAggregationResults1OneOf5Nested**](NestedAggregationResults1OneOf5Nested.md) |  | [optional] 

## Example

```python
from openapi_client.models.aggregation_results1 import AggregationResults1

# TODO update the JSON string below
json = "{}"
# create an instance of AggregationResults1 from a JSON string
aggregation_results1_instance = AggregationResults1.from_json(json)
# print the JSON string representation of the object
print(AggregationResults1.to_json())

# convert the object into a dict
aggregation_results1_dict = aggregation_results1_instance.to_dict()
# create an instance of AggregationResults1 from a dict
aggregation_results1_from_dict = AggregationResults1.from_dict(aggregation_results1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


