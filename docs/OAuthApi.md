# openapi_client.OAuthApi

All URIs are relative to *https://platform.rise.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**some_operation**](OAuthApi.md#some_operation) | **POST** /oauth2/token | 


# **some_operation**
> CreateAccessTokenResponse some_operation(o_auth_oauth2_token_post_some_operation_request_body=o_auth_oauth2_token_post_some_operation_request_body)

Creates an access token.

Use this access token as Authorization header to call any other Rise api.

The token is valid for 4 hours.

### Example


```python
import openapi_client
from openapi_client.models.create_access_token_response import CreateAccessTokenResponse
from openapi_client.models.o_auth_oauth2_token_post_some_operation_request_body import OAuthOauth2TokenPostSomeOperationRequestBody
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://platform.rise.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://platform.rise.ai"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.OAuthApi(api_client)
    o_auth_oauth2_token_post_some_operation_request_body = openapi_client.OAuthOauth2TokenPostSomeOperationRequestBody() # OAuthOauth2TokenPostSomeOperationRequestBody |  (optional)

    try:
        api_response = api_instance.some_operation(o_auth_oauth2_token_post_some_operation_request_body=o_auth_oauth2_token_post_some_operation_request_body)
        print("The response of OAuthApi->some_operation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->some_operation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_auth_oauth2_token_post_some_operation_request_body** | [**OAuthOauth2TokenPostSomeOperationRequestBody**](OAuthOauth2TokenPostSomeOperationRequestBody.md)|  | [optional] 

### Return type

[**CreateAccessTokenResponse**](CreateAccessTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - The request was successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

