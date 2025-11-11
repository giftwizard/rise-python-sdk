# QueryWalletsByContactRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **object** | Contact query object. | [optional] 

## Example

```python
from openapi_client.models.query_wallets_by_contact_request import QueryWalletsByContactRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QueryWalletsByContactRequest from a JSON string
query_wallets_by_contact_request_instance = QueryWalletsByContactRequest.from_json(json)
# print the JSON string representation of the object
print(QueryWalletsByContactRequest.to_json())

# convert the object into a dict
query_wallets_by_contact_request_dict = query_wallets_by_contact_request_instance.to_dict()
# create an instance of QueryWalletsByContactRequest from a dict
query_wallets_by_contact_request_from_dict = QueryWalletsByContactRequest.from_dict(query_wallets_by_contact_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


