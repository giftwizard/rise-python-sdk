# By


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**identifier** | **str** |  | [optional] 
**configuration_correlation_id** | **str** |  | [optional] 
**activation_id** | **str** |  | [optional] 
**identifier_pattern** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.by import By

# TODO update the JSON string below
json = "{}"
# create an instance of By from a JSON string
by_instance = By.from_json(json)
# print the JSON string representation of the object
print(By.to_json())

# convert the object into a dict
by_dict = by_instance.to_dict()
# create an instance of By from a dict
by_from_dict = By.from_dict(by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


