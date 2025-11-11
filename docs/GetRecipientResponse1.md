# GetRecipientResponse1



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipient** | [**Recipient2**](Recipient2.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_recipient_response1 import GetRecipientResponse1

# TODO update the JSON string below
json = "{}"
# create an instance of GetRecipientResponse1 from a JSON string
get_recipient_response1_instance = GetRecipientResponse1.from_json(json)
# print the JSON string representation of the object
print(GetRecipientResponse1.to_json())

# convert the object into a dict
get_recipient_response1_dict = get_recipient_response1_instance.to_dict()
# create an instance of GetRecipientResponse1 from a dict
get_recipient_response1_from_dict = GetRecipientResponse1.from_dict(get_recipient_response1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


