# BulkOptionsBulkOptions

Bulk Options. (**Deprecated**: Use `wallet_action_start_options` instead.)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bulk_id** | **str** | ID of the bulk that issued the gift card or transaction. | [optional] 
**liability** | **bool** | Indicates whether the gift card or transaction is a liability. | [optional] 
**note** | **str** | Internal note about the bulk | [optional] 

## Example

```python
from openapi_client.models.bulk_options_bulk_options import BulkOptionsBulkOptions

# TODO update the JSON string below
json = "{}"
# create an instance of BulkOptionsBulkOptions from a JSON string
bulk_options_bulk_options_instance = BulkOptionsBulkOptions.from_json(json)
# print the JSON string representation of the object
print(BulkOptionsBulkOptions.to_json())

# convert the object into a dict
bulk_options_bulk_options_dict = bulk_options_bulk_options_instance.to_dict()
# create an instance of BulkOptionsBulkOptions from a dict
bulk_options_bulk_options_from_dict = BulkOptionsBulkOptions.from_dict(bulk_options_bulk_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


