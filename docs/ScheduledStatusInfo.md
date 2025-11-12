# ScheduledStatusInfo



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule_id** | **str** | Schedule identifier | [optional] 
**var_date** | **datetime** | Indicates when the activation should start | [optional] 

## Example

```python
from openapi_client.models.scheduled_status_info import ScheduledStatusInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledStatusInfo from a JSON string
scheduled_status_info_instance = ScheduledStatusInfo.from_json(json)
# print the JSON string representation of the object
print(ScheduledStatusInfo.to_json())

# convert the object into a dict
scheduled_status_info_dict = scheduled_status_info_instance.to_dict()
# create an instance of ScheduledStatusInfo from a dict
scheduled_status_info_from_dict = ScheduledStatusInfo.from_dict(scheduled_status_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


