# MigrationOptions2

Detailed information about a Gift Card or Gift Card Transaction whose source is a migration from Rise V1 or another platform.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**migration_options** | [**MigrationOptions2**](MigrationOptions2.md) |  | [optional] 

## Example

```python
from openapi_client.models.migration_options2 import MigrationOptions2

# TODO update the JSON string below
json = "{}"
# create an instance of MigrationOptions2 from a JSON string
migration_options2_instance = MigrationOptions2.from_json(json)
# print the JSON string representation of the object
print(MigrationOptions2.to_json())

# convert the object into a dict
migration_options2_dict = migration_options2_instance.to_dict()
# create an instance of MigrationOptions2 from a dict
migration_options2_from_dict = MigrationOptions2.from_dict(migration_options2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


