# ApplicationOrigin



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** | Application ID. | [optional] 
**app_defined_external_id** | **str** | External ID to correlate multiple sites to an automation | [optional] 

## Example

```python
from openapi_client.models.application_origin import ApplicationOrigin

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationOrigin from a JSON string
application_origin_instance = ApplicationOrigin.from_json(json)
# print the JSON string representation of the object
print(ApplicationOrigin.to_json())

# convert the object into a dict
application_origin_dict = application_origin_instance.to_dict()
# create an instance of ApplicationOrigin from a dict
application_origin_from_dict = ApplicationOrigin.from_dict(application_origin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


