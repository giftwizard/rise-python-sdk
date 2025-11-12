# DecreaseBalance428Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Error message | 
**details** | [**INSUFFICIENTFUNDSDetails**](INSUFFICIENTFUNDSDetails.md) |  | 

## Example

```python
from openapi_client.models.decrease_balance428_response import DecreaseBalance428Response

# TODO update the JSON string below
json = "{}"
# create an instance of DecreaseBalance428Response from a JSON string
decrease_balance428_response_instance = DecreaseBalance428Response.from_json(json)
# print the JSON string representation of the object
print(DecreaseBalance428Response.to_json())

# convert the object into a dict
decrease_balance428_response_dict = decrease_balance428_response_instance.to_dict()
# create an instance of DecreaseBalance428Response from a dict
decrease_balance428_response_from_dict = DecreaseBalance428Response.from_dict(decrease_balance428_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


