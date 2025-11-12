# INVALIDEXPIRATIONDATEDetailsApplicationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Error code: INVALID_EXPIRATION_DATE | 
**description** | **str** | Error description | 
**data** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.invalidexpirationdate_details_application_error import INVALIDEXPIRATIONDATEDetailsApplicationError

# TODO update the JSON string below
json = "{}"
# create an instance of INVALIDEXPIRATIONDATEDetailsApplicationError from a JSON string
invalidexpirationdate_details_application_error_instance = INVALIDEXPIRATIONDATEDetailsApplicationError.from_json(json)
# print the JSON string representation of the object
print(INVALIDEXPIRATIONDATEDetailsApplicationError.to_json())

# convert the object into a dict
invalidexpirationdate_details_application_error_dict = invalidexpirationdate_details_application_error_instance.to_dict()
# create an instance of INVALIDEXPIRATIONDATEDetailsApplicationError from a dict
invalidexpirationdate_details_application_error_from_dict = INVALIDEXPIRATIONDATEDetailsApplicationError.from_dict(invalidexpirationdate_details_application_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


