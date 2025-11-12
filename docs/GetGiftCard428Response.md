# GetGiftCard428Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Error message | 
**details** | [**GIFTCARDEXPIREDDetails**](GIFTCARDEXPIREDDetails.md) |  | 

## Example

```python
from openapi_client.models.get_gift_card428_response import GetGiftCard428Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetGiftCard428Response from a JSON string
get_gift_card428_response_instance = GetGiftCard428Response.from_json(json)
# print the JSON string representation of the object
print(GetGiftCard428Response.to_json())

# convert the object into a dict
get_gift_card428_response_dict = get_gift_card428_response_instance.to_dict()
# create an instance of GetGiftCard428Response from a dict
get_gift_card428_response_from_dict = GetGiftCard428Response.from_dict(get_gift_card428_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


