# DelayHelper



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule_identifier** | **str** | jsonata expression, for example: triggerName + eventId | [optional] 
**delay** | **object** | decide how long we should wait | [optional] 
**post_actions** | **List[object]** | Delay&#39;s post actions. | [optional] 
**overrideable** | **bool** | Optional: if true, any new schedule with the same schedule identifier will override the existing one. If false, the new schedule will be ignored. | [optional] 
**post_actions_ids** | **List[str]** | Delay&#39;s post actions ids. | [optional] 

## Example

```python
from openapi_client.models.delay_helper import DelayHelper

# TODO update the JSON string below
json = "{}"
# create an instance of DelayHelper from a JSON string
delay_helper_instance = DelayHelper.from_json(json)
# print the JSON string representation of the object
print(DelayHelper.to_json())

# convert the object into a dict
delay_helper_dict = delay_helper_instance.to_dict()
# create an instance of DelayHelper from a dict
delay_helper_from_dict = DelayHelper.from_dict(delay_helper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


