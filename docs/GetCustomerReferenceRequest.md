# GetCustomerReferenceRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **object** | Customer Reference query object. | [optional] 

## Example

```python
from openapi_client.models.get_customer_reference_request import GetCustomerReferenceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetCustomerReferenceRequest from a JSON string
get_customer_reference_request_instance = GetCustomerReferenceRequest.from_json(json)
# print the JSON string representation of the object
print(GetCustomerReferenceRequest.to_json())

# convert the object into a dict
get_customer_reference_request_dict = get_customer_reference_request_instance.to_dict()
# create an instance of GetCustomerReferenceRequest from a dict
get_customer_reference_request_from_dict = GetCustomerReferenceRequest.from_dict(get_customer_reference_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


