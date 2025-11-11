# CustomerReferenceQuery



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_reference_source** | **object** | CustomerReference source (i.e. source channel, tenant, and customer IDs) | [optional] 

## Example

```python
from openapi_client.models.customer_reference_query import CustomerReferenceQuery

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerReferenceQuery from a JSON string
customer_reference_query_instance = CustomerReferenceQuery.from_json(json)
# print the JSON string representation of the object
print(CustomerReferenceQuery.to_json())

# convert the object into a dict
customer_reference_query_dict = customer_reference_query_instance.to_dict()
# create an instance of CustomerReferenceQuery from a dict
customer_reference_query_from_dict = CustomerReferenceQuery.from_dict(customer_reference_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


