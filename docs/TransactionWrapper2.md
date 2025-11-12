# TransactionWrapper2

The last transaction that decreased the gift card balance, such as redemption or refund.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Transaction ID. | [optional] [readonly] 
**created_date** | **datetime** | Date and time the Transaction was created. | [optional] [readonly] 

## Example

```python
from openapi_client.models.transaction_wrapper2 import TransactionWrapper2

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionWrapper2 from a JSON string
transaction_wrapper2_instance = TransactionWrapper2.from_json(json)
# print the JSON string representation of the object
print(TransactionWrapper2.to_json())

# convert the object into a dict
transaction_wrapper2_dict = transaction_wrapper2_instance.to_dict()
# create an instance of TransactionWrapper2 from a dict
transaction_wrapper2_from_dict = TransactionWrapper2.from_dict(transaction_wrapper2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


