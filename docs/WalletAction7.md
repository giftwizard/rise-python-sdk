# WalletAction7

WalletAction to be created.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | WalletAction ID. | [optional] [readonly] 
**revision** | **str** | Represents the current state of an item. Each time the item is modified, its &#x60;revision&#x60; changes. For an update operation to succeed, you MUST pass the latest revision. | [optional] [readonly] 
**created_date** | **datetime** | Represents the time this WalletAction was created. | [optional] [readonly] 
**updated_date** | **datetime** | Represents the time this WalletAction was last updated. | [optional] [readonly] 
**start_date** | **datetime** | Represents the time at which the WalletAction&#39;s amount will be added to the account. Defaults to immediately. | [optional] 
**expiration_date** | **datetime** | Represents the time at which the unused balance of the WalletAction will be deducted from the account. Defaults to never. | [optional] 
**disable_date** | **datetime** | Represents the time at which the WalletAction was manually disabled, if applicable. | [optional] [readonly] 
**amount** | **str** | The amount to be added to the Wallet. | 
**note** | **str** | Free text comment regarding the WalletAction context (**Deprecated**: Use &#x60;note&#x60; instead.) | [optional] 
**type** | **str** | Indicates the kind of the specific WalletAction (**Deprecated**) | [optional] 
**wallet_action_started** | [**WalletActionExecutionDetails1**](WalletActionExecutionDetails1.md) |  | [optional] 
**wallet_action_ended** | [**WalletActionExecutionDetails2**](WalletActionExecutionDetails2.md) |  | [optional] 
**status** | **str** | The current status of the WalletAction. Set to PENDING when the WalletAction is created and updated to ACTIVE when the amount is added to the wallet. | [optional] [readonly] 
**source** | [**ActionInitiator2**](ActionInitiator2.md) |  | [optional] 
**notifications** | [**Notifications1**](Notifications1.md) |  | [optional] 
**liability** | **bool** | Indicates whether the WalletAction is a liability. The default is false. | [optional] 
**store_credit_context** | [**StoreCreditContext1**](StoreCreditContext1.md) |  | 
**external_event** | [**ExternalEvent2**](ExternalEvent2.md) |  | [optional] 
**wallet_id** | **str** | ID of the wallet to which the WalletAction belongs. | [optional] 
**idempotency_key** | **str** | Unique key to identify the WalletAction, used to prevent duplicate WalletActions from being created in case of retries or network issues. The key should be unique for each WalletAction and should not be reused. | [optional] 

## Example

```python
from openapi_client.models.wallet_action7 import WalletAction7

# TODO update the JSON string below
json = "{}"
# create an instance of WalletAction7 from a JSON string
wallet_action7_instance = WalletAction7.from_json(json)
# print the JSON string representation of the object
print(WalletAction7.to_json())

# convert the object into a dict
wallet_action7_dict = wallet_action7_instance.to_dict()
# create an instance of WalletAction7 from a dict
wallet_action7_from_dict = WalletAction7.from_dict(wallet_action7_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


