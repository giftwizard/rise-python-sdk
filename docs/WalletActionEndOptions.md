# WalletActionEndOptions



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_action_id** | **str** | ID of the wallet action being ended. | [optional] 
**transaction_id** | **str** | ID of the transaction being reversed. | [optional] 
**liability** | **bool** | Indicates whether the wallet action end is a liability. | [optional] 
**reason** | **str** | Reason the wallet action is ending. | [optional] 

## Example

```python
from openapi_client.models.wallet_action_end_options import WalletActionEndOptions

# TODO update the JSON string below
json = "{}"
# create an instance of WalletActionEndOptions from a JSON string
wallet_action_end_options_instance = WalletActionEndOptions.from_json(json)
# print the JSON string representation of the object
print(WalletActionEndOptions.to_json())

# convert the object into a dict
wallet_action_end_options_dict = wallet_action_end_options_instance.to_dict()
# create an instance of WalletActionEndOptions from a dict
wallet_action_end_options_from_dict = WalletActionEndOptions.from_dict(wallet_action_end_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


