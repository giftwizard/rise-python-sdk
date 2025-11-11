# FailedStatusInfo



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_description** | **str** | Error description | [optional] 
**error_code** | **str** | Error code | [optional] 

## Example

```python
from openapi_client.models.failed_status_info import FailedStatusInfo

# TODO update the JSON string below
json = "{}"
# create an instance of FailedStatusInfo from a JSON string
failed_status_info_instance = FailedStatusInfo.from_json(json)
# print the JSON string representation of the object
print(FailedStatusInfo.to_json())

# convert the object into a dict
failed_status_info_dict = failed_status_info_instance.to_dict()
# create an instance of FailedStatusInfo from a dict
failed_status_info_from_dict = FailedStatusInfo.from_dict(failed_status_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


