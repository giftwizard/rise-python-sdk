# CustomerReference5

The customer reference with which to create or retrieve the wallet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_channel_id** | **str** | Source channel, i.e. Shopify. | 
**source_tenant_id** | **str** | Tenant ID in Source, i.e. shop ID. | 
**source_customer_id** | **str** | Customer ID in Source. | 
**first_name** | **str** | First name. | [optional] 
**last_name** | **str** | Last name. | [optional] 
**phone** | **str** | Phone number. | [optional] 
**email** | **str** | Email address. | 

## Example

```python
from openapi_client.models.customer_reference5 import CustomerReference5

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerReference5 from a JSON string
customer_reference5_instance = CustomerReference5.from_json(json)
# print the JSON string representation of the object
print(CustomerReference5.to_json())

# convert the object into a dict
customer_reference5_dict = customer_reference5_instance.to_dict()
# create an instance of CustomerReference5 from a dict
customer_reference5_from_dict = CustomerReference5.from_dict(customer_reference5_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


