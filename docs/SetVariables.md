# SetVariables



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**output_mapping** | **str** | Action&#39;s output mapping. Jsonata expressions to set variables for example: { \&quot;var1\&quot;: \&quot;$average([10,20])\&quot;, \&quot;var2\&quot;: \&quot;$number($lookup($, $decodeUrlComponent(\\\&quot;var1\\\&quot;))) &gt;&#x3D; $number(8)\&quot;\&quot; } | [optional] 
**post_actions** | **List[object]** | Action&#39;s post actions. | [optional] 
**post_actions_ids** | **List[str]** | Action&#39;s post actions ids. | [optional] 
**namespace** | **str** | The namespace of the action | [optional] 
**output_schema** | **object** | Json Schema for the output mapping | [optional] 

## Example

```python
from openapi_client.models.set_variables import SetVariables

# TODO update the JSON string below
json = "{}"
# create an instance of SetVariables from a JSON string
set_variables_instance = SetVariables.from_json(json)
# print the JSON string representation of the object
print(SetVariables.to_json())

# convert the object into a dict
set_variables_dict = set_variables_instance.to_dict()
# create an instance of SetVariables from a dict
set_variables_from_dict = SetVariables.from_dict(set_variables_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


