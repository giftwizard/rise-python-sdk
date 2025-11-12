# openapi_client.WalletApi

All URIs are relative to *https://platform.rise.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_wallets**](WalletApi.md#count_wallets) | **POST** /v1/rise/wallets/count | 
[**create_wallet**](WalletApi.md#create_wallet) | **POST** /v1/rise/wallets | 
[**get_customer_reference**](WalletApi.md#get_customer_reference) | **GET** /v1/rise/customers | 
[**get_or_create_wallet**](WalletApi.md#get_or_create_wallet) | **POST** /v1/rise/wallets/issue | 
[**get_wallet**](WalletApi.md#get_wallet) | **GET** /v1/rise/wallets | 
[**query_wallets**](WalletApi.md#query_wallets) | **POST** /v1/rise/wallets/query | 
[**query_wallets_by_contact**](WalletApi.md#query_wallets_by_contact) | **POST** /v1/rise/wallets/query_by_contact | 


# **count_wallets**
> CountWalletsResponse count_wallets(wallet_wallet_service_v1_rise_wallets_count_post_count_wallets_request_body)

Count wallets based on the given filter.

### Example


```python
import openapi_client
from openapi_client.models.count_wallets_response import CountWalletsResponse
from openapi_client.models.wallet_wallet_service_v1_rise_wallets_count_post_count_wallets_request_body import WalletWalletServiceV1RiseWalletsCountPostCountWalletsRequestBody
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
    api_instance = openapi_client.WalletApi(api_client)
    wallet_wallet_service_v1_rise_wallets_count_post_count_wallets_request_body = openapi_client.WalletWalletServiceV1RiseWalletsCountPostCountWalletsRequestBody() # WalletWalletServiceV1RiseWalletsCountPostCountWalletsRequestBody | 

    try:
        api_response = api_instance.count_wallets(wallet_wallet_service_v1_rise_wallets_count_post_count_wallets_request_body)
        print("The response of WalletApi->count_wallets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->count_wallets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_wallet_service_v1_rise_wallets_count_post_count_wallets_request_body** | [**WalletWalletServiceV1RiseWalletsCountPostCountWalletsRequestBody**](WalletWalletServiceV1RiseWalletsCountPostCountWalletsRequestBody.md)|  | 

### Return type

[**CountWalletsResponse**](CountWalletsResponse.md)

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

# **create_wallet**
> CreateWalletResponse1 create_wallet(wallet_wallet_service_v1_rise_wallets_post_create_wallet_request_body)

Creates a new Wallet.

### Example


```python
import openapi_client
from openapi_client.models.create_wallet_response1 import CreateWalletResponse1
from openapi_client.models.wallet_wallet_service_v1_rise_wallets_post_create_wallet_request_body import WalletWalletServiceV1RiseWalletsPostCreateWalletRequestBody
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
    api_instance = openapi_client.WalletApi(api_client)
    wallet_wallet_service_v1_rise_wallets_post_create_wallet_request_body = openapi_client.WalletWalletServiceV1RiseWalletsPostCreateWalletRequestBody() # WalletWalletServiceV1RiseWalletsPostCreateWalletRequestBody | 

    try:
        api_response = api_instance.create_wallet(wallet_wallet_service_v1_rise_wallets_post_create_wallet_request_body)
        print("The response of WalletApi->create_wallet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->create_wallet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_wallet_service_v1_rise_wallets_post_create_wallet_request_body** | [**WalletWalletServiceV1RiseWalletsPostCreateWalletRequestBody**](WalletWalletServiceV1RiseWalletsPostCreateWalletRequestBody.md)|  | 

### Return type

[**CreateWalletResponse1**](CreateWalletResponse1.md)

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

# **get_customer_reference**
> GetCustomerReferenceResponse get_customer_reference(query)

Get a CustomerReference by source (i.e. source channel, tenant, and customer IDs).

### Example


```python
import openapi_client
from openapi_client.models.customer_reference_query import CustomerReferenceQuery
from openapi_client.models.get_customer_reference_response import GetCustomerReferenceResponse
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
    api_instance = openapi_client.WalletApi(api_client)
    query = openapi_client.CustomerReferenceQuery() # CustomerReferenceQuery | Customer Reference query object.

    try:
        api_response = api_instance.get_customer_reference(query)
        print("The response of WalletApi->get_customer_reference:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->get_customer_reference: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**CustomerReferenceQuery**](.md)| Customer Reference query object. | 

### Return type

[**GetCustomerReferenceResponse**](GetCustomerReferenceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - The request was successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_or_create_wallet**
> GetOrCreateWalletResponse get_or_create_wallet(wallet_wallet_service_v1_rise_wallets_issue_post_get_or_create_wallet_request_body)

Retrieves or creates a Wallet for the provided customer reference.

- In case the Wallet doesn't exist - creates a new Wallet with the provided customer reference.
- In case the Wallet already exists - returns the existing Wallet.
- If the provided customer reference doesn't exist yet - adds it to the wallet.
- If the provided customer reference already exists - doesn't update anything.

### Example


```python
import openapi_client
from openapi_client.models.get_or_create_wallet_response import GetOrCreateWalletResponse
from openapi_client.models.wallet_wallet_service_v1_rise_wallets_issue_post_get_or_create_wallet_request_body import WalletWalletServiceV1RiseWalletsIssuePostGetOrCreateWalletRequestBody
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
    api_instance = openapi_client.WalletApi(api_client)
    wallet_wallet_service_v1_rise_wallets_issue_post_get_or_create_wallet_request_body = openapi_client.WalletWalletServiceV1RiseWalletsIssuePostGetOrCreateWalletRequestBody() # WalletWalletServiceV1RiseWalletsIssuePostGetOrCreateWalletRequestBody | 

    try:
        api_response = api_instance.get_or_create_wallet(wallet_wallet_service_v1_rise_wallets_issue_post_get_or_create_wallet_request_body)
        print("The response of WalletApi->get_or_create_wallet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->get_or_create_wallet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_wallet_service_v1_rise_wallets_issue_post_get_or_create_wallet_request_body** | [**WalletWalletServiceV1RiseWalletsIssuePostGetOrCreateWalletRequestBody**](WalletWalletServiceV1RiseWalletsIssuePostGetOrCreateWalletRequestBody.md)|  | 

### Return type

[**GetOrCreateWalletResponse**](GetOrCreateWalletResponse.md)

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

# **get_wallet**
> GetWalletResponse get_wallet(query)

Get a Wallet by ID, email, or a customer reference in the wallet.

### Example


```python
import openapi_client
from openapi_client.models.get_wallet_response import GetWalletResponse
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
    api_instance = openapi_client.WalletApi(api_client)
    query = None # object | Query object.

    try:
        api_response = api_instance.get_wallet(query)
        print("The response of WalletApi->get_wallet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->get_wallet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**object**](.md)| Query object. | 

### Return type

[**GetWalletResponse**](GetWalletResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - The request was successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_wallets**
> QueryWalletsResponse1 query_wallets(wallet_action_wallet_action_service_v1_rise_wallet_actions_query_post_query_wallet_actions_request_body)

Query wallets enriched with gift card and contact information. See [API Query Language](https://platform.rise.ai/docs/#tag/About-API-Query-Language).

### Example


```python
import openapi_client
from openapi_client.models.query_wallets_response1 import QueryWalletsResponse1
from openapi_client.models.wallet_action_wallet_action_service_v1_rise_wallet_actions_query_post_query_wallet_actions_request_body import WalletActionWalletActionServiceV1RiseWalletActionsQueryPostQueryWalletActionsRequestBody
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
    api_instance = openapi_client.WalletApi(api_client)
    wallet_action_wallet_action_service_v1_rise_wallet_actions_query_post_query_wallet_actions_request_body = openapi_client.WalletActionWalletActionServiceV1RiseWalletActionsQueryPostQueryWalletActionsRequestBody() # WalletActionWalletActionServiceV1RiseWalletActionsQueryPostQueryWalletActionsRequestBody | 

    try:
        api_response = api_instance.query_wallets(wallet_action_wallet_action_service_v1_rise_wallet_actions_query_post_query_wallet_actions_request_body)
        print("The response of WalletApi->query_wallets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->query_wallets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_action_wallet_action_service_v1_rise_wallet_actions_query_post_query_wallet_actions_request_body** | [**WalletActionWalletActionServiceV1RiseWalletActionsQueryPostQueryWalletActionsRequestBody**](WalletActionWalletActionServiceV1RiseWalletActionsQueryPostQueryWalletActionsRequestBody.md)|  | 

### Return type

[**QueryWalletsResponse1**](QueryWalletsResponse1.md)

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

# **query_wallets_by_contact**
> QueryWalletsByContactResponse1 query_wallets_by_contact(wallet_wallet_service_v1_rise_wallets_query_by_contact_post_query_wallets_by_contact_request_body)

Query wallets by contact using [API Query Language](https://platform.rise.ai/docs/#tag/About-API-Query-Language).
The result is a list of wallets with gift card and contact information.

### Example


```python
import openapi_client
from openapi_client.models.query_wallets_by_contact_response1 import QueryWalletsByContactResponse1
from openapi_client.models.wallet_wallet_service_v1_rise_wallets_query_by_contact_post_query_wallets_by_contact_request_body import WalletWalletServiceV1RiseWalletsQueryByContactPostQueryWalletsByContactRequestBody
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
    api_instance = openapi_client.WalletApi(api_client)
    wallet_wallet_service_v1_rise_wallets_query_by_contact_post_query_wallets_by_contact_request_body = openapi_client.WalletWalletServiceV1RiseWalletsQueryByContactPostQueryWalletsByContactRequestBody() # WalletWalletServiceV1RiseWalletsQueryByContactPostQueryWalletsByContactRequestBody | 

    try:
        api_response = api_instance.query_wallets_by_contact(wallet_wallet_service_v1_rise_wallets_query_by_contact_post_query_wallets_by_contact_request_body)
        print("The response of WalletApi->query_wallets_by_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->query_wallets_by_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_wallet_service_v1_rise_wallets_query_by_contact_post_query_wallets_by_contact_request_body** | [**WalletWalletServiceV1RiseWalletsQueryByContactPostQueryWalletsByContactRequestBody**](WalletWalletServiceV1RiseWalletsQueryByContactPostQueryWalletsByContactRequestBody.md)|  | 

### Return type

[**QueryWalletsByContactResponse1**](QueryWalletsByContactResponse1.md)

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

