# QueryWalletActionBalancesResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_actions** | **List[object]** | The retrieved WalletActions with their balances. | [optional] 
**paging_metadata** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.query_wallet_action_balances_response import QueryWalletActionBalancesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QueryWalletActionBalancesResponse from a JSON string
query_wallet_action_balances_response_instance = QueryWalletActionBalancesResponse.from_json(json)
# print the JSON string representation of the object
print(QueryWalletActionBalancesResponse.to_json())

# convert the object into a dict
query_wallet_action_balances_response_dict = query_wallet_action_balances_response_instance.to_dict()
# create an instance of QueryWalletActionBalancesResponse from a dict
query_wallet_action_balances_response_from_dict = QueryWalletActionBalancesResponse.from_dict(query_wallet_action_balances_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


