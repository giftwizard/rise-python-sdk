# ValueResultsValues

Value aggregation results.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[ValueAggregationResult1]**](ValueAggregationResult1.md) | List of value aggregations. | [optional] 

## Example

```python
from openapi_client.models.value_results_values import ValueResultsValues

# TODO update the JSON string below
json = "{}"
# create an instance of ValueResultsValues from a JSON string
value_results_values_instance = ValueResultsValues.from_json(json)
# print the JSON string representation of the object
print(ValueResultsValues.to_json())

# convert the object into a dict
value_results_values_dict = value_results_values_instance.to_dict()
# create an instance of ValueResultsValues from a dict
value_results_values_from_dict = ValueResultsValues.from_dict(value_results_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


