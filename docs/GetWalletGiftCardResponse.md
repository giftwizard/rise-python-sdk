# GetWalletGiftCardResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gift_card** | **object** | The retrieved Gift Card. | [optional] 

## Example

```python
from openapi_client.models.get_wallet_gift_card_response import GetWalletGiftCardResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetWalletGiftCardResponse from a JSON string
get_wallet_gift_card_response_instance = GetWalletGiftCardResponse.from_json(json)
# print the JSON string representation of the object
print(GetWalletGiftCardResponse.to_json())

# convert the object into a dict
get_wallet_gift_card_response_dict = get_wallet_gift_card_response_instance.to_dict()
# create an instance of GetWalletGiftCardResponse from a dict
get_wallet_gift_card_response_from_dict = GetWalletGiftCardResponse.from_dict(get_wallet_gift_card_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


