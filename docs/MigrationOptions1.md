# MigrationOptions1

Information about a transaction whose source is a migration from Rise V1 or another platform.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**migration_options** | [**MigrationOptions1**](MigrationOptions1.md) |  | [optional] 

## Example

```python
from openapi_client.models.migration_options1 import MigrationOptions1

# TODO update the JSON string below
json = "{}"
# create an instance of MigrationOptions1 from a JSON string
migration_options1_instance = MigrationOptions1.from_json(json)
# print the JSON string representation of the object
print(MigrationOptions1.to_json())

# convert the object into a dict
migration_options1_dict = migration_options1_instance.to_dict()
# create an instance of MigrationOptions1 from a dict
migration_options1_from_dict = MigrationOptions1.from_dict(migration_options1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


