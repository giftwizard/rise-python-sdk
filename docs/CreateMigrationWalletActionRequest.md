# CreateMigrationWalletActionRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_action** | **object** | WalletAction to be created. | [optional] 
**gift_card_id** | **str** | ID of the giftcard that belongs to the wallet. | [optional] 

## Example

```python
from openapi_client.models.create_migration_wallet_action_request import CreateMigrationWalletActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMigrationWalletActionRequest from a JSON string
create_migration_wallet_action_request_instance = CreateMigrationWalletActionRequest.from_json(json)
# print the JSON string representation of the object
print(CreateMigrationWalletActionRequest.to_json())

# convert the object into a dict
create_migration_wallet_action_request_dict = create_migration_wallet_action_request_instance.to_dict()
# create an instance of CreateMigrationWalletActionRequest from a dict
create_migration_wallet_action_request_from_dict = CreateMigrationWalletActionRequest.from_dict(create_migration_wallet_action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


