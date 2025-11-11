# QueryWalletActionBalancesResponse1



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_actions** | [**List[WalletActionWithBalance1]**](WalletActionWithBalance1.md) | The retrieved WalletActions with their balances. | [optional] 
**paging_metadata** | [**PagingMetadataV22**](PagingMetadataV22.md) |  | [optional] 

## Example

```python
from openapi_client.models.query_wallet_action_balances_response1 import QueryWalletActionBalancesResponse1

# TODO update the JSON string below
json = "{}"
# create an instance of QueryWalletActionBalancesResponse1 from a JSON string
query_wallet_action_balances_response1_instance = QueryWalletActionBalancesResponse1.from_json(json)
# print the JSON string representation of the object
print(QueryWalletActionBalancesResponse1.to_json())

# convert the object into a dict
query_wallet_action_balances_response1_dict = query_wallet_action_balances_response1_instance.to_dict()
# create an instance of QueryWalletActionBalancesResponse1 from a dict
query_wallet_action_balances_response1_from_dict = QueryWalletActionBalancesResponse1.from_dict(query_wallet_action_balances_response1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


