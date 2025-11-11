# RewardOptions



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_action_id** | **str** |  | [optional] 
**liability** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.reward_options import RewardOptions

# TODO update the JSON string below
json = "{}"
# create an instance of RewardOptions from a JSON string
reward_options_instance = RewardOptions.from_json(json)
# print the JSON string representation of the object
print(RewardOptions.to_json())

# convert the object into a dict
reward_options_dict = reward_options_instance.to_dict()
# create an instance of RewardOptions from a dict
reward_options_from_dict = RewardOptions.from_dict(reward_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


