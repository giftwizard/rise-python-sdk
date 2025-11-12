# RefundableAmount



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_action_id** | **str** |  | [optional] 
**amount** | **str** |  | [optional] 
**funding_transaction_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.refundable_amount import RefundableAmount

# TODO update the JSON string below
json = "{}"
# create an instance of RefundableAmount from a JSON string
refundable_amount_instance = RefundableAmount.from_json(json)
# print the JSON string representation of the object
print(RefundableAmount.to_json())

# convert the object into a dict
refundable_amount_dict = refundable_amount_instance.to_dict()
# create an instance of RefundableAmount from a dict
refundable_amount_from_dict = RefundableAmount.from_dict(refundable_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


