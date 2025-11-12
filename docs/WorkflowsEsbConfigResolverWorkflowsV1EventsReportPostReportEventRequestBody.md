# WorkflowsEsbConfigResolverWorkflowsV1EventsReportPostReportEventRequestBody



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trigger_key** | **str** | Trigger key as defined in your app&#39;s trigger configuration. For example, &#x60;order_returned&#x60; or &#x60;order_paid&#x60;. | 
**payload** | **object** | Event payload, formatted as key:value pairs. Must comply with the payload schema if you provided one when configuring your trigger.  Key names can include only alphanumeric characters or underscores (&#x60;A-Z&#x60;, &#x60;a-z&#x60;, &#x60;0-9&#x60;, &#x60;_&#x60;). They cannot start with an underscore.  Values can be strings, numbers, integers, booleans, or arrays. If a value is an array, the array items must be objects, and nested object properties must be strings, numbers, integers, or booleans only. | [optional] 
**external_entity_id** | **str** | ID of the related resource in GUID format | [optional] 
**idempotency** | [**Idempotency1**](Idempotency1.md) |  | [optional] 

## Example

```python
from openapi_client.models.workflows_esb_config_resolver_workflows_v1_events_report_post_report_event_request_body import WorkflowsEsbConfigResolverWorkflowsV1EventsReportPostReportEventRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowsEsbConfigResolverWorkflowsV1EventsReportPostReportEventRequestBody from a JSON string
workflows_esb_config_resolver_workflows_v1_events_report_post_report_event_request_body_instance = WorkflowsEsbConfigResolverWorkflowsV1EventsReportPostReportEventRequestBody.from_json(json)
# print the JSON string representation of the object
print(WorkflowsEsbConfigResolverWorkflowsV1EventsReportPostReportEventRequestBody.to_json())

# convert the object into a dict
workflows_esb_config_resolver_workflows_v1_events_report_post_report_event_request_body_dict = workflows_esb_config_resolver_workflows_v1_events_report_post_report_event_request_body_instance.to_dict()
# create an instance of WorkflowsEsbConfigResolverWorkflowsV1EventsReportPostReportEventRequestBody from a dict
workflows_esb_config_resolver_workflows_v1_events_report_post_report_event_request_body_from_dict = WorkflowsEsbConfigResolverWorkflowsV1EventsReportPostReportEventRequestBody.from_dict(workflows_esb_config_resolver_workflows_v1_events_report_post_report_event_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


