# IfFilter



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**condition** | **str** | If filter&#39;s condition. | [optional] 
**true_post_actions** | **List[object]** | If&#39;s true post actions. | [optional] 
**false_post_actions** | **List[object]** | If&#39;s false post actions. | [optional] 
**true_post_actions_ids** | **List[str]** | If&#39;s true post actions ids. | [optional] 
**false_post_actions_ids** | **List[str]** | If&#39;s false post actions ids. | [optional] 

## Example

```python
from openapi_client.models.if_filter import IfFilter

# TODO update the JSON string below
json = "{}"
# create an instance of IfFilter from a JSON string
if_filter_instance = IfFilter.from_json(json)
# print the JSON string representation of the object
print(IfFilter.to_json())

# convert the object into a dict
if_filter_dict = if_filter_instance.to_dict()
# create an instance of IfFilter from a dict
if_filter_from_dict = IfFilter.from_dict(if_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


