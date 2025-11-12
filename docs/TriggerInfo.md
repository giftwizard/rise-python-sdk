# TriggerInfo



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** | Trigger app ID | [optional] 
**trigger_key** | **str** | Trigger key | [optional] 

## Example

```python
from openapi_client.models.trigger_info import TriggerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerInfo from a JSON string
trigger_info_instance = TriggerInfo.from_json(json)
# print the JSON string representation of the object
print(TriggerInfo.to_json())

# convert the object into a dict
trigger_info_dict = trigger_info_instance.to_dict()
# create an instance of TriggerInfo from a dict
trigger_info_from_dict = TriggerInfo.from_dict(trigger_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


