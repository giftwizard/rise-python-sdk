# IncludeMissingValuesOptions



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_to_bucket** | **str** | Specify a custom name for the bucket containing the missing values. Defaults are &#x60;\&quot;N/A\&quot;&#x60; for strings, &#x60;0&#x60; for integers, and &#x60;false&#x60; for booleans. | [optional] 

## Example

```python
from openapi_client.models.include_missing_values_options import IncludeMissingValuesOptions

# TODO update the JSON string below
json = "{}"
# create an instance of IncludeMissingValuesOptions from a JSON string
include_missing_values_options_instance = IncludeMissingValuesOptions.from_json(json)
# print the JSON string representation of the object
print(IncludeMissingValuesOptions.to_json())

# convert the object into a dict
include_missing_values_options_dict = include_missing_values_options_instance.to_dict()
# create an instance of IncludeMissingValuesOptions from a dict
include_missing_values_options_from_dict = IncludeMissingValuesOptions.from_dict(include_missing_values_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


