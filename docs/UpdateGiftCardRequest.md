# UpdateGiftCardRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gift_card_id** | **str** | The ID of the GiftCard to update. | [optional] 
**gift_card** | **object** | The GiftCard to update. | [optional] 

## Example

```python
from openapi_client.models.update_gift_card_request import UpdateGiftCardRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGiftCardRequest from a JSON string
update_gift_card_request_instance = UpdateGiftCardRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateGiftCardRequest.to_json())

# convert the object into a dict
update_gift_card_request_dict = update_gift_card_request_instance.to_dict()
# create an instance of UpdateGiftCardRequest from a dict
update_gift_card_request_from_dict = UpdateGiftCardRequest.from_dict(update_gift_card_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


