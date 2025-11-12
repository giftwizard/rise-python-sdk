# RateLimiting



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_num_of_activations** | **float** | The maximum number of activations allowed in the given time frame | [optional] 
**max_num_of_activations_expression** | **str** | Optional, used if provided: A jsonata expression that evaluates to the maximum number of activations allowed in the given time frame | [optional] 
**time_frame_in_minutes** | **int** | If given - the time frame in minutes, otherwise, for life | [optional] 
**time_frame_in_minutes_expression** | **str** | Optional, used if provided - A jsonata expression that evaluates to the time frame in minutes, otherwise, for life | [optional] 
**key_jsonata** | **str** | The jsonata to use to extract the entity/resource key from the enriched event payload | [optional] 
**post_actions** | **List[object]** | The actions to perform if this rate limiting action succeeded - meaning we are still in the allowed number of activations in the given time frame | [optional] 
**post_actions_ids** | **List[str]** | The ids of actions to perform if this rate limiting action succeeded - meaning we are still in the allowed number of activations in the given time frame | [optional] 

## Example

```python
from openapi_client.models.rate_limiting import RateLimiting

# TODO update the JSON string below
json = "{}"
# create an instance of RateLimiting from a JSON string
rate_limiting_instance = RateLimiting.from_json(json)
# print the JSON string representation of the object
print(RateLimiting.to_json())

# convert the object into a dict
rate_limiting_dict = rate_limiting_instance.to_dict()
# create an instance of RateLimiting from a dict
rate_limiting_from_dict = RateLimiting.from_dict(rate_limiting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


