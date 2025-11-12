# QueryGiftCardsResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gift_cards** | **List[object]** | The retrieved GiftCards. | [optional] 
**paging_metadata** | **object** | Response paging metadata. | [optional] 

## Example

```python
from openapi_client.models.query_gift_cards_response import QueryGiftCardsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QueryGiftCardsResponse from a JSON string
query_gift_cards_response_instance = QueryGiftCardsResponse.from_json(json)
# print the JSON string representation of the object
print(QueryGiftCardsResponse.to_json())

# convert the object into a dict
query_gift_cards_response_dict = query_gift_cards_response_instance.to_dict()
# create an instance of QueryGiftCardsResponse from a dict
query_gift_cards_response_from_dict = QueryGiftCardsResponse.from_dict(query_gift_cards_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


