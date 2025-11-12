# WalletActionIdempotencyKeyDetails



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_id** | **str** | Wallet Id | [optional] 
**idempotency_key** | **str** | Idempotency Key | [optional] 

## Example

```python
from openapi_client.models.wallet_action_idempotency_key_details import WalletActionIdempotencyKeyDetails

# TODO update the JSON string below
json = "{}"
# create an instance of WalletActionIdempotencyKeyDetails from a JSON string
wallet_action_idempotency_key_details_instance = WalletActionIdempotencyKeyDetails.from_json(json)
# print the JSON string representation of the object
print(WalletActionIdempotencyKeyDetails.to_json())

# convert the object into a dict
wallet_action_idempotency_key_details_dict = wallet_action_idempotency_key_details_instance.to_dict()
# create an instance of WalletActionIdempotencyKeyDetails from a dict
wallet_action_idempotency_key_details_from_dict = WalletActionIdempotencyKeyDetails.from_dict(wallet_action_idempotency_key_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


