# CountWalletsResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of wallets matching the filter. | [optional] 

## Example

```python
from openapi_client.models.count_wallets_response import CountWalletsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CountWalletsResponse from a JSON string
count_wallets_response_instance = CountWalletsResponse.from_json(json)
# print the JSON string representation of the object
print(CountWalletsResponse.to_json())

# convert the object into a dict
count_wallets_response_dict = count_wallets_response_instance.to_dict()
# create an instance of CountWalletsResponse from a dict
count_wallets_response_from_dict = CountWalletsResponse.from_dict(count_wallets_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


