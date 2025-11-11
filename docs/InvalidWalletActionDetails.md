# InvalidWalletActionDetails



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_action_id** | **str** | WalletAction ID. | [optional] 

## Example

```python
from openapi_client.models.invalid_wallet_action_details import InvalidWalletActionDetails

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidWalletActionDetails from a JSON string
invalid_wallet_action_details_instance = InvalidWalletActionDetails.from_json(json)
# print the JSON string representation of the object
print(InvalidWalletActionDetails.to_json())

# convert the object into a dict
invalid_wallet_action_details_dict = invalid_wallet_action_details_instance.to_dict()
# create an instance of InvalidWalletActionDetails from a dict
invalid_wallet_action_details_from_dict = InvalidWalletActionDetails.from_dict(invalid_wallet_action_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


