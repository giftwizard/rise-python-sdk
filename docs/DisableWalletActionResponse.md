# DisableWalletActionResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_action** | [**WalletAction3**](WalletAction3.md) |  | [optional] 

## Example

```python
from openapi_client.models.disable_wallet_action_response import DisableWalletActionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DisableWalletActionResponse from a JSON string
disable_wallet_action_response_instance = DisableWalletActionResponse.from_json(json)
# print the JSON string representation of the object
print(DisableWalletActionResponse.to_json())

# convert the object into a dict
disable_wallet_action_response_dict = disable_wallet_action_response_instance.to_dict()
# create an instance of DisableWalletActionResponse from a dict
disable_wallet_action_response_from_dict = DisableWalletActionResponse.from_dict(disable_wallet_action_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


