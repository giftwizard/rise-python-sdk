# TransactionSourceInfo1

Information about the source of the transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**initiator** | [**ActionInitiator1**](ActionInitiator1.md) |  | [optional] 
**source_tenant_id** | **str** | The Tenant ID that is associated with the action. | [optional] 
**source_channel_id** | **str** | The Channel ID that is associated with the action. | [optional] 
**source_location_id** | **str** | The location ID that is associated with the action (supports POS cases). | [optional] 

## Example

```python
from openapi_client.models.transaction_source_info1 import TransactionSourceInfo1

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionSourceInfo1 from a JSON string
transaction_source_info1_instance = TransactionSourceInfo1.from_json(json)
# print the JSON string representation of the object
print(TransactionSourceInfo1.to_json())

# convert the object into a dict
transaction_source_info1_dict = transaction_source_info1_instance.to_dict()
# create an instance of TransactionSourceInfo1 from a dict
transaction_source_info1_from_dict = TransactionSourceInfo1.from_dict(transaction_source_info1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


