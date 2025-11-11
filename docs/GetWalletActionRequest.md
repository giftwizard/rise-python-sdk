# GetWalletActionRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_action_id** | **str** | ID of the WalletAction to retrieve. | [optional] 

## Example

```python
from openapi_client.models.get_wallet_action_request import GetWalletActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetWalletActionRequest from a JSON string
get_wallet_action_request_instance = GetWalletActionRequest.from_json(json)
# print the JSON string representation of the object
print(GetWalletActionRequest.to_json())

# convert the object into a dict
get_wallet_action_request_dict = get_wallet_action_request_instance.to_dict()
# create an instance of GetWalletActionRequest from a dict
get_wallet_action_request_from_dict = GetWalletActionRequest.from_dict(get_wallet_action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


