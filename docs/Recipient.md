# Recipient

The Recipient entity contains the information about the recipient of a gift card, such as name, email, gifting details, and the created gift card.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Recipient ID. | [optional] [readonly] 
**revision** | **str** | Revision number, which increments by 1 each time the Recipient is updated. To prevent conflicting changes, the current revision must be passed when updating the Recipient.  Ignored when creating a Recipient. | [optional] [readonly] 
**created_date** | **datetime** | Date and time the Recipient was created. | [optional] [readonly] 
**updated_date** | **datetime** | Date and time the Recipient was last updated. | [optional] [readonly] 
**name** | **str** | The name of the recipient. | [optional] 
**email** | **str** | The email of the recipient. | [optional] 
**gift_card_id** | **str** | The ID of the gift card that was sent to the recipient. | [optional] 
**gifting_details** | **object** | Optional gifting details to add to the email. | [optional] 

## Example

```python
from openapi_client.models.recipient import Recipient

# TODO update the JSON string below
json = "{}"
# create an instance of Recipient from a JSON string
recipient_instance = Recipient.from_json(json)
# print the JSON string representation of the object
print(Recipient.to_json())

# convert the object into a dict
recipient_dict = recipient_instance.to_dict()
# create an instance of Recipient from a dict
recipient_from_dict = Recipient.from_dict(recipient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


