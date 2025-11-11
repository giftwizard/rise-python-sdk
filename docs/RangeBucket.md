# RangeBucket



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **float** | Inclusive lower bound of the range. Required if &#x60;to&#x60; is not provided. | [optional] 
**to** | **float** | Exclusive upper bound of the range. Required if &#x60;from&#x60; is not provided. | [optional] 

## Example

```python
from openapi_client.models.range_bucket import RangeBucket

# TODO update the JSON string below
json = "{}"
# create an instance of RangeBucket from a JSON string
range_bucket_instance = RangeBucket.from_json(json)
# print the JSON string representation of the object
print(RangeBucket.to_json())

# convert the object into a dict
range_bucket_dict = range_bucket_instance.to_dict()
# create an instance of RangeBucket from a dict
range_bucket_from_dict = RangeBucket.from_dict(range_bucket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


