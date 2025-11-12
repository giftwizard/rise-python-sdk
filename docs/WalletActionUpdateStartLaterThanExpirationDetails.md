# WalletActionUpdateStartLaterThanExpirationDetails



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_action_id** | **str** | WalletAction ID. | [optional] 
**start_date** | **datetime** | The requested start date of the walletAction, which is after the expiration date. | [optional] 
**expiration_date** | **datetime** | The date of the requested wallet action expiration, which is before the requested start date. | [optional] 

## Example

```python
from openapi_client.models.wallet_action_update_start_later_than_expiration_details import WalletActionUpdateStartLaterThanExpirationDetails

# TODO update the JSON string below
json = "{}"
# create an instance of WalletActionUpdateStartLaterThanExpirationDetails from a JSON string
wallet_action_update_start_later_than_expiration_details_instance = WalletActionUpdateStartLaterThanExpirationDetails.from_json(json)
# print the JSON string representation of the object
print(WalletActionUpdateStartLaterThanExpirationDetails.to_json())

# convert the object into a dict
wallet_action_update_start_later_than_expiration_details_dict = wallet_action_update_start_later_than_expiration_details_instance.to_dict()
# create an instance of WalletActionUpdateStartLaterThanExpirationDetails from a dict
wallet_action_update_start_later_than_expiration_details_from_dict = WalletActionUpdateStartLaterThanExpirationDetails.from_dict(wallet_action_update_start_later_than_expiration_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


