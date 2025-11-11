# QueryWalletActionResponse1



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_actions** | [**List[WalletAction4]**](WalletAction4.md) | The retrieved WalletActions. | [optional] 
**paging_metadata** | [**PagingMetadataV22**](PagingMetadataV22.md) |  | [optional] 

## Example

```python
from openapi_client.models.query_wallet_action_response1 import QueryWalletActionResponse1

# TODO update the JSON string below
json = "{}"
# create an instance of QueryWalletActionResponse1 from a JSON string
query_wallet_action_response1_instance = QueryWalletActionResponse1.from_json(json)
# print the JSON string representation of the object
print(QueryWalletActionResponse1.to_json())

# convert the object into a dict
query_wallet_action_response1_dict = query_wallet_action_response1_instance.to_dict()
# create an instance of QueryWalletActionResponse1 from a dict
query_wallet_action_response1_from_dict = QueryWalletActionResponse1.from_dict(query_wallet_action_response1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


