# DeleteCustomerReferenceRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **object** | Query by customer reference source (i.e. source channel, tenant, and customer IDs) | [optional] 

## Example

```python
from openapi_client.models.delete_customer_reference_request import DeleteCustomerReferenceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteCustomerReferenceRequest from a JSON string
delete_customer_reference_request_instance = DeleteCustomerReferenceRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteCustomerReferenceRequest.to_json())

# convert the object into a dict
delete_customer_reference_request_dict = delete_customer_reference_request_instance.to_dict()
# create an instance of DeleteCustomerReferenceRequest from a dict
delete_customer_reference_request_from_dict = DeleteCustomerReferenceRequest.from_dict(delete_customer_reference_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


