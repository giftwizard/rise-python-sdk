# FilterableAppDefinedActions



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_identifiers** | **List[str]** | App defined action identifiers, each identifier in form &#x60;${appId}_${actionKey}&#x60; | [optional] 

## Example

```python
from openapi_client.models.filterable_app_defined_actions import FilterableAppDefinedActions

# TODO update the JSON string below
json = "{}"
# create an instance of FilterableAppDefinedActions from a JSON string
filterable_app_defined_actions_instance = FilterableAppDefinedActions.from_json(json)
# print the JSON string representation of the object
print(FilterableAppDefinedActions.to_json())

# convert the object into a dict
filterable_app_defined_actions_dict = filterable_app_defined_actions_instance.to_dict()
# create an instance of FilterableAppDefinedActions from a dict
filterable_app_defined_actions_from_dict = FilterableAppDefinedActions.from_dict(filterable_app_defined_actions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


