# ContactDetails1



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Email of the wallet. | [optional] 
**phone** | **str** | Phone number of the wallet. | [optional] 
**first_name** | **str** | First name of the wallet. | [optional] 
**last_name** | **str** | Last name of the wallet. | [optional] 

## Example

```python
from openapi_client.models.contact_details1 import ContactDetails1

# TODO update the JSON string below
json = "{}"
# create an instance of ContactDetails1 from a JSON string
contact_details1_instance = ContactDetails1.from_json(json)
# print the JSON string representation of the object
print(ContactDetails1.to_json())

# convert the object into a dict
contact_details1_dict = contact_details1_instance.to_dict()
# create an instance of ContactDetails1 from a dict
contact_details1_from_dict = ContactDetails1.from_dict(contact_details1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


