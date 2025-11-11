# ActionCompletedRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**execution_identifier** | **str** | The execution identifier that was given to the spi provider when we invoked the action | [optional] 
**result** | **object** | The result of invoking the action. Must conform to the output schema configured by the action provider. | [optional] 

## Example

```python
from openapi_client.models.action_completed_request import ActionCompletedRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActionCompletedRequest from a JSON string
action_completed_request_instance = ActionCompletedRequest.from_json(json)
# print the JSON string representation of the object
print(ActionCompletedRequest.to_json())

# convert the object into a dict
action_completed_request_dict = action_completed_request_instance.to_dict()
# create an instance of ActionCompletedRequest from a dict
action_completed_request_from_dict = ActionCompletedRequest.from_dict(action_completed_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


