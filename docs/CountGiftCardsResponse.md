# CountGiftCardsResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The number of gift cards that match the provided filter. | [optional] 

## Example

```python
from openapi_client.models.count_gift_cards_response import CountGiftCardsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CountGiftCardsResponse from a JSON string
count_gift_cards_response_instance = CountGiftCardsResponse.from_json(json)
# print the JSON string representation of the object
print(CountGiftCardsResponse.to_json())

# convert the object into a dict
count_gift_cards_response_dict = count_gift_cards_response_instance.to_dict()
# create an instance of CountGiftCardsResponse from a dict
count_gift_cards_response_from_dict = CountGiftCardsResponse.from_dict(count_gift_cards_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


