# ConditionAction



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**or_expression_groups** | **List[object]** | The condition evaluates to &#x60;true&#x60; if either of the expression groups evaluate to &#x60;true&#x60;. | [optional] 
**true_post_action_ids** | **List[str]** | List of IDs of actions to run when the entire condition is evaluated to &#x60;true&#x60;. | [optional] 
**false_post_action_ids** | **List[str]** | List of IDs of actions to run when the entire condition is evaluated to &#x60;false&#x60;. | [optional] 

## Example

```python
from openapi_client.models.condition_action import ConditionAction

# TODO update the JSON string below
json = "{}"
# create an instance of ConditionAction from a JSON string
condition_action_instance = ConditionAction.from_json(json)
# print the JSON string representation of the object
print(ConditionAction.to_json())

# convert the object into a dict
condition_action_dict = condition_action_instance.to_dict()
# create an instance of ConditionAction from a dict
condition_action_from_dict = ConditionAction.from_dict(condition_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


