# RewardOptionsRewardOptions

Reward Options. (**Deprecated**: Use `wallet_action_start_options` instead.)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_action_id** | **str** |  | [optional] 
**liability** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.reward_options_reward_options import RewardOptionsRewardOptions

# TODO update the JSON string below
json = "{}"
# create an instance of RewardOptionsRewardOptions from a JSON string
reward_options_reward_options_instance = RewardOptionsRewardOptions.from_json(json)
# print the JSON string representation of the object
print(RewardOptionsRewardOptions.to_json())

# convert the object into a dict
reward_options_reward_options_dict = reward_options_reward_options_instance.to_dict()
# create an instance of RewardOptionsRewardOptions from a dict
reward_options_reward_options_from_dict = RewardOptionsRewardOptions.from_dict(reward_options_reward_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


