# QueryByContact1

Contact query object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**Filter4**](Filter4.md) |  | [optional] 
**sort** | [**List[Sorting2]**](Sorting2.md) | Sort object. | [optional] 
**limit** | **int** | Limit for the number of wallets to return. | [optional] 

## Example

```python
from openapi_client.models.query_by_contact1 import QueryByContact1

# TODO update the JSON string below
json = "{}"
# create an instance of QueryByContact1 from a JSON string
query_by_contact1_instance = QueryByContact1.from_json(json)
# print the JSON string representation of the object
print(QueryByContact1.to_json())

# convert the object into a dict
query_by_contact1_dict = query_by_contact1_instance.to_dict()
# create an instance of QueryByContact1 from a dict
query_by_contact1_from_dict = QueryByContact1.from_dict(query_by_contact1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


