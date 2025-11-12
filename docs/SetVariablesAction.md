# SetVariablesAction



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**output_mapping** | **object** | output mapping for example: {\&quot;someField\&quot;: \&quot;{{10}}\&quot;, \&quot;someOtherField\&quot;: \&quot;{{multiply( var(&#39;account.points.balance&#39;) ;2 )}}\&quot; } | [optional] 
**output_schema** | **object** | output json schema representation could be string instead of Struct (and introduce some compression to minimize the size of it) | [optional] 
**post_action_ids** | **List[str]** | List of IDs of actions to run in parallel after variable initialization. | [optional] 

## Example

```python
from openapi_client.models.set_variables_action import SetVariablesAction

# TODO update the JSON string below
json = "{}"
# create an instance of SetVariablesAction from a JSON string
set_variables_action_instance = SetVariablesAction.from_json(json)
# print the JSON string representation of the object
print(SetVariablesAction.to_json())

# convert the object into a dict
set_variables_action_dict = set_variables_action_instance.to_dict()
# create an instance of SetVariablesAction from a dict
set_variables_action_from_dict = SetVariablesAction.from_dict(set_variables_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


