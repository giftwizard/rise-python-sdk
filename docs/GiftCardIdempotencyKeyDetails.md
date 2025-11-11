# GiftCardIdempotencyKeyDetails



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**idempotency_key** | **str** | Idempotency Key | [optional] 

## Example

```python
from openapi_client.models.gift_card_idempotency_key_details import GiftCardIdempotencyKeyDetails

# TODO update the JSON string below
json = "{}"
# create an instance of GiftCardIdempotencyKeyDetails from a JSON string
gift_card_idempotency_key_details_instance = GiftCardIdempotencyKeyDetails.from_json(json)
# print the JSON string representation of the object
print(GiftCardIdempotencyKeyDetails.to_json())

# convert the object into a dict
gift_card_idempotency_key_details_dict = gift_card_idempotency_key_details_instance.to_dict()
# create an instance of GiftCardIdempotencyKeyDetails from a dict
gift_card_idempotency_key_details_from_dict = GiftCardIdempotencyKeyDetails.from_dict(gift_card_idempotency_key_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


