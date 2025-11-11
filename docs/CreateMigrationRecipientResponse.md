# CreateMigrationRecipientResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipient** | **object** | The created Recipient. | [optional] 

## Example

```python
from openapi_client.models.create_migration_recipient_response import CreateMigrationRecipientResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMigrationRecipientResponse from a JSON string
create_migration_recipient_response_instance = CreateMigrationRecipientResponse.from_json(json)
# print the JSON string representation of the object
print(CreateMigrationRecipientResponse.to_json())

# convert the object into a dict
create_migration_recipient_response_dict = create_migration_recipient_response_instance.to_dict()
# create an instance of CreateMigrationRecipientResponse from a dict
create_migration_recipient_response_from_dict = CreateMigrationRecipientResponse.from_dict(create_migration_recipient_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


