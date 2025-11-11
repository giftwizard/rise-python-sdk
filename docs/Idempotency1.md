# Idempotency1

Idempotency information for the event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | A unique identifier for the event. If you send the same idempotency key in multiple report event requests, for the same trigger key and app id, consecutive requests will be ignored after the first one. Note that the idempotency key is kept for a week before it expires. | [optional] 
**ttl_in_milliseconds** | **str** | Optional. The time to live (TTL) in milliseconds before the key will expire. Default is a week. | [optional] 

## Example

```python
from openapi_client.models.idempotency1 import Idempotency1

# TODO update the JSON string below
json = "{}"
# create an instance of Idempotency1 from a JSON string
idempotency1_instance = Idempotency1.from_json(json)
# print the JSON string representation of the object
print(Idempotency1.to_json())

# convert the object into a dict
idempotency1_dict = idempotency1_instance.to_dict()
# create an instance of Idempotency1 from a dict
idempotency1_from_dict = Idempotency1.from_dict(idempotency1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


