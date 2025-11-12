# ActionInitiator



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the initiator (e.g., app, user) | [optional] 
**id** | **str** | ID of the initiator | [optional] 

## Example

```python
from openapi_client.models.action_initiator import ActionInitiator

# TODO update the JSON string below
json = "{}"
# create an instance of ActionInitiator from a JSON string
action_initiator_instance = ActionInitiator.from_json(json)
# print the JSON string representation of the object
print(ActionInitiator.to_json())

# convert the object into a dict
action_initiator_dict = action_initiator_instance.to_dict()
# create an instance of ActionInitiator from a dict
action_initiator_from_dict = ActionInitiator.from_dict(action_initiator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


