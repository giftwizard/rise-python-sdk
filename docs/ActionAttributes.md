# ActionAttributes



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retry** | **object** | Indicates if this action run is part of a retry attempt If it&#39;s not null, it&#39;s a retry action run | [optional] 

## Example

```python
from openapi_client.models.action_attributes import ActionAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ActionAttributes from a JSON string
action_attributes_instance = ActionAttributes.from_json(json)
# print the JSON string representation of the object
print(ActionAttributes.to_json())

# convert the object into a dict
action_attributes_dict = action_attributes_instance.to_dict()
# create an instance of ActionAttributes from a dict
action_attributes_from_dict = ActionAttributes.from_dict(action_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


