# StoreCreditContext



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issuer** | **str** | The issuer type of the store credit (e.g., workflow, bulk, manual) | [optional] 
**issuer_id** | **str** | Indicates a specific instance of the issuer (relevant for workflow/bulk) | [optional] 
**note** | **str** | An internal note associated with the store credit | [optional] 
**source_channel_id** | **str** | The Channel ID of the sales channel that is associated with the store credit (e.g. Shopify channel id) | [optional] 
**source_tenant_id** | **str** | The Tenant ID of the sales channel that is associated with the store credit (e.g. Shopify shop id) | [optional] 

## Example

```python
from openapi_client.models.store_credit_context import StoreCreditContext

# TODO update the JSON string below
json = "{}"
# create an instance of StoreCreditContext from a JSON string
store_credit_context_instance = StoreCreditContext.from_json(json)
# print the JSON string representation of the object
print(StoreCreditContext.to_json())

# convert the object into a dict
store_credit_context_dict = store_credit_context_instance.to_dict()
# create an instance of StoreCreditContext from a dict
store_credit_context_from_dict = StoreCreditContext.from_dict(store_credit_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


