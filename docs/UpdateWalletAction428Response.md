# UpdateWalletAction428Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Error message | 
**details** | [**WALLETACTIONALREADYEXPIREDDetails**](WALLETACTIONALREADYEXPIREDDetails.md) |  | 

## Example

```python
from openapi_client.models.update_wallet_action428_response import UpdateWalletAction428Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWalletAction428Response from a JSON string
update_wallet_action428_response_instance = UpdateWalletAction428Response.from_json(json)
# print the JSON string representation of the object
print(UpdateWalletAction428Response.to_json())

# convert the object into a dict
update_wallet_action428_response_dict = update_wallet_action428_response_instance.to_dict()
# create an instance of UpdateWalletAction428Response from a dict
update_wallet_action428_response_from_dict = UpdateWalletAction428Response.from_dict(update_wallet_action428_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


