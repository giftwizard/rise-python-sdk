# QueryWalletActionBalancesRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **object** | API Query Language expression. | [optional] 

## Example

```python
from openapi_client.models.query_wallet_action_balances_request import QueryWalletActionBalancesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QueryWalletActionBalancesRequest from a JSON string
query_wallet_action_balances_request_instance = QueryWalletActionBalancesRequest.from_json(json)
# print the JSON string representation of the object
print(QueryWalletActionBalancesRequest.to_json())

# convert the object into a dict
query_wallet_action_balances_request_dict = query_wallet_action_balances_request_instance.to_dict()
# create an instance of QueryWalletActionBalancesRequest from a dict
query_wallet_action_balances_request_from_dict = QueryWalletActionBalancesRequest.from_dict(query_wallet_action_balances_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


