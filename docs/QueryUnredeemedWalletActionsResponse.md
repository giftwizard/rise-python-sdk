# QueryUnredeemedWalletActionsResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_actions** | **List[object]** | The retrieved unredeemed WalletActions with their balances. | [optional] 
**paging_metadata** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.query_unredeemed_wallet_actions_response import QueryUnredeemedWalletActionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QueryUnredeemedWalletActionsResponse from a JSON string
query_unredeemed_wallet_actions_response_instance = QueryUnredeemedWalletActionsResponse.from_json(json)
# print the JSON string representation of the object
print(QueryUnredeemedWalletActionsResponse.to_json())

# convert the object into a dict
query_unredeemed_wallet_actions_response_dict = query_unredeemed_wallet_actions_response_instance.to_dict()
# create an instance of QueryUnredeemedWalletActionsResponse from a dict
query_unredeemed_wallet_actions_response_from_dict = QueryUnredeemedWalletActionsResponse.from_dict(query_unredeemed_wallet_actions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


