# Transaction3

The Transaction to be created.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Transaction unique id. | [optional] [readonly] 
**created_date** | **datetime** | Transaction creation date. | [optional] [readonly] 
**type** | **str** | Type of transaction. | 
**gift_card_id** | **str** | Unique ID of the gift card associated with this transaction. | 
**amount** | **str** | Transaction amount. | 
**operation_type** | **str** | Indicates whether the transaction adds or subtracts from the GiftCard balance. | [optional] [readonly] 
**idempotency_key** | **str** | Idempotency key, to prevent duplicate creation. | [optional] 
**updated_balance** | **str** | Gift card Balance after this transaction operation. | [optional] [readonly] 
**source_info** | [**TransactionSourceInfo1**](TransactionSourceInfo1.md) |  | [optional] 
**external_event** | [**ExternalEvent1**](ExternalEvent1.md) |  | [optional] 
**external_id** | **str** | ID of the transaction in a 3rd party system if created there. | [optional] 
**redeem_options** | [**RedeemOptionsRedeemOptions**](RedeemOptionsRedeemOptions.md) |  | [optional] 
**void_options** | [**VoidOptionsVoidOptions**](VoidOptionsVoidOptions.md) |  | [optional] 
**reward_options** | [**RewardOptionsRewardOptions**](RewardOptionsRewardOptions.md) |  | [optional] 
**wallet_action_end_options** | [**WalletActionEndOptionsWalletActionEndOptions**](WalletActionEndOptionsWalletActionEndOptions.md) |  | [optional] 
**campaign_options** | [**CampaignOptionsCampaignOptions**](CampaignOptionsCampaignOptions.md) |  | [optional] 
**store_credit_refund_options** | [**StoreCreditRefundOptionsStoreCreditRefundOptions**](StoreCreditRefundOptionsStoreCreditRefundOptions.md) |  | [optional] 
**migration_options** | [**MigrationOptionsMigrationOptions**](MigrationOptionsMigrationOptions.md) |  | [optional] 
**payment_method_refund_options** | [**PaymentMethodRefundOptionsPaymentMethodRefundOptions**](PaymentMethodRefundOptionsPaymentMethodRefundOptions.md) |  | [optional] 
**initial_options** | [**InitialOptionsInitialOptions**](InitialOptionsInitialOptions.md) |  | [optional] 
**wallet_action_start_options** | [**WalletActionStartOptionsWalletActionStartOptions**](WalletActionStartOptionsWalletActionStartOptions.md) |  | [optional] 
**bulk_options** | [**BulkOptionsBulkOptions**](BulkOptionsBulkOptions.md) |  | [optional] 
**manual_options** | [**ManualOptionsManualOptions**](ManualOptionsManualOptions.md) |  | [optional] 

## Example

```python
from openapi_client.models.transaction3 import Transaction3

# TODO update the JSON string below
json = "{}"
# create an instance of Transaction3 from a JSON string
transaction3_instance = Transaction3.from_json(json)
# print the JSON string representation of the object
print(Transaction3.to_json())

# convert the object into a dict
transaction3_dict = transaction3_instance.to_dict()
# create an instance of Transaction3 from a dict
transaction3_from_dict = Transaction3.from_dict(transaction3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


