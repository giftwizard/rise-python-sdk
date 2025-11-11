# EntityDeletedEvent



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted_entity_as_json** | **str** | Entity that was deleted | [optional] 

## Example

```python
from openapi_client.models.entity_deleted_event import EntityDeletedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of EntityDeletedEvent from a JSON string
entity_deleted_event_instance = EntityDeletedEvent.from_json(json)
# print the JSON string representation of the object
print(EntityDeletedEvent.to_json())

# convert the object into a dict
entity_deleted_event_dict = entity_deleted_event_instance.to_dict()
# create an instance of EntityDeletedEvent from a dict
entity_deleted_event_from_dict = EntityDeletedEvent.from_dict(entity_deleted_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


