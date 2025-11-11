# BulkReportEventResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trigger_key** | **str** | Trigger key associated with the event. | [optional] 
**results** | **List[object]** | List of results for each item in the bulk report event request. | [optional] 
**bulk_action_metadata** | **object** | Metadata for the overall bulk action, including success and failure counts. | [optional] 

## Example

```python
from openapi_client.models.bulk_report_event_response import BulkReportEventResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkReportEventResponse from a JSON string
bulk_report_event_response_instance = BulkReportEventResponse.from_json(json)
# print the JSON string representation of the object
print(BulkReportEventResponse.to_json())

# convert the object into a dict
bulk_report_event_response_dict = bulk_report_event_response_instance.to_dict()
# create an instance of BulkReportEventResponse from a dict
bulk_report_event_response_from_dict = BulkReportEventResponse.from_dict(bulk_report_event_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


