# BulkUpdateWalletActionTagsResult



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_metadata** | **object** | Metadata regarding the specific single update operation | [optional] 

## Example

```python
from openapi_client.models.bulk_update_wallet_action_tags_result import BulkUpdateWalletActionTagsResult

# TODO update the JSON string below
json = "{}"
# create an instance of BulkUpdateWalletActionTagsResult from a JSON string
bulk_update_wallet_action_tags_result_instance = BulkUpdateWalletActionTagsResult.from_json(json)
# print the JSON string representation of the object
print(BulkUpdateWalletActionTagsResult.to_json())

# convert the object into a dict
bulk_update_wallet_action_tags_result_dict = bulk_update_wallet_action_tags_result_instance.to_dict()
# create an instance of BulkUpdateWalletActionTagsResult from a dict
bulk_update_wallet_action_tags_result_from_dict = BulkUpdateWalletActionTagsResult.from_dict(bulk_update_wallet_action_tags_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


