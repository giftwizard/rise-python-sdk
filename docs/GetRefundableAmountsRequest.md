# GetRefundableAmountsRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | ID of the transaction to get refundable amounts for | [optional] 

## Example

```python
from openapi_client.models.get_refundable_amounts_request import GetRefundableAmountsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetRefundableAmountsRequest from a JSON string
get_refundable_amounts_request_instance = GetRefundableAmountsRequest.from_json(json)
# print the JSON string representation of the object
print(GetRefundableAmountsRequest.to_json())

# convert the object into a dict
get_refundable_amounts_request_dict = get_refundable_amounts_request_instance.to_dict()
# create an instance of GetRefundableAmountsRequest from a dict
get_refundable_amounts_request_from_dict = GetRefundableAmountsRequest.from_dict(get_refundable_amounts_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


