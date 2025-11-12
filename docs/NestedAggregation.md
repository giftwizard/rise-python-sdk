# NestedAggregation

Nested aggregation expressed through a list of aggregation where each next aggregation is nested within previous one.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nested_aggregations** | **List[object]** | Flattened list of aggregations, where each aggregation is nested within previous one. | [optional] 

## Example

```python
from openapi_client.models.nested_aggregation import NestedAggregation

# TODO update the JSON string below
json = "{}"
# create an instance of NestedAggregation from a JSON string
nested_aggregation_instance = NestedAggregation.from_json(json)
# print the JSON string representation of the object
print(NestedAggregation.to_json())

# convert the object into a dict
nested_aggregation_dict = nested_aggregation_instance.to_dict()
# create an instance of NestedAggregation from a dict
nested_aggregation_from_dict = NestedAggregation.from_dict(nested_aggregation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


