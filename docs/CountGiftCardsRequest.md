# CountGiftCardsRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | **object** | [API Query Language](https://platform.rise.ai/docs/#tag/About-API-Query-Language) filter to count gift cards. | [optional] 

## Example

```python
from openapi_client.models.count_gift_cards_request import CountGiftCardsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CountGiftCardsRequest from a JSON string
count_gift_cards_request_instance = CountGiftCardsRequest.from_json(json)
# print the JSON string representation of the object
print(CountGiftCardsRequest.to_json())

# convert the object into a dict
count_gift_cards_request_dict = count_gift_cards_request_instance.to_dict()
# create an instance of CountGiftCardsRequest from a dict
count_gift_cards_request_from_dict = CountGiftCardsRequest.from_dict(count_gift_cards_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


