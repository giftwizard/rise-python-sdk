# DateHistogramResults



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | **List[object]** | List of date histogram aggregations. | [optional] 

## Example

```python
from openapi_client.models.date_histogram_results import DateHistogramResults

# TODO update the JSON string below
json = "{}"
# create an instance of DateHistogramResults from a JSON string
date_histogram_results_instance = DateHistogramResults.from_json(json)
# print the JSON string representation of the object
print(DateHistogramResults.to_json())

# convert the object into a dict
date_histogram_results_dict = date_histogram_results_instance.to_dict()
# create an instance of DateHistogramResults from a dict
date_histogram_results_from_dict = DateHistogramResults.from_dict(date_histogram_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


