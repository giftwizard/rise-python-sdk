# CreateGiftCardRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gift_card** | **object** | The GiftCard to create. | [optional] 

## Example

```python
from openapi_client.models.create_gift_card_request import CreateGiftCardRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGiftCardRequest from a JSON string
create_gift_card_request_instance = CreateGiftCardRequest.from_json(json)
# print the JSON string representation of the object
print(CreateGiftCardRequest.to_json())

# convert the object into a dict
create_gift_card_request_dict = create_gift_card_request_instance.to_dict()
# create an instance of CreateGiftCardRequest from a dict
create_gift_card_request_from_dict = CreateGiftCardRequest.from_dict(create_gift_card_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


