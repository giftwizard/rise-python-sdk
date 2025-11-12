# Service



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_mapping** | **object** | Action&#39;s service mapping. | [optional] 
**input_mapping** | **str** | Action&#39;s input mapping. Jsonata description of the input this service gets. | [optional] 
**output_mapping** | **str** | Action&#39;s output mapping. Jsonata description of the output this service returns. | [optional] 
**post_actions** | **List[object]** | Action&#39;s post actions. | [optional] 
**post_actions_ids** | **List[str]** | Action&#39;s post actions ids. | [optional] 
**namespace** | **str** | The namespace of the action | [optional] 

## Example

```python
from openapi_client.models.service import Service

# TODO update the JSON string below
json = "{}"
# create an instance of Service from a JSON string
service_instance = Service.from_json(json)
# print the JSON string representation of the object
print(Service.to_json())

# convert the object into a dict
service_dict = service_instance.to_dict()
# create an instance of Service from a dict
service_from_dict = Service.from_dict(service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


