# DateHistogramResult1



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Date in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
**count** | **int** | Number of entities in the bucket. | [optional] 

## Example

```python
from openapi_client.models.date_histogram_result1 import DateHistogramResult1

# TODO update the JSON string below
json = "{}"
# create an instance of DateHistogramResult1 from a JSON string
date_histogram_result1_instance = DateHistogramResult1.from_json(json)
# print the JSON string representation of the object
print(DateHistogramResult1.to_json())

# convert the object into a dict
date_histogram_result1_dict = date_histogram_result1_instance.to_dict()
# create an instance of DateHistogramResult1 from a dict
date_histogram_result1_from_dict = DateHistogramResult1.from_dict(date_histogram_result1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


