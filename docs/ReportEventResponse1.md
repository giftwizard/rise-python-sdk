# ReportEventResponse1



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activation_ids** | **List[str]** | The activation IDs of triggered ReportEvents. | [optional] 

## Example

```python
from openapi_client.models.report_event_response1 import ReportEventResponse1

# TODO update the JSON string below
json = "{}"
# create an instance of ReportEventResponse1 from a JSON string
report_event_response1_instance = ReportEventResponse1.from_json(json)
# print the JSON string representation of the object
print(ReportEventResponse1.to_json())

# convert the object into a dict
report_event_response1_dict = report_event_response1_instance.to_dict()
# create an instance of ReportEventResponse1 from a dict
report_event_response1_from_dict = ReportEventResponse1.from_dict(report_event_response1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


