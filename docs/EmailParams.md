# EmailParams



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skip_email_dispatch** | **bool** | Indicates whether to skip email dispatch for the WalletAction. The default is false. | [optional] 
**override_template_id** | **str** | ID of the email template to be used for the WalletAction, if default template is to be overridden. | [optional] 

## Example

```python
from openapi_client.models.email_params import EmailParams

# TODO update the JSON string below
json = "{}"
# create an instance of EmailParams from a JSON string
email_params_instance = EmailParams.from_json(json)
# print the JSON string representation of the object
print(EmailParams.to_json())

# convert the object into a dict
email_params_dict = email_params_instance.to_dict()
# create an instance of EmailParams from a dict
email_params_from_dict = EmailParams.from_dict(email_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


