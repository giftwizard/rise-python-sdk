# EntityCreatedEvent



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_as_json** | **str** |  | [optional] 
**restore_info** | **object** | Indicates the event was triggered by a restore-from-trashbin operation for a previously deleted entity | [optional] 

## Example

```python
from openapi_client.models.entity_created_event import EntityCreatedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of EntityCreatedEvent from a JSON string
entity_created_event_instance = EntityCreatedEvent.from_json(json)
# print the JSON string representation of the object
print(EntityCreatedEvent.to_json())

# convert the object into a dict
entity_created_event_dict = entity_created_event_instance.to_dict()
# create an instance of EntityCreatedEvent from a dict
entity_created_event_from_dict = EntityCreatedEvent.from_dict(entity_created_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


