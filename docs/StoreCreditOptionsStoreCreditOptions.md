# StoreCreditOptionsStoreCreditOptions

Detailed information about a Gift Card that belongs to a Store Credit Wallet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_id** | **str** | ID of the store credit wallet. | [optional] 

## Example

```python
from openapi_client.models.store_credit_options_store_credit_options import StoreCreditOptionsStoreCreditOptions

# TODO update the JSON string below
json = "{}"
# create an instance of StoreCreditOptionsStoreCreditOptions from a JSON string
store_credit_options_store_credit_options_instance = StoreCreditOptionsStoreCreditOptions.from_json(json)
# print the JSON string representation of the object
print(StoreCreditOptionsStoreCreditOptions.to_json())

# convert the object into a dict
store_credit_options_store_credit_options_dict = store_credit_options_store_credit_options_instance.to_dict()
# create an instance of StoreCreditOptionsStoreCreditOptions from a dict
store_credit_options_store_credit_options_from_dict = StoreCreditOptionsStoreCreditOptions.from_dict(store_credit_options_store_credit_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


