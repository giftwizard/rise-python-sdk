# DateHistogramAggregation



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | **str** | Interval for date histogram aggregation. | [optional] 

## Example

```python
from openapi_client.models.date_histogram_aggregation import DateHistogramAggregation

# TODO update the JSON string below
json = "{}"
# create an instance of DateHistogramAggregation from a JSON string
date_histogram_aggregation_instance = DateHistogramAggregation.from_json(json)
# print the JSON string representation of the object
print(DateHistogramAggregation.to_json())

# convert the object into a dict
date_histogram_aggregation_dict = date_histogram_aggregation_instance.to_dict()
# create an instance of DateHistogramAggregation from a dict
date_histogram_aggregation_from_dict = DateHistogramAggregation.from_dict(date_histogram_aggregation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


