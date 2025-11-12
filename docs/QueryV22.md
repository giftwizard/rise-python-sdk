# QueryV22

API Query Language expression.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**Filter1**](Filter1.md) |  | [optional] 
**sort** | [**List[Sorting2]**](Sorting2.md) | Sort object in the following format: &#x60;[{\&quot;fieldName\&quot;:\&quot;sortField1\&quot;,\&quot;order\&quot;:\&quot;ASC\&quot;},{\&quot;fieldName\&quot;:\&quot;sortField2\&quot;,\&quot;order\&quot;:\&quot;DESC\&quot;}]&#x60; | [optional] 
**fields** | **List[str]** | Array of projected fields. A list of specific field names to return. If &#x60;fieldsets&#x60; are also specified, the union of &#x60;fieldsets&#x60; and &#x60;fields&#x60; is returned. | [optional] 
**fieldsets** | **List[str]** | Array of named, predefined sets of projected fields. A array of predefined named sets of fields to be returned. Specifying multiple &#x60;fieldsets&#x60; will return the union of fields from all sets. If &#x60;fields&#x60; are also specified, the union of &#x60;fieldsets&#x60; and &#x60;fields&#x60; is returned. | [optional] 
**paging** | [**PagingPaging**](PagingPaging.md) |  | [optional] 
**cursor_paging** | [**PagingMethodCursorPaging**](PagingMethodCursorPaging.md) |  | [optional] 

## Example

```python
from openapi_client.models.query_v22 import QueryV22

# TODO update the JSON string below
json = "{}"
# create an instance of QueryV22 from a JSON string
query_v22_instance = QueryV22.from_json(json)
# print the JSON string representation of the object
print(QueryV22.to_json())

# convert the object into a dict
query_v22_dict = query_v22_instance.to_dict()
# create an instance of QueryV22 from a dict
query_v22_from_dict = QueryV22.from_dict(query_v22_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


