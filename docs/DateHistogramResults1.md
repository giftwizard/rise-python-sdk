# DateHistogramResults1

Date histogram aggregation results.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_histogram** | [**DateHistogramResults1**](DateHistogramResults1.md) |  | [optional] 

## Example

```python
from openapi_client.models.date_histogram_results1 import DateHistogramResults1

# TODO update the JSON string below
json = "{}"
# create an instance of DateHistogramResults1 from a JSON string
date_histogram_results1_instance = DateHistogramResults1.from_json(json)
# print the JSON string representation of the object
print(DateHistogramResults1.to_json())

# convert the object into a dict
date_histogram_results1_dict = date_histogram_results1_instance.to_dict()
# create an instance of DateHistogramResults1 from a dict
date_histogram_results1_from_dict = DateHistogramResults1.from_dict(date_histogram_results1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


