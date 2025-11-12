# WalletWalletServiceV1RiseWalletsPostCreateWalletRequestBody



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_reference** | [**CustomerReference4**](CustomerReference4.md) |  | 
**initial_value** | **str** | Initial amount of store credit. | [optional] 
**currency** | **str** | Currency of the wallet. | [optional] 

## Example

```python
from openapi_client.models.wallet_wallet_service_v1_rise_wallets_post_create_wallet_request_body import WalletWalletServiceV1RiseWalletsPostCreateWalletRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of WalletWalletServiceV1RiseWalletsPostCreateWalletRequestBody from a JSON string
wallet_wallet_service_v1_rise_wallets_post_create_wallet_request_body_instance = WalletWalletServiceV1RiseWalletsPostCreateWalletRequestBody.from_json(json)
# print the JSON string representation of the object
print(WalletWalletServiceV1RiseWalletsPostCreateWalletRequestBody.to_json())

# convert the object into a dict
wallet_wallet_service_v1_rise_wallets_post_create_wallet_request_body_dict = wallet_wallet_service_v1_rise_wallets_post_create_wallet_request_body_instance.to_dict()
# create an instance of WalletWalletServiceV1RiseWalletsPostCreateWalletRequestBody from a dict
wallet_wallet_service_v1_rise_wallets_post_create_wallet_request_body_from_dict = WalletWalletServiceV1RiseWalletsPostCreateWalletRequestBody.from_dict(wallet_wallet_service_v1_rise_wallets_post_create_wallet_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


