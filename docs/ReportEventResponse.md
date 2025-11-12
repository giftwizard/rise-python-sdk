# ReportEventResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activation_ids** | **List[str]** | The activation IDs of triggered ReportEvents. | [optional] 

## Example

```python
from openapi_client.models.report_event_response import ReportEventResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReportEventResponse from a JSON string
report_event_response_instance = ReportEventResponse.from_json(json)
# print the JSON string representation of the object
print(ReportEventResponse.to_json())

# convert the object into a dict
report_event_response_dict = report_event_response_instance.to_dict()
# create an instance of ReportEventResponse from a dict
report_event_response_from_dict = ReportEventResponse.from_dict(report_event_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


