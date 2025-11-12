# BulkCancelEventRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trigger_key** | **str** | gger key whose events you want to cancel. For example, &#x60;form_submitted&#x60; or &#x60;invoice_due&#x60;. | [optional] 
**external_entity_ids** | **List[str]** | Repeated list of external_entity_id, representing the related resources&#39; IDs. | [optional] 

## Example

```python
from openapi_client.models.bulk_cancel_event_request import BulkCancelEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkCancelEventRequest from a JSON string
bulk_cancel_event_request_instance = BulkCancelEventRequest.from_json(json)
# print the JSON string representation of the object
print(BulkCancelEventRequest.to_json())

# convert the object into a dict
bulk_cancel_event_request_dict = bulk_cancel_event_request_instance.to_dict()
# create an instance of BulkCancelEventRequest from a dict
bulk_cancel_event_request_from_dict = BulkCancelEventRequest.from_dict(bulk_cancel_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


