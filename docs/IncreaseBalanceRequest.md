# IncreaseBalanceRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction** | **object** | The Transaction to be created. | [optional] 

## Example

```python
from openapi_client.models.increase_balance_request import IncreaseBalanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IncreaseBalanceRequest from a JSON string
increase_balance_request_instance = IncreaseBalanceRequest.from_json(json)
# print the JSON string representation of the object
print(IncreaseBalanceRequest.to_json())

# convert the object into a dict
increase_balance_request_dict = increase_balance_request_instance.to_dict()
# create an instance of IncreaseBalanceRequest from a dict
increase_balance_request_from_dict = IncreaseBalanceRequest.from_dict(increase_balance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


