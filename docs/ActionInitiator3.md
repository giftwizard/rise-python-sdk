# ActionInitiator3

Details of the API client creating this Gift Card.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the initiator (e.g., app, user) | [optional] 
**id** | **str** | ID of the initiator | [optional] 

## Example

```python
from openapi_client.models.action_initiator3 import ActionInitiator3

# TODO update the JSON string below
json = "{}"
# create an instance of ActionInitiator3 from a JSON string
action_initiator3_instance = ActionInitiator3.from_json(json)
# print the JSON string representation of the object
print(ActionInitiator3.to_json())

# convert the object into a dict
action_initiator3_dict = action_initiator3_instance.to_dict()
# create an instance of ActionInitiator3 from a dict
action_initiator3_from_dict = ActionInitiator3.from_dict(action_initiator3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


