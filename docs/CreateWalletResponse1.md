# CreateWalletResponse1



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet** | [**Wallet3**](Wallet3.md) |  | [optional] 
**wallet_action_id** | **str** | ID of the walletAction (store credit) created by this request. | [optional] 

## Example

```python
from openapi_client.models.create_wallet_response1 import CreateWalletResponse1

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWalletResponse1 from a JSON string
create_wallet_response1_instance = CreateWalletResponse1.from_json(json)
# print the JSON string representation of the object
print(CreateWalletResponse1.to_json())

# convert the object into a dict
create_wallet_response1_dict = create_wallet_response1_instance.to_dict()
# create an instance of CreateWalletResponse1 from a dict
create_wallet_response1_from_dict = CreateWalletResponse1.from_dict(create_wallet_response1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


