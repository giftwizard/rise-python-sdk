# GIFTCARDEXPIREDDetailsApplicationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Error code: GIFT_CARD_EXPIRED | 
**description** | **str** | Error description | 
**data** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.giftcardexpired_details_application_error import GIFTCARDEXPIREDDetailsApplicationError

# TODO update the JSON string below
json = "{}"
# create an instance of GIFTCARDEXPIREDDetailsApplicationError from a JSON string
giftcardexpired_details_application_error_instance = GIFTCARDEXPIREDDetailsApplicationError.from_json(json)
# print the JSON string representation of the object
print(GIFTCARDEXPIREDDetailsApplicationError.to_json())

# convert the object into a dict
giftcardexpired_details_application_error_dict = giftcardexpired_details_application_error_instance.to_dict()
# create an instance of GIFTCARDEXPIREDDetailsApplicationError from a dict
giftcardexpired_details_application_error_from_dict = GIFTCARDEXPIREDDetailsApplicationError.from_dict(giftcardexpired_details_application_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


