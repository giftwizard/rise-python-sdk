# InsufficientFundsDetails



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gift_card_id** | **str** | Gift Card Id | [optional] 
**balance** | **str** | Gift Card Balance | [optional] 
**amount** | **str** | Transaction amount | [optional] 

## Example

```python
from openapi_client.models.insufficient_funds_details import InsufficientFundsDetails

# TODO update the JSON string below
json = "{}"
# create an instance of InsufficientFundsDetails from a JSON string
insufficient_funds_details_instance = InsufficientFundsDetails.from_json(json)
# print the JSON string representation of the object
print(InsufficientFundsDetails.to_json())

# convert the object into a dict
insufficient_funds_details_dict = insufficient_funds_details_instance.to_dict()
# create an instance of InsufficientFundsDetails from a dict
insufficient_funds_details_from_dict = InsufficientFundsDetails.from_dict(insufficient_funds_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


