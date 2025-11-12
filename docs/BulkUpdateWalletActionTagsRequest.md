# BulkUpdateWalletActionTagsRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** | List of wallet-actions that their tags will update. | [optional] 
**assign_tags** | **object** | List of Tags to assign | [optional] 
**unassign_tags** | **object** | List of Tags to unAssign | [optional] 

## Example

```python
from openapi_client.models.bulk_update_wallet_action_tags_request import BulkUpdateWalletActionTagsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkUpdateWalletActionTagsRequest from a JSON string
bulk_update_wallet_action_tags_request_instance = BulkUpdateWalletActionTagsRequest.from_json(json)
# print the JSON string representation of the object
print(BulkUpdateWalletActionTagsRequest.to_json())

# convert the object into a dict
bulk_update_wallet_action_tags_request_dict = bulk_update_wallet_action_tags_request_instance.to_dict()
# create an instance of BulkUpdateWalletActionTagsRequest from a dict
bulk_update_wallet_action_tags_request_from_dict = BulkUpdateWalletActionTagsRequest.from_dict(bulk_update_wallet_action_tags_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


