# GetGiftCardRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gift_card_id** | **str** | The ID of the GiftCard to retrieve. | [optional] 

## Example

```python
from openapi_client.models.get_gift_card_request import GetGiftCardRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetGiftCardRequest from a JSON string
get_gift_card_request_instance = GetGiftCardRequest.from_json(json)
# print the JSON string representation of the object
print(GetGiftCardRequest.to_json())

# convert the object into a dict
get_gift_card_request_dict = get_gift_card_request_instance.to_dict()
# create an instance of GetGiftCardRequest from a dict
get_gift_card_request_from_dict = GetGiftCardRequest.from_dict(get_gift_card_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


