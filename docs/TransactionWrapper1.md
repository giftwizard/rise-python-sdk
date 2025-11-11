# TransactionWrapper1

The last transaction that modified the gift card balance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Transaction ID. | [optional] [readonly] 
**created_date** | **datetime** | Date and time the Transaction was created. | [optional] [readonly] 

## Example

```python
from openapi_client.models.transaction_wrapper1 import TransactionWrapper1

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionWrapper1 from a JSON string
transaction_wrapper1_instance = TransactionWrapper1.from_json(json)
# print the JSON string representation of the object
print(TransactionWrapper1.to_json())

# convert the object into a dict
transaction_wrapper1_dict = transaction_wrapper1_instance.to_dict()
# create an instance of TransactionWrapper1 from a dict
transaction_wrapper1_from_dict = TransactionWrapper1.from_dict(transaction_wrapper1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


