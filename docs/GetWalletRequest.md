# GetWalletRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **object** | Query object. | [optional] 

## Example

```python
from openapi_client.models.get_wallet_request import GetWalletRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetWalletRequest from a JSON string
get_wallet_request_instance = GetWalletRequest.from_json(json)
# print the JSON string representation of the object
print(GetWalletRequest.to_json())

# convert the object into a dict
get_wallet_request_dict = get_wallet_request_instance.to_dict()
# create an instance of GetWalletRequest from a dict
get_wallet_request_from_dict = GetWalletRequest.from_dict(get_wallet_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


