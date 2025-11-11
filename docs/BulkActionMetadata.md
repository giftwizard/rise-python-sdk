# BulkActionMetadata



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_successes** | **int** | Number of items that were successfully processed. | [optional] 
**total_failures** | **int** | Number of items that couldn&#39;t be processed. | [optional] 
**undetailed_failures** | **int** | Number of failures without details because detailed failure threshold was exceeded. | [optional] 

## Example

```python
from openapi_client.models.bulk_action_metadata import BulkActionMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of BulkActionMetadata from a JSON string
bulk_action_metadata_instance = BulkActionMetadata.from_json(json)
# print the JSON string representation of the object
print(BulkActionMetadata.to_json())

# convert the object into a dict
bulk_action_metadata_dict = bulk_action_metadata_instance.to_dict()
# create an instance of BulkActionMetadata from a dict
bulk_action_metadata_from_dict = BulkActionMetadata.from_dict(bulk_action_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


