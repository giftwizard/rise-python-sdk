# UpdateWalletActionRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_action** | **object** | WalletAction to be updated, may be partial. | [optional] 

## Example

```python
from openapi_client.models.update_wallet_action_request import UpdateWalletActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWalletActionRequest from a JSON string
update_wallet_action_request_instance = UpdateWalletActionRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateWalletActionRequest.to_json())

# convert the object into a dict
update_wallet_action_request_dict = update_wallet_action_request_instance.to_dict()
# create an instance of UpdateWalletActionRequest from a dict
update_wallet_action_request_from_dict = UpdateWalletActionRequest.from_dict(update_wallet_action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


