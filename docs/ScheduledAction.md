# ScheduledAction



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Action&#39;s id. | [optional] 
**delay** | **object** | decide how long we should wait | [optional] 

## Example

```python
from openapi_client.models.scheduled_action import ScheduledAction

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledAction from a JSON string
scheduled_action_instance = ScheduledAction.from_json(json)
# print the JSON string representation of the object
print(ScheduledAction.to_json())

# convert the object into a dict
scheduled_action_dict = scheduled_action_instance.to_dict()
# create an instance of ScheduledAction from a dict
scheduled_action_from_dict = ScheduledAction.from_dict(scheduled_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


