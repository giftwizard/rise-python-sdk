# QueryWalletActionRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **object** | API Query Language expression. | [optional] 

## Example

```python
from openapi_client.models.query_wallet_action_request import QueryWalletActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QueryWalletActionRequest from a JSON string
query_wallet_action_request_instance = QueryWalletActionRequest.from_json(json)
# print the JSON string representation of the object
print(QueryWalletActionRequest.to_json())

# convert the object into a dict
query_wallet_action_request_dict = query_wallet_action_request_instance.to_dict()
# create an instance of QueryWalletActionRequest from a dict
query_wallet_action_request_from_dict = QueryWalletActionRequest.from_dict(query_wallet_action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


