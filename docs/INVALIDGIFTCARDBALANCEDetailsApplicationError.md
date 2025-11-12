# INVALIDGIFTCARDBALANCEDetailsApplicationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Error code: INVALID_GIFT_CARD_BALANCE | 
**description** | **str** | Error description | 
**data** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.invalidgiftcardbalance_details_application_error import INVALIDGIFTCARDBALANCEDetailsApplicationError

# TODO update the JSON string below
json = "{}"
# create an instance of INVALIDGIFTCARDBALANCEDetailsApplicationError from a JSON string
invalidgiftcardbalance_details_application_error_instance = INVALIDGIFTCARDBALANCEDetailsApplicationError.from_json(json)
# print the JSON string representation of the object
print(INVALIDGIFTCARDBALANCEDetailsApplicationError.to_json())

# convert the object into a dict
invalidgiftcardbalance_details_application_error_dict = invalidgiftcardbalance_details_application_error_instance.to_dict()
# create an instance of INVALIDGIFTCARDBALANCEDetailsApplicationError from a dict
invalidgiftcardbalance_details_application_error_from_dict = INVALIDGIFTCARDBALANCEDetailsApplicationError.from_dict(invalidgiftcardbalance_details_application_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


