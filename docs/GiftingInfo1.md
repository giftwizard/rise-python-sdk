# GiftingInfo1

The line Item's Gifting Information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipient_first_name** | **str** | First Name of the recipient. | [optional] 
**recipient_last_name** | **str** | Last Name of the recipient. | [optional] 
**recipient_email** | **str** | Email address of the recipient. | [optional] 
**send_at** | **datetime** | Date and time the Gift Card is scheduled to be sent. Default is now. | [optional] 
**message** | **str** | Message to be added to the gift card email. | [optional] 
**media_url** | **str** | Media to be added to the gift card email. | [optional] 

## Example

```python
from openapi_client.models.gifting_info1 import GiftingInfo1

# TODO update the JSON string below
json = "{}"
# create an instance of GiftingInfo1 from a JSON string
gifting_info1_instance = GiftingInfo1.from_json(json)
# print the JSON string representation of the object
print(GiftingInfo1.to_json())

# convert the object into a dict
gifting_info1_dict = gifting_info1_instance.to_dict()
# create an instance of GiftingInfo1 from a dict
gifting_info1_from_dict = GiftingInfo1.from_dict(gifting_info1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


