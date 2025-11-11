# GetCustomerReferenceResponse1



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_reference** | [**CustomerReference2**](CustomerReference2.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_customer_reference_response1 import GetCustomerReferenceResponse1

# TODO update the JSON string below
json = "{}"
# create an instance of GetCustomerReferenceResponse1 from a JSON string
get_customer_reference_response1_instance = GetCustomerReferenceResponse1.from_json(json)
# print the JSON string representation of the object
print(GetCustomerReferenceResponse1.to_json())

# convert the object into a dict
get_customer_reference_response1_dict = get_customer_reference_response1_instance.to_dict()
# create an instance of GetCustomerReferenceResponse1 from a dict
get_customer_reference_response1_from_dict = GetCustomerReferenceResponse1.from_dict(get_customer_reference_response1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


