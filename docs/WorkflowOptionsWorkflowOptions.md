# WorkflowOptionsWorkflowOptions

Detailed information about a Gift Card issued from a workflow.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_id** | **str** | ID of the workflow that issued the gift card. | [optional] 

## Example

```python
from openapi_client.models.workflow_options_workflow_options import WorkflowOptionsWorkflowOptions

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowOptionsWorkflowOptions from a JSON string
workflow_options_workflow_options_instance = WorkflowOptionsWorkflowOptions.from_json(json)
# print the JSON string representation of the object
print(WorkflowOptionsWorkflowOptions.to_json())

# convert the object into a dict
workflow_options_workflow_options_dict = workflow_options_workflow_options_instance.to_dict()
# create an instance of WorkflowOptionsWorkflowOptions from a dict
workflow_options_workflow_options_from_dict = WorkflowOptionsWorkflowOptions.from_dict(workflow_options_workflow_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


