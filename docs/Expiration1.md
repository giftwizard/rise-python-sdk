# Expiration1

The expiration date to apply to the Gift Card.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fixed_date** | **datetime** | Expiration date | [optional] 
**relative** | [**RelativeExpiresAtRelative**](RelativeExpiresAtRelative.md) |  | [optional] 

## Example

```python
from openapi_client.models.expiration1 import Expiration1

# TODO update the JSON string below
json = "{}"
# create an instance of Expiration1 from a JSON string
expiration1_instance = Expiration1.from_json(json)
# print the JSON string representation of the object
print(Expiration1.to_json())

# convert the object into a dict
expiration1_dict = expiration1_instance.to_dict()
# create an instance of Expiration1 from a dict
expiration1_from_dict = Expiration1.from_dict(expiration1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


