# RateLimit



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_activations_expression** | **str** | Value expressing the maximum number of times the trigger can be activated. | [optional] 
**duration_expression** | **str** | Duration of the rate limiting window in the selected time unit. If no value is set, the rate limit is permanent. | [optional] 
**duration_time_unit** | **str** | Time unit for the rate limit duration. | [optional] 
**unique_identifier_expression** | **str** | Unique identifier of each activation, by which rate limiter will count activations. | [optional] 

## Example

```python
from openapi_client.models.rate_limit import RateLimit

# TODO update the JSON string below
json = "{}"
# create an instance of RateLimit from a JSON string
rate_limit_instance = RateLimit.from_json(json)
# print the JSON string representation of the object
print(RateLimit.to_json())

# convert the object into a dict
rate_limit_dict = rate_limit_instance.to_dict()
# create an instance of RateLimit from a dict
rate_limit_from_dict = RateLimit.from_dict(rate_limit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


