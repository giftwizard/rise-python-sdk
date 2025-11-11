# CreateMigrationRecipientRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipient** | **object** | Recipient to be created. | [optional] 
**side_effects** | **object** | Optional information about some side effects regarding the creation of the Recipient. | [optional] 

## Example

```python
from openapi_client.models.create_migration_recipient_request import CreateMigrationRecipientRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMigrationRecipientRequest from a JSON string
create_migration_recipient_request_instance = CreateMigrationRecipientRequest.from_json(json)
# print the JSON string representation of the object
print(CreateMigrationRecipientRequest.to_json())

# convert the object into a dict
create_migration_recipient_request_dict = create_migration_recipient_request_instance.to_dict()
# create an instance of CreateMigrationRecipientRequest from a dict
create_migration_recipient_request_from_dict = CreateMigrationRecipientRequest.from_dict(create_migration_recipient_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


