# RangeResults



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | **List[object]** | List of ranges returned in the same order as requested. | [optional] 

## Example

```python
from openapi_client.models.range_results import RangeResults

# TODO update the JSON string below
json = "{}"
# create an instance of RangeResults from a JSON string
range_results_instance = RangeResults.from_json(json)
# print the JSON string representation of the object
print(RangeResults.to_json())

# convert the object into a dict
range_results_dict = range_results_instance.to_dict()
# create an instance of RangeResults from a dict
range_results_from_dict = RangeResults.from_dict(range_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


