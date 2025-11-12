# CreateWalletV2Request



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | Currency of the wallet. | [optional] 
**contact_details** | **object** | Contact details of the wallet. | [optional] 
**customer_reference** | **object** | Optional initial Customer Reference for the wallet. | [optional] 

## Example

```python
from openapi_client.models.create_wallet_v2_request import CreateWalletV2Request

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWalletV2Request from a JSON string
create_wallet_v2_request_instance = CreateWalletV2Request.from_json(json)
# print the JSON string representation of the object
print(CreateWalletV2Request.to_json())

# convert the object into a dict
create_wallet_v2_request_dict = create_wallet_v2_request_instance.to_dict()
# create an instance of CreateWalletV2Request from a dict
create_wallet_v2_request_from_dict = CreateWalletV2Request.from_dict(create_wallet_v2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


