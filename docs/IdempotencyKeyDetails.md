# IdempotencyKeyDetails



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gift_card_id** | **str** | Gift Card Id | [optional] 
**idempotency_key** | **str** | Idempotency Key | [optional] 

## Example

```python
from openapi_client.models.idempotency_key_details import IdempotencyKeyDetails

# TODO update the JSON string below
json = "{}"
# create an instance of IdempotencyKeyDetails from a JSON string
idempotency_key_details_instance = IdempotencyKeyDetails.from_json(json)
# print the JSON string representation of the object
print(IdempotencyKeyDetails.to_json())

# convert the object into a dict
idempotency_key_details_dict = idempotency_key_details_instance.to_dict()
# create an instance of IdempotencyKeyDetails from a dict
idempotency_key_details_from_dict = IdempotencyKeyDetails.from_dict(idempotency_key_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


