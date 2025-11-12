# TransactionOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redeem_options** | **object** | Information about a transaction whose source is a gift card redemption. | [optional] 
**void_options** | **object** | Information about a transaction that comes to void a previous transaction. | [optional] 
**reward_options** | **object** | Reward Options. | [optional] 
**wallet_action_end_options** | **object** | Information about a transaction whose source is the end of a wallet action (store credit). | [optional] 
**campaign_options** | **object** | Bulk Options. | [optional] 
**store_credit_refund_options** | **object** | Information about a transaction whose source is a store credit refund. | [optional] 
**migration_options** | **object** | Information about a transaction whose source is a migration from Rise V1 or another platform. | [optional] 
**payment_method_refund_options** | **object** | Information about a transaction whose source is a refunding a payment method. | [optional] 
**initial_options** | **object** | Information about the first transaction that initializes a gift card. | [optional] 
**wallet_action_start_options** | **object** | Information about a transaction whose source is a wallet action (store credit) to a customer. | [optional] 
**bulk_options** | **object** | Bulk Options. | [optional] 
**manual_options** | **object** | Information about a transaction issued manually from the Rise dashboard. | [optional] 

## Example

```python
from openapi_client.models.transaction_options import TransactionOptions

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionOptions from a JSON string
transaction_options_instance = TransactionOptions.from_json(json)
# print the JSON string representation of the object
print(TransactionOptions.to_json())

# convert the object into a dict
transaction_options_dict = transaction_options_instance.to_dict()
# create an instance of TransactionOptions from a dict
transaction_options_from_dict = TransactionOptions.from_dict(transaction_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


