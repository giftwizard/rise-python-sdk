# BulkCancelEventResult



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_metadata** | **object** | Metadata of the item, including its ID and success or failure status. | [optional] 
**external_entity_id** | **str** | ID of the related resource in GUID format. | [optional] 

## Example

```python
from openapi_client.models.bulk_cancel_event_result import BulkCancelEventResult

# TODO update the JSON string below
json = "{}"
# create an instance of BulkCancelEventResult from a JSON string
bulk_cancel_event_result_instance = BulkCancelEventResult.from_json(json)
# print the JSON string representation of the object
print(BulkCancelEventResult.to_json())

# convert the object into a dict
bulk_cancel_event_result_dict = bulk_cancel_event_result_instance.to_dict()
# create an instance of BulkCancelEventResult from a dict
bulk_cancel_event_result_from_dict = BulkCancelEventResult.from_dict(bulk_cancel_event_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


