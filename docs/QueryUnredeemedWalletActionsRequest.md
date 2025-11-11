# QueryUnredeemedWalletActionsRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **object** | API Query Language expression. | [optional] 

## Example

```python
from openapi_client.models.query_unredeemed_wallet_actions_request import QueryUnredeemedWalletActionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QueryUnredeemedWalletActionsRequest from a JSON string
query_unredeemed_wallet_actions_request_instance = QueryUnredeemedWalletActionsRequest.from_json(json)
# print the JSON string representation of the object
print(QueryUnredeemedWalletActionsRequest.to_json())

# convert the object into a dict
query_unredeemed_wallet_actions_request_dict = query_unredeemed_wallet_actions_request_instance.to_dict()
# create an instance of QueryUnredeemedWalletActionsRequest from a dict
query_unredeemed_wallet_actions_request_from_dict = QueryUnredeemedWalletActionsRequest.from_dict(query_unredeemed_wallet_actions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


