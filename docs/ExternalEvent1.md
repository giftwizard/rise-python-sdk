# ExternalEvent1

Information about an external event that lead to the transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Event type indicator | [optional] 
**description** | **str** | Short description or identifier of the event | [optional] 

## Example

```python
from openapi_client.models.external_event1 import ExternalEvent1

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalEvent1 from a JSON string
external_event1_instance = ExternalEvent1.from_json(json)
# print the JSON string representation of the object
print(ExternalEvent1.to_json())

# convert the object into a dict
external_event1_dict = external_event1_instance.to_dict()
# create an instance of ExternalEvent1 from a dict
external_event1_from_dict = ExternalEvent1.from_dict(external_event1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


