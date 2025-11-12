# WalletActionCreationExpirationDateInThePastDetails



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiration_date** | **datetime** | The date on which the walletAction was requested to expire, which is in the past. | [optional] 
**current_date** | **datetime** | The current date, which is after the requested expiration date. | [optional] 

## Example

```python
from openapi_client.models.wallet_action_creation_expiration_date_in_the_past_details import WalletActionCreationExpirationDateInThePastDetails

# TODO update the JSON string below
json = "{}"
# create an instance of WalletActionCreationExpirationDateInThePastDetails from a JSON string
wallet_action_creation_expiration_date_in_the_past_details_instance = WalletActionCreationExpirationDateInThePastDetails.from_json(json)
# print the JSON string representation of the object
print(WalletActionCreationExpirationDateInThePastDetails.to_json())

# convert the object into a dict
wallet_action_creation_expiration_date_in_the_past_details_dict = wallet_action_creation_expiration_date_in_the_past_details_instance.to_dict()
# create an instance of WalletActionCreationExpirationDateInThePastDetails from a dict
wallet_action_creation_expiration_date_in_the_past_details_from_dict = WalletActionCreationExpirationDateInThePastDetails.from_dict(wallet_action_creation_expiration_date_in_the_past_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


