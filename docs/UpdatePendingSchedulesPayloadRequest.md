# UpdatePendingSchedulesPayloadRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** |  | [optional] 
**event_payload** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.update_pending_schedules_payload_request import UpdatePendingSchedulesPayloadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePendingSchedulesPayloadRequest from a JSON string
update_pending_schedules_payload_request_instance = UpdatePendingSchedulesPayloadRequest.from_json(json)
# print the JSON string representation of the object
print(UpdatePendingSchedulesPayloadRequest.to_json())

# convert the object into a dict
update_pending_schedules_payload_request_dict = update_pending_schedules_payload_request_instance.to_dict()
# create an instance of UpdatePendingSchedulesPayloadRequest from a dict
update_pending_schedules_payload_request_from_dict = UpdatePendingSchedulesPayloadRequest.from_dict(update_pending_schedules_payload_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


