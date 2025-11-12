# SideEffects2

Optional information about some side effects regarding the creation of the Recipient.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skip_notifications** | **bool** | Whether to skip sending notifications for this recipient. | [optional] 

## Example

```python
from openapi_client.models.side_effects2 import SideEffects2

# TODO update the JSON string below
json = "{}"
# create an instance of SideEffects2 from a JSON string
side_effects2_instance = SideEffects2.from_json(json)
# print the JSON string representation of the object
print(SideEffects2.to_json())

# convert the object into a dict
side_effects2_dict = side_effects2_instance.to_dict()
# create an instance of SideEffects2 from a dict
side_effects2_from_dict = SideEffects2.from_dict(side_effects2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


