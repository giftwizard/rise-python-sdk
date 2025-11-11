# DisableGiftCardRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gift_card_id** | **str** | The ID of the GiftCard to disable. | [optional] 

## Example

```python
from openapi_client.models.disable_gift_card_request import DisableGiftCardRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DisableGiftCardRequest from a JSON string
disable_gift_card_request_instance = DisableGiftCardRequest.from_json(json)
# print the JSON string representation of the object
print(DisableGiftCardRequest.to_json())

# convert the object into a dict
disable_gift_card_request_dict = disable_gift_card_request_instance.to_dict()
# create an instance of DisableGiftCardRequest from a dict
disable_gift_card_request_from_dict = DisableGiftCardRequest.from_dict(disable_gift_card_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


