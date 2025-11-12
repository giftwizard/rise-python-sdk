# ActionInitiator1

Details of the API client creating this Transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the initiator (e.g., app, user) | [optional] 
**id** | **str** | ID of the initiator | [optional] 

## Example

```python
from openapi_client.models.action_initiator1 import ActionInitiator1

# TODO update the JSON string below
json = "{}"
# create an instance of ActionInitiator1 from a JSON string
action_initiator1_instance = ActionInitiator1.from_json(json)
# print the JSON string representation of the object
print(ActionInitiator1.to_json())

# convert the object into a dict
action_initiator1_dict = action_initiator1_instance.to_dict()
# create an instance of ActionInitiator1 from a dict
action_initiator1_from_dict = ActionInitiator1.from_dict(action_initiator1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


