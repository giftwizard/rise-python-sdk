# BulkReportEventRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trigger_key** | **str** | ey as defined in your app&#39;s trigger configuration in the app dashboard. For example, &#x60;form_submitted&#x60; or &#x60;invoice_due&#x60;. | [optional] 
**events_info** | **List[object]** | Repeated list of event details for bulk reporting. | [optional] 

## Example

```python
from openapi_client.models.bulk_report_event_request import BulkReportEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkReportEventRequest from a JSON string
bulk_report_event_request_instance = BulkReportEventRequest.from_json(json)
# print the JSON string representation of the object
print(BulkReportEventRequest.to_json())

# convert the object into a dict
bulk_report_event_request_dict = bulk_report_event_request_instance.to_dict()
# create an instance of BulkReportEventRequest from a dict
bulk_report_event_request_from_dict = BulkReportEventRequest.from_dict(bulk_report_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


