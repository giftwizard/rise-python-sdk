# OriginInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_info** | **object** | Application info | [optional] 
**preinstalled_info** | **object** | Preinstalled info | [optional] 

## Example

```python
from openapi_client.models.origin_info import OriginInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OriginInfo from a JSON string
origin_info_instance = OriginInfo.from_json(json)
# print the JSON string representation of the object
print(OriginInfo.to_json())

# convert the object into a dict
origin_info_dict = origin_info_instance.to_dict()
# create an instance of OriginInfo from a dict
origin_info_from_dict = OriginInfo.from_dict(origin_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


