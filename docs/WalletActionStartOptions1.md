# WalletActionStartOptions1

Information about a transaction whose source is a wallet action (store credit) to a customer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_action_start_options** | [**WalletActionStartOptions1**](WalletActionStartOptions1.md) |  | [optional] 

## Example

```python
from openapi_client.models.wallet_action_start_options1 import WalletActionStartOptions1

# TODO update the JSON string below
json = "{}"
# create an instance of WalletActionStartOptions1 from a JSON string
wallet_action_start_options1_instance = WalletActionStartOptions1.from_json(json)
# print the JSON string representation of the object
print(WalletActionStartOptions1.to_json())

# convert the object into a dict
wallet_action_start_options1_dict = wallet_action_start_options1_instance.to_dict()
# create an instance of WalletActionStartOptions1 from a dict
wallet_action_start_options1_from_dict = WalletActionStartOptions1.from_dict(wallet_action_start_options1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


