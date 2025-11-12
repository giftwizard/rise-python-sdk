# CreateRecipientRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipient** | **object** | Recipient to be created. | [optional] 
**side_effects** | **object** | Optional information about some side effects regarding the creation of the Recipient. | [optional] 

## Example

```python
from openapi_client.models.create_recipient_request import CreateRecipientRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRecipientRequest from a JSON string
create_recipient_request_instance = CreateRecipientRequest.from_json(json)
# print the JSON string representation of the object
print(CreateRecipientRequest.to_json())

# convert the object into a dict
create_recipient_request_dict = create_recipient_request_instance.to_dict()
# create an instance of CreateRecipientRequest from a dict
create_recipient_request_from_dict = CreateRecipientRequest.from_dict(create_recipient_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


