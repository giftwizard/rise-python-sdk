# CustomerReference4

Initial Customer Reference for the wallet.

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
from openapi_client.models.customer_reference4 import CustomerReference4

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerReference4 from a JSON string
customer_reference4_instance = CustomerReference4.from_json(json)
# print the JSON string representation of the object
print(CustomerReference4.to_json())

# convert the object into a dict
customer_reference4_dict = customer_reference4_instance.to_dict()
# create an instance of CustomerReference4 from a dict
customer_reference4_from_dict = CustomerReference4.from_dict(customer_reference4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


