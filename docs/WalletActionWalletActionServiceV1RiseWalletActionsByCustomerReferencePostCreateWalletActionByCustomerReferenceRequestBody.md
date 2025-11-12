# WalletActionWalletActionServiceV1RiseWalletActionsByCustomerReferencePostCreateWalletActionByCustomerReferenceRequestBody



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_reference** | [**CustomerReference3**](CustomerReference3.md) |  | 
**wallet_action** | [**WalletAction7**](WalletAction7.md) |  | 
**new_wallet_currency** | **str** | The currency for the new wallet, if no wallet already exists. | [optional] 

## Example

```python
from openapi_client.models.wallet_action_wallet_action_service_v1_rise_wallet_actions_by_customer_reference_post_create_wallet_action_by_customer_reference_request_body import WalletActionWalletActionServiceV1RiseWalletActionsByCustomerReferencePostCreateWalletActionByCustomerReferenceRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of WalletActionWalletActionServiceV1RiseWalletActionsByCustomerReferencePostCreateWalletActionByCustomerReferenceRequestBody from a JSON string
wallet_action_wallet_action_service_v1_rise_wallet_actions_by_customer_reference_post_create_wallet_action_by_customer_reference_request_body_instance = WalletActionWalletActionServiceV1RiseWalletActionsByCustomerReferencePostCreateWalletActionByCustomerReferenceRequestBody.from_json(json)
# print the JSON string representation of the object
print(WalletActionWalletActionServiceV1RiseWalletActionsByCustomerReferencePostCreateWalletActionByCustomerReferenceRequestBody.to_json())

# convert the object into a dict
wallet_action_wallet_action_service_v1_rise_wallet_actions_by_customer_reference_post_create_wallet_action_by_customer_reference_request_body_dict = wallet_action_wallet_action_service_v1_rise_wallet_actions_by_customer_reference_post_create_wallet_action_by_customer_reference_request_body_instance.to_dict()
# create an instance of WalletActionWalletActionServiceV1RiseWalletActionsByCustomerReferencePostCreateWalletActionByCustomerReferenceRequestBody from a dict
wallet_action_wallet_action_service_v1_rise_wallet_actions_by_customer_reference_post_create_wallet_action_by_customer_reference_request_body_from_dict = WalletActionWalletActionServiceV1RiseWalletActionsByCustomerReferencePostCreateWalletActionByCustomerReferenceRequestBody.from_dict(wallet_action_wallet_action_service_v1_rise_wallet_actions_by_customer_reference_post_create_wallet_action_by_customer_reference_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


