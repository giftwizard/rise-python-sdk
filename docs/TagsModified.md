# TagsModified



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_action** | **object** |  | [optional] 
**assigned_tags** | **object** | Tags that were assigned to the Diff. | [optional] 
**unassigned_tags** | **object** | Tags that were unassigned to the Diff. | [optional] 

## Example

```python
from openapi_client.models.tags_modified import TagsModified

# TODO update the JSON string below
json = "{}"
# create an instance of TagsModified from a JSON string
tags_modified_instance = TagsModified.from_json(json)
# print the JSON string representation of the object
print(TagsModified.to_json())

# convert the object into a dict
tags_modified_dict = tags_modified_instance.to_dict()
# create an instance of TagsModified from a dict
tags_modified_from_dict = TagsModified.from_dict(tags_modified_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


