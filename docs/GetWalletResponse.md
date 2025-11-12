# GetWalletResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet** | [**Wallet2**](Wallet2.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_wallet_response import GetWalletResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetWalletResponse from a JSON string
get_wallet_response_instance = GetWalletResponse.from_json(json)
# print the JSON string representation of the object
print(GetWalletResponse.to_json())

# convert the object into a dict
get_wallet_response_dict = get_wallet_response_instance.to_dict()
# create an instance of GetWalletResponse from a dict
get_wallet_response_from_dict = GetWalletResponse.from_dict(get_wallet_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


