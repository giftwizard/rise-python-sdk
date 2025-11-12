# RangeResult



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **float** | Inclusive lower bound of the range. | [optional] 
**to** | **float** | Exclusive upper bound of the range. | [optional] 
**count** | **int** | Number of entities in this range. | [optional] 

## Example

```python
from openapi_client.models.range_result import RangeResult

# TODO update the JSON string below
json = "{}"
# create an instance of RangeResult from a JSON string
range_result_instance = RangeResult.from_json(json)
# print the JSON string representation of the object
print(RangeResult.to_json())

# convert the object into a dict
range_result_dict = range_result_instance.to_dict()
# create an instance of RangeResult from a dict
range_result_from_dict = RangeResult.from_dict(range_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


