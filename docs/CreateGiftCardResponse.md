# CreateGiftCardResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gift_card** | **object** | The created GiftCard. | [optional] 

## Example

```python
from openapi_client.models.create_gift_card_response import CreateGiftCardResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGiftCardResponse from a JSON string
create_gift_card_response_instance = CreateGiftCardResponse.from_json(json)
# print the JSON string representation of the object
print(CreateGiftCardResponse.to_json())

# convert the object into a dict
create_gift_card_response_dict = create_gift_card_response_instance.to_dict()
# create an instance of CreateGiftCardResponse from a dict
create_gift_card_response_from_dict = CreateGiftCardResponse.from_dict(create_gift_card_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


