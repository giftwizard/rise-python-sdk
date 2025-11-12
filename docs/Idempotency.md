# Idempotency



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | A unique identifier for the event. If you send the same idempotency key in multiple report event requests, for the same trigger key and app id, consecutive requests will be ignored after the first one. Note that the idempotency key is kept for a week before it expires. | [optional] 
**ttl_in_milliseconds** | **str** | Optional. The time to live (TTL) in milliseconds before the key will expire. Default is a week. | [optional] 

## Example

```python
from openapi_client.models.idempotency import Idempotency

# TODO update the JSON string below
json = "{}"
# create an instance of Idempotency from a JSON string
idempotency_instance = Idempotency.from_json(json)
# print the JSON string representation of the object
print(Idempotency.to_json())

# convert the object into a dict
idempotency_dict = idempotency_instance.to_dict()
# create an instance of Idempotency from a dict
idempotency_from_dict = Idempotency.from_dict(idempotency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


