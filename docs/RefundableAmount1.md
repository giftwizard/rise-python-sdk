# RefundableAmount1



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_action_id** | **str** |  | [optional] 
**amount** | **str** |  | [optional] 
**funding_transaction_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.refundable_amount1 import RefundableAmount1

# TODO update the JSON string below
json = "{}"
# create an instance of RefundableAmount1 from a JSON string
refundable_amount1_instance = RefundableAmount1.from_json(json)
# print the JSON string representation of the object
print(RefundableAmount1.to_json())

# convert the object into a dict
refundable_amount1_dict = refundable_amount1_instance.to_dict()
# create an instance of RefundableAmount1 from a dict
refundable_amount1_from_dict = RefundableAmount1.from_dict(refundable_amount1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


