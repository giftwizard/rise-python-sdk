# TransactionSourceInfo



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**initiator** | **object** | Details of the API client creating this Transaction. | [optional] 
**source_tenant_id** | **str** | The Tenant ID that is associated with the action. | [optional] 
**source_channel_id** | **str** | The Channel ID that is associated with the action. | [optional] 
**source_location_id** | **str** | The location ID that is associated with the action (supports POS cases). | [optional] 

## Example

```python
from openapi_client.models.transaction_source_info import TransactionSourceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionSourceInfo from a JSON string
transaction_source_info_instance = TransactionSourceInfo.from_json(json)
# print the JSON string representation of the object
print(TransactionSourceInfo.to_json())

# convert the object into a dict
transaction_source_info_dict = transaction_source_info_instance.to_dict()
# create an instance of TransactionSourceInfo from a dict
transaction_source_info_from_dict = TransactionSourceInfo.from_dict(transaction_source_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


