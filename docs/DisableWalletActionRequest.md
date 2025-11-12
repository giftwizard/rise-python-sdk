# DisableWalletActionRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_action_id** | **str** | ID of the WalletAction to delete. | [optional] 
**revision** | **str** | The revision of the WalletAction. | [optional] 

## Example

```python
from openapi_client.models.disable_wallet_action_request import DisableWalletActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DisableWalletActionRequest from a JSON string
disable_wallet_action_request_instance = DisableWalletActionRequest.from_json(json)
# print the JSON string representation of the object
print(DisableWalletActionRequest.to_json())

# convert the object into a dict
disable_wallet_action_request_dict = disable_wallet_action_request_instance.to_dict()
# create an instance of DisableWalletActionRequest from a dict
disable_wallet_action_request_from_dict = DisableWalletActionRequest.from_dict(disable_wallet_action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


