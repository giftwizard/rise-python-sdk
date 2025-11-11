# ConditionExpressionGroup



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operator** | **str** | Expression group operator. | [optional] 
**boolean_expressions** | **List[str]** | List of boolean expressions to be evaluated with the given operator. | [optional] 

## Example

```python
from openapi_client.models.condition_expression_group import ConditionExpressionGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ConditionExpressionGroup from a JSON string
condition_expression_group_instance = ConditionExpressionGroup.from_json(json)
# print the JSON string representation of the object
print(ConditionExpressionGroup.to_json())

# convert the object into a dict
condition_expression_group_dict = condition_expression_group_instance.to_dict()
# create an instance of ConditionExpressionGroup from a dict
condition_expression_group_from_dict = ConditionExpressionGroup.from_dict(condition_expression_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


