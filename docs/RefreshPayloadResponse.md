# RefreshPayloadResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payload** | **object** | Updated payload. | [optional] 
**cancel_activation** | **bool** | If the automation activation should be canceled (default is false) | [optional] 

## Example

```python
from openapi_client.models.refresh_payload_response import RefreshPayloadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RefreshPayloadResponse from a JSON string
refresh_payload_response_instance = RefreshPayloadResponse.from_json(json)
# print the JSON string representation of the object
print(RefreshPayloadResponse.to_json())

# convert the object into a dict
refresh_payload_response_dict = refresh_payload_response_instance.to_dict()
# create an instance of RefreshPayloadResponse from a dict
refresh_payload_response_from_dict = RefreshPayloadResponse.from_dict(refresh_payload_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


