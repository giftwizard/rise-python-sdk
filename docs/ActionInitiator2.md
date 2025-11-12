# ActionInitiator2

Information about the initiator of the WalletAction, such as the app or user that initiated the action. Set when the WalletAction is created.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the initiator (e.g., app, user) | [optional] 
**id** | **str** | ID of the initiator | [optional] 

## Example

```python
from openapi_client.models.action_initiator2 import ActionInitiator2

# TODO update the JSON string below
json = "{}"
# create an instance of ActionInitiator2 from a JSON string
action_initiator2_instance = ActionInitiator2.from_json(json)
# print the JSON string representation of the object
print(ActionInitiator2.to_json())

# convert the object into a dict
action_initiator2_dict = action_initiator2_instance.to_dict()
# create an instance of ActionInitiator2 from a dict
action_initiator2_from_dict = ActionInitiator2.from_dict(action_initiator2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


