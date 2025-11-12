# GiftingDetails



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
from openapi_client.models.gifting_details import GiftingDetails

# TODO update the JSON string below
json = "{}"
# create an instance of GiftingDetails from a JSON string
gifting_details_instance = GiftingDetails.from_json(json)
# print the JSON string representation of the object
print(GiftingDetails.to_json())

# convert the object into a dict
gifting_details_dict = gifting_details_instance.to_dict()
# create an instance of GiftingDetails from a dict
gifting_details_from_dict = GiftingDetails.from_dict(gifting_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


