# CreateWalletActionByCustomerReferenceRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_reference** | **object** | CustomerReference of the customer for which to create the wallet action. | [optional] 
**wallet_action** | **object** | WalletAction to be created. | [optional] 
**new_wallet_currency** | **str** | The currency for the new wallet, if no wallet already exists. | [optional] 

## Example

```python
from openapi_client.models.create_wallet_action_by_customer_reference_request import CreateWalletActionByCustomerReferenceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWalletActionByCustomerReferenceRequest from a JSON string
create_wallet_action_by_customer_reference_request_instance = CreateWalletActionByCustomerReferenceRequest.from_json(json)
# print the JSON string representation of the object
print(CreateWalletActionByCustomerReferenceRequest.to_json())

# convert the object into a dict
create_wallet_action_by_customer_reference_request_dict = create_wallet_action_by_customer_reference_request_instance.to_dict()
# create an instance of CreateWalletActionByCustomerReferenceRequest from a dict
create_wallet_action_by_customer_reference_request_from_dict = CreateWalletActionByCustomerReferenceRequest.from_dict(create_wallet_action_by_customer_reference_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


