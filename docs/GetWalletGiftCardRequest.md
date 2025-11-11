# GetWalletGiftCardRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **object** | Wallet ID, email, or customer reference source by which to retrieve the gift card. | [optional] 

## Example

```python
from openapi_client.models.get_wallet_gift_card_request import GetWalletGiftCardRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetWalletGiftCardRequest from a JSON string
get_wallet_gift_card_request_instance = GetWalletGiftCardRequest.from_json(json)
# print the JSON string representation of the object
print(GetWalletGiftCardRequest.to_json())

# convert the object into a dict
get_wallet_gift_card_request_dict = get_wallet_gift_card_request_instance.to_dict()
# create an instance of GetWalletGiftCardRequest from a dict
get_wallet_gift_card_request_from_dict = GetWalletGiftCardRequest.from_dict(get_wallet_gift_card_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


