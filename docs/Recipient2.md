# Recipient2

The requested Recipient.

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
from openapi_client.models.recipient2 import Recipient2

# TODO update the JSON string below
json = "{}"
# create an instance of Recipient2 from a JSON string
recipient2_instance = Recipient2.from_json(json)
# print the JSON string representation of the object
print(Recipient2.to_json())

# convert the object into a dict
recipient2_dict = recipient2_instance.to_dict()
# create an instance of Recipient2 from a dict
recipient2_from_dict = Recipient2.from_dict(recipient2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


