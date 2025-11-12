# BulkDeleteGiftCardsByFilterRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **object** | WQL expression | [optional] 
**meta_site_id** | **str** | MSID from which to delete the gift cards | [optional] 
**expected_amount** | **int** | Expected gift card amount to delete | [optional] 

## Example

```python
from openapi_client.models.bulk_delete_gift_cards_by_filter_request import BulkDeleteGiftCardsByFilterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkDeleteGiftCardsByFilterRequest from a JSON string
bulk_delete_gift_cards_by_filter_request_instance = BulkDeleteGiftCardsByFilterRequest.from_json(json)
# print the JSON string representation of the object
print(BulkDeleteGiftCardsByFilterRequest.to_json())

# convert the object into a dict
bulk_delete_gift_cards_by_filter_request_dict = bulk_delete_gift_cards_by_filter_request_instance.to_dict()
# create an instance of BulkDeleteGiftCardsByFilterRequest from a dict
bulk_delete_gift_cards_by_filter_request_from_dict = BulkDeleteGiftCardsByFilterRequest.from_dict(bulk_delete_gift_cards_by_filter_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


