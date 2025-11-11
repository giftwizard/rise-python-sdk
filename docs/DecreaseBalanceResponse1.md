# DecreaseBalanceResponse1



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction** | [**Transaction2**](Transaction2.md) |  | [optional] 
**balance** | **str** | GiftCard balance after Transaction. | [optional] 
**currency** | **str** | Transaction Currency. | [optional] 

## Example

```python
from openapi_client.models.decrease_balance_response1 import DecreaseBalanceResponse1

# TODO update the JSON string below
json = "{}"
# create an instance of DecreaseBalanceResponse1 from a JSON string
decrease_balance_response1_instance = DecreaseBalanceResponse1.from_json(json)
# print the JSON string representation of the object
print(DecreaseBalanceResponse1.to_json())

# convert the object into a dict
decrease_balance_response1_dict = decrease_balance_response1_instance.to_dict()
# create an instance of DecreaseBalanceResponse1 from a dict
decrease_balance_response1_from_dict = DecreaseBalanceResponse1.from_dict(decrease_balance_response1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


