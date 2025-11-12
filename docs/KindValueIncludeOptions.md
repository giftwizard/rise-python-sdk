# KindValueIncludeOptions

Options for including missing values in results.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_to_bucket** | **str** | Specify a custom name for the bucket containing the missing values. Defaults are &#x60;\&quot;N/A\&quot;&#x60; for strings, &#x60;0&#x60; for integers, and &#x60;false&#x60; for booleans. | [optional] 

## Example

```python
from openapi_client.models.kind_value_include_options import KindValueIncludeOptions

# TODO update the JSON string below
json = "{}"
# create an instance of KindValueIncludeOptions from a JSON string
kind_value_include_options_instance = KindValueIncludeOptions.from_json(json)
# print the JSON string representation of the object
print(KindValueIncludeOptions.to_json())

# convert the object into a dict
kind_value_include_options_dict = kind_value_include_options_instance.to_dict()
# create an instance of KindValueIncludeOptions from a dict
kind_value_include_options_from_dict = KindValueIncludeOptions.from_dict(kind_value_include_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


