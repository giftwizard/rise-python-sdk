# openapi_client.TransactionApi

All URIs are relative to *https://platform.rise.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query_transactions**](TransactionApi.md#query_transactions) | **POST** /v1/rise/gift-cards/transactions/query | 


# **query_transactions**
> QueryTransactionsResponse1 query_transactions(transaction_transaction_query_service_v1_rise_gift_cards_transactions_query_post_query_transactions_request_body)

Query Transactions using [API Query Language](https://platform.rise.ai/docs/#tag/About-API-Query-Language).

### Example


```python
import openapi_client
from openapi_client.models.query_transactions_response1 import QueryTransactionsResponse1
from openapi_client.models.transaction_transaction_query_service_v1_rise_gift_cards_transactions_query_post_query_transactions_request_body import TransactionTransactionQueryServiceV1RiseGiftCardsTransactionsQueryPostQueryTransactionsRequestBody
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
    api_instance = openapi_client.TransactionApi(api_client)
    transaction_transaction_query_service_v1_rise_gift_cards_transactions_query_post_query_transactions_request_body = openapi_client.TransactionTransactionQueryServiceV1RiseGiftCardsTransactionsQueryPostQueryTransactionsRequestBody() # TransactionTransactionQueryServiceV1RiseGiftCardsTransactionsQueryPostQueryTransactionsRequestBody | 

    try:
        api_response = api_instance.query_transactions(transaction_transaction_query_service_v1_rise_gift_cards_transactions_query_post_query_transactions_request_body)
        print("The response of TransactionApi->query_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionApi->query_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_transaction_query_service_v1_rise_gift_cards_transactions_query_post_query_transactions_request_body** | [**TransactionTransactionQueryServiceV1RiseGiftCardsTransactionsQueryPostQueryTransactionsRequestBody**](TransactionTransactionQueryServiceV1RiseGiftCardsTransactionsQueryPostQueryTransactionsRequestBody.md)|  | 

### Return type

[**QueryTransactionsResponse1**](QueryTransactionsResponse1.md)

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

