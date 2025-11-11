# INSUFFICIENTFUNDSDetailsApplicationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Error code: INSUFFICIENT_FUNDS | 
**description** | **str** | Error description | 
**data** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.insufficientfunds_details_application_error import INSUFFICIENTFUNDSDetailsApplicationError

# TODO update the JSON string below
json = "{}"
# create an instance of INSUFFICIENTFUNDSDetailsApplicationError from a JSON string
insufficientfunds_details_application_error_instance = INSUFFICIENTFUNDSDetailsApplicationError.from_json(json)
# print the JSON string representation of the object
print(INSUFFICIENTFUNDSDetailsApplicationError.to_json())

# convert the object into a dict
insufficientfunds_details_application_error_dict = insufficientfunds_details_application_error_instance.to_dict()
# create an instance of INSUFFICIENTFUNDSDetailsApplicationError from a dict
insufficientfunds_details_application_error_from_dict = INSUFFICIENTFUNDSDetailsApplicationError.from_dict(insufficientfunds_details_application_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


