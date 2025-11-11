# ConditionFilter



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**condition_blocks** | **List[object]** | condition evaluates to &#x60;true&#x60; if either of the blocks evaluate to &#x60;true&#x60; (aka OR between all). | [optional] 
**post_actions** | **List[object]** | Actions to perform when condition_blocks evaluates to &#x60;true&#x60;. | [optional] 
**post_actions_ids** | **List[str]** | Action&#39;s post actions ids. | [optional] 
**else_post_actions** | **List[object]** | Actions to perform when condition_blocks evaluates to &#x60;false&#x60;. | [optional] 

## Example

```python
from openapi_client.models.condition_filter import ConditionFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ConditionFilter from a JSON string
condition_filter_instance = ConditionFilter.from_json(json)
# print the JSON string representation of the object
print(ConditionFilter.to_json())

# convert the object into a dict
condition_filter_dict = condition_filter_instance.to_dict()
# create an instance of ConditionFilter from a dict
condition_filter_from_dict = ConditionFilter.from_dict(condition_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


