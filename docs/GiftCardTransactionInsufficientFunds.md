# GiftCardTransactionInsufficientFunds



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction** | **object** | the transaction that failed due to insufficient funds | [optional] 
**current_balance** | **str** | the current balance of the gift card | [optional] 

## Example

```python
from openapi_client.models.gift_card_transaction_insufficient_funds import GiftCardTransactionInsufficientFunds

# TODO update the JSON string below
json = "{}"
# create an instance of GiftCardTransactionInsufficientFunds from a JSON string
gift_card_transaction_insufficient_funds_instance = GiftCardTransactionInsufficientFunds.from_json(json)
# print the JSON string representation of the object
print(GiftCardTransactionInsufficientFunds.to_json())

# convert the object into a dict
gift_card_transaction_insufficient_funds_dict = gift_card_transaction_insufficient_funds_instance.to_dict()
# create an instance of GiftCardTransactionInsufficientFunds from a dict
gift_card_transaction_insufficient_funds_from_dict = GiftCardTransactionInsufficientFunds.from_dict(gift_card_transaction_insufficient_funds_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


