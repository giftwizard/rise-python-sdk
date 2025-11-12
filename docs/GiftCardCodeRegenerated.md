# GiftCardCodeRegenerated



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**previous_code** | **str** | previous gift card full code (pii) | [optional] 
**previous_code_suffix** | **str** | the previous code suffix of the gift card | [optional] 
**gift_card** | **object** | updated gift card | [optional] 

## Example

```python
from openapi_client.models.gift_card_code_regenerated import GiftCardCodeRegenerated

# TODO update the JSON string below
json = "{}"
# create an instance of GiftCardCodeRegenerated from a JSON string
gift_card_code_regenerated_instance = GiftCardCodeRegenerated.from_json(json)
# print the JSON string representation of the object
print(GiftCardCodeRegenerated.to_json())

# convert the object into a dict
gift_card_code_regenerated_dict = gift_card_code_regenerated_instance.to_dict()
# create an instance of GiftCardCodeRegenerated from a dict
gift_card_code_regenerated_from_dict = GiftCardCodeRegenerated.from_dict(gift_card_code_regenerated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


