# RateLimitActionInfo



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**passed** | **bool** | Indicates if the rate limiter passed (not reached the quota) | [optional] 

## Example

```python
from openapi_client.models.rate_limit_action_info import RateLimitActionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RateLimitActionInfo from a JSON string
rate_limit_action_info_instance = RateLimitActionInfo.from_json(json)
# print the JSON string representation of the object
print(RateLimitActionInfo.to_json())

# convert the object into a dict
rate_limit_action_info_dict = rate_limit_action_info_instance.to_dict()
# create an instance of RateLimitActionInfo from a dict
rate_limit_action_info_from_dict = RateLimitActionInfo.from_dict(rate_limit_action_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


