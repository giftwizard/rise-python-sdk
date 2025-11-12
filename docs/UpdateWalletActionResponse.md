# UpdateWalletActionResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_action** | [**WalletAction2**](WalletAction2.md) |  | [optional] 

## Example

```python
from openapi_client.models.update_wallet_action_response import UpdateWalletActionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWalletActionResponse from a JSON string
update_wallet_action_response_instance = UpdateWalletActionResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateWalletActionResponse.to_json())

# convert the object into a dict
update_wallet_action_response_dict = update_wallet_action_response_instance.to_dict()
# create an instance of UpdateWalletActionResponse from a dict
update_wallet_action_response_from_dict = UpdateWalletActionResponse.from_dict(update_wallet_action_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


