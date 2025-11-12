# QueryByContact



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | **object** | Contact filter object. | [optional] 
**sort** | **List[object]** | Sort object. | [optional] 
**limit** | **int** | Limit for the number of wallets to return. | [optional] 

## Example

```python
from openapi_client.models.query_by_contact import QueryByContact

# TODO update the JSON string below
json = "{}"
# create an instance of QueryByContact from a JSON string
query_by_contact_instance = QueryByContact.from_json(json)
# print the JSON string representation of the object
print(QueryByContact.to_json())

# convert the object into a dict
query_by_contact_dict = query_by_contact_instance.to_dict()
# create an instance of QueryByContact from a dict
query_by_contact_from_dict = QueryByContact.from_dict(query_by_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


