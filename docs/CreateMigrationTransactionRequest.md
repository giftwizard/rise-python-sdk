# CreateMigrationTransactionRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction** | **object** | The transaction to create. | [optional] 

## Example

```python
from openapi_client.models.create_migration_transaction_request import CreateMigrationTransactionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMigrationTransactionRequest from a JSON string
create_migration_transaction_request_instance = CreateMigrationTransactionRequest.from_json(json)
# print the JSON string representation of the object
print(CreateMigrationTransactionRequest.to_json())

# convert the object into a dict
create_migration_transaction_request_dict = create_migration_transaction_request_instance.to_dict()
# create an instance of CreateMigrationTransactionRequest from a dict
create_migration_transaction_request_from_dict = CreateMigrationTransactionRequest.from_dict(create_migration_transaction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


