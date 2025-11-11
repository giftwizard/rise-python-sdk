# DeleteWalletActionRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_action_id** | **str** | ID of the WalletAction to delete. | [optional] 
**revision** | **str** | The revision of the WalletAction. | [optional] 

## Example

```python
from openapi_client.models.delete_wallet_action_request import DeleteWalletActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteWalletActionRequest from a JSON string
delete_wallet_action_request_instance = DeleteWalletActionRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteWalletActionRequest.to_json())

# convert the object into a dict
delete_wallet_action_request_dict = delete_wallet_action_request_instance.to_dict()
# create an instance of DeleteWalletActionRequest from a dict
delete_wallet_action_request_from_dict = DeleteWalletActionRequest.from_dict(delete_wallet_action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


