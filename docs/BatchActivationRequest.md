# BatchActivationRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activation_requests** | **List[object]** | List of Activation-Request. | [optional] 

## Example

```python
from openapi_client.models.batch_activation_request import BatchActivationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BatchActivationRequest from a JSON string
batch_activation_request_instance = BatchActivationRequest.from_json(json)
# print the JSON string representation of the object
print(BatchActivationRequest.to_json())

# convert the object into a dict
batch_activation_request_dict = batch_activation_request_instance.to_dict()
# create an instance of BatchActivationRequest from a dict
batch_activation_request_from_dict = BatchActivationRequest.from_dict(batch_activation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


