# EXPIRATIONDATEINTHEPASTDetailsApplicationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Error code: EXPIRATION_DATE_IN_THE_PAST | 
**description** | **str** | Error description | 
**data** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.expirationdateinthepast_details_application_error import EXPIRATIONDATEINTHEPASTDetailsApplicationError

# TODO update the JSON string below
json = "{}"
# create an instance of EXPIRATIONDATEINTHEPASTDetailsApplicationError from a JSON string
expirationdateinthepast_details_application_error_instance = EXPIRATIONDATEINTHEPASTDetailsApplicationError.from_json(json)
# print the JSON string representation of the object
print(EXPIRATIONDATEINTHEPASTDetailsApplicationError.to_json())

# convert the object into a dict
expirationdateinthepast_details_application_error_dict = expirationdateinthepast_details_application_error_instance.to_dict()
# create an instance of EXPIRATIONDATEINTHEPASTDetailsApplicationError from a dict
expirationdateinthepast_details_application_error_from_dict = EXPIRATIONDATEINTHEPASTDetailsApplicationError.from_dict(expirationdateinthepast_details_application_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


