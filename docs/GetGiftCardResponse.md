# GetGiftCardResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gift_card** | **object** | The retrieved GiftCard. | [optional] 

## Example

```python
from openapi_client.models.get_gift_card_response import GetGiftCardResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetGiftCardResponse from a JSON string
get_gift_card_response_instance = GetGiftCardResponse.from_json(json)
# print the JSON string representation of the object
print(GetGiftCardResponse.to_json())

# convert the object into a dict
get_gift_card_response_dict = get_gift_card_response_instance.to_dict()
# create an instance of GetGiftCardResponse from a dict
get_gift_card_response_from_dict = GetGiftCardResponse.from_dict(get_gift_card_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


