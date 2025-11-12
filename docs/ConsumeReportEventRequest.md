# ConsumeReportEventRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events_info** | **List[object]** | Repeated list of event details for bulk reporting. | [optional] 
**trigger_app_id** | **str** | trigger app id | [optional] 
**trigger_key** | **str** | trigger key | [optional] 

## Example

```python
from openapi_client.models.consume_report_event_request import ConsumeReportEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConsumeReportEventRequest from a JSON string
consume_report_event_request_instance = ConsumeReportEventRequest.from_json(json)
# print the JSON string representation of the object
print(ConsumeReportEventRequest.to_json())

# convert the object into a dict
consume_report_event_request_dict = consume_report_event_request_instance.to_dict()
# create an instance of ConsumeReportEventRequest from a dict
consume_report_event_request_from_dict = ConsumeReportEventRequest.from_dict(consume_report_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


