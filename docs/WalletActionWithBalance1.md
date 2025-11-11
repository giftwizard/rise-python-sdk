# WalletActionWithBalance1

WalletActionWithBalance an entity of WalletActionService that align a balance with WalletAction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_action** | [**WalletAction5**](WalletAction5.md) |  | [optional] 
**balance** | **str** | Remaining balance of the WalletAction. | [optional] 

## Example

```python
from openapi_client.models.wallet_action_with_balance1 import WalletActionWithBalance1

# TODO update the JSON string below
json = "{}"
# create an instance of WalletActionWithBalance1 from a JSON string
wallet_action_with_balance1_instance = WalletActionWithBalance1.from_json(json)
# print the JSON string representation of the object
print(WalletActionWithBalance1.to_json())

# convert the object into a dict
wallet_action_with_balance1_dict = wallet_action_with_balance1_instance.to_dict()
# create an instance of WalletActionWithBalance1 from a dict
wallet_action_with_balance1_from_dict = WalletActionWithBalance1.from_dict(wallet_action_with_balance1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


