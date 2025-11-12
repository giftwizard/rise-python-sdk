# WalletAction

WalletAction is the main entity of WalletActionService. It represents a Store Credit that adds to the balance of a customer's wallet. It contains information about the amount and expiration date (if applicable) of the Store Credit, the context of its source (e.g. refund, workflow, etc.), and its status.

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
**amount** | **str** | The amount to be added to the Wallet. | [optional] 
**note** | **str** | Free text comment regarding the WalletAction context | [optional] 
**type** | **str** | Indicates the kind of the specific WalletAction | [optional] 
**wallet_action_started** | **object** | Details about the WalletAction&#39;s execution, such as transaction ID and execution date. Set when the WalletAction is executed (e.g., when the amount is added to the account). | [optional] [readonly] 
**wallet_action_ended** | **object** | Details about the execution of the ending of the wallet action (due to expiration, disabling, etc), such as transaction ID and execution date. Set when the WalletAction is ended (i.e. when the amount is deducted from the account). | [optional] [readonly] 
**status** | **str** | The current status of the WalletAction. Set to PENDING when the WalletAction is created and updated to ACTIVE when the amount is added to the wallet. | [optional] [readonly] 
**source** | **object** | Information about the initiator of the WalletAction, such as the app or user that initiated the action. Set when the WalletAction is created. | [optional] [readonly] 
**notifications** | **object** | Settings of the notifications related to the WalletAction. This field is used to specify whether to skip email dispatch or override the template ID for email notifications. | [optional] 
**liability** | **bool** | Indicates whether the WalletAction is a liability. The default is false. | [optional] 
**store_credit_context** | **object** | Detailed information about the context of a store credit, such as the issuer type and sales channel. | [optional] [readonly] 
**external_event** | **object** | Information about the external event that triggered the WalletAction, such as type of event and a short description or identifier of the event. | [optional] 
**wallet_id** | **str** | ID of the wallet to which the WalletAction belongs. | [optional] 
**idempotency_key** | **str** | Unique key to identify the WalletAction, used to prevent duplicate WalletActions from being created in case of retries or network issues. The key should be unique for each WalletAction and should not be reused. | [optional] 

## Example

```python
from openapi_client.models.wallet_action import WalletAction

# TODO update the JSON string below
json = "{}"
# create an instance of WalletAction from a JSON string
wallet_action_instance = WalletAction.from_json(json)
# print the JSON string representation of the object
print(WalletAction.to_json())

# convert the object into a dict
wallet_action_dict = wallet_action_instance.to_dict()
# create an instance of WalletAction from a dict
wallet_action_from_dict = WalletAction.from_dict(wallet_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


