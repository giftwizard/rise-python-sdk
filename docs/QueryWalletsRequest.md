# QueryWalletsRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **object** | API Query Language expression. | [optional] 

## Example

```python
from openapi_client.models.query_wallets_request import QueryWalletsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QueryWalletsRequest from a JSON string
query_wallets_request_instance = QueryWalletsRequest.from_json(json)
# print the JSON string representation of the object
print(QueryWalletsRequest.to_json())

# convert the object into a dict
query_wallets_request_dict = query_wallets_request_instance.to_dict()
# create an instance of QueryWalletsRequest from a dict
query_wallets_request_from_dict = QueryWalletsRequest.from_dict(query_wallets_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


