# AggregationResults1



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Aggregation name, returned in &#x60;aggregations.results.name&#x60;. | [optional] 
**type** | **str** | Aggregation type. Must align with the corresponding aggregation field. | [optional] 
**field_path** | **str** | Field to aggregate by. Use dot notation to specify a JSON path. For example, &#x60;order.address.streetName&#x60;. | [optional] 
**values** | [**ValueResults1**](ValueResults1.md) |  | [optional] 
**ranges** | [**RangeResults1**](RangeResults1.md) |  | [optional] 
**scalar** | [**ScalarResult1**](ScalarResult1.md) |  | [optional] 
**grouped_by_value** | [**GroupByValueResults1**](GroupByValueResults1.md) |  | [optional] 
**date_histogram** | [**DateHistogramResults1**](DateHistogramResults1.md) |  | [optional] 
**nested** | [**NestedResults1**](NestedResults1.md) |  | [optional] 

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


