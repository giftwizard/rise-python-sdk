# GetOrCreateWalletRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_reference** | **object** | The customer reference with which to create or retrieve the wallet. | [optional] 
**currency** | **str** | Currency of the wallet. | [optional] 

## Example

```python
from openapi_client.models.get_or_create_wallet_request import GetOrCreateWalletRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrCreateWalletRequest from a JSON string
get_or_create_wallet_request_instance = GetOrCreateWalletRequest.from_json(json)
# print the JSON string representation of the object
print(GetOrCreateWalletRequest.to_json())

# convert the object into a dict
get_or_create_wallet_request_dict = get_or_create_wallet_request_instance.to_dict()
# create an instance of GetOrCreateWalletRequest from a dict
get_or_create_wallet_request_from_dict = GetOrCreateWalletRequest.from_dict(get_or_create_wallet_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


