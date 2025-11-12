# ActionsData



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**root_action_ids** | **List[str]** | Ids of the first level actions. | [optional] 
**actions** | [**Actions1**](Actions1.md) |  | [optional] 

## Example

```python
from openapi_client.models.actions_data import ActionsData

# TODO update the JSON string below
json = "{}"
# create an instance of ActionsData from a JSON string
actions_data_instance = ActionsData.from_json(json)
# print the JSON string representation of the object
print(ActionsData.to_json())

# convert the object into a dict
actions_data_dict = actions_data_instance.to_dict()
# create an instance of ActionsData from a dict
actions_data_from_dict = ActionsData.from_dict(actions_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


