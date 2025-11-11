# ValueAggregationResult1



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Value of the field. | [optional] 
**count** | **int** | Number of entities with this value. | [optional] 

## Example

```python
from openapi_client.models.value_aggregation_result1 import ValueAggregationResult1

# TODO update the JSON string below
json = "{}"
# create an instance of ValueAggregationResult1 from a JSON string
value_aggregation_result1_instance = ValueAggregationResult1.from_json(json)
# print the JSON string representation of the object
print(ValueAggregationResult1.to_json())

# convert the object into a dict
value_aggregation_result1_dict = value_aggregation_result1_instance.to_dict()
# create an instance of ValueAggregationResult1 from a dict
value_aggregation_result1_from_dict = ValueAggregationResult1.from_dict(value_aggregation_result1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


