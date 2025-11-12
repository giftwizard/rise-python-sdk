# IncreaseBalance428Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Error message | 
**details** | [**INVALIDGIFTCARDBALANCEDetails**](INVALIDGIFTCARDBALANCEDetails.md) |  | 

## Example

```python
from openapi_client.models.increase_balance428_response import IncreaseBalance428Response

# TODO update the JSON string below
json = "{}"
# create an instance of IncreaseBalance428Response from a JSON string
increase_balance428_response_instance = IncreaseBalance428Response.from_json(json)
# print the JSON string representation of the object
print(IncreaseBalance428Response.to_json())

# convert the object into a dict
increase_balance428_response_dict = increase_balance428_response_instance.to_dict()
# create an instance of IncreaseBalance428Response from a dict
increase_balance428_response_from_dict = IncreaseBalance428Response.from_dict(increase_balance428_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


