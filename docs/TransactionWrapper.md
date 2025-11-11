# TransactionWrapper



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Transaction ID. | [optional] [readonly] 
**created_date** | **datetime** | Date and time the Transaction was created. | [optional] [readonly] 

## Example

```python
from openapi_client.models.transaction_wrapper import TransactionWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionWrapper from a JSON string
transaction_wrapper_instance = TransactionWrapper.from_json(json)
# print the JSON string representation of the object
print(TransactionWrapper.to_json())

# convert the object into a dict
transaction_wrapper_dict = transaction_wrapper_instance.to_dict()
# create an instance of TransactionWrapper from a dict
transaction_wrapper_from_dict = TransactionWrapper.from_dict(transaction_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


