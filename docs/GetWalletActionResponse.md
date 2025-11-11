# GetWalletActionResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_action** | **object** | The retrieved WalletAction. | [optional] 

## Example

```python
from openapi_client.models.get_wallet_action_response import GetWalletActionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetWalletActionResponse from a JSON string
get_wallet_action_response_instance = GetWalletActionResponse.from_json(json)
# print the JSON string representation of the object
print(GetWalletActionResponse.to_json())

# convert the object into a dict
get_wallet_action_response_dict = get_wallet_action_response_instance.to_dict()
# create an instance of GetWalletActionResponse from a dict
get_wallet_action_response_from_dict = GetWalletActionResponse.from_dict(get_wallet_action_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


