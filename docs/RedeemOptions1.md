# RedeemOptions1

Information about a transaction whose source is a gift card redemption.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redeem_options** | [**RedeemOptions1**](RedeemOptions1.md) |  | [optional] 

## Example

```python
from openapi_client.models.redeem_options1 import RedeemOptions1

# TODO update the JSON string below
json = "{}"
# create an instance of RedeemOptions1 from a JSON string
redeem_options1_instance = RedeemOptions1.from_json(json)
# print the JSON string representation of the object
print(RedeemOptions1.to_json())

# convert the object into a dict
redeem_options1_dict = redeem_options1_instance.to_dict()
# create an instance of RedeemOptions1 from a dict
redeem_options1_from_dict = RedeemOptions1.from_dict(redeem_options1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


