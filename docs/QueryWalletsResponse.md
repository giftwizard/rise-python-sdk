# QueryWalletsResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallets** | **List[object]** | List of retrieved wallets with gift card information. | [optional] [readonly] 
**paging_metadata** | **object** | Paging metadata. | [optional] 

## Example

```python
from openapi_client.models.query_wallets_response import QueryWalletsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QueryWalletsResponse from a JSON string
query_wallets_response_instance = QueryWalletsResponse.from_json(json)
# print the JSON string representation of the object
print(QueryWalletsResponse.to_json())

# convert the object into a dict
query_wallets_response_dict = query_wallets_response_instance.to_dict()
# create an instance of QueryWalletsResponse from a dict
query_wallets_response_from_dict = QueryWalletsResponse.from_dict(query_wallets_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


