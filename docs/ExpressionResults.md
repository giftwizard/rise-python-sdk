# ExpressionResults

Collects results per each expression evaluation that took place

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**value** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.expression_results import ExpressionResults

# TODO update the JSON string below
json = "{}"
# create an instance of ExpressionResults from a JSON string
expression_results_instance = ExpressionResults.from_json(json)
# print the JSON string representation of the object
print(ExpressionResults.to_json())

# convert the object into a dict
expression_results_dict = expression_results_instance.to_dict()
# create an instance of ExpressionResults from a dict
expression_results_from_dict = ExpressionResults.from_dict(expression_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


