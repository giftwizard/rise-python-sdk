# REQUIREDPROPERTYDetailsApplicationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Error code: REQUIRED_PROPERTY | 
**description** | **str** | Error description | 
**data** | **object** | Error specific data | [optional] 

## Example

```python
from openapi_client.models.requiredproperty_details_application_error import REQUIREDPROPERTYDetailsApplicationError

# TODO update the JSON string below
json = "{}"
# create an instance of REQUIREDPROPERTYDetailsApplicationError from a JSON string
requiredproperty_details_application_error_instance = REQUIREDPROPERTYDetailsApplicationError.from_json(json)
# print the JSON string representation of the object
print(REQUIREDPROPERTYDetailsApplicationError.to_json())

# convert the object into a dict
requiredproperty_details_application_error_dict = requiredproperty_details_application_error_instance.to_dict()
# create an instance of REQUIREDPROPERTYDetailsApplicationError from a dict
requiredproperty_details_application_error_from_dict = REQUIREDPROPERTYDetailsApplicationError.from_dict(requiredproperty_details_application_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


