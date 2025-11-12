# ConditionBlock



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**line_expressions** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.condition_block import ConditionBlock

# TODO update the JSON string below
json = "{}"
# create an instance of ConditionBlock from a JSON string
condition_block_instance = ConditionBlock.from_json(json)
# print the JSON string representation of the object
print(ConditionBlock.to_json())

# convert the object into a dict
condition_block_dict = condition_block_instance.to_dict()
# create an instance of ConditionBlock from a dict
condition_block_from_dict = ConditionBlock.from_dict(condition_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


