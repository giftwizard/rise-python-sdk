# MigrateWalletRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_reference** | **object** | Customer reference | [optional] 
**gift_card** | **object** | gift card id | [optional] 
**tenant_id** | **str** | tenant id | [optional] 
**channel_id** | **str** | channel id | [optional] 

## Example

```python
from openapi_client.models.migrate_wallet_request import MigrateWalletRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MigrateWalletRequest from a JSON string
migrate_wallet_request_instance = MigrateWalletRequest.from_json(json)
# print the JSON string representation of the object
print(MigrateWalletRequest.to_json())

# convert the object into a dict
migrate_wallet_request_dict = migrate_wallet_request_instance.to_dict()
# create an instance of MigrateWalletRequest from a dict
migrate_wallet_request_from_dict = MigrateWalletRequest.from_dict(migrate_wallet_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


