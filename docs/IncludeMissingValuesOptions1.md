# IncludeMissingValuesOptions1

Options for including missing values in results.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_to_bucket** | **str** | Specify a custom name for the bucket containing the missing values. Defaults are &#x60;\&quot;N/A\&quot;&#x60; for strings, &#x60;0&#x60; for integers, and &#x60;false&#x60; for booleans. | [optional] 

## Example

```python
from openapi_client.models.include_missing_values_options1 import IncludeMissingValuesOptions1

# TODO update the JSON string below
json = "{}"
# create an instance of IncludeMissingValuesOptions1 from a JSON string
include_missing_values_options1_instance = IncludeMissingValuesOptions1.from_json(json)
# print the JSON string representation of the object
print(IncludeMissingValuesOptions1.to_json())

# convert the object into a dict
include_missing_values_options1_dict = include_missing_values_options1_instance.to_dict()
# create an instance of IncludeMissingValuesOptions1 from a dict
include_missing_values_options1_from_dict = IncludeMissingValuesOptions1.from_dict(include_missing_values_options1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


