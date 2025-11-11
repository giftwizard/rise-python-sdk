# WalletActionStartOptions



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_action_id** | **str** | ID of the wallet action. | [optional] 
**liability** | **bool** | Indicates whether the wallet action is a liability. | [optional] 
**context** | **object** | Detailed information about the context of a store credit, such as the issuer type and sales channel. | [optional] 

## Example

```python
from openapi_client.models.wallet_action_start_options import WalletActionStartOptions

# TODO update the JSON string below
json = "{}"
# create an instance of WalletActionStartOptions from a JSON string
wallet_action_start_options_instance = WalletActionStartOptions.from_json(json)
# print the JSON string representation of the object
print(WalletActionStartOptions.to_json())

# convert the object into a dict
wallet_action_start_options_dict = wallet_action_start_options_instance.to_dict()
# create an instance of WalletActionStartOptions from a dict
wallet_action_start_options_from_dict = WalletActionStartOptions.from_dict(wallet_action_start_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


