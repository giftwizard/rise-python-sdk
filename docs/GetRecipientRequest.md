# GetRecipientRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipient_id** | **str** | ID of the Recipient to retrieve. | [optional] 

## Example

```python
from openapi_client.models.get_recipient_request import GetRecipientRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetRecipientRequest from a JSON string
get_recipient_request_instance = GetRecipientRequest.from_json(json)
# print the JSON string representation of the object
print(GetRecipientRequest.to_json())

# convert the object into a dict
get_recipient_request_dict = get_recipient_request_instance.to_dict()
# create an instance of GetRecipientRequest from a dict
get_recipient_request_from_dict = GetRecipientRequest.from_dict(get_recipient_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


