# SideEffects1

Side effect for the gift card creation flow.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skip_notifications** | **bool** | Whether to skip sending notifications such as emails. | [optional] 

## Example

```python
from openapi_client.models.side_effects1 import SideEffects1

# TODO update the JSON string below
json = "{}"
# create an instance of SideEffects1 from a JSON string
side_effects1_instance = SideEffects1.from_json(json)
# print the JSON string representation of the object
print(SideEffects1.to_json())

# convert the object into a dict
side_effects1_dict = side_effects1_instance.to_dict()
# create an instance of SideEffects1 from a dict
side_effects1_from_dict = SideEffects1.from_dict(side_effects1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


