# INVALIDCODEDetailsApplicationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Error code: INVALID_CODE | 
**description** | **str** | Error description | 
**data** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.invalidcode_details_application_error import INVALIDCODEDetailsApplicationError

# TODO update the JSON string below
json = "{}"
# create an instance of INVALIDCODEDetailsApplicationError from a JSON string
invalidcode_details_application_error_instance = INVALIDCODEDetailsApplicationError.from_json(json)
# print the JSON string representation of the object
print(INVALIDCODEDetailsApplicationError.to_json())

# convert the object into a dict
invalidcode_details_application_error_dict = invalidcode_details_application_error_instance.to_dict()
# create an instance of INVALIDCODEDetailsApplicationError from a dict
invalidcode_details_application_error_from_dict = INVALIDCODEDetailsApplicationError.from_dict(invalidcode_details_application_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


