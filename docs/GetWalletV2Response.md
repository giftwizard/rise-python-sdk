# GetWalletV2Response



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet** | **object** | The retrieved Wallet. | [optional] 

## Example

```python
from openapi_client.models.get_wallet_v2_response import GetWalletV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetWalletV2Response from a JSON string
get_wallet_v2_response_instance = GetWalletV2Response.from_json(json)
# print the JSON string representation of the object
print(GetWalletV2Response.to_json())

# convert the object into a dict
get_wallet_v2_response_dict = get_wallet_v2_response_instance.to_dict()
# create an instance of GetWalletV2Response from a dict
get_wallet_v2_response_from_dict = GetWalletV2Response.from_dict(get_wallet_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


