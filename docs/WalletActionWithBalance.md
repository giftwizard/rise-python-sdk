# WalletActionWithBalance

WalletActionWithBalance an entity of WalletActionService that align a balance with WalletAction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_action** | **object** | WalletAction. | [optional] 
**balance** | **str** | Remaining balance of the WalletAction. | [optional] 

## Example

```python
from openapi_client.models.wallet_action_with_balance import WalletActionWithBalance

# TODO update the JSON string below
json = "{}"
# create an instance of WalletActionWithBalance from a JSON string
wallet_action_with_balance_instance = WalletActionWithBalance.from_json(json)
# print the JSON string representation of the object
print(WalletActionWithBalance.to_json())

# convert the object into a dict
wallet_action_with_balance_dict = wallet_action_with_balance_instance.to_dict()
# create an instance of WalletActionWithBalance from a dict
wallet_action_with_balance_from_dict = WalletActionWithBalance.from_dict(wallet_action_with_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


