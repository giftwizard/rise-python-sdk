# GetCustomerReferenceResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_reference** | [**CustomerReference2**](CustomerReference2.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_customer_reference_response import GetCustomerReferenceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCustomerReferenceResponse from a JSON string
get_customer_reference_response_instance = GetCustomerReferenceResponse.from_json(json)
# print the JSON string representation of the object
print(GetCustomerReferenceResponse.to_json())

# convert the object into a dict
get_customer_reference_response_dict = get_customer_reference_response_instance.to_dict()
# create an instance of GetCustomerReferenceResponse from a dict
get_customer_reference_response_from_dict = GetCustomerReferenceResponse.from_dict(get_customer_reference_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


