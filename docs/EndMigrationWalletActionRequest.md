# EndMigrationWalletActionRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_action_id** | **str** | ID of the WalletAction to be ended. | [optional] 
**gift_card_id** | **str** | ID of the giftcard that belongs to the wallet. | [optional] 
**amount_to_subtract** | **str** | Amount of the WalletAction to subtract from the wallet. | [optional] 

## Example

```python
from openapi_client.models.end_migration_wallet_action_request import EndMigrationWalletActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EndMigrationWalletActionRequest from a JSON string
end_migration_wallet_action_request_instance = EndMigrationWalletActionRequest.from_json(json)
# print the JSON string representation of the object
print(EndMigrationWalletActionRequest.to_json())

# convert the object into a dict
end_migration_wallet_action_request_dict = end_migration_wallet_action_request_instance.to_dict()
# create an instance of EndMigrationWalletActionRequest from a dict
end_migration_wallet_action_request_from_dict = EndMigrationWalletActionRequest.from_dict(end_migration_wallet_action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


