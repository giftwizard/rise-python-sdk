# InitiatedStatusInfo



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | **str** | Activation target | [optional] 
**payload** | **object** | Event payload | [optional] 
**external_entity_id** | **str** | External entity ID | [optional] 
**request_id** | **str** | Unique identifier for the request that initiated the automation | [optional] 

## Example

```python
from openapi_client.models.initiated_status_info import InitiatedStatusInfo

# TODO update the JSON string below
json = "{}"
# create an instance of InitiatedStatusInfo from a JSON string
initiated_status_info_instance = InitiatedStatusInfo.from_json(json)
# print the JSON string representation of the object
print(InitiatedStatusInfo.to_json())

# convert the object into a dict
initiated_status_info_dict = initiated_status_info_instance.to_dict()
# create an instance of InitiatedStatusInfo from a dict
initiated_status_info_from_dict = InitiatedStatusInfo.from_dict(initiated_status_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


