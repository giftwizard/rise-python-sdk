# SCHEMAVALIDATIONFAILED


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Error message | 
**details** | [**SCHEMAVALIDATIONFAILEDDetails**](SCHEMAVALIDATIONFAILEDDetails.md) |  | 

## Example

```python
from openapi_client.models.schemavalidationfailed import SCHEMAVALIDATIONFAILED

# TODO update the JSON string below
json = "{}"
# create an instance of SCHEMAVALIDATIONFAILED from a JSON string
schemavalidationfailed_instance = SCHEMAVALIDATIONFAILED.from_json(json)
# print the JSON string representation of the object
print(SCHEMAVALIDATIONFAILED.to_json())

# convert the object into a dict
schemavalidationfailed_dict = schemavalidationfailed_instance.to_dict()
# create an instance of SCHEMAVALIDATIONFAILED from a dict
schemavalidationfailed_from_dict = SCHEMAVALIDATIONFAILED.from_dict(schemavalidationfailed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


