# CustomerReference2

Retrieved Customer reference.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_channel_id** | **str** | Source channel, i.e. Shopify. | [optional] 
**source_tenant_id** | **str** | Tenant ID in Source, i.e. shop ID. | [optional] 
**source_customer_id** | **str** | Customer ID in Source. | [optional] 
**first_name** | **str** | First name. | [optional] 
**last_name** | **str** | Last name. | [optional] 
**phone** | **str** | Phone number. | [optional] 
**email** | **str** | Email address. | [optional] 

## Example

```python
from openapi_client.models.customer_reference2 import CustomerReference2

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerReference2 from a JSON string
customer_reference2_instance = CustomerReference2.from_json(json)
# print the JSON string representation of the object
print(CustomerReference2.to_json())

# convert the object into a dict
customer_reference2_dict = customer_reference2_instance.to_dict()
# create an instance of CustomerReference2 from a dict
customer_reference2_from_dict = CustomerReference2.from_dict(customer_reference2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


