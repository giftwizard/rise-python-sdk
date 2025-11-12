# WalletActionUpdateStartDateInThePastDetails



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_action_id** | **str** | WalletAction ID. | [optional] 
**new_start_date** | **datetime** | The requested start date of the walletAction, which is in the past. | [optional] 
**current_date** | **datetime** | The current date. | [optional] 

## Example

```python
from openapi_client.models.wallet_action_update_start_date_in_the_past_details import WalletActionUpdateStartDateInThePastDetails

# TODO update the JSON string below
json = "{}"
# create an instance of WalletActionUpdateStartDateInThePastDetails from a JSON string
wallet_action_update_start_date_in_the_past_details_instance = WalletActionUpdateStartDateInThePastDetails.from_json(json)
# print the JSON string representation of the object
print(WalletActionUpdateStartDateInThePastDetails.to_json())

# convert the object into a dict
wallet_action_update_start_date_in_the_past_details_dict = wallet_action_update_start_date_in_the_past_details_instance.to_dict()
# create an instance of WalletActionUpdateStartDateInThePastDetails from a dict
wallet_action_update_start_date_in_the_past_details_from_dict = WalletActionUpdateStartDateInThePastDetails.from_dict(wallet_action_update_start_date_in_the_past_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


