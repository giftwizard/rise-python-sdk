# RangeResultsRanges

Range aggregation results.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[RangeAggregationResult1]**](RangeAggregationResult1.md) | List of ranges returned in the same order as requested. | [optional] 

## Example

```python
from openapi_client.models.range_results_ranges import RangeResultsRanges

# TODO update the JSON string below
json = "{}"
# create an instance of RangeResultsRanges from a JSON string
range_results_ranges_instance = RangeResultsRanges.from_json(json)
# print the JSON string representation of the object
print(RangeResultsRanges.to_json())

# convert the object into a dict
range_results_ranges_dict = range_results_ranges_instance.to_dict()
# create an instance of RangeResultsRanges from a dict
range_results_ranges_from_dict = RangeResultsRanges.from_dict(range_results_ranges_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


