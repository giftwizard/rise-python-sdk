# Tags

Common object for tags. Should be use as in this example: message Foo { option (.wix.api.decomposite_of) = \"wix.commons.v2.tags.Foo\"; string id = 1; ... Tags tags = 5 }  example of taggable entity { id: \"123\" tags: { public_tags: { tag_ids:[\"11\",\"22\"] }, private_tags: { tag_ids: [\"33\", \"44\"] } } }

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**private_tags** | **object** | Tags that require an additional permission in order to access them, typically restricted from site members and visitors. | [optional] 
**public_tags** | **object** | Tags that are exposed to anyone with access to the entity, including site members and visitors. | [optional] 

## Example

```python
from openapi_client.models.tags import Tags

# TODO update the JSON string below
json = "{}"
# create an instance of Tags from a JSON string
tags_instance = Tags.from_json(json)
# print the JSON string representation of the object
print(Tags.to_json())

# convert the object into a dict
tags_dict = tags_instance.to_dict()
# create an instance of Tags from a dict
tags_from_dict = Tags.from_dict(tags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


