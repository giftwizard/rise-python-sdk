# CreateWalletActionByCustomerReferenceResponse1



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_action** | [**WalletAction1**](WalletAction1.md) |  | [optional] 
**wallet** | [**Wallet1**](Wallet1.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_wallet_action_by_customer_reference_response1 import CreateWalletActionByCustomerReferenceResponse1

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWalletActionByCustomerReferenceResponse1 from a JSON string
create_wallet_action_by_customer_reference_response1_instance = CreateWalletActionByCustomerReferenceResponse1.from_json(json)
# print the JSON string representation of the object
print(CreateWalletActionByCustomerReferenceResponse1.to_json())

# convert the object into a dict
create_wallet_action_by_customer_reference_response1_dict = create_wallet_action_by_customer_reference_response1_instance.to_dict()
# create an instance of CreateWalletActionByCustomerReferenceResponse1 from a dict
create_wallet_action_by_customer_reference_response1_from_dict = CreateWalletActionByCustomerReferenceResponse1.from_dict(create_wallet_action_by_customer_reference_response1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


