# REQUIREDPROPERTY


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Error message | 
**details** | [**REQUIREDPROPERTYDetails**](REQUIREDPROPERTYDetails.md) |  | 

## Example

```python
from openapi_client.models.requiredproperty import REQUIREDPROPERTY

# TODO update the JSON string below
json = "{}"
# create an instance of REQUIREDPROPERTY from a JSON string
requiredproperty_instance = REQUIREDPROPERTY.from_json(json)
# print the JSON string representation of the object
print(REQUIREDPROPERTY.to_json())

# convert the object into a dict
requiredproperty_dict = requiredproperty_instance.to_dict()
# create an instance of REQUIREDPROPERTY from a dict
requiredproperty_from_dict = REQUIREDPROPERTY.from_dict(requiredproperty_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


