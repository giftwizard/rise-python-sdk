# ExternalEvent



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Event type indicator | [optional] 
**description** | **str** | Short description or identifier of the event | [optional] 

## Example

```python
from openapi_client.models.external_event import ExternalEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalEvent from a JSON string
external_event_instance = ExternalEvent.from_json(json)
# print the JSON string representation of the object
print(ExternalEvent.to_json())

# convert the object into a dict
external_event_dict = external_event_instance.to_dict()
# create an instance of ExternalEvent from a dict
external_event_from_dict = ExternalEvent.from_dict(external_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


