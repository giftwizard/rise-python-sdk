# AggregationData1

Aggregation data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[AggregationResults1]**](AggregationResults1.md) | List of the aggregated data results. | [optional] 

## Example

```python
from openapi_client.models.aggregation_data1 import AggregationData1

# TODO update the JSON string below
json = "{}"
# create an instance of AggregationData1 from a JSON string
aggregation_data1_instance = AggregationData1.from_json(json)
# print the JSON string representation of the object
print(AggregationData1.to_json())

# convert the object into a dict
aggregation_data1_dict = aggregation_data1_instance.to_dict()
# create an instance of AggregationData1 from a dict
aggregation_data1_from_dict = AggregationData1.from_dict(aggregation_data1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


