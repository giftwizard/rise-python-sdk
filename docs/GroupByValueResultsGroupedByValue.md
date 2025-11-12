# GroupByValueResultsGroupedByValue

Group by value aggregation results.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[NestedValueAggregationResult1]**](NestedValueAggregationResult1.md) | List of value aggregations. | [optional] 

## Example

```python
from openapi_client.models.group_by_value_results_grouped_by_value import GroupByValueResultsGroupedByValue

# TODO update the JSON string below
json = "{}"
# create an instance of GroupByValueResultsGroupedByValue from a JSON string
group_by_value_results_grouped_by_value_instance = GroupByValueResultsGroupedByValue.from_json(json)
# print the JSON string representation of the object
print(GroupByValueResultsGroupedByValue.to_json())

# convert the object into a dict
group_by_value_results_grouped_by_value_dict = group_by_value_results_grouped_by_value_instance.to_dict()
# create an instance of GroupByValueResultsGroupedByValue from a dict
group_by_value_results_grouped_by_value_from_dict = GroupByValueResultsGroupedByValue.from_dict(group_by_value_results_grouped_by_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


