# SkippedStatusInfo



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | The reason why the automation activation was skipped | [optional] 
**payload** | **object** | Event payload | [optional] 
**external_entity_id** | **str** | External entity ID | [optional] 
**request_id** | **str** | Unique identifier for the request that initiated the automation | [optional] 

## Example

```python
from openapi_client.models.skipped_status_info import SkippedStatusInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SkippedStatusInfo from a JSON string
skipped_status_info_instance = SkippedStatusInfo.from_json(json)
# print the JSON string representation of the object
print(SkippedStatusInfo.to_json())

# convert the object into a dict
skipped_status_info_dict = skipped_status_info_instance.to_dict()
# create an instance of SkippedStatusInfo from a dict
skipped_status_info_from_dict = SkippedStatusInfo.from_dict(skipped_status_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


