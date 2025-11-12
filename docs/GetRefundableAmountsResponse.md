# GetRefundableAmountsResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amounts** | **List[object]** |  | [optional] 

## Example

```python
from openapi_client.models.get_refundable_amounts_response import GetRefundableAmountsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetRefundableAmountsResponse from a JSON string
get_refundable_amounts_response_instance = GetRefundableAmountsResponse.from_json(json)
# print the JSON string representation of the object
print(GetRefundableAmountsResponse.to_json())

# convert the object into a dict
get_refundable_amounts_response_dict = get_refundable_amounts_response_instance.to_dict()
# create an instance of GetRefundableAmountsResponse from a dict
get_refundable_amounts_response_from_dict = GetRefundableAmountsResponse.from_dict(get_refundable_amounts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


