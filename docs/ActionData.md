# ActionData



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Action&#39;s id. | [optional] [readonly] 
**action** | **object** | Action&#39;s data. | [optional] 

## Example

```python
from openapi_client.models.action_data import ActionData

# TODO update the JSON string below
json = "{}"
# create an instance of ActionData from a JSON string
action_data_instance = ActionData.from_json(json)
# print the JSON string representation of the object
print(ActionData.to_json())

# convert the object into a dict
action_data_dict = action_data_instance.to_dict()
# create an instance of ActionData from a dict
action_data_from_dict = ActionData.from_dict(action_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


