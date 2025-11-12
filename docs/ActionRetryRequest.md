# ActionRetryRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activation_context** | **object** | The activation context | [optional] 
**action_to_retry_data** | **object** | The action to retry | [optional] 

## Example

```python
from openapi_client.models.action_retry_request import ActionRetryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActionRetryRequest from a JSON string
action_retry_request_instance = ActionRetryRequest.from_json(json)
# print the JSON string representation of the object
print(ActionRetryRequest.to_json())

# convert the object into a dict
action_retry_request_dict = action_retry_request_instance.to_dict()
# create an instance of ActionRetryRequest from a dict
action_retry_request_from_dict = ActionRetryRequest.from_dict(action_retry_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


