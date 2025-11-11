# InvalidGiftCardBalanceDetails



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gift_card_id** | **str** | Gift Card Id | [optional] 
**current_balance** | **str** | Current Gift Card balance | [optional] 
**max_balance** | **str** | Max balance allowed | [optional] 
**invalid_balance** | **str** | Attempted invalid balance | [optional] 

## Example

```python
from openapi_client.models.invalid_gift_card_balance_details import InvalidGiftCardBalanceDetails

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidGiftCardBalanceDetails from a JSON string
invalid_gift_card_balance_details_instance = InvalidGiftCardBalanceDetails.from_json(json)
# print the JSON string representation of the object
print(InvalidGiftCardBalanceDetails.to_json())

# convert the object into a dict
invalid_gift_card_balance_details_dict = invalid_gift_card_balance_details_instance.to_dict()
# create an instance of InvalidGiftCardBalanceDetails from a dict
invalid_gift_card_balance_details_from_dict = InvalidGiftCardBalanceDetails.from_dict(invalid_gift_card_balance_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


