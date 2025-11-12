# ReportEventRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trigger_key** | **str** | Trigger key as defined in your app&#39;s trigger configuration. For example, &#x60;order_returned&#x60; or &#x60;order_paid&#x60;.. | [optional] 
**payload** | **object** | Event payload, formatted as key:value pairs. Must comply with the payload schema if you provided one when configuring your trigger.  Key names can include only alphanumeric characters or underscores (&#x60;A-Z&#x60;, &#x60;a-z&#x60;, &#x60;0-9&#x60;, &#x60;_&#x60;). They cannot start with an underscore.  Values can be strings, numbers, integers, booleans, or arrays. If a value is an array, the array items must be objects, and nested object properties must be strings, numbers, integers, or booleans only. | [optional] 
**external_entity_id** | **str** | ID of the related resource in GUID format. For example, &#x60;fc81a355-3429-50fc-a4c7-def486e828f3&#x60;.  Required if your app needs to [cancel the event](https://dev.wix.com/docs/rest/business-management/automations/triggered-events/cancel-event) if the automation becomes no longer relevant.  Typically, this ID is defined in your system, but you can also use any resource GUID, such as contact ID, member ID, or invoice ID. See [Choose the right &#x60;externalEntityId&#x60;](https://dev.wix.com/docs/rest/business-management/automations/triggered-events/reporting-and-canceling-events#about-canceling-events) for more information. | [optional] 
**idempotency** | **object** | Idempotency information for the event. | [optional] 

## Example

```python
from openapi_client.models.report_event_request import ReportEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReportEventRequest from a JSON string
report_event_request_instance = ReportEventRequest.from_json(json)
# print the JSON string representation of the object
print(ReportEventRequest.to_json())

# convert the object into a dict
report_event_request_dict = report_event_request_instance.to_dict()
# create an instance of ReportEventRequest from a dict
report_event_request_from_dict = ReportEventRequest.from_dict(report_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


