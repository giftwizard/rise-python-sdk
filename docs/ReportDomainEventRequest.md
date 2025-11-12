# ReportDomainEventRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trigger_app_id** | **str** | trigger app id | [optional] 
**report_event_request** | **object** | report event request | [optional] 

## Example

```python
from openapi_client.models.report_domain_event_request import ReportDomainEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReportDomainEventRequest from a JSON string
report_domain_event_request_instance = ReportDomainEventRequest.from_json(json)
# print the JSON string representation of the object
print(ReportDomainEventRequest.to_json())

# convert the object into a dict
report_domain_event_request_dict = report_domain_event_request_instance.to_dict()
# create an instance of ReportDomainEventRequest from a dict
report_domain_event_request_from_dict = ReportDomainEventRequest.from_dict(report_domain_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


