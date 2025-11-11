# BulkReportEventResult



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_metadata** | **object** | Metadata for the individual item in the request. | [optional] 
**event_info** | **object** | Event details for the item in the request. | [optional] 
**activation_ids** | **List[str]** | The activation IDs of triggered ReportEvents. | [optional] 

## Example

```python
from openapi_client.models.bulk_report_event_result import BulkReportEventResult

# TODO update the JSON string below
json = "{}"
# create an instance of BulkReportEventResult from a JSON string
bulk_report_event_result_instance = BulkReportEventResult.from_json(json)
# print the JSON string representation of the object
print(BulkReportEventResult.to_json())

# convert the object into a dict
bulk_report_event_result_dict = bulk_report_event_result_instance.to_dict()
# create an instance of BulkReportEventResult from a dict
bulk_report_event_result_from_dict = BulkReportEventResult.from_dict(bulk_report_event_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


