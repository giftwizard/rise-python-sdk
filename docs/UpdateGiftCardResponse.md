# UpdateGiftCardResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gift_card** | [**GiftCard3**](GiftCard3.md) |  | [optional] 

## Example

```python
from openapi_client.models.update_gift_card_response import UpdateGiftCardResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGiftCardResponse from a JSON string
update_gift_card_response_instance = UpdateGiftCardResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateGiftCardResponse.to_json())

# convert the object into a dict
update_gift_card_response_dict = update_gift_card_response_instance.to_dict()
# create an instance of UpdateGiftCardResponse from a dict
update_gift_card_response_from_dict = UpdateGiftCardResponse.from_dict(update_gift_card_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


