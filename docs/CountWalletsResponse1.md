# CountWalletsResponse1



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of wallets matching the filter. | [optional] 

## Example

```python
from openapi_client.models.count_wallets_response1 import CountWalletsResponse1

# TODO update the JSON string below
json = "{}"
# create an instance of CountWalletsResponse1 from a JSON string
count_wallets_response1_instance = CountWalletsResponse1.from_json(json)
# print the JSON string representation of the object
print(CountWalletsResponse1.to_json())

# convert the object into a dict
count_wallets_response1_dict = count_wallets_response1_instance.to_dict()
# create an instance of CountWalletsResponse1 from a dict
count_wallets_response1_from_dict = CountWalletsResponse1.from_dict(count_wallets_response1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


