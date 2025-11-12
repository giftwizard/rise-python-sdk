# RateLimitAction



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_activations_expression** | **str** | The maximum number of activations allowed for the action. | [optional] 
**rate_limit_duration_expression** | **str** | Duration of the rate limiting window, expressed in selected time unit. If no value is set, then there is no time limit on the rate limiter. | [optional] 
**rate_limit_duration_time_unit** | **str** | Time unit for the rate limit duration. | [optional] 
**unique_identifier_expression** | **str** | Unique identifier of each activation by which rate limiter counts activations. | [optional] 
**post_action_ids** | **List[str]** | List of IDs of actions to run in parallel once the action completes. | [optional] 

## Example

```python
from openapi_client.models.rate_limit_action import RateLimitAction

# TODO update the JSON string below
json = "{}"
# create an instance of RateLimitAction from a JSON string
rate_limit_action_instance = RateLimitAction.from_json(json)
# print the JSON string representation of the object
print(RateLimitAction.to_json())

# convert the object into a dict
rate_limit_action_dict = rate_limit_action_instance.to_dict()
# create an instance of RateLimitAction from a dict
rate_limit_action_from_dict = RateLimitAction.from_dict(rate_limit_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


