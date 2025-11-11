# WALLETACTIONNOTACTIVEDetailsApplicationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Error code: WALLET_ACTION_NOT_ACTIVE | 
**description** | **str** | Error description | 
**data** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.walletactionnotactive_details_application_error import WALLETACTIONNOTACTIVEDetailsApplicationError

# TODO update the JSON string below
json = "{}"
# create an instance of WALLETACTIONNOTACTIVEDetailsApplicationError from a JSON string
walletactionnotactive_details_application_error_instance = WALLETACTIONNOTACTIVEDetailsApplicationError.from_json(json)
# print the JSON string representation of the object
print(WALLETACTIONNOTACTIVEDetailsApplicationError.to_json())

# convert the object into a dict
walletactionnotactive_details_application_error_dict = walletactionnotactive_details_application_error_instance.to_dict()
# create an instance of WALLETACTIONNOTACTIVEDetailsApplicationError from a dict
walletactionnotactive_details_application_error_from_dict = WALLETACTIONNOTACTIVEDetailsApplicationError.from_dict(walletactionnotactive_details_application_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


