# GetWalletV2Request



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **object** | Query object. | [optional] 
**fields** | **List[object]** | Additional fields to include in the response. | [optional] 

## Example

```python
from openapi_client.models.get_wallet_v2_request import GetWalletV2Request

# TODO update the JSON string below
json = "{}"
# create an instance of GetWalletV2Request from a JSON string
get_wallet_v2_request_instance = GetWalletV2Request.from_json(json)
# print the JSON string representation of the object
print(GetWalletV2Request.to_json())

# convert the object into a dict
get_wallet_v2_request_dict = get_wallet_v2_request_instance.to_dict()
# create an instance of GetWalletV2Request from a dict
get_wallet_v2_request_from_dict = GetWalletV2Request.from_dict(get_wallet_v2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


