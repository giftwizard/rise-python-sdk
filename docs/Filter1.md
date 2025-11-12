# Filter1

Filter object in the following format: `\"filter\" : { \"fieldName1\": \"value1\", \"fieldName2\":{\"$operator\":\"value2\"} }` Example of operators: `$eq`, `$ne`, `$lt`, `$lte`, `$gt`, `$gte`, `$in`, `$hasSome`, `$hasAll`, `$startsWith`, `$contains`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | [**Fields1**](Fields1.md) |  | [optional] 

## Example

```python
from openapi_client.models.filter1 import Filter1

# TODO update the JSON string below
json = "{}"
# create an instance of Filter1 from a JSON string
filter1_instance = Filter1.from_json(json)
# print the JSON string representation of the object
print(Filter1.to_json())

# convert the object into a dict
filter1_dict = filter1_instance.to_dict()
# create an instance of Filter1 from a dict
filter1_from_dict = Filter1.from_dict(filter1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


