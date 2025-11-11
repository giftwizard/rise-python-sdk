# CancelEventRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_entity_id** | **str** | ID of the related resource in GUID format. For example, &#x60;fc81a355-3429-50fc-a4c7-def486e828f3&#x60;.  Typically, this ID is defined in your system, but you can also use any resource GUID, such as contact ID, member ID, or invoice ID. See [Choose the right &#x60;externalEntityId&#x60;](https://dev.wix.com/docs/rest/business-management/automations/triggered-events/reporting-and-canceling-events#choose-the-right-externalentityid) for more information. | [optional] 
**trigger_key** | **str** | er key whose event you want to cancel. For example, &#x60;form_submitted&#x60; or &#x60;invoice_due&#x60;. | [optional] 

## Example

```python
from openapi_client.models.cancel_event_request import CancelEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CancelEventRequest from a JSON string
cancel_event_request_instance = CancelEventRequest.from_json(json)
# print the JSON string representation of the object
print(CancelEventRequest.to_json())

# convert the object into a dict
cancel_event_request_dict = cancel_event_request_instance.to_dict()
# create an instance of CancelEventRequest from a dict
cancel_event_request_from_dict = CancelEventRequest.from_dict(cancel_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


