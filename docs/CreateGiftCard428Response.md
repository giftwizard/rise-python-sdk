# CreateGiftCard428Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Error message | 
**details** | [**EXISTINGIDEMPOTENCYKEYDetails**](EXISTINGIDEMPOTENCYKEYDetails.md) |  | 

## Example

```python
from openapi_client.models.create_gift_card428_response import CreateGiftCard428Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGiftCard428Response from a JSON string
create_gift_card428_response_instance = CreateGiftCard428Response.from_json(json)
# print the JSON string representation of the object
print(CreateGiftCard428Response.to_json())

# convert the object into a dict
create_gift_card428_response_dict = create_gift_card428_response_instance.to_dict()
# create an instance of CreateGiftCard428Response from a dict
create_gift_card428_response_from_dict = CreateGiftCard428Response.from_dict(create_gift_card428_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


