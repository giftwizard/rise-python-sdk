# WalletActionExecutionDetails



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | ID of the Gift Card Transaction created by the WalletAction. | [optional] [readonly] 
**execution_date** | **datetime** | Represents the time at which the WalletAction was executed. | [optional] [readonly] 

## Example

```python
from openapi_client.models.wallet_action_execution_details import WalletActionExecutionDetails

# TODO update the JSON string below
json = "{}"
# create an instance of WalletActionExecutionDetails from a JSON string
wallet_action_execution_details_instance = WalletActionExecutionDetails.from_json(json)
# print the JSON string representation of the object
print(WalletActionExecutionDetails.to_json())

# convert the object into a dict
wallet_action_execution_details_dict = wallet_action_execution_details_instance.to_dict()
# create an instance of WalletActionExecutionDetails from a dict
wallet_action_execution_details_from_dict = WalletActionExecutionDetails.from_dict(wallet_action_execution_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


