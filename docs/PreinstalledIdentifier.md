# PreinstalledIdentifier



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** | identifier for the application of the preinstalled | [optional] 
**component_id** | **str** | application component id | [optional] 

## Example

```python
from openapi_client.models.preinstalled_identifier import PreinstalledIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of PreinstalledIdentifier from a JSON string
preinstalled_identifier_instance = PreinstalledIdentifier.from_json(json)
# print the JSON string representation of the object
print(PreinstalledIdentifier.to_json())

# convert the object into a dict
preinstalled_identifier_dict = preinstalled_identifier_instance.to_dict()
# create an instance of PreinstalledIdentifier from a dict
preinstalled_identifier_from_dict = PreinstalledIdentifier.from_dict(preinstalled_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


