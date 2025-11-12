# RefreshPayloadRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_def_id** | **str** | Application definition ID. | [optional] 
**trigger_key** | **str** | Trigger key. | [optional] 
**payload** | **object** | Payload to refresh. | [optional] 
**external_entity_id** | **str** | External entity ID. | [optional] 

## Example

```python
from openapi_client.models.refresh_payload_request import RefreshPayloadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RefreshPayloadRequest from a JSON string
refresh_payload_request_instance = RefreshPayloadRequest.from_json(json)
# print the JSON string representation of the object
print(RefreshPayloadRequest.to_json())

# convert the object into a dict
refresh_payload_request_dict = refresh_payload_request_instance.to_dict()
# create an instance of RefreshPayloadRequest from a dict
refresh_payload_request_from_dict = RefreshPayloadRequest.from_dict(refresh_payload_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


