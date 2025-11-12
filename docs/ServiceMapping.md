# ServiceMapping



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Sevice name. | [optional] 
**method** | **str** | Method name. | [optional] 

## Example

```python
from openapi_client.models.service_mapping import ServiceMapping

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceMapping from a JSON string
service_mapping_instance = ServiceMapping.from_json(json)
# print the JSON string representation of the object
print(ServiceMapping.to_json())

# convert the object into a dict
service_mapping_dict = service_mapping_instance.to_dict()
# create an instance of ServiceMapping from a dict
service_mapping_from_dict = ServiceMapping.from_dict(service_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


