# OAuthOauth2TokenPostSomeOperationRequestBody

The endpoint accepts raw HTTP requests. You must pass the request\\'s body parameters formatted as bytes in the raw HTTP request\\'s `body` field, following this template: `{\"grantType\": \"client_credentials\", \"client_id\": \"<appId>\", \"client_secret\": \"<appSecretKey>\", \"instance_id\": \"<instanceId>\"}`. The access token is valid for 4 hours.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grant_type** | **str** | Request type. You must pass &#x60;\&quot;client_credentials\&quot;&#x60; to request a new access token when using basic OAuth. | [optional] 
**client_id** | **str** | Your app ID | [optional] 
**client_secret** | **str** | Your app&#39;s secret key ID | [optional] 
**instance_id** | **str** | The instance ID of your app for which you want to create the access token. Instance id represents a unique installation of your app on a specific Rise account.  | [optional] 

## Example

```python
from openapi_client.models.o_auth_oauth2_token_post_some_operation_request_body import OAuthOauth2TokenPostSomeOperationRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthOauth2TokenPostSomeOperationRequestBody from a JSON string
o_auth_oauth2_token_post_some_operation_request_body_instance = OAuthOauth2TokenPostSomeOperationRequestBody.from_json(json)
# print the JSON string representation of the object
print(OAuthOauth2TokenPostSomeOperationRequestBody.to_json())

# convert the object into a dict
o_auth_oauth2_token_post_some_operation_request_body_dict = o_auth_oauth2_token_post_some_operation_request_body_instance.to_dict()
# create an instance of OAuthOauth2TokenPostSomeOperationRequestBody from a dict
o_auth_oauth2_token_post_some_operation_request_body_from_dict = OAuthOauth2TokenPostSomeOperationRequestBody.from_dict(o_auth_oauth2_token_post_some_operation_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


