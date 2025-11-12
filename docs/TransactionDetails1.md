# TransactionDetails1

Transaction details related to the gift card.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_transaction** | [**TransactionWrapper1**](TransactionWrapper1.md) |  | [optional] 
**last_decreasing_transaction** | [**TransactionWrapper2**](TransactionWrapper2.md) |  | [optional] 
**last_increasing_transaction** | [**TransactionWrapper3**](TransactionWrapper3.md) |  | [optional] 

## Example

```python
from openapi_client.models.transaction_details1 import TransactionDetails1

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionDetails1 from a JSON string
transaction_details1_instance = TransactionDetails1.from_json(json)
# print the JSON string representation of the object
print(TransactionDetails1.to_json())

# convert the object into a dict
transaction_details1_dict = transaction_details1_instance.to_dict()
# create an instance of TransactionDetails1 from a dict
transaction_details1_from_dict = TransactionDetails1.from_dict(transaction_details1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


