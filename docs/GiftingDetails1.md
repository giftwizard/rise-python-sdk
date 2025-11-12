# GiftingDetails1

Optional gifting details to add to the email.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**send_date** | **datetime** | Optional date for when to send the email. Leave it empty for immediate dispatch. | [optional] [readonly] 
**greeting** | **str** | Optional custom text to add to the email. | [optional] 
**image_url** | **str** | Optional image to add to the email. | [optional] 
**sender_name** | **str** | The name of the sender. | [optional] 
**sender_email** | **str** | The email of the sender. | [optional] 

## Example

```python
from openapi_client.models.gifting_details1 import GiftingDetails1

# TODO update the JSON string below
json = "{}"
# create an instance of GiftingDetails1 from a JSON string
gifting_details1_instance = GiftingDetails1.from_json(json)
# print the JSON string representation of the object
print(GiftingDetails1.to_json())

# convert the object into a dict
gifting_details1_dict = gifting_details1_instance.to_dict()
# create an instance of GiftingDetails1 from a dict
gifting_details1_from_dict = GiftingDetails1.from_dict(gifting_details1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


