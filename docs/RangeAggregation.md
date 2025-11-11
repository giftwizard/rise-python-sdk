# RangeAggregation



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buckets** | **List[object]** | List of range buckets. During aggregation each entity is placed in the first bucket its value falls into, based on the provided range bounds. | [optional] 

## Example

```python
from openapi_client.models.range_aggregation import RangeAggregation

# TODO update the JSON string below
json = "{}"
# create an instance of RangeAggregation from a JSON string
range_aggregation_instance = RangeAggregation.from_json(json)
# print the JSON string representation of the object
print(RangeAggregation.to_json())

# convert the object into a dict
range_aggregation_dict = range_aggregation_instance.to_dict()
# create an instance of RangeAggregation from a dict
range_aggregation_from_dict = RangeAggregation.from_dict(range_aggregation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


