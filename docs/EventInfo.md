# EventInfo



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payload** | **object** | Event payload, formatted as key:value pairs. Must comply with the payload schema if you provided one when configuring your trigger. | [optional] 
**external_entity_id** | **str** | ID of the related resource in GUID format. | [optional] 
**idempotency** | **object** | Idempotency information for the event. | [optional] 

## Example

```python
from openapi_client.models.event_info import EventInfo

# TODO update the JSON string below
json = "{}"
# create an instance of EventInfo from a JSON string
event_info_instance = EventInfo.from_json(json)
# print the JSON string representation of the object
print(EventInfo.to_json())

# convert the object into a dict
event_info_dict = event_info_instance.to_dict()
# create an instance of EventInfo from a dict
event_info_from_dict = EventInfo.from_dict(event_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


