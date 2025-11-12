# WalletActionExecutionDetails1

Details about the WalletAction's execution, such as transaction ID and execution date. Set when the WalletAction is executed (e.g., when the amount is added to the account).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | ID of the Gift Card Transaction created by the WalletAction. | [optional] [readonly] 
**execution_date** | **datetime** | Represents the time at which the WalletAction was executed. | [optional] [readonly] 

## Example

```python
from openapi_client.models.wallet_action_execution_details1 import WalletActionExecutionDetails1

# TODO update the JSON string below
json = "{}"
# create an instance of WalletActionExecutionDetails1 from a JSON string
wallet_action_execution_details1_instance = WalletActionExecutionDetails1.from_json(json)
# print the JSON string representation of the object
print(WalletActionExecutionDetails1.to_json())

# convert the object into a dict
wallet_action_execution_details1_dict = wallet_action_execution_details1_instance.to_dict()
# create an instance of WalletActionExecutionDetails1 from a dict
wallet_action_execution_details1_from_dict = WalletActionExecutionDetails1.from_dict(wallet_action_execution_details1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


