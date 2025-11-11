# TransactionWrapper3

ID of the last transaction that increased the gift card balance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Transaction ID. | [optional] [readonly] 
**created_date** | **datetime** | Date and time the Transaction was created. | [optional] [readonly] 

## Example

```python
from openapi_client.models.transaction_wrapper3 import TransactionWrapper3

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionWrapper3 from a JSON string
transaction_wrapper3_instance = TransactionWrapper3.from_json(json)
# print the JSON string representation of the object
print(TransactionWrapper3.to_json())

# convert the object into a dict
transaction_wrapper3_dict = transaction_wrapper3_instance.to_dict()
# create an instance of TransactionWrapper3 from a dict
transaction_wrapper3_from_dict = TransactionWrapper3.from_dict(transaction_wrapper3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


