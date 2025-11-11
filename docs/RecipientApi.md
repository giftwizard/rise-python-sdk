# openapi_client.RecipientApi

All URIs are relative to *https://platform.rise.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_recipient**](RecipientApi.md#create_recipient) | **POST** /v1/rise/recipients | 
[**delete_recipient**](RecipientApi.md#delete_recipient) | **DELETE** /v1/rise/recipients/{recipientId} | 
[**get_recipient**](RecipientApi.md#get_recipient) | **GET** /v1/rise/recipients/{recipientId} | 
[**query_recipients**](RecipientApi.md#query_recipients) | **POST** /v1/rise/recipients/query | 


# **create_recipient**
> CreateRecipientResponse1 create_recipient(recipient_gift_card_recipient_service_v1_rise_recipients_post_create_recipient_request_body)

Creates a Recipient.
Note: This method is already called by GiftCardOrderService when an order is fulfilled.

### Example


```python
import openapi_client
from openapi_client.models.create_recipient_response1 import CreateRecipientResponse1
from openapi_client.models.recipient_gift_card_recipient_service_v1_rise_recipients_post_create_recipient_request_body import RecipientGiftCardRecipientServiceV1RiseRecipientsPostCreateRecipientRequestBody
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
    api_instance = openapi_client.RecipientApi(api_client)
    recipient_gift_card_recipient_service_v1_rise_recipients_post_create_recipient_request_body = openapi_client.RecipientGiftCardRecipientServiceV1RiseRecipientsPostCreateRecipientRequestBody() # RecipientGiftCardRecipientServiceV1RiseRecipientsPostCreateRecipientRequestBody | 

    try:
        api_response = api_instance.create_recipient(recipient_gift_card_recipient_service_v1_rise_recipients_post_create_recipient_request_body)
        print("The response of RecipientApi->create_recipient:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecipientApi->create_recipient: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recipient_gift_card_recipient_service_v1_rise_recipients_post_create_recipient_request_body** | [**RecipientGiftCardRecipientServiceV1RiseRecipientsPostCreateRecipientRequestBody**](RecipientGiftCardRecipientServiceV1RiseRecipientsPostCreateRecipientRequestBody.md)|  | 

### Return type

[**CreateRecipientResponse1**](CreateRecipientResponse1.md)

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

# **delete_recipient**
> delete_recipient(recipient_id)

Deletes a Recipient by ID.

### Example


```python
import openapi_client
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
    api_instance = openapi_client.RecipientApi(api_client)
    recipient_id = 'recipient_id_example' # str | Id of the Recipient to delete.

    try:
        api_instance.delete_recipient(recipient_id)
    except Exception as e:
        print("Exception when calling RecipientApi->delete_recipient: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recipient_id** | **str**| Id of the Recipient to delete. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an empty object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recipient**
> GetRecipientResponse1 get_recipient(recipient_id)

Retrieves a Recipient by ID.

### Example


```python
import openapi_client
from openapi_client.models.get_recipient_response1 import GetRecipientResponse1
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
    api_instance = openapi_client.RecipientApi(api_client)
    recipient_id = 'recipient_id_example' # str | ID of the Recipient to retrieve.

    try:
        api_response = api_instance.get_recipient(recipient_id)
        print("The response of RecipientApi->get_recipient:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecipientApi->get_recipient: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recipient_id** | **str**| ID of the Recipient to retrieve. | 

### Return type

[**GetRecipientResponse1**](GetRecipientResponse1.md)

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

# **query_recipients**
> QueryRecipientsResponse1 query_recipients(recipient_gift_card_recipient_service_v1_rise_recipients_query_post_query_recipients_request_body)

Retrieves a list of Recipients, given the provided paging, filtering, and sorting.
To learn how to query Recipients, see [API Query Language](https://platform.rise.ai/docs/#tag/About-API-Query-Language).

### Example


```python
import openapi_client
from openapi_client.models.query_recipients_response1 import QueryRecipientsResponse1
from openapi_client.models.recipient_gift_card_recipient_service_v1_rise_recipients_query_post_query_recipients_request_body import RecipientGiftCardRecipientServiceV1RiseRecipientsQueryPostQueryRecipientsRequestBody
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
    api_instance = openapi_client.RecipientApi(api_client)
    recipient_gift_card_recipient_service_v1_rise_recipients_query_post_query_recipients_request_body = openapi_client.RecipientGiftCardRecipientServiceV1RiseRecipientsQueryPostQueryRecipientsRequestBody() # RecipientGiftCardRecipientServiceV1RiseRecipientsQueryPostQueryRecipientsRequestBody | 

    try:
        api_response = api_instance.query_recipients(recipient_gift_card_recipient_service_v1_rise_recipients_query_post_query_recipients_request_body)
        print("The response of RecipientApi->query_recipients:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecipientApi->query_recipients: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recipient_gift_card_recipient_service_v1_rise_recipients_query_post_query_recipients_request_body** | [**RecipientGiftCardRecipientServiceV1RiseRecipientsQueryPostQueryRecipientsRequestBody**](RecipientGiftCardRecipientServiceV1RiseRecipientsQueryPostQueryRecipientsRequestBody.md)|  | 

### Return type

[**QueryRecipientsResponse1**](QueryRecipientsResponse1.md)

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

