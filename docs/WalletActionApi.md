# openapi_client.WalletActionApi

All URIs are relative to *https://platform.rise.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_wallet_action**](WalletActionApi.md#create_wallet_action) | **POST** /v1/rise/wallet_actions | 
[**create_wallet_action_by_customer_reference**](WalletActionApi.md#create_wallet_action_by_customer_reference) | **POST** /v1/rise/wallet_actions/by_customer_reference | 
[**disable_wallet_action**](WalletActionApi.md#disable_wallet_action) | **POST** /v1/rise/wallet_actions/{walletActionId}/disable | 
[**get_refundable_amounts**](WalletActionApi.md#get_refundable_amounts) | **GET** /v1/rise/wallet_actions/refund/amounts | 
[**query_unredeemed_wallet_actions**](WalletActionApi.md#query_unredeemed_wallet_actions) | **POST** /v1/rise/wallet_actions/query/unredeemed | 
[**query_wallet_actions**](WalletActionApi.md#query_wallet_actions) | **POST** /v1/rise/wallet_actions/query | 
[**query_wallet_actions_balances**](WalletActionApi.md#query_wallet_actions_balances) | **POST** /v1/rise/wallet_actions/query/balances | 
[**update_wallet_action**](WalletActionApi.md#update_wallet_action) | **PATCH** /v1/rise/wallet_actions/{walletActionId} | 


# **create_wallet_action**
> CreateWalletActionResponse1 create_wallet_action(wallet_action_wallet_action_service_v1_rise_wallet_actions_post_create_wallet_action_request_body)

Creates a new WalletAction.

### Example


```python
import openapi_client
from openapi_client.models.create_wallet_action_response1 import CreateWalletActionResponse1
from openapi_client.models.wallet_action_wallet_action_service_v1_rise_wallet_actions_post_create_wallet_action_request_body import WalletActionWalletActionServiceV1RiseWalletActionsPostCreateWalletActionRequestBody
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
    api_instance = openapi_client.WalletActionApi(api_client)
    wallet_action_wallet_action_service_v1_rise_wallet_actions_post_create_wallet_action_request_body = openapi_client.WalletActionWalletActionServiceV1RiseWalletActionsPostCreateWalletActionRequestBody() # WalletActionWalletActionServiceV1RiseWalletActionsPostCreateWalletActionRequestBody | 

    try:
        api_response = api_instance.create_wallet_action(wallet_action_wallet_action_service_v1_rise_wallet_actions_post_create_wallet_action_request_body)
        print("The response of WalletActionApi->create_wallet_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletActionApi->create_wallet_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_action_wallet_action_service_v1_rise_wallet_actions_post_create_wallet_action_request_body** | [**WalletActionWalletActionServiceV1RiseWalletActionsPostCreateWalletActionRequestBody**](WalletActionWalletActionServiceV1RiseWalletActionsPostCreateWalletActionRequestBody.md)|  | 

### Return type

[**CreateWalletActionResponse1**](CreateWalletActionResponse1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - The request was successful |  -  |
**400** | Bad Request - Invalid input or parameters  Possible error codes: &#x60;EXPIRATION_DATE_IN_THE_PAST&#x60;, &#x60;START_LATER_THAN_EXPIRATION&#x60;, &#x60;DISABLED_AT_DATE_SET&#x60; |  -  |
**409** | Conflict - Request conflicts with current state  Possible error codes: &#x60;EXISTING_IDEMPOTENCY_KEY&#x60; |  -  |
**428** | Precondition Required - Precondition failed  Possible error codes: &#x60;WALLET_ACTION_EXCEEDS_MAXIMUM_BALANCE&#x60; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_wallet_action_by_customer_reference**
> CreateWalletActionByCustomerReferenceResponse1 create_wallet_action_by_customer_reference(wallet_action_wallet_action_service_v1_rise_wallet_actions_by_customer_reference_post_create_wallet_action_by_customer_reference_request_body)

Creates a new WalletAction by customer reference instead of wallet ID.
If the customer already has a wallet, the action will be created on that wallet.
If the customer does not have a wallet, a new wallet will be created for them.

### Example


```python
import openapi_client
from openapi_client.models.create_wallet_action_by_customer_reference_response1 import CreateWalletActionByCustomerReferenceResponse1
from openapi_client.models.wallet_action_wallet_action_service_v1_rise_wallet_actions_by_customer_reference_post_create_wallet_action_by_customer_reference_request_body import WalletActionWalletActionServiceV1RiseWalletActionsByCustomerReferencePostCreateWalletActionByCustomerReferenceRequestBody
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
    api_instance = openapi_client.WalletActionApi(api_client)
    wallet_action_wallet_action_service_v1_rise_wallet_actions_by_customer_reference_post_create_wallet_action_by_customer_reference_request_body = openapi_client.WalletActionWalletActionServiceV1RiseWalletActionsByCustomerReferencePostCreateWalletActionByCustomerReferenceRequestBody() # WalletActionWalletActionServiceV1RiseWalletActionsByCustomerReferencePostCreateWalletActionByCustomerReferenceRequestBody | 

    try:
        api_response = api_instance.create_wallet_action_by_customer_reference(wallet_action_wallet_action_service_v1_rise_wallet_actions_by_customer_reference_post_create_wallet_action_by_customer_reference_request_body)
        print("The response of WalletActionApi->create_wallet_action_by_customer_reference:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletActionApi->create_wallet_action_by_customer_reference: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_action_wallet_action_service_v1_rise_wallet_actions_by_customer_reference_post_create_wallet_action_by_customer_reference_request_body** | [**WalletActionWalletActionServiceV1RiseWalletActionsByCustomerReferencePostCreateWalletActionByCustomerReferenceRequestBody**](WalletActionWalletActionServiceV1RiseWalletActionsByCustomerReferencePostCreateWalletActionByCustomerReferenceRequestBody.md)|  | 

### Return type

[**CreateWalletActionByCustomerReferenceResponse1**](CreateWalletActionByCustomerReferenceResponse1.md)

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

# **disable_wallet_action**
> DisableWalletActionResponse1 disable_wallet_action(wallet_action_id, wallet_action_wallet_action_service_v1_rise_wallet_actions_wallet_action_id_disable_post_disable_wallet_action_request_body)

Disable a WalletAction immediately and deduct the remaining balance from the wallet.

### Example


```python
import openapi_client
from openapi_client.models.disable_wallet_action_response1 import DisableWalletActionResponse1
from openapi_client.models.wallet_action_wallet_action_service_v1_rise_wallet_actions_wallet_action_id_disable_post_disable_wallet_action_request_body import WalletActionWalletActionServiceV1RiseWalletActionsWalletActionIdDisablePostDisableWalletActionRequestBody
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
    api_instance = openapi_client.WalletActionApi(api_client)
    wallet_action_id = 'wallet_action_id_example' # str | ID of the WalletAction to delete.
    wallet_action_wallet_action_service_v1_rise_wallet_actions_wallet_action_id_disable_post_disable_wallet_action_request_body = openapi_client.WalletActionWalletActionServiceV1RiseWalletActionsWalletActionIdDisablePostDisableWalletActionRequestBody() # WalletActionWalletActionServiceV1RiseWalletActionsWalletActionIdDisablePostDisableWalletActionRequestBody | 

    try:
        api_response = api_instance.disable_wallet_action(wallet_action_id, wallet_action_wallet_action_service_v1_rise_wallet_actions_wallet_action_id_disable_post_disable_wallet_action_request_body)
        print("The response of WalletActionApi->disable_wallet_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletActionApi->disable_wallet_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_action_id** | **str**| ID of the WalletAction to delete. | 
 **wallet_action_wallet_action_service_v1_rise_wallet_actions_wallet_action_id_disable_post_disable_wallet_action_request_body** | [**WalletActionWalletActionServiceV1RiseWalletActionsWalletActionIdDisablePostDisableWalletActionRequestBody**](WalletActionWalletActionServiceV1RiseWalletActionsWalletActionIdDisablePostDisableWalletActionRequestBody.md)|  | 

### Return type

[**DisableWalletActionResponse1**](DisableWalletActionResponse1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - The request was successful |  -  |
**428** | Precondition Required - Precondition failed  Possible error codes: &#x60;WALLET_ACTION_ALREADY_EXPIRED&#x60;, &#x60;WALLET_ACTION_NOT_ACTIVE&#x60; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_refundable_amounts**
> GetRefundableAmountsResponse1 get_refundable_amounts(transaction_id)



### Example


```python
import openapi_client
from openapi_client.models.get_refundable_amounts_response1 import GetRefundableAmountsResponse1
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
    api_instance = openapi_client.WalletActionApi(api_client)
    transaction_id = 'transaction_id_example' # str | ID of the transaction to get refundable amounts for

    try:
        api_response = api_instance.get_refundable_amounts(transaction_id)
        print("The response of WalletActionApi->get_refundable_amounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletActionApi->get_refundable_amounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**| ID of the transaction to get refundable amounts for | 

### Return type

[**GetRefundableAmountsResponse1**](GetRefundableAmountsResponse1.md)

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

# **query_unredeemed_wallet_actions**
> QueryUnredeemedWalletActionsResponse1 query_unredeemed_wallet_actions(wallet_action_wallet_action_service_v1_rise_wallet_actions_query_unredeemed_post_query_unredeemed_wallet_actions_request_body)

Query wallet actions that have not been entirely redeemed using [API Query Language](https://platform.rise.ai/docs/#tag/About-API-Query-Language).
Results are enriched with the remaining balance of each wallet action.
Note:
The returned result may contain fewer items than the requested page limit—or even be empty—while still providing a next cursor, because of in memory filtering.
Always check the next cursor to determine if there are more items to fetch.

### Example


```python
import openapi_client
from openapi_client.models.query_unredeemed_wallet_actions_response1 import QueryUnredeemedWalletActionsResponse1
from openapi_client.models.wallet_action_wallet_action_service_v1_rise_wallet_actions_query_unredeemed_post_query_unredeemed_wallet_actions_request_body import WalletActionWalletActionServiceV1RiseWalletActionsQueryUnredeemedPostQueryUnredeemedWalletActionsRequestBody
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
    api_instance = openapi_client.WalletActionApi(api_client)
    wallet_action_wallet_action_service_v1_rise_wallet_actions_query_unredeemed_post_query_unredeemed_wallet_actions_request_body = openapi_client.WalletActionWalletActionServiceV1RiseWalletActionsQueryUnredeemedPostQueryUnredeemedWalletActionsRequestBody() # WalletActionWalletActionServiceV1RiseWalletActionsQueryUnredeemedPostQueryUnredeemedWalletActionsRequestBody | 

    try:
        api_response = api_instance.query_unredeemed_wallet_actions(wallet_action_wallet_action_service_v1_rise_wallet_actions_query_unredeemed_post_query_unredeemed_wallet_actions_request_body)
        print("The response of WalletActionApi->query_unredeemed_wallet_actions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletActionApi->query_unredeemed_wallet_actions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_action_wallet_action_service_v1_rise_wallet_actions_query_unredeemed_post_query_unredeemed_wallet_actions_request_body** | [**WalletActionWalletActionServiceV1RiseWalletActionsQueryUnredeemedPostQueryUnredeemedWalletActionsRequestBody**](WalletActionWalletActionServiceV1RiseWalletActionsQueryUnredeemedPostQueryUnredeemedWalletActionsRequestBody.md)|  | 

### Return type

[**QueryUnredeemedWalletActionsResponse1**](QueryUnredeemedWalletActionsResponse1.md)

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

# **query_wallet_actions**
> QueryWalletActionResponse1 query_wallet_actions(wallet_action_wallet_action_service_v1_rise_wallet_actions_query_post_query_wallet_actions_request_body)

Query WalletActions using [API Query Language](https://platform.rise.ai/docs/#tag/About-API-Query-Language).

### Example


```python
import openapi_client
from openapi_client.models.query_wallet_action_response1 import QueryWalletActionResponse1
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
    api_instance = openapi_client.WalletActionApi(api_client)
    wallet_action_wallet_action_service_v1_rise_wallet_actions_query_post_query_wallet_actions_request_body = openapi_client.WalletActionWalletActionServiceV1RiseWalletActionsQueryPostQueryWalletActionsRequestBody() # WalletActionWalletActionServiceV1RiseWalletActionsQueryPostQueryWalletActionsRequestBody | 

    try:
        api_response = api_instance.query_wallet_actions(wallet_action_wallet_action_service_v1_rise_wallet_actions_query_post_query_wallet_actions_request_body)
        print("The response of WalletActionApi->query_wallet_actions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletActionApi->query_wallet_actions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_action_wallet_action_service_v1_rise_wallet_actions_query_post_query_wallet_actions_request_body** | [**WalletActionWalletActionServiceV1RiseWalletActionsQueryPostQueryWalletActionsRequestBody**](WalletActionWalletActionServiceV1RiseWalletActionsQueryPostQueryWalletActionsRequestBody.md)|  | 

### Return type

[**QueryWalletActionResponse1**](QueryWalletActionResponse1.md)

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

# **query_wallet_actions_balances**
> QueryWalletActionBalancesResponse1 query_wallet_actions_balances(wallet_action_wallet_action_service_v1_rise_wallet_actions_query_balances_post_query_wallet_actions_balances_request_body)

Query all WalletActions using [API Query Language](https://platform.rise.ai/docs/#tag/About-API-Query-Language).
Results are enriched with the remaining balance of each WalletAction.

### Example


```python
import openapi_client
from openapi_client.models.query_wallet_action_balances_response1 import QueryWalletActionBalancesResponse1
from openapi_client.models.wallet_action_wallet_action_service_v1_rise_wallet_actions_query_balances_post_query_wallet_actions_balances_request_body import WalletActionWalletActionServiceV1RiseWalletActionsQueryBalancesPostQueryWalletActionsBalancesRequestBody
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
    api_instance = openapi_client.WalletActionApi(api_client)
    wallet_action_wallet_action_service_v1_rise_wallet_actions_query_balances_post_query_wallet_actions_balances_request_body = openapi_client.WalletActionWalletActionServiceV1RiseWalletActionsQueryBalancesPostQueryWalletActionsBalancesRequestBody() # WalletActionWalletActionServiceV1RiseWalletActionsQueryBalancesPostQueryWalletActionsBalancesRequestBody | 

    try:
        api_response = api_instance.query_wallet_actions_balances(wallet_action_wallet_action_service_v1_rise_wallet_actions_query_balances_post_query_wallet_actions_balances_request_body)
        print("The response of WalletActionApi->query_wallet_actions_balances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletActionApi->query_wallet_actions_balances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_action_wallet_action_service_v1_rise_wallet_actions_query_balances_post_query_wallet_actions_balances_request_body** | [**WalletActionWalletActionServiceV1RiseWalletActionsQueryBalancesPostQueryWalletActionsBalancesRequestBody**](WalletActionWalletActionServiceV1RiseWalletActionsQueryBalancesPostQueryWalletActionsBalancesRequestBody.md)|  | 

### Return type

[**QueryWalletActionBalancesResponse1**](QueryWalletActionBalancesResponse1.md)

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

# **update_wallet_action**
> UpdateWalletActionResponse1 update_wallet_action(wallet_action_id, wallet_action_wallet_action_service_v1_rise_wallet_actions_wallet_action_id_patch_update_wallet_action_request_body)

Update a WalletAction, supports partial update.
Pass the latest `revision` for a successful update.

### Example


```python
import openapi_client
from openapi_client.models.update_wallet_action_response1 import UpdateWalletActionResponse1
from openapi_client.models.wallet_action_wallet_action_service_v1_rise_wallet_actions_wallet_action_id_patch_update_wallet_action_request_body import WalletActionWalletActionServiceV1RiseWalletActionsWalletActionIdPatchUpdateWalletActionRequestBody
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
    api_instance = openapi_client.WalletActionApi(api_client)
    wallet_action_id = 'wallet_action_id_example' # str | WalletAction ID.
    wallet_action_wallet_action_service_v1_rise_wallet_actions_wallet_action_id_patch_update_wallet_action_request_body = openapi_client.WalletActionWalletActionServiceV1RiseWalletActionsWalletActionIdPatchUpdateWalletActionRequestBody() # WalletActionWalletActionServiceV1RiseWalletActionsWalletActionIdPatchUpdateWalletActionRequestBody | 

    try:
        api_response = api_instance.update_wallet_action(wallet_action_id, wallet_action_wallet_action_service_v1_rise_wallet_actions_wallet_action_id_patch_update_wallet_action_request_body)
        print("The response of WalletActionApi->update_wallet_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletActionApi->update_wallet_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_action_id** | **str**| WalletAction ID. | 
 **wallet_action_wallet_action_service_v1_rise_wallet_actions_wallet_action_id_patch_update_wallet_action_request_body** | [**WalletActionWalletActionServiceV1RiseWalletActionsWalletActionIdPatchUpdateWalletActionRequestBody**](WalletActionWalletActionServiceV1RiseWalletActionsWalletActionIdPatchUpdateWalletActionRequestBody.md)|  | 

### Return type

[**UpdateWalletActionResponse1**](UpdateWalletActionResponse1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - The request was successful |  -  |
**400** | Bad Request - Invalid input or parameters  Possible error codes: &#x60;START_DATE_IN_THE_PAST&#x60;, &#x60;EXPIRATION_DATE_IN_THE_PAST&#x60;, &#x60;START_LATER_THAN_EXPIRATION&#x60; |  -  |
**428** | Precondition Required - Precondition failed  Possible error codes: &#x60;WALLET_ACTION_ALREADY_ACTIVE&#x60;, &#x60;WALLET_ACTION_ALREADY_EXPIRED&#x60; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

