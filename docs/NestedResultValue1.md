# NestedResultValue1



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**ValueResultsValues**](ValueResultsValues.md) |  | [optional] 
**ranges** | [**RangeResultsRanges**](RangeResultsRanges.md) |  | [optional] 
**scalar** | [**NestedAggregationResults1OneOf2Scalar**](NestedAggregationResults1OneOf2Scalar.md) |  | [optional] 
**grouped_by_value** | **object** | Circular reference to #/components/schemas/wix.common.AggregationData.AggregationResults.GroupByValueResults (simplified) | [optional] 
**date_histogram** | [**NestedAggregationResults1OneOf4DateHistogram**](NestedAggregationResults1OneOf4DateHistogram.md) |  | [optional] 
**nested** | **object** | Circular reference to #/components/schemas/wix.common.AggregationData.AggregationResults.NestedResults (simplified) | [optional] 

## Example

```python
from openapi_client.models.nested_result_value1 import NestedResultValue1

# TODO update the JSON string below
json = "{}"
# create an instance of NestedResultValue1 from a JSON string
nested_result_value1_instance = NestedResultValue1.from_json(json)
# print the JSON string representation of the object
print(NestedResultValue1.to_json())

# convert the object into a dict
nested_result_value1_dict = nested_result_value1_instance.to_dict()
# create an instance of NestedResultValue1 from a dict
nested_result_value1_from_dict = NestedResultValue1.from_dict(nested_result_value1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


