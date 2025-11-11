# Recipient1

The created Recipient.

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
**gifting_details** | [**GiftingDetails1**](GiftingDetails1.md) |  | [optional] 

## Example

```python
from openapi_client.models.recipient1 import Recipient1

# TODO update the JSON string below
json = "{}"
# create an instance of Recipient1 from a JSON string
recipient1_instance = Recipient1.from_json(json)
# print the JSON string representation of the object
print(Recipient1.to_json())

# convert the object into a dict
recipient1_dict = recipient1_instance.to_dict()
# create an instance of Recipient1 from a dict
recipient1_from_dict = Recipient1.from_dict(recipient1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


