# QueryGiftCardsRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **object** | API Query Language expression. | [optional] 

## Example

```python
from openapi_client.models.query_gift_cards_request import QueryGiftCardsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QueryGiftCardsRequest from a JSON string
query_gift_cards_request_instance = QueryGiftCardsRequest.from_json(json)
# print the JSON string representation of the object
print(QueryGiftCardsRequest.to_json())

# convert the object into a dict
query_gift_cards_request_dict = query_gift_cards_request_instance.to_dict()
# create an instance of QueryGiftCardsRequest from a dict
query_gift_cards_request_from_dict = QueryGiftCardsRequest.from_dict(query_gift_cards_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


