# DecreaseBalanceRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction** | **object** | The Transaction to be created. | [optional] 

## Example

```python
from openapi_client.models.decrease_balance_request import DecreaseBalanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DecreaseBalanceRequest from a JSON string
decrease_balance_request_instance = DecreaseBalanceRequest.from_json(json)
# print the JSON string representation of the object
print(DecreaseBalanceRequest.to_json())

# convert the object into a dict
decrease_balance_request_dict = decrease_balance_request_instance.to_dict()
# create an instance of DecreaseBalanceRequest from a dict
decrease_balance_request_from_dict = DecreaseBalanceRequest.from_dict(decrease_balance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


