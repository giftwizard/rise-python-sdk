# AccessTokenRequest

Once a user has completed the installation process and given your app permission to access their data, use the authorization code we sent you, together with your secret key, to request an access token and a refresh token. (The access token is only valid for 5 minutes.).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grant_type** | **str** | Value must be set to \&quot;authorization_code\&quot; | [optional] 
**client_id** | **str** | The App ID as defined | [optional] 
**client_secret** | **str** | The Secret Key for your app | [optional] 
**code** | **str** | The authorization code received from us. | [optional] 

## Example

```python
from openapi_client.models.access_token_request import AccessTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AccessTokenRequest from a JSON string
access_token_request_instance = AccessTokenRequest.from_json(json)
# print the JSON string representation of the object
print(AccessTokenRequest.to_json())

# convert the object into a dict
access_token_request_dict = access_token_request_instance.to_dict()
# create an instance of AccessTokenRequest from a dict
access_token_request_from_dict = AccessTokenRequest.from_dict(access_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


