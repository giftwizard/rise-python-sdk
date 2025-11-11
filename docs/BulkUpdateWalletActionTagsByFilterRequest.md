# BulkUpdateWalletActionTagsByFilterRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | **object** | Filter | [optional] 
**assign_tags** | **object** | List of Tags to assign | [optional] 
**unassign_tags** | **object** | List of Tags to unAssign | [optional] 

## Example

```python
from openapi_client.models.bulk_update_wallet_action_tags_by_filter_request import BulkUpdateWalletActionTagsByFilterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkUpdateWalletActionTagsByFilterRequest from a JSON string
bulk_update_wallet_action_tags_by_filter_request_instance = BulkUpdateWalletActionTagsByFilterRequest.from_json(json)
# print the JSON string representation of the object
print(BulkUpdateWalletActionTagsByFilterRequest.to_json())

# convert the object into a dict
bulk_update_wallet_action_tags_by_filter_request_dict = bulk_update_wallet_action_tags_by_filter_request_instance.to_dict()
# create an instance of BulkUpdateWalletActionTagsByFilterRequest from a dict
bulk_update_wallet_action_tags_by_filter_request_from_dict = BulkUpdateWalletActionTagsByFilterRequest.from_dict(bulk_update_wallet_action_tags_by_filter_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


