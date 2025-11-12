# CreateWalletActionByCustomerReferenceResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_action** | **object** | The created WalletAction. | [optional] 
**wallet** | **object** | The wallet to which the wallet action was added. | [optional] 

## Example

```python
from openapi_client.models.create_wallet_action_by_customer_reference_response import CreateWalletActionByCustomerReferenceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWalletActionByCustomerReferenceResponse from a JSON string
create_wallet_action_by_customer_reference_response_instance = CreateWalletActionByCustomerReferenceResponse.from_json(json)
# print the JSON string representation of the object
print(CreateWalletActionByCustomerReferenceResponse.to_json())

# convert the object into a dict
create_wallet_action_by_customer_reference_response_dict = create_wallet_action_by_customer_reference_response_instance.to_dict()
# create an instance of CreateWalletActionByCustomerReferenceResponse from a dict
create_wallet_action_by_customer_reference_response_from_dict = CreateWalletActionByCustomerReferenceResponse.from_dict(create_wallet_action_by_customer_reference_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


