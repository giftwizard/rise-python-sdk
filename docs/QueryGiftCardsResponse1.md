# QueryGiftCardsResponse1



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gift_cards** | [**List[GiftCard5]**](GiftCard5.md) | The retrieved GiftCards. | [optional] 
**paging_metadata** | [**PagingMetadataV23**](PagingMetadataV23.md) |  | [optional] 

## Example

```python
from openapi_client.models.query_gift_cards_response1 import QueryGiftCardsResponse1

# TODO update the JSON string below
json = "{}"
# create an instance of QueryGiftCardsResponse1 from a JSON string
query_gift_cards_response1_instance = QueryGiftCardsResponse1.from_json(json)
# print the JSON string representation of the object
print(QueryGiftCardsResponse1.to_json())

# convert the object into a dict
query_gift_cards_response1_dict = query_gift_cards_response1_instance.to_dict()
# create an instance of QueryGiftCardsResponse1 from a dict
query_gift_cards_response1_from_dict = QueryGiftCardsResponse1.from_dict(query_gift_cards_response1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


