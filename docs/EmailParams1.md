# EmailParams1

Settings for email notifications related to the WalletAction. This field is used to specify whether to skip email dispatch or override the template ID for email notifications.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skip_email_dispatch** | **bool** | Indicates whether to skip email dispatch for the WalletAction. The default is false. | [optional] 
**override_template_id** | **str** | ID of the email template to be used for the WalletAction, if default template is to be overridden. | [optional] 

## Example

```python
from openapi_client.models.email_params1 import EmailParams1

# TODO update the JSON string below
json = "{}"
# create an instance of EmailParams1 from a JSON string
email_params1_instance = EmailParams1.from_json(json)
# print the JSON string representation of the object
print(EmailParams1.to_json())

# convert the object into a dict
email_params1_dict = email_params1_instance.to_dict()
# create an instance of EmailParams1 from a dict
email_params1_from_dict = EmailParams1.from_dict(email_params1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


