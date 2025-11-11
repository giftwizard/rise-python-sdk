# Recipient4

Recipient to be created.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Recipient ID. | [optional] [readonly] 
**revision** | **str** | Revision number, which increments by 1 each time the Recipient is updated. To prevent conflicting changes, the current revision must be passed when updating the Recipient.  Ignored when creating a Recipient. | [optional] [readonly] 
**created_date** | **datetime** | Date and time the Recipient was created. | [optional] [readonly] 
**updated_date** | **datetime** | Date and time the Recipient was last updated. | [optional] [readonly] 
**name** | **str** | The name of the recipient. | 
**email** | **str** | The email of the recipient. | 
**gift_card_id** | **str** | The ID of the gift card that was sent to the recipient. | 
**gifting_details** | [**GiftingDetails1**](GiftingDetails1.md) |  | [optional] 

## Example

```python
from openapi_client.models.recipient4 import Recipient4

# TODO update the JSON string below
json = "{}"
# create an instance of Recipient4 from a JSON string
recipient4_instance = Recipient4.from_json(json)
# print the JSON string representation of the object
print(Recipient4.to_json())

# convert the object into a dict
recipient4_dict = recipient4_instance.to_dict()
# create an instance of Recipient4 from a dict
recipient4_from_dict = Recipient4.from_dict(recipient4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


