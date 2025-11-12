# GetOrCreateWalletV2Request



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_details** | **object** | Contact details of the wallet. | [optional] 
**customer_reference** | **object** | Optional initial Customer Reference for the wallet. | [optional] 

## Example

```python
from openapi_client.models.get_or_create_wallet_v2_request import GetOrCreateWalletV2Request

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrCreateWalletV2Request from a JSON string
get_or_create_wallet_v2_request_instance = GetOrCreateWalletV2Request.from_json(json)
# print the JSON string representation of the object
print(GetOrCreateWalletV2Request.to_json())

# convert the object into a dict
get_or_create_wallet_v2_request_dict = get_or_create_wallet_v2_request_instance.to_dict()
# create an instance of GetOrCreateWalletV2Request from a dict
get_or_create_wallet_v2_request_from_dict = GetOrCreateWalletV2Request.from_dict(get_or_create_wallet_v2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


