# CancelledStatusInfo



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | Cancellation reason | [optional] 
**initiator** | **object** | Identity (such as user, app, etc.) that caused the cancellation. | [optional] 

## Example

```python
from openapi_client.models.cancelled_status_info import CancelledStatusInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CancelledStatusInfo from a JSON string
cancelled_status_info_instance = CancelledStatusInfo.from_json(json)
# print the JSON string representation of the object
print(CancelledStatusInfo.to_json())

# convert the object into a dict
cancelled_status_info_dict = cancelled_status_info_instance.to_dict()
# create an instance of CancelledStatusInfo from a dict
cancelled_status_info_from_dict = CancelledStatusInfo.from_dict(cancelled_status_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


