# QueryV21

WQL expression.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**Filter**](Filter.md) |  | [optional] 
**sort** | [**List[Sorting1]**](Sorting1.md) | Sort object.  Learn more about [sorting](https://dev.wix.com/docs/rest/articles/getting-started/api-query-language#sorting). | [optional] 
**fields** | **List[str]** | Array of projected fields. A list of specific field names to return. If &#x60;fieldsets&#x60; are also specified, the union of &#x60;fieldsets&#x60; and &#x60;fields&#x60; is returned. | [optional] 
**fieldsets** | **List[str]** | Array of named, predefined sets of projected fields. A array of predefined named sets of fields to be returned. Specifying multiple &#x60;fieldsets&#x60; will return the union of fields from all sets. If &#x60;fields&#x60; are also specified, the union of &#x60;fieldsets&#x60; and &#x60;fields&#x60; is returned. | [optional] 
**paging** | [**PagingPaging**](PagingPaging.md) |  | [optional] 
**cursor_paging** | [**PagingMethodCursorPaging**](PagingMethodCursorPaging.md) |  | [optional] 

## Example

```python
from openapi_client.models.query_v21 import QueryV21

# TODO update the JSON string below
json = "{}"
# create an instance of QueryV21 from a JSON string
query_v21_instance = QueryV21.from_json(json)
# print the JSON string representation of the object
print(QueryV21.to_json())

# convert the object into a dict
query_v21_dict = query_v21_instance.to_dict()
# create an instance of QueryV21 from a dict
query_v21_from_dict = QueryV21.from_dict(query_v21_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


