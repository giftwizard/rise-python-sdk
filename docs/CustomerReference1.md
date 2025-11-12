# CustomerReference1

A reference to a customer in a specific source channel, containing the channel, tenant, and customer ID of the customer in that source, as well as the customer's first name, last name, phone number, and email address.

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
from openapi_client.models.customer_reference1 import CustomerReference1

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerReference1 from a JSON string
customer_reference1_instance = CustomerReference1.from_json(json)
# print the JSON string representation of the object
print(CustomerReference1.to_json())

# convert the object into a dict
customer_reference1_dict = customer_reference1_instance.to_dict()
# create an instance of CustomerReference1 from a dict
customer_reference1_from_dict = CustomerReference1.from_dict(customer_reference1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


