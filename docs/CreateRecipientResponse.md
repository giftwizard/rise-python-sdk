# CreateRecipientResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipient** | **object** | The created Recipient. | [optional] 

## Example

```python
from openapi_client.models.create_recipient_response import CreateRecipientResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRecipientResponse from a JSON string
create_recipient_response_instance = CreateRecipientResponse.from_json(json)
# print the JSON string representation of the object
print(CreateRecipientResponse.to_json())

# convert the object into a dict
create_recipient_response_dict = create_recipient_response_instance.to_dict()
# create an instance of CreateRecipientResponse from a dict
create_recipient_response_from_dict = CreateRecipientResponse.from_dict(create_recipient_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


