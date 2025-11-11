# Id


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anonymous_visitor_id** | **str** | ID of a site visitor that has not logged in to the site. | [optional] 
**member_id** | **str** | ID of a site visitor that has logged in to the site. | [optional] 
**user_id** | **str** | ID of a User (site owner, contributor, etc.). | [optional] 
**app_id** | **str** | ID of an app. | [optional] 

## Example

```python
from openapi_client.models.id import Id

# TODO update the JSON string below
json = "{}"
# create an instance of Id from a JSON string
id_instance = Id.from_json(json)
# print the JSON string representation of the object
print(Id.to_json())

# convert the object into a dict
id_dict = id_instance.to_dict()
# create an instance of Id from a dict
id_from_dict = Id.from_dict(id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


