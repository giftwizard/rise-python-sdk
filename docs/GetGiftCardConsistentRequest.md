# GetGiftCardConsistentRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gift_card_id** | **str** | The ID of the GiftCard to retrieve. | [optional] 

## Example

```python
from openapi_client.models.get_gift_card_consistent_request import GetGiftCardConsistentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetGiftCardConsistentRequest from a JSON string
get_gift_card_consistent_request_instance = GetGiftCardConsistentRequest.from_json(json)
# print the JSON string representation of the object
print(GetGiftCardConsistentRequest.to_json())

# convert the object into a dict
get_gift_card_consistent_request_dict = get_gift_card_consistent_request_instance.to_dict()
# create an instance of GetGiftCardConsistentRequest from a dict
get_gift_card_consistent_request_from_dict = GetGiftCardConsistentRequest.from_dict(get_gift_card_consistent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


