# WALLETACTIONEXCEEDSMAXIMUMBALANCE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Error message | 
**details** | [**WALLETACTIONEXCEEDSMAXIMUMBALANCEDetails**](WALLETACTIONEXCEEDSMAXIMUMBALANCEDetails.md) |  | 

## Example

```python
from openapi_client.models.walletactionexceedsmaximumbalance import WALLETACTIONEXCEEDSMAXIMUMBALANCE

# TODO update the JSON string below
json = "{}"
# create an instance of WALLETACTIONEXCEEDSMAXIMUMBALANCE from a JSON string
walletactionexceedsmaximumbalance_instance = WALLETACTIONEXCEEDSMAXIMUMBALANCE.from_json(json)
# print the JSON string representation of the object
print(WALLETACTIONEXCEEDSMAXIMUMBALANCE.to_json())

# convert the object into a dict
walletactionexceedsmaximumbalance_dict = walletactionexceedsmaximumbalance_instance.to_dict()
# create an instance of WALLETACTIONEXCEEDSMAXIMUMBALANCE from a dict
walletactionexceedsmaximumbalance_from_dict = WALLETACTIONEXCEEDSMAXIMUMBALANCE.from_dict(walletactionexceedsmaximumbalance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


