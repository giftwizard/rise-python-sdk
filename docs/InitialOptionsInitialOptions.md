# InitialOptionsInitialOptions

Information about the first transaction that initializes a gift card.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gift_card_type** | **str** | Type of the gift card being initialized. | [optional] 

## Example

```python
from openapi_client.models.initial_options_initial_options import InitialOptionsInitialOptions

# TODO update the JSON string below
json = "{}"
# create an instance of InitialOptionsInitialOptions from a JSON string
initial_options_initial_options_instance = InitialOptionsInitialOptions.from_json(json)
# print the JSON string representation of the object
print(InitialOptionsInitialOptions.to_json())

# convert the object into a dict
initial_options_initial_options_dict = initial_options_initial_options_instance.to_dict()
# create an instance of InitialOptionsInitialOptions from a dict
initial_options_initial_options_from_dict = InitialOptionsInitialOptions.from_dict(initial_options_initial_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


