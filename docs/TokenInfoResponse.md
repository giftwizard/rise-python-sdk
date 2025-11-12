# TokenInfoResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Whether the token is active. | [optional] 
**subject_type** | **str** | Type of subject to which the token is issued. | [optional] 
**subject_id** | **str** | ID of the subject to which the token is issued. | [optional] 
**exp** | **float** | Token expiration timestamp. | [optional] 
**iat** | **float** | Token issue timestamp. | [optional] 
**client_id** | **float** | ID of the app that [created](https://dev.wix.com/docs/rest/app-management/oauth-2/create-access-token) the token, as defined in the [Wix Dev Center](https://dev.wix.com). | [optional] 
**account_id** | **float** | ID of the account that [created](https://dev.wix.com/docs/rest/app-management/oauth-2/create-access-token) the token, as defined in the [Wix Dev Center](https://dev.wix.com/apps/my-apps). | [optional] 
**site_id** | **float** | ID of the site to which the token is issued. | [optional] 
**instance_id** | **float** | The [instance ID](https://dev.wix.com/docs/rest/app-management/app-instance/introduction) of the app that the access token was created for. Subscribe to the [Instance App Installed](https://dev.wix.com/docs/rest/app-management/app-instance/app-instance-installed) webhook to receive a notification including the new app instance ID whenever a version of your app is installed on a Wix site. | [optional] 

## Example

```python
from openapi_client.models.token_info_response import TokenInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TokenInfoResponse from a JSON string
token_info_response_instance = TokenInfoResponse.from_json(json)
# print the JSON string representation of the object
print(TokenInfoResponse.to_json())

# convert the object into a dict
token_info_response_dict = token_info_response_instance.to_dict()
# create an instance of TokenInfoResponse from a dict
token_info_response_from_dict = TokenInfoResponse.from_dict(token_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


