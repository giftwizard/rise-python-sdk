# WalletActionExecutionDetails2

Details about the execution of the ending of the wallet action (due to expiration, disabling, etc), such as transaction ID and execution date. Set when the WalletAction is ended (i.e. when the amount is deducted from the account).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | ID of the Gift Card Transaction created by the WalletAction. | [optional] [readonly] 
**execution_date** | **datetime** | Represents the time at which the WalletAction was executed. | [optional] [readonly] 

## Example

```python
from openapi_client.models.wallet_action_execution_details2 import WalletActionExecutionDetails2

# TODO update the JSON string below
json = "{}"
# create an instance of WalletActionExecutionDetails2 from a JSON string
wallet_action_execution_details2_instance = WalletActionExecutionDetails2.from_json(json)
# print the JSON string representation of the object
print(WalletActionExecutionDetails2.to_json())

# convert the object into a dict
wallet_action_execution_details2_dict = wallet_action_execution_details2_instance.to_dict()
# create an instance of WalletActionExecutionDetails2 from a dict
wallet_action_execution_details2_from_dict = WalletActionExecutionDetails2.from_dict(wallet_action_execution_details2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


