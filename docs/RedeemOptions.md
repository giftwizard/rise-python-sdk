# RedeemOptions



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | ID of the order associated with the redemption. | [optional] 
**liability** | **bool** | Indicates whether the redemption is a liability. | [optional] 
**total_price** | **str** | Total price of the order. | [optional] 
**order_number** | **str** | Order number associated with the redemption. | [optional] 

## Example

```python
from openapi_client.models.redeem_options import RedeemOptions

# TODO update the JSON string below
json = "{}"
# create an instance of RedeemOptions from a JSON string
redeem_options_instance = RedeemOptions.from_json(json)
# print the JSON string representation of the object
print(RedeemOptions.to_json())

# convert the object into a dict
redeem_options_dict = redeem_options_instance.to_dict()
# create an instance of RedeemOptions from a dict
redeem_options_from_dict = RedeemOptions.from_dict(redeem_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


