# CreateWalletActionRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_action** | **object** | WalletAction to be created. | [optional] 

## Example

```python
from openapi_client.models.create_wallet_action_request import CreateWalletActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWalletActionRequest from a JSON string
create_wallet_action_request_instance = CreateWalletActionRequest.from_json(json)
# print the JSON string representation of the object
print(CreateWalletActionRequest.to_json())

# convert the object into a dict
create_wallet_action_request_dict = create_wallet_action_request_instance.to_dict()
# create an instance of CreateWalletActionRequest from a dict
create_wallet_action_request_from_dict = CreateWalletActionRequest.from_dict(create_wallet_action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


