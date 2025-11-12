# IncreaseBalanceResponse1



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction** | [**Transaction2**](Transaction2.md) |  | [optional] 
**balance** | **str** | GiftCard balance after transaction. | [optional] 
**currency** | **str** | Transaction Currency. | [optional] 

## Example

```python
from openapi_client.models.increase_balance_response1 import IncreaseBalanceResponse1

# TODO update the JSON string below
json = "{}"
# create an instance of IncreaseBalanceResponse1 from a JSON string
increase_balance_response1_instance = IncreaseBalanceResponse1.from_json(json)
# print the JSON string representation of the object
print(IncreaseBalanceResponse1.to_json())

# convert the object into a dict
increase_balance_response1_dict = increase_balance_response1_instance.to_dict()
# create an instance of IncreaseBalanceResponse1 from a dict
increase_balance_response1_from_dict = IncreaseBalanceResponse1.from_dict(increase_balance_response1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


