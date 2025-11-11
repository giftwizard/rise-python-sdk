# ApplicationError



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Error code. | [optional] 
**description** | **str** | Description of the error. | [optional] 
**data** | **object** | Data related to the error. | [optional] 

## Example

```python
from openapi_client.models.application_error import ApplicationError

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationError from a JSON string
application_error_instance = ApplicationError.from_json(json)
# print the JSON string representation of the object
print(ApplicationError.to_json())

# convert the object into a dict
application_error_dict = application_error_instance.to_dict()
# create an instance of ApplicationError from a dict
application_error_from_dict = ApplicationError.from_dict(application_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


