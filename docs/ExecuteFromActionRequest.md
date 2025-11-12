# ExecuteFromActionRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_id** | **str** | Requested action id | [optional] 
**activation_id** | **str** | Optional: an activation id to link this action to | [optional] 
**payload** | **object** | Activation payload | [optional] 
**configuration_correlation_id** | **str** | Configuration correlation id to run this action from | [optional] 
**schedule_id** | **str** | Optional - schedule id that this action was scheduled from | [optional] 
**external_entity_id** | **str** | Optional - an external entity id that this execution is related to | [optional] 
**automation** | **object** | Optional - Activation automation | [optional] 

## Example

```python
from openapi_client.models.execute_from_action_request import ExecuteFromActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExecuteFromActionRequest from a JSON string
execute_from_action_request_instance = ExecuteFromActionRequest.from_json(json)
# print the JSON string representation of the object
print(ExecuteFromActionRequest.to_json())

# convert the object into a dict
execute_from_action_request_dict = execute_from_action_request_instance.to_dict()
# create an instance of ExecuteFromActionRequest from a dict
execute_from_action_request_from_dict = ExecuteFromActionRequest.from_dict(execute_from_action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


