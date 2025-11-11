# ValueAggregationResult



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Value of the field. | [optional] 
**count** | **int** | Number of entities with this value. | [optional] 

## Example

```python
from openapi_client.models.value_aggregation_result import ValueAggregationResult

# TODO update the JSON string below
json = "{}"
# create an instance of ValueAggregationResult from a JSON string
value_aggregation_result_instance = ValueAggregationResult.from_json(json)
# print the JSON string representation of the object
print(ValueAggregationResult.to_json())

# convert the object into a dict
value_aggregation_result_dict = value_aggregation_result_instance.to_dict()
# create an instance of ValueAggregationResult from a dict
value_aggregation_result_from_dict = ValueAggregationResult.from_dict(value_aggregation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


