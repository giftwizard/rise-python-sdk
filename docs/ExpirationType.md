# ExpirationType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fixed_date** | **datetime** | Expiration date | [optional] 
**relative** | **object** | Relative Expiration period | [optional] 

## Example

```python
from openapi_client.models.expiration_type import ExpirationType

# TODO update the JSON string below
json = "{}"
# create an instance of ExpirationType from a JSON string
expiration_type_instance = ExpirationType.from_json(json)
# print the JSON string representation of the object
print(ExpirationType.to_json())

# convert the object into a dict
expiration_type_dict = expiration_type_instance.to_dict()
# create an instance of ExpirationType from a dict
expiration_type_from_dict = ExpirationType.from_dict(expiration_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


