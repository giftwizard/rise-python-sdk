# SearchGiftCardsResponse1



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gift_cards** | [**List[GiftCard5]**](GiftCard5.md) | Gift Cards which satisfy the provided query. | [optional] 
**paging_metadata** | [**CursorPagingMetadata2**](CursorPagingMetadata2.md) |  | [optional] 
**aggregation_data** | [**AggregationData1**](AggregationData1.md) |  | [optional] 

## Example

```python
from openapi_client.models.search_gift_cards_response1 import SearchGiftCardsResponse1

# TODO update the JSON string below
json = "{}"
# create an instance of SearchGiftCardsResponse1 from a JSON string
search_gift_cards_response1_instance = SearchGiftCardsResponse1.from_json(json)
# print the JSON string representation of the object
print(SearchGiftCardsResponse1.to_json())

# convert the object into a dict
search_gift_cards_response1_dict = search_gift_cards_response1_instance.to_dict()
# create an instance of SearchGiftCardsResponse1 from a dict
search_gift_cards_response1_from_dict = SearchGiftCardsResponse1.from_dict(search_gift_cards_response1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


