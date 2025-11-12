# IncreaseBalanceResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction** | **object** | The created Transaction. | [optional] 
**balance** | **str** | GiftCard balance after transaction. | [optional] 
**currency** | **str** | Transaction Currency. | [optional] 

## Example

```python
from openapi_client.models.increase_balance_response import IncreaseBalanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IncreaseBalanceResponse from a JSON string
increase_balance_response_instance = IncreaseBalanceResponse.from_json(json)
# print the JSON string representation of the object
print(IncreaseBalanceResponse.to_json())

# convert the object into a dict
increase_balance_response_dict = increase_balance_response_instance.to_dict()
# create an instance of IncreaseBalanceResponse from a dict
increase_balance_response_from_dict = IncreaseBalanceResponse.from_dict(increase_balance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


