# DeleteRecipientRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipient_id** | **str** | Id of the Recipient to delete. | [optional] 

## Example

```python
from openapi_client.models.delete_recipient_request import DeleteRecipientRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteRecipientRequest from a JSON string
delete_recipient_request_instance = DeleteRecipientRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteRecipientRequest.to_json())

# convert the object into a dict
delete_recipient_request_dict = delete_recipient_request_instance.to_dict()
# create an instance of DeleteRecipientRequest from a dict
delete_recipient_request_from_dict = DeleteRecipientRequest.from_dict(delete_recipient_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


