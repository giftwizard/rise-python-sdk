# QueryWalletsByContactResponse1



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallets** | [**List[Wallet5]**](Wallet5.md) | List of retrieved wallets with gift card information. | [optional] [readonly] 

## Example

```python
from openapi_client.models.query_wallets_by_contact_response1 import QueryWalletsByContactResponse1

# TODO update the JSON string below
json = "{}"
# create an instance of QueryWalletsByContactResponse1 from a JSON string
query_wallets_by_contact_response1_instance = QueryWalletsByContactResponse1.from_json(json)
# print the JSON string representation of the object
print(QueryWalletsByContactResponse1.to_json())

# convert the object into a dict
query_wallets_by_contact_response1_dict = query_wallets_by_contact_response1_instance.to_dict()
# create an instance of QueryWalletsByContactResponse1 from a dict
query_wallets_by_contact_response1_from_dict = QueryWalletsByContactResponse1.from_dict(query_wallets_by_contact_response1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


