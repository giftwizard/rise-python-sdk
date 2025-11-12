# CreateRecipientResponse1



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipient** | [**Recipient1**](Recipient1.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_recipient_response1 import CreateRecipientResponse1

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRecipientResponse1 from a JSON string
create_recipient_response1_instance = CreateRecipientResponse1.from_json(json)
# print the JSON string representation of the object
print(CreateRecipientResponse1.to_json())

# convert the object into a dict
create_recipient_response1_dict = create_recipient_response1_instance.to_dict()
# create an instance of CreateRecipientResponse1 from a dict
create_recipient_response1_from_dict = CreateRecipientResponse1.from_dict(create_recipient_response1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


