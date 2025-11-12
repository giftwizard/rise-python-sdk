# CreateWalletActionResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_action** | [**WalletAction1**](WalletAction1.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_wallet_action_response import CreateWalletActionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWalletActionResponse from a JSON string
create_wallet_action_response_instance = CreateWalletActionResponse.from_json(json)
# print the JSON string representation of the object
print(CreateWalletActionResponse.to_json())

# convert the object into a dict
create_wallet_action_response_dict = create_wallet_action_response_instance.to_dict()
# create an instance of CreateWalletActionResponse from a dict
create_wallet_action_response_from_dict = CreateWalletActionResponse.from_dict(create_wallet_action_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


