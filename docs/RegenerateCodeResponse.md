# RegenerateCodeResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gift_card** | **object** | The GiftCard with the new code. | [optional] 

## Example

```python
from openapi_client.models.regenerate_code_response import RegenerateCodeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RegenerateCodeResponse from a JSON string
regenerate_code_response_instance = RegenerateCodeResponse.from_json(json)
# print the JSON string representation of the object
print(RegenerateCodeResponse.to_json())

# convert the object into a dict
regenerate_code_response_dict = regenerate_code_response_instance.to_dict()
# create an instance of RegenerateCodeResponse from a dict
regenerate_code_response_from_dict = RegenerateCodeResponse.from_dict(regenerate_code_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


