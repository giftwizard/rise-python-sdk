# EntityUpdatedEvent



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_entity_as_json** | **str** | Since platformized APIs only expose PATCH and not PUT we can&#39;t assume that the fields sent from the client are the actual diff. This means that to generate a list of changed fields (as opposed to sent fields) one needs to traverse both objects. We don&#39;t want to impose this on all developers and so we leave this traversal to the notification recipients which need it. | [optional] 

## Example

```python
from openapi_client.models.entity_updated_event import EntityUpdatedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of EntityUpdatedEvent from a JSON string
entity_updated_event_instance = EntityUpdatedEvent.from_json(json)
# print the JSON string representation of the object
print(EntityUpdatedEvent.to_json())

# convert the object into a dict
entity_updated_event_dict = entity_updated_event_instance.to_dict()
# create an instance of EntityUpdatedEvent from a dict
entity_updated_event_from_dict = EntityUpdatedEvent.from_dict(entity_updated_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


