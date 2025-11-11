# WalletActionUpdateExpirationDateInThePastDetails



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_action_id** | **str** | WalletAction ID. | [optional] 
**new_expiration_date** | **datetime** | The requested expiration date of the walletAction, which is in the past. | [optional] 
**current_date** | **datetime** | The current date. | [optional] 

## Example

```python
from openapi_client.models.wallet_action_update_expiration_date_in_the_past_details import WalletActionUpdateExpirationDateInThePastDetails

# TODO update the JSON string below
json = "{}"
# create an instance of WalletActionUpdateExpirationDateInThePastDetails from a JSON string
wallet_action_update_expiration_date_in_the_past_details_instance = WalletActionUpdateExpirationDateInThePastDetails.from_json(json)
# print the JSON string representation of the object
print(WalletActionUpdateExpirationDateInThePastDetails.to_json())

# convert the object into a dict
wallet_action_update_expiration_date_in_the_past_details_dict = wallet_action_update_expiration_date_in_the_past_details_instance.to_dict()
# create an instance of WalletActionUpdateExpirationDateInThePastDetails from a dict
wallet_action_update_expiration_date_in_the_past_details_from_dict = WalletActionUpdateExpirationDateInThePastDetails.from_dict(wallet_action_update_expiration_date_in_the_past_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


