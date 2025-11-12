# WalletActionStartOptionsWalletActionStartOptions

Information about a transaction whose source is a wallet action (store credit) to a customer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_action_id** | **str** | ID of the wallet action. | [optional] 
**liability** | **bool** | Indicates whether the wallet action is a liability. | [optional] 
**context** | [**StoreCreditContext2**](StoreCreditContext2.md) |  | [optional] 

## Example

```python
from openapi_client.models.wallet_action_start_options_wallet_action_start_options import WalletActionStartOptionsWalletActionStartOptions

# TODO update the JSON string below
json = "{}"
# create an instance of WalletActionStartOptionsWalletActionStartOptions from a JSON string
wallet_action_start_options_wallet_action_start_options_instance = WalletActionStartOptionsWalletActionStartOptions.from_json(json)
# print the JSON string representation of the object
print(WalletActionStartOptionsWalletActionStartOptions.to_json())

# convert the object into a dict
wallet_action_start_options_wallet_action_start_options_dict = wallet_action_start_options_wallet_action_start_options_instance.to_dict()
# create an instance of WalletActionStartOptionsWalletActionStartOptions from a dict
wallet_action_start_options_wallet_action_start_options_from_dict = WalletActionStartOptionsWalletActionStartOptions.from_dict(wallet_action_start_options_wallet_action_start_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


