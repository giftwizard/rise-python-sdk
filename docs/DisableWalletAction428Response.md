# DisableWalletAction428Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Error message | 
**details** | [**WALLETACTIONNOTACTIVEDetails**](WALLETACTIONNOTACTIVEDetails.md) |  | 

## Example

```python
from openapi_client.models.disable_wallet_action428_response import DisableWalletAction428Response

# TODO update the JSON string below
json = "{}"
# create an instance of DisableWalletAction428Response from a JSON string
disable_wallet_action428_response_instance = DisableWalletAction428Response.from_json(json)
# print the JSON string representation of the object
print(DisableWalletAction428Response.to_json())

# convert the object into a dict
disable_wallet_action428_response_dict = disable_wallet_action428_response_instance.to_dict()
# create an instance of DisableWalletAction428Response from a dict
disable_wallet_action428_response_from_dict = DisableWalletAction428Response.from_dict(disable_wallet_action428_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


