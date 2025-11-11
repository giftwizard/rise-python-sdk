# CountWalletsRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | **object** | Filter by which to count wallets. | [optional] 

## Example

```python
from openapi_client.models.count_wallets_request import CountWalletsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CountWalletsRequest from a JSON string
count_wallets_request_instance = CountWalletsRequest.from_json(json)
# print the JSON string representation of the object
print(CountWalletsRequest.to_json())

# convert the object into a dict
count_wallets_request_dict = count_wallets_request_instance.to_dict()
# create an instance of CountWalletsRequest from a dict
count_wallets_request_from_dict = CountWalletsRequest.from_dict(count_wallets_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


