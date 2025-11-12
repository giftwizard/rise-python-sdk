# RelativeExpiresAtRelative

Relative Expiration period

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **int** | Number of time units until expiration | [optional] 
**period** | **str** | Units of time for expiration | [optional] 

## Example

```python
from openapi_client.models.relative_expires_at_relative import RelativeExpiresAtRelative

# TODO update the JSON string below
json = "{}"
# create an instance of RelativeExpiresAtRelative from a JSON string
relative_expires_at_relative_instance = RelativeExpiresAtRelative.from_json(json)
# print the JSON string representation of the object
print(RelativeExpiresAtRelative.to_json())

# convert the object into a dict
relative_expires_at_relative_dict = relative_expires_at_relative_instance.to_dict()
# create an instance of RelativeExpiresAtRelative from a dict
relative_expires_at_relative_from_dict = RelativeExpiresAtRelative.from_dict(relative_expires_at_relative_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


