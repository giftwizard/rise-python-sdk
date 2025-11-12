# ManualOptionsManualOptions

Information about a transaction issued manually from the Rise dashboard.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note** | **str** | Internal note about the Transaction/Gift Card. | [optional] 

## Example

```python
from openapi_client.models.manual_options_manual_options import ManualOptionsManualOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ManualOptionsManualOptions from a JSON string
manual_options_manual_options_instance = ManualOptionsManualOptions.from_json(json)
# print the JSON string representation of the object
print(ManualOptionsManualOptions.to_json())

# convert the object into a dict
manual_options_manual_options_dict = manual_options_manual_options_instance.to_dict()
# create an instance of ManualOptionsManualOptions from a dict
manual_options_manual_options_from_dict = ManualOptionsManualOptions.from_dict(manual_options_manual_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


