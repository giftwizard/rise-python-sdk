# CreateMigrationGiftCardRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gift_card** | **object** | The gift card to create. | [optional] 

## Example

```python
from openapi_client.models.create_migration_gift_card_request import CreateMigrationGiftCardRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMigrationGiftCardRequest from a JSON string
create_migration_gift_card_request_instance = CreateMigrationGiftCardRequest.from_json(json)
# print the JSON string representation of the object
print(CreateMigrationGiftCardRequest.to_json())

# convert the object into a dict
create_migration_gift_card_request_dict = create_migration_gift_card_request_instance.to_dict()
# create an instance of CreateMigrationGiftCardRequest from a dict
create_migration_gift_card_request_from_dict = CreateMigrationGiftCardRequest.from_dict(create_migration_gift_card_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


