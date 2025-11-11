# PreinstalledOrigin



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** | ID of the app that defines the preinstalled automation. | [optional] 
**component_id** | **str** | Application component ID. | [optional] 
**component_version** | **int** | Application component version. | [optional] 
**override** | **bool** | Whether the automation is an override automation. If the user modifies the preinstalled automation installed on their site, a site-specific automation is created that overrides the original one. If the user makes no modifications this boolean is set to &#x60;false&#x60; and the original preinstalled automation is used.  Default: &#x60;false&#x60; | [optional] [readonly] 

## Example

```python
from openapi_client.models.preinstalled_origin import PreinstalledOrigin

# TODO update the JSON string below
json = "{}"
# create an instance of PreinstalledOrigin from a JSON string
preinstalled_origin_instance = PreinstalledOrigin.from_json(json)
# print the JSON string representation of the object
print(PreinstalledOrigin.to_json())

# convert the object into a dict
preinstalled_origin_dict = preinstalled_origin_instance.to_dict()
# create an instance of PreinstalledOrigin from a dict
preinstalled_origin_from_dict = PreinstalledOrigin.from_dict(preinstalled_origin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


