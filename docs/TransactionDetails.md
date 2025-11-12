# TransactionDetails



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_transaction** | **object** | The last transaction that modified the gift card balance. | [optional] [readonly] 
**last_decreasing_transaction** | **object** | The last transaction that decreased the gift card balance, such as redemption or refund. | [optional] [readonly] 
**last_increasing_transaction** | **object** | ID of the last transaction that increased the gift card balance. | [optional] [readonly] 

## Example

```python
from openapi_client.models.transaction_details import TransactionDetails

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionDetails from a JSON string
transaction_details_instance = TransactionDetails.from_json(json)
# print the JSON string representation of the object
print(TransactionDetails.to_json())

# convert the object into a dict
transaction_details_dict = transaction_details_instance.to_dict()
# create an instance of TransactionDetails from a dict
transaction_details_from_dict = TransactionDetails.from_dict(transaction_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


