# BulkUpdateWalletActionTagsResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | **List[object]** | Results | [optional] 
**bulk_action_metadata** | **object** | Metadata regarding the bulk update operation | [optional] 

## Example

```python
from openapi_client.models.bulk_update_wallet_action_tags_response import BulkUpdateWalletActionTagsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkUpdateWalletActionTagsResponse from a JSON string
bulk_update_wallet_action_tags_response_instance = BulkUpdateWalletActionTagsResponse.from_json(json)
# print the JSON string representation of the object
print(BulkUpdateWalletActionTagsResponse.to_json())

# convert the object into a dict
bulk_update_wallet_action_tags_response_dict = bulk_update_wallet_action_tags_response_instance.to_dict()
# create an instance of BulkUpdateWalletActionTagsResponse from a dict
bulk_update_wallet_action_tags_response_from_dict = BulkUpdateWalletActionTagsResponse.from_dict(bulk_update_wallet_action_tags_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


