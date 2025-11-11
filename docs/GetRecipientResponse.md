# GetRecipientResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipient** | **object** | The requested Recipient. | [optional] 

## Example

```python
from openapi_client.models.get_recipient_response import GetRecipientResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetRecipientResponse from a JSON string
get_recipient_response_instance = GetRecipientResponse.from_json(json)
# print the JSON string representation of the object
print(GetRecipientResponse.to_json())

# convert the object into a dict
get_recipient_response_dict = get_recipient_response_instance.to_dict()
# create an instance of GetRecipientResponse from a dict
get_recipient_response_from_dict = GetRecipientResponse.from_dict(get_recipient_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


