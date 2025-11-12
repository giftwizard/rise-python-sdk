# SpiAction



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_def_id** | **str** | The App Def Id of the action provider | [optional] 
**action_key** | **str** | Identifier for this action - human readable action key - unique per app def id | [optional] 
**user_action_config** | **str** | The configuration of the user for this action, can include params that are taken from the trigger event payload | [optional] 
**post_actions** | **List[object]** | The post action to execute after this action | [optional] 
**user_output_action_config** | **str** | The output configuration of the user for this action, can include params that are taken from the trigger event payload | [optional] 
**skip_condition_expression** | **str** | optional skip condition expression for current action decides whether to skip the action before executing it&#39;s post actions | [optional] 
**post_actions_ids** | **List[str]** | Action&#39;s post actions ids. | [optional] 
**namespace** | **str** | The namespace of the action | [optional] 

## Example

```python
from openapi_client.models.spi_action import SpiAction

# TODO update the JSON string below
json = "{}"
# create an instance of SpiAction from a JSON string
spi_action_instance = SpiAction.from_json(json)
# print the JSON string representation of the object
print(SpiAction.to_json())

# convert the object into a dict
spi_action_dict = spi_action_instance.to_dict()
# create an instance of SpiAction from a dict
spi_action_from_dict = SpiAction.from_dict(spi_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


