# EXISTINGIDEMPOTENCYKEY


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Error message | 
**details** | [**EXISTINGIDEMPOTENCYKEYDetails**](EXISTINGIDEMPOTENCYKEYDetails.md) |  | 

## Example

```python
from openapi_client.models.existingidempotencykey import EXISTINGIDEMPOTENCYKEY

# TODO update the JSON string below
json = "{}"
# create an instance of EXISTINGIDEMPOTENCYKEY from a JSON string
existingidempotencykey_instance = EXISTINGIDEMPOTENCYKEY.from_json(json)
# print the JSON string representation of the object
print(EXISTINGIDEMPOTENCYKEY.to_json())

# convert the object into a dict
existingidempotencykey_dict = existingidempotencykey_instance.to_dict()
# create an instance of EXISTINGIDEMPOTENCYKEY from a dict
existingidempotencykey_from_dict = EXISTINGIDEMPOTENCYKEY.from_dict(existingidempotencykey_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


