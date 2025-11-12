# GiftingInfo

Optional Gifting Information for the Gift Card.

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
from openapi_client.models.gifting_info import GiftingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GiftingInfo from a JSON string
gifting_info_instance = GiftingInfo.from_json(json)
# print the JSON string representation of the object
print(GiftingInfo.to_json())

# convert the object into a dict
gifting_info_dict = gifting_info_instance.to_dict()
# create an instance of GiftingInfo from a dict
gifting_info_from_dict = GiftingInfo.from_dict(gifting_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


