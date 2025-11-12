# SearchGiftCardsResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gift_cards** | **List[object]** | Gift Cards which satisfy the provided query. | [optional] 
**paging_metadata** | **object** | Paging metadata. Contains cursor which can be used in next query. | [optional] 
**aggregation_data** | **object** | Aggregation data. | [optional] 

## Example

```python
from openapi_client.models.search_gift_cards_response import SearchGiftCardsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SearchGiftCardsResponse from a JSON string
search_gift_cards_response_instance = SearchGiftCardsResponse.from_json(json)
# print the JSON string representation of the object
print(SearchGiftCardsResponse.to_json())

# convert the object into a dict
search_gift_cards_response_dict = search_gift_cards_response_instance.to_dict()
# create an instance of SearchGiftCardsResponse from a dict
search_gift_cards_response_from_dict = SearchGiftCardsResponse.from_dict(search_gift_cards_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


