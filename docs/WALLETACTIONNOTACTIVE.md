# WALLETACTIONNOTACTIVE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Error message | 
**details** | [**WALLETACTIONNOTACTIVEDetails**](WALLETACTIONNOTACTIVEDetails.md) |  | 

## Example

```python
from openapi_client.models.walletactionnotactive import WALLETACTIONNOTACTIVE

# TODO update the JSON string below
json = "{}"
# create an instance of WALLETACTIONNOTACTIVE from a JSON string
walletactionnotactive_instance = WALLETACTIONNOTACTIVE.from_json(json)
# print the JSON string representation of the object
print(WALLETACTIONNOTACTIVE.to_json())

# convert the object into a dict
walletactionnotactive_dict = walletactionnotactive_instance.to_dict()
# create an instance of WALLETACTIONNOTACTIVE from a dict
walletactionnotactive_from_dict = WALLETACTIONNOTACTIVE.from_dict(walletactionnotactive_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


