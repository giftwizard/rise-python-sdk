# openapi_client.GiftCardApi

All URIs are relative to *https://platform.rise.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_gift_cards**](GiftCardApi.md#count_gift_cards) | **POST** /v1/rise/gift-cards/count | 
[**create_gift_card**](GiftCardApi.md#create_gift_card) | **POST** /v1/rise/gift-cards | 
[**decrease_balance**](GiftCardApi.md#decrease_balance) | **POST** /v1/rise/gift-cards/{transactionGiftCardId}/decrease | 
[**disable_gift_card**](GiftCardApi.md#disable_gift_card) | **POST** /v1/rise/gift-cards/{giftCardId}/disable | 
[**get_gift_card**](GiftCardApi.md#get_gift_card) | **GET** /v1/rise/gift-cards/{giftCardId} | 
[**increase_balance**](GiftCardApi.md#increase_balance) | **POST** /v1/rise/gift-cards/{transactionGiftCardId}/increase | 
[**query_gift_cards**](GiftCardApi.md#query_gift_cards) | **POST** /v1/rise/gift-cards/query | 
[**search_gift_cards**](GiftCardApi.md#search_gift_cards) | **POST** /v1/rise/gift-cards/search | 
[**update_gift_card**](GiftCardApi.md#update_gift_card) | **PATCH** /v1/rise/gift-cards/{giftCardId} | 


# **count_gift_cards**
> CountGiftCardsResponse1 count_gift_cards(gift_card_gift_card_service_v1_rise_gift_cards_count_post_count_gift_cards_request_body)

TODO: change to Rise domain when it's ready
Count GiftCards that match the given [API Query Language](https://platform.rise.ai/docs/#tag/About-API-Query-Language) filter.

### Example


```python
import openapi_client
from openapi_client.models.count_gift_cards_response1 import CountGiftCardsResponse1
from openapi_client.models.gift_card_gift_card_service_v1_rise_gift_cards_count_post_count_gift_cards_request_body import GiftCardGiftCardServiceV1RiseGiftCardsCountPostCountGiftCardsRequestBody
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
    api_instance = openapi_client.GiftCardApi(api_client)
    gift_card_gift_card_service_v1_rise_gift_cards_count_post_count_gift_cards_request_body = openapi_client.GiftCardGiftCardServiceV1RiseGiftCardsCountPostCountGiftCardsRequestBody() # GiftCardGiftCardServiceV1RiseGiftCardsCountPostCountGiftCardsRequestBody | 

    try:
        api_response = api_instance.count_gift_cards(gift_card_gift_card_service_v1_rise_gift_cards_count_post_count_gift_cards_request_body)
        print("The response of GiftCardApi->count_gift_cards:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GiftCardApi->count_gift_cards: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gift_card_gift_card_service_v1_rise_gift_cards_count_post_count_gift_cards_request_body** | [**GiftCardGiftCardServiceV1RiseGiftCardsCountPostCountGiftCardsRequestBody**](GiftCardGiftCardServiceV1RiseGiftCardsCountPostCountGiftCardsRequestBody.md)|  | 

### Return type

[**CountGiftCardsResponse1**](CountGiftCardsResponse1.md)

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

# **create_gift_card**
> CreateGiftCardResponse1 create_gift_card(gift_card_gift_card_service_v1_rise_gift_cards_post_create_gift_card_request_body)

Creates a new GiftCard.

### Example


```python
import openapi_client
from openapi_client.models.create_gift_card_response1 import CreateGiftCardResponse1
from openapi_client.models.gift_card_gift_card_service_v1_rise_gift_cards_post_create_gift_card_request_body import GiftCardGiftCardServiceV1RiseGiftCardsPostCreateGiftCardRequestBody
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
    api_instance = openapi_client.GiftCardApi(api_client)
    gift_card_gift_card_service_v1_rise_gift_cards_post_create_gift_card_request_body = openapi_client.GiftCardGiftCardServiceV1RiseGiftCardsPostCreateGiftCardRequestBody() # GiftCardGiftCardServiceV1RiseGiftCardsPostCreateGiftCardRequestBody | 

    try:
        api_response = api_instance.create_gift_card(gift_card_gift_card_service_v1_rise_gift_cards_post_create_gift_card_request_body)
        print("The response of GiftCardApi->create_gift_card:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GiftCardApi->create_gift_card: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gift_card_gift_card_service_v1_rise_gift_cards_post_create_gift_card_request_body** | [**GiftCardGiftCardServiceV1RiseGiftCardsPostCreateGiftCardRequestBody**](GiftCardGiftCardServiceV1RiseGiftCardsPostCreateGiftCardRequestBody.md)|  | 

### Return type

[**CreateGiftCardResponse1**](CreateGiftCardResponse1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - The request was successful |  -  |
**428** | Precondition Required - Precondition failed  Possible error codes: &#x60;INVALID_CODE&#x60;, &#x60;INVALID_EXPIRATION_DATE&#x60;, &#x60;EXISTING_IDEMPOTENCY_KEY&#x60; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **decrease_balance**
> DecreaseBalanceResponse1 decrease_balance(transaction_gift_card_id, gift_card_gift_card_service_v1_rise_gift_cards_transaction_gift_card_id_decrease_post_decrease_balance_request_body)

Subtracts from the GiftCard balance and creates a balance Transaction.

### Example


```python
import openapi_client
from openapi_client.models.decrease_balance_response1 import DecreaseBalanceResponse1
from openapi_client.models.gift_card_gift_card_service_v1_rise_gift_cards_transaction_gift_card_id_decrease_post_decrease_balance_request_body import GiftCardGiftCardServiceV1RiseGiftCardsTransactionGiftCardIdDecreasePostDecreaseBalanceRequestBody
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
    api_instance = openapi_client.GiftCardApi(api_client)
    transaction_gift_card_id = 'transaction_gift_card_id_example' # str | Unique ID of the gift card associated with this transaction.
    gift_card_gift_card_service_v1_rise_gift_cards_transaction_gift_card_id_decrease_post_decrease_balance_request_body = openapi_client.GiftCardGiftCardServiceV1RiseGiftCardsTransactionGiftCardIdDecreasePostDecreaseBalanceRequestBody() # GiftCardGiftCardServiceV1RiseGiftCardsTransactionGiftCardIdDecreasePostDecreaseBalanceRequestBody | 

    try:
        api_response = api_instance.decrease_balance(transaction_gift_card_id, gift_card_gift_card_service_v1_rise_gift_cards_transaction_gift_card_id_decrease_post_decrease_balance_request_body)
        print("The response of GiftCardApi->decrease_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GiftCardApi->decrease_balance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_gift_card_id** | **str**| Unique ID of the gift card associated with this transaction. | 
 **gift_card_gift_card_service_v1_rise_gift_cards_transaction_gift_card_id_decrease_post_decrease_balance_request_body** | [**GiftCardGiftCardServiceV1RiseGiftCardsTransactionGiftCardIdDecreasePostDecreaseBalanceRequestBody**](GiftCardGiftCardServiceV1RiseGiftCardsTransactionGiftCardIdDecreasePostDecreaseBalanceRequestBody.md)|  | 

### Return type

[**DecreaseBalanceResponse1**](DecreaseBalanceResponse1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - The request was successful |  -  |
**428** | Precondition Required - Precondition failed  Possible error codes: &#x60;EXISTING_IDEMPOTENCY_KEY&#x60;, &#x60;INSUFFICIENT_FUNDS&#x60; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_gift_card**
> DisableGiftCardResponse1 disable_gift_card(gift_card_id, body)

Disable a GiftCard. It cannot be re-enabled.

### Example


```python
import openapi_client
from openapi_client.models.disable_gift_card_response1 import DisableGiftCardResponse1
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
    api_instance = openapi_client.GiftCardApi(api_client)
    gift_card_id = 'gift_card_id_example' # str | The ID of the GiftCard to disable.
    body = None # object | 

    try:
        api_response = api_instance.disable_gift_card(gift_card_id, body)
        print("The response of GiftCardApi->disable_gift_card:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GiftCardApi->disable_gift_card: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gift_card_id** | **str**| The ID of the GiftCard to disable. | 
 **body** | **object**|  | 

### Return type

[**DisableGiftCardResponse1**](DisableGiftCardResponse1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - The request was successful |  -  |
**404** | Not Found - Resource not found  Possible error codes: &#x60;GIFT_CARD_NOT_FOUND&#x60; |  -  |
**428** | Precondition Required - Precondition failed  Possible error codes: &#x60;GIFT_CARD_DISABLED&#x60;, &#x60;GIFT_CARD_EXPIRED&#x60; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gift_card**
> GetGiftCardResponse1 get_gift_card(gift_card_id)

Get a GiftCard by ID.

### Example


```python
import openapi_client
from openapi_client.models.get_gift_card_response1 import GetGiftCardResponse1
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
    api_instance = openapi_client.GiftCardApi(api_client)
    gift_card_id = 'gift_card_id_example' # str | The ID of the GiftCard to retrieve.

    try:
        api_response = api_instance.get_gift_card(gift_card_id)
        print("The response of GiftCardApi->get_gift_card:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GiftCardApi->get_gift_card: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gift_card_id** | **str**| The ID of the GiftCard to retrieve. | 

### Return type

[**GetGiftCardResponse1**](GetGiftCardResponse1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - The request was successful |  -  |
**404** | Not Found - Resource not found  Possible error codes: &#x60;GIFT_CARD_NOT_FOUND&#x60; |  -  |
**428** | Precondition Required - Precondition failed  Possible error codes: &#x60;GIFT_CARD_DISABLED&#x60;, &#x60;GIFT_CARD_EXPIRED&#x60; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **increase_balance**
> IncreaseBalanceResponse1 increase_balance(transaction_gift_card_id, gift_card_gift_card_service_v1_rise_gift_cards_transaction_gift_card_id_increase_post_increase_balance_request_body)

Adds to the GiftCard balance and creates a balance Transaction.

### Example


```python
import openapi_client
from openapi_client.models.gift_card_gift_card_service_v1_rise_gift_cards_transaction_gift_card_id_increase_post_increase_balance_request_body import GiftCardGiftCardServiceV1RiseGiftCardsTransactionGiftCardIdIncreasePostIncreaseBalanceRequestBody
from openapi_client.models.increase_balance_response1 import IncreaseBalanceResponse1
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
    api_instance = openapi_client.GiftCardApi(api_client)
    transaction_gift_card_id = 'transaction_gift_card_id_example' # str | Unique ID of the gift card associated with this transaction.
    gift_card_gift_card_service_v1_rise_gift_cards_transaction_gift_card_id_increase_post_increase_balance_request_body = openapi_client.GiftCardGiftCardServiceV1RiseGiftCardsTransactionGiftCardIdIncreasePostIncreaseBalanceRequestBody() # GiftCardGiftCardServiceV1RiseGiftCardsTransactionGiftCardIdIncreasePostIncreaseBalanceRequestBody | 

    try:
        api_response = api_instance.increase_balance(transaction_gift_card_id, gift_card_gift_card_service_v1_rise_gift_cards_transaction_gift_card_id_increase_post_increase_balance_request_body)
        print("The response of GiftCardApi->increase_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GiftCardApi->increase_balance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_gift_card_id** | **str**| Unique ID of the gift card associated with this transaction. | 
 **gift_card_gift_card_service_v1_rise_gift_cards_transaction_gift_card_id_increase_post_increase_balance_request_body** | [**GiftCardGiftCardServiceV1RiseGiftCardsTransactionGiftCardIdIncreasePostIncreaseBalanceRequestBody**](GiftCardGiftCardServiceV1RiseGiftCardsTransactionGiftCardIdIncreasePostIncreaseBalanceRequestBody.md)|  | 

### Return type

[**IncreaseBalanceResponse1**](IncreaseBalanceResponse1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - The request was successful |  -  |
**428** | Precondition Required - Precondition failed  Possible error codes: &#x60;EXISTING_IDEMPOTENCY_KEY&#x60;, &#x60;INVALID_GIFT_CARD_BALANCE&#x60; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_gift_cards**
> QueryGiftCardsResponse1 query_gift_cards(gift_card_gift_card_service_v1_rise_gift_cards_query_post_query_gift_cards_request_body)

Query GiftCards using [API Query Language](https://platform.rise.ai/docs/#tag/About-API-Query-Language).

### Example


```python
import openapi_client
from openapi_client.models.gift_card_gift_card_service_v1_rise_gift_cards_query_post_query_gift_cards_request_body import GiftCardGiftCardServiceV1RiseGiftCardsQueryPostQueryGiftCardsRequestBody
from openapi_client.models.query_gift_cards_response1 import QueryGiftCardsResponse1
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
    api_instance = openapi_client.GiftCardApi(api_client)
    gift_card_gift_card_service_v1_rise_gift_cards_query_post_query_gift_cards_request_body = openapi_client.GiftCardGiftCardServiceV1RiseGiftCardsQueryPostQueryGiftCardsRequestBody() # GiftCardGiftCardServiceV1RiseGiftCardsQueryPostQueryGiftCardsRequestBody | 

    try:
        api_response = api_instance.query_gift_cards(gift_card_gift_card_service_v1_rise_gift_cards_query_post_query_gift_cards_request_body)
        print("The response of GiftCardApi->query_gift_cards:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GiftCardApi->query_gift_cards: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gift_card_gift_card_service_v1_rise_gift_cards_query_post_query_gift_cards_request_body** | [**GiftCardGiftCardServiceV1RiseGiftCardsQueryPostQueryGiftCardsRequestBody**](GiftCardGiftCardServiceV1RiseGiftCardsQueryPostQueryGiftCardsRequestBody.md)|  | 

### Return type

[**QueryGiftCardsResponse1**](QueryGiftCardsResponse1.md)

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

# **search_gift_cards**
> SearchGiftCardsResponse1 search_gift_cards(gift_card_gift_card_service_v1_rise_gift_cards_search_post_search_gift_cards_request_body)

Search for GiftCards by field.

### Example


```python
import openapi_client
from openapi_client.models.gift_card_gift_card_service_v1_rise_gift_cards_search_post_search_gift_cards_request_body import GiftCardGiftCardServiceV1RiseGiftCardsSearchPostSearchGiftCardsRequestBody
from openapi_client.models.search_gift_cards_response1 import SearchGiftCardsResponse1
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
    api_instance = openapi_client.GiftCardApi(api_client)
    gift_card_gift_card_service_v1_rise_gift_cards_search_post_search_gift_cards_request_body = openapi_client.GiftCardGiftCardServiceV1RiseGiftCardsSearchPostSearchGiftCardsRequestBody() # GiftCardGiftCardServiceV1RiseGiftCardsSearchPostSearchGiftCardsRequestBody | 

    try:
        api_response = api_instance.search_gift_cards(gift_card_gift_card_service_v1_rise_gift_cards_search_post_search_gift_cards_request_body)
        print("The response of GiftCardApi->search_gift_cards:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GiftCardApi->search_gift_cards: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gift_card_gift_card_service_v1_rise_gift_cards_search_post_search_gift_cards_request_body** | [**GiftCardGiftCardServiceV1RiseGiftCardsSearchPostSearchGiftCardsRequestBody**](GiftCardGiftCardServiceV1RiseGiftCardsSearchPostSearchGiftCardsRequestBody.md)|  | 

### Return type

[**SearchGiftCardsResponse1**](SearchGiftCardsResponse1.md)

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

# **update_gift_card**
> UpdateGiftCardResponse1 update_gift_card(gift_card_id, gift_card_gift_card_service_v1_rise_gift_cards_gift_card_id_patch_update_gift_card_request_body)

Update a GiftCard, supports partial update.
Pass the latest `revision` for a successful update.

### Example


```python
import openapi_client
from openapi_client.models.gift_card_gift_card_service_v1_rise_gift_cards_gift_card_id_patch_update_gift_card_request_body import GiftCardGiftCardServiceV1RiseGiftCardsGiftCardIdPatchUpdateGiftCardRequestBody
from openapi_client.models.update_gift_card_response1 import UpdateGiftCardResponse1
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
    api_instance = openapi_client.GiftCardApi(api_client)
    gift_card_id = 'gift_card_id_example' # str | The ID of the GiftCard to update.
    gift_card_gift_card_service_v1_rise_gift_cards_gift_card_id_patch_update_gift_card_request_body = openapi_client.GiftCardGiftCardServiceV1RiseGiftCardsGiftCardIdPatchUpdateGiftCardRequestBody() # GiftCardGiftCardServiceV1RiseGiftCardsGiftCardIdPatchUpdateGiftCardRequestBody | 

    try:
        api_response = api_instance.update_gift_card(gift_card_id, gift_card_gift_card_service_v1_rise_gift_cards_gift_card_id_patch_update_gift_card_request_body)
        print("The response of GiftCardApi->update_gift_card:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GiftCardApi->update_gift_card: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gift_card_id** | **str**| The ID of the GiftCard to update. | 
 **gift_card_gift_card_service_v1_rise_gift_cards_gift_card_id_patch_update_gift_card_request_body** | [**GiftCardGiftCardServiceV1RiseGiftCardsGiftCardIdPatchUpdateGiftCardRequestBody**](GiftCardGiftCardServiceV1RiseGiftCardsGiftCardIdPatchUpdateGiftCardRequestBody.md)|  | 

### Return type

[**UpdateGiftCardResponse1**](UpdateGiftCardResponse1.md)

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

