# MigrationOptionsMigrationOptions

Information about a transaction whose source is a migration from Rise V1 or another platform.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**previous_id** | **str** | ID of the gift card or transaction in Rise V1. | [optional] 
**liability** | **bool** | Indicates whether the gift card or transaction is a liability. | [optional] 
**note** | **str** | Note about the gift card or transaction being migrated. | [optional] 

## Example

```python
from openapi_client.models.migration_options_migration_options import MigrationOptionsMigrationOptions

# TODO update the JSON string below
json = "{}"
# create an instance of MigrationOptionsMigrationOptions from a JSON string
migration_options_migration_options_instance = MigrationOptionsMigrationOptions.from_json(json)
# print the JSON string representation of the object
print(MigrationOptionsMigrationOptions.to_json())

# convert the object into a dict
migration_options_migration_options_dict = migration_options_migration_options_instance.to_dict()
# create an instance of MigrationOptionsMigrationOptions from a dict
migration_options_migration_options_from_dict = MigrationOptionsMigrationOptions.from_dict(migration_options_migration_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


