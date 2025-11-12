# INSUFFICIENTFUNDS


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Error message | 
**details** | [**INSUFFICIENTFUNDSDetails**](INSUFFICIENTFUNDSDetails.md) |  | 

## Example

```python
from openapi_client.models.insufficientfunds import INSUFFICIENTFUNDS

# TODO update the JSON string below
json = "{}"
# create an instance of INSUFFICIENTFUNDS from a JSON string
insufficientfunds_instance = INSUFFICIENTFUNDS.from_json(json)
# print the JSON string representation of the object
print(INSUFFICIENTFUNDS.to_json())

# convert the object into a dict
insufficientfunds_dict = insufficientfunds_instance.to_dict()
# create an instance of INSUFFICIENTFUNDS from a dict
insufficientfunds_from_dict = INSUFFICIENTFUNDS.from_dict(insufficientfunds_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


