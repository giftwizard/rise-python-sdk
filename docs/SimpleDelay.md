# SimpleDelay



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** |  | [optional] 
**units** | **str** |  | [optional] 
**delay_expression** | **str** | Optional, used if provided: Jsonata expression that evaluates to a number of milliseconds to wait | [optional] 

## Example

```python
from openapi_client.models.simple_delay import SimpleDelay

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleDelay from a JSON string
simple_delay_instance = SimpleDelay.from_json(json)
# print the JSON string representation of the object
print(SimpleDelay.to_json())

# convert the object into a dict
simple_delay_dict = simple_delay_instance.to_dict()
# create an instance of SimpleDelay from a dict
simple_delay_from_dict = SimpleDelay.from_dict(simple_delay_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


