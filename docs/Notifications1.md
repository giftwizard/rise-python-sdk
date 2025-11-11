# Notifications1

Settings of the notifications related to the WalletAction. This field is used to specify whether to skip email dispatch or override the template ID for email notifications.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_params** | [**EmailParams1**](EmailParams1.md) |  | [optional] 

## Example

```python
from openapi_client.models.notifications1 import Notifications1

# TODO update the JSON string below
json = "{}"
# create an instance of Notifications1 from a JSON string
notifications1_instance = Notifications1.from_json(json)
# print the JSON string representation of the object
print(Notifications1.to_json())

# convert the object into a dict
notifications1_dict = notifications1_instance.to_dict()
# create an instance of Notifications1 from a dict
notifications1_from_dict = Notifications1.from_dict(notifications1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


