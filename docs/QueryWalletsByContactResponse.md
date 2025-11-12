# QueryWalletsByContactResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallets** | **List[object]** | List of retrieved wallets with gift card information. | [optional] [readonly] 

## Example

```python
from openapi_client.models.query_wallets_by_contact_response import QueryWalletsByContactResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QueryWalletsByContactResponse from a JSON string
query_wallets_by_contact_response_instance = QueryWalletsByContactResponse.from_json(json)
# print the JSON string representation of the object
print(QueryWalletsByContactResponse.to_json())

# convert the object into a dict
query_wallets_by_contact_response_dict = query_wallets_by_contact_response_instance.to_dict()
# create an instance of QueryWalletsByContactResponse from a dict
query_wallets_by_contact_response_from_dict = QueryWalletsByContactResponse.from_dict(query_wallets_by_contact_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


