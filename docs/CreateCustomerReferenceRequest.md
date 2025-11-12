# CreateCustomerReferenceRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_reference** | **object** | Customer reference | [optional] 

## Example

```python
from openapi_client.models.create_customer_reference_request import CreateCustomerReferenceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCustomerReferenceRequest from a JSON string
create_customer_reference_request_instance = CreateCustomerReferenceRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCustomerReferenceRequest.to_json())

# convert the object into a dict
create_customer_reference_request_dict = create_customer_reference_request_instance.to_dict()
# create an instance of CreateCustomerReferenceRequest from a dict
create_customer_reference_request_from_dict = CreateCustomerReferenceRequest.from_dict(create_customer_reference_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


