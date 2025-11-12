# CreateWalletAction400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Error message | 
**details** | [**DISABLEDATDATESETDetails**](DISABLEDATDATESETDetails.md) |  | 

## Example

```python
from openapi_client.models.create_wallet_action400_response import CreateWalletAction400Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWalletAction400Response from a JSON string
create_wallet_action400_response_instance = CreateWalletAction400Response.from_json(json)
# print the JSON string representation of the object
print(CreateWalletAction400Response.to_json())

# convert the object into a dict
create_wallet_action400_response_dict = create_wallet_action400_response_instance.to_dict()
# create an instance of CreateWalletAction400Response from a dict
create_wallet_action400_response_from_dict = CreateWalletAction400Response.from_dict(create_wallet_action400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


