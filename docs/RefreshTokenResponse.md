# RefreshTokenResponse

Once a user has completed the installation process and given your app permission to access their data, use the authorization code we sent you, together with your secret key, to request an access token and a refresh token. (The access token is only valid for 5 minutes.) You can find your secret key in the Wix Developers Center.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refresh_token** | **str** | Your app instance’s refresh token that never expires. Identical to the one that you’ve sent in the request. | [optional] 
**access_token** | **str** | Created access token that you can use to make Wix API calls. It expires after 5 minutes. | [optional] 

## Example

```python
from openapi_client.models.refresh_token_response import RefreshTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RefreshTokenResponse from a JSON string
refresh_token_response_instance = RefreshTokenResponse.from_json(json)
# print the JSON string representation of the object
print(RefreshTokenResponse.to_json())

# convert the object into a dict
refresh_token_response_dict = refresh_token_response_instance.to_dict()
# create an instance of RefreshTokenResponse from a dict
refresh_token_response_from_dict = RefreshTokenResponse.from_dict(refresh_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


