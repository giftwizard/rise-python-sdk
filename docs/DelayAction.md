# DelayAction



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset_expression** | **str** | Value expressing the amount of time to wait from a specific date or from the time the action is executed. | [optional] 
**offset_time_unit** | **str** | Time unit for delay offset. | [optional] 
**due_date_epoch_expression** | **str** | The action due date. If defined without an offset, the automation will wait until this date to execute the next step. If an offset is defined, it&#39;s calculated from this date. The date is expressed in the number of milliseconds since the Unix Epoch (1 January, 1970 UTC). | [optional] 
**post_action_ids** | **List[str]** | List of IDs of actions to run in parallel after the delay. | [optional] 

## Example

```python
from openapi_client.models.delay_action import DelayAction

# TODO update the JSON string below
json = "{}"
# create an instance of DelayAction from a JSON string
delay_action_instance = DelayAction.from_json(json)
# print the JSON string representation of the object
print(DelayAction.to_json())

# convert the object into a dict
delay_action_dict = delay_action_instance.to_dict()
# create an instance of DelayAction from a dict
delay_action_from_dict = DelayAction.from_dict(delay_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


