# RangeAggregationResult1



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **float** | Inclusive lower bound of the range. | [optional] 
**to** | **float** | Exclusive upper bound of the range. | [optional] 
**count** | **int** | Total number of entities in this range. | [optional] 

## Example

```python
from openapi_client.models.range_aggregation_result1 import RangeAggregationResult1

# TODO update the JSON string below
json = "{}"
# create an instance of RangeAggregationResult1 from a JSON string
range_aggregation_result1_instance = RangeAggregationResult1.from_json(json)
# print the JSON string representation of the object
print(RangeAggregationResult1.to_json())

# convert the object into a dict
range_aggregation_result1_dict = range_aggregation_result1_instance.to_dict()
# create an instance of RangeAggregationResult1 from a dict
range_aggregation_result1_from_dict = RangeAggregationResult1.from_dict(range_aggregation_result1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


