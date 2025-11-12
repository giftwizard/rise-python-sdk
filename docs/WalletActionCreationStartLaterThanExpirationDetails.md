# WalletActionCreationStartLaterThanExpirationDetails



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The date on which the walletAction was requested to become active, which is after the expiration date. | [optional] 
**expiration_date** | **datetime** | The date when the walletAction was requested to expire, which is before the requested start date. | [optional] 

## Example

```python
from openapi_client.models.wallet_action_creation_start_later_than_expiration_details import WalletActionCreationStartLaterThanExpirationDetails

# TODO update the JSON string below
json = "{}"
# create an instance of WalletActionCreationStartLaterThanExpirationDetails from a JSON string
wallet_action_creation_start_later_than_expiration_details_instance = WalletActionCreationStartLaterThanExpirationDetails.from_json(json)
# print the JSON string representation of the object
print(WalletActionCreationStartLaterThanExpirationDetails.to_json())

# convert the object into a dict
wallet_action_creation_start_later_than_expiration_details_dict = wallet_action_creation_start_later_than_expiration_details_instance.to_dict()
# create an instance of WalletActionCreationStartLaterThanExpirationDetails from a dict
wallet_action_creation_start_later_than_expiration_details_from_dict = WalletActionCreationStartLaterThanExpirationDetails.from_dict(wallet_action_creation_start_later_than_expiration_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


