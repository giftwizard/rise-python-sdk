# ExpressionEvaluationResult



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**passed** | **bool** | Indicates if the expression was evaluated to true or false | [optional] 
**error** | **bool** | Indicates if there was an error in the evaluation process | [optional] 

## Example

```python
from openapi_client.models.expression_evaluation_result import ExpressionEvaluationResult

# TODO update the JSON string below
json = "{}"
# create an instance of ExpressionEvaluationResult from a JSON string
expression_evaluation_result_instance = ExpressionEvaluationResult.from_json(json)
# print the JSON string representation of the object
print(ExpressionEvaluationResult.to_json())

# convert the object into a dict
expression_evaluation_result_dict = expression_evaluation_result_instance.to_dict()
# create an instance of ExpressionEvaluationResult from a dict
expression_evaluation_result_from_dict = ExpressionEvaluationResult.from_dict(expression_evaluation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


