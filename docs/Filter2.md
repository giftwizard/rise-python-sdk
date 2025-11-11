# Filter2

[API Query Language](https://platform.rise.ai/docs/#tag/About-API-Query-Language) filter to count gift cards.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | [**Fields2**](Fields2.md) |  | [optional] 

## Example

```python
from openapi_client.models.filter2 import Filter2

# TODO update the JSON string below
json = "{}"
# create an instance of Filter2 from a JSON string
filter2_instance = Filter2.from_json(json)
# print the JSON string representation of the object
print(Filter2.to_json())

# convert the object into a dict
filter2_dict = filter2_instance.to_dict()
# create an instance of Filter2 from a dict
filter2_from_dict = Filter2.from_dict(filter2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


