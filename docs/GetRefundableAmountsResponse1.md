# GetRefundableAmountsResponse1



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amounts** | [**List[RefundableAmount1]**](RefundableAmount1.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_refundable_amounts_response1 import GetRefundableAmountsResponse1

# TODO update the JSON string below
json = "{}"
# create an instance of GetRefundableAmountsResponse1 from a JSON string
get_refundable_amounts_response1_instance = GetRefundableAmountsResponse1.from_json(json)
# print the JSON string representation of the object
print(GetRefundableAmountsResponse1.to_json())

# convert the object into a dict
get_refundable_amounts_response1_dict = get_refundable_amounts_response1_instance.to_dict()
# create an instance of GetRefundableAmountsResponse1 from a dict
get_refundable_amounts_response1_from_dict = GetRefundableAmountsResponse1.from_dict(get_refundable_amounts_response1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


