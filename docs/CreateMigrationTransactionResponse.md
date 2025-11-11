# CreateMigrationTransactionResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction** | **object** | The created transaction. | [optional] 

## Example

```python
from openapi_client.models.create_migration_transaction_response import CreateMigrationTransactionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMigrationTransactionResponse from a JSON string
create_migration_transaction_response_instance = CreateMigrationTransactionResponse.from_json(json)
# print the JSON string representation of the object
print(CreateMigrationTransactionResponse.to_json())

# convert the object into a dict
create_migration_transaction_response_dict = create_migration_transaction_response_instance.to_dict()
# create an instance of CreateMigrationTransactionResponse from a dict
create_migration_transaction_response_from_dict = CreateMigrationTransactionResponse.from_dict(create_migration_transaction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


