# AddCustomerReferenceRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_reference** | **object** | Customer reference | [optional] 
**wallet_id** | **str** | Wallet ID | [optional] 

## Example

```python
from openapi_client.models.add_customer_reference_request import AddCustomerReferenceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddCustomerReferenceRequest from a JSON string
add_customer_reference_request_instance = AddCustomerReferenceRequest.from_json(json)
# print the JSON string representation of the object
print(AddCustomerReferenceRequest.to_json())

# convert the object into a dict
add_customer_reference_request_dict = add_customer_reference_request_instance.to_dict()
# create an instance of AddCustomerReferenceRequest from a dict
add_customer_reference_request_from_dict = AddCustomerReferenceRequest.from_dict(add_customer_reference_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


