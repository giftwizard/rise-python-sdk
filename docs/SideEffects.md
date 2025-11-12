# SideEffects

Side effects for the gift card creation flow.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skip_notifications** | **bool** | Whether to skip sending notifications such as emails. | [optional] 

## Example

```python
from openapi_client.models.side_effects import SideEffects

# TODO update the JSON string below
json = "{}"
# create an instance of SideEffects from a JSON string
side_effects_instance = SideEffects.from_json(json)
# print the JSON string representation of the object
print(SideEffects.to_json())

# convert the object into a dict
side_effects_dict = side_effects_instance.to_dict()
# create an instance of SideEffects from a dict
side_effects_from_dict = SideEffects.from_dict(side_effects_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


