# WalletActionEndOptions1

Information about a transaction whose source is the end of a wallet action (store credit).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_action_end_options** | [**WalletActionEndOptions1**](WalletActionEndOptions1.md) |  | [optional] 

## Example

```python
from openapi_client.models.wallet_action_end_options1 import WalletActionEndOptions1

# TODO update the JSON string below
json = "{}"
# create an instance of WalletActionEndOptions1 from a JSON string
wallet_action_end_options1_instance = WalletActionEndOptions1.from_json(json)
# print the JSON string representation of the object
print(WalletActionEndOptions1.to_json())

# convert the object into a dict
wallet_action_end_options1_dict = wallet_action_end_options1_instance.to_dict()
# create an instance of WalletActionEndOptions1 from a dict
wallet_action_end_options1_from_dict = WalletActionEndOptions1.from_dict(wallet_action_end_options1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


