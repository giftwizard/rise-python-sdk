# ExternalEvent2

Information about the external event that triggered the WalletAction, such as type of event and a short description or identifier of the event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Event type indicator | [optional] 
**description** | **str** | Short description or identifier of the event | [optional] 

## Example

```python
from openapi_client.models.external_event2 import ExternalEvent2

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalEvent2 from a JSON string
external_event2_instance = ExternalEvent2.from_json(json)
# print the JSON string representation of the object
print(ExternalEvent2.to_json())

# convert the object into a dict
external_event2_dict = external_event2_instance.to_dict()
# create an instance of ExternalEvent2 from a dict
external_event2_from_dict = ExternalEvent2.from_dict(external_event2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


