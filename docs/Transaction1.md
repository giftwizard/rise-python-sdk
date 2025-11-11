# Transaction1

Transaction is the secondary entity of GiftCardService that indicate an action that modifies the balance of a gift card.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Transaction unique id. | [optional] [readonly] 
**created_date** | **datetime** | Transaction creation date. | [optional] [readonly] 
**type** | **str** | Type of transaction. | [optional] 
**gift_card_id** | **str** | Unique ID of the gift card associated with this transaction. | [optional] 
**amount** | **str** | Transaction amount. | [optional] 
**operation_type** | **str** | Indicates whether the transaction adds or subtracts from the GiftCard balance. | [optional] [readonly] 
**idempotency_key** | **str** | Idempotency key, to prevent duplicate creation. | [optional] 
**updated_balance** | **str** | Gift card Balance after this transaction operation. | [optional] [readonly] 
**source_info** | [**TransactionSourceInfo1**](TransactionSourceInfo1.md) |  | [optional] 
**external_event** | [**ExternalEvent1**](ExternalEvent1.md) |  | [optional] 
**external_id** | **str** | ID of the transaction in a 3rd party system if created there. | [optional] 
**redeem_options** | [**RedeemOptions1**](RedeemOptions1.md) |  | [optional] 
**void_options** | [**VoidOptions1**](VoidOptions1.md) |  | [optional] 
**reward_options** | [**RewardOptions1**](RewardOptions1.md) |  | [optional] 
**wallet_action_end_options** | [**WalletActionEndOptions1**](WalletActionEndOptions1.md) |  | [optional] 
**campaign_options** | [**CampaignOptions1**](CampaignOptions1.md) |  | [optional] 
**store_credit_refund_options** | [**StoreCreditRefundOptions1**](StoreCreditRefundOptions1.md) |  | [optional] 
**migration_options** | [**MigrationOptions1**](MigrationOptions1.md) |  | [optional] 
**payment_method_refund_options** | [**PaymentMethodRefundOptions1**](PaymentMethodRefundOptions1.md) |  | [optional] 
**initial_options** | [**InitialOptions1**](InitialOptions1.md) |  | [optional] 
**wallet_action_start_options** | [**WalletActionStartOptions1**](WalletActionStartOptions1.md) |  | [optional] 
**bulk_options** | [**BulkOptions1**](BulkOptions1.md) |  | [optional] 
**manual_options** | [**ManualOptions1**](ManualOptions1.md) |  | [optional] 

## Example

```python
from openapi_client.models.transaction1 import Transaction1

# TODO update the JSON string below
json = "{}"
# create an instance of Transaction1 from a JSON string
transaction1_instance = Transaction1.from_json(json)
# print the JSON string representation of the object
print(Transaction1.to_json())

# convert the object into a dict
transaction1_dict = transaction1_instance.to_dict()
# create an instance of Transaction1 from a dict
transaction1_from_dict = Transaction1.from_dict(transaction1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


