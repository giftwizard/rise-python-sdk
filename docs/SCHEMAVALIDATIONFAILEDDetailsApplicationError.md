# SCHEMAVALIDATIONFAILEDDetailsApplicationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Error code: SCHEMA_VALIDATION_FAILED | 
**description** | **str** | Error description | 
**data** | **object** | Error specific data | [optional] 

## Example

```python
from openapi_client.models.schemavalidationfailed_details_application_error import SCHEMAVALIDATIONFAILEDDetailsApplicationError

# TODO update the JSON string below
json = "{}"
# create an instance of SCHEMAVALIDATIONFAILEDDetailsApplicationError from a JSON string
schemavalidationfailed_details_application_error_instance = SCHEMAVALIDATIONFAILEDDetailsApplicationError.from_json(json)
# print the JSON string representation of the object
print(SCHEMAVALIDATIONFAILEDDetailsApplicationError.to_json())

# convert the object into a dict
schemavalidationfailed_details_application_error_dict = schemavalidationfailed_details_application_error_instance.to_dict()
# create an instance of SCHEMAVALIDATIONFAILEDDetailsApplicationError from a dict
schemavalidationfailed_details_application_error_from_dict = SCHEMAVALIDATIONFAILEDDetailsApplicationError.from_dict(schemavalidationfailed_details_application_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


