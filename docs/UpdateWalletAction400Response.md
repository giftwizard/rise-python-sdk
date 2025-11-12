# UpdateWalletAction400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Error message | 
**details** | [**STARTLATERTHANEXPIRATIONDetails**](STARTLATERTHANEXPIRATIONDetails.md) |  | 

## Example

```python
from openapi_client.models.update_wallet_action400_response import UpdateWalletAction400Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWalletAction400Response from a JSON string
update_wallet_action400_response_instance = UpdateWalletAction400Response.from_json(json)
# print the JSON string representation of the object
print(UpdateWalletAction400Response.to_json())

# convert the object into a dict
update_wallet_action400_response_dict = update_wallet_action400_response_instance.to_dict()
# create an instance of UpdateWalletAction400Response from a dict
update_wallet_action400_response_from_dict = UpdateWalletAction400Response.from_dict(update_wallet_action400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


