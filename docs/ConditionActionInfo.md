# ConditionActionInfo



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**passed** | **bool** | Indicates that the condition &#x60;if&#x60; clause evaluated to &#x60;true&#x60;. | [optional] 
**expression_results** | [**ExpressionResults**](ExpressionResults.md) |  | [optional] 

## Example

```python
from openapi_client.models.condition_action_info import ConditionActionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ConditionActionInfo from a JSON string
condition_action_info_instance = ConditionActionInfo.from_json(json)
# print the JSON string representation of the object
print(ConditionActionInfo.to_json())

# convert the object into a dict
condition_action_info_dict = condition_action_info_instance.to_dict()
# create an instance of ConditionActionInfo from a dict
condition_action_info_from_dict = ConditionActionInfo.from_dict(condition_action_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


