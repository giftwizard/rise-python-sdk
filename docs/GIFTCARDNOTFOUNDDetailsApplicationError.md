# GIFTCARDNOTFOUNDDetailsApplicationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Error code: GIFT_CARD_NOT_FOUND | 
**description** | **str** | Error description | 
**data** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.giftcardnotfound_details_application_error import GIFTCARDNOTFOUNDDetailsApplicationError

# TODO update the JSON string below
json = "{}"
# create an instance of GIFTCARDNOTFOUNDDetailsApplicationError from a JSON string
giftcardnotfound_details_application_error_instance = GIFTCARDNOTFOUNDDetailsApplicationError.from_json(json)
# print the JSON string representation of the object
print(GIFTCARDNOTFOUNDDetailsApplicationError.to_json())

# convert the object into a dict
giftcardnotfound_details_application_error_dict = giftcardnotfound_details_application_error_instance.to_dict()
# create an instance of GIFTCARDNOTFOUNDDetailsApplicationError from a dict
giftcardnotfound_details_application_error_from_dict = GIFTCARDNOTFOUNDDetailsApplicationError.from_dict(giftcardnotfound_details_application_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


