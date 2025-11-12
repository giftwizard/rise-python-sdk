# openapi_client.WorkflowsApi

All URIs are relative to *https://platform.rise.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**report_event**](WorkflowsApi.md#report_event) | **POST** /workflows/v1/events/report | 


# **report_event**
> ReportEventResponse1 report_event(workflows_esb_config_resolver_workflows_v1_events_report_post_report_event_request_body)

Reports an event and activates account workflows with the specified trigger key. Only the app that created a trigger can report events for it. This means other apps can't report events for your triggers, and you can't report events for another app's triggers.

### Example


```python
import openapi_client
from openapi_client.models.report_event_response1 import ReportEventResponse1
from openapi_client.models.workflows_esb_config_resolver_workflows_v1_events_report_post_report_event_request_body import WorkflowsEsbConfigResolverWorkflowsV1EventsReportPostReportEventRequestBody
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://platform.rise.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://platform.rise.ai"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WorkflowsApi(api_client)
    workflows_esb_config_resolver_workflows_v1_events_report_post_report_event_request_body = openapi_client.WorkflowsEsbConfigResolverWorkflowsV1EventsReportPostReportEventRequestBody() # WorkflowsEsbConfigResolverWorkflowsV1EventsReportPostReportEventRequestBody | 

    try:
        api_response = api_instance.report_event(workflows_esb_config_resolver_workflows_v1_events_report_post_report_event_request_body)
        print("The response of WorkflowsApi->report_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->report_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflows_esb_config_resolver_workflows_v1_events_report_post_report_event_request_body** | [**WorkflowsEsbConfigResolverWorkflowsV1EventsReportPostReportEventRequestBody**](WorkflowsEsbConfigResolverWorkflowsV1EventsReportPostReportEventRequestBody.md)|  | 

### Return type

[**ReportEventResponse1**](ReportEventResponse1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - The request was successful |  -  |
**400** | Bad Request - Invalid input or parameters  Possible error codes: &#x60;REQUIRED_PROPERTY&#x60; |  -  |
**428** | Precondition Required - Precondition failed  Possible error codes: &#x60;SCHEMA_VALIDATION_FAILED&#x60; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

