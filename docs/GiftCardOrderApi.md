# openapi_client.GiftCardOrderApi

All URIs are relative to *https://platform.rise.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_order**](GiftCardOrderApi.md#create_order) | **POST** /v1/rise/orders | 
[**fulfill_order**](GiftCardOrderApi.md#fulfill_order) | **POST** /v1/rise/orders/fulfill | 
[**query_orders**](GiftCardOrderApi.md#query_orders) | **POST** /v1/rise/orders/query | 
[**update_order**](GiftCardOrderApi.md#update_order) | **PATCH** /v1/rise/orders/{orderId} | 
[**update_order_status**](GiftCardOrderApi.md#update_order_status) | **POST** /v1/rise/orders/status | 


# **create_order**
> CreateOrderResponse create_order(gift_card_order_gift_card_order_service_v1_rise_orders_post_create_order_request_body)

Creates an Order for a Rise Gift Card.

### Example


```python
import openapi_client
from openapi_client.models.create_order_response import CreateOrderResponse
from openapi_client.models.gift_card_order_gift_card_order_service_v1_rise_orders_post_create_order_request_body import GiftCardOrderGiftCardOrderServiceV1RiseOrdersPostCreateOrderRequestBody
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
    api_instance = openapi_client.GiftCardOrderApi(api_client)
    gift_card_order_gift_card_order_service_v1_rise_orders_post_create_order_request_body = openapi_client.GiftCardOrderGiftCardOrderServiceV1RiseOrdersPostCreateOrderRequestBody() # GiftCardOrderGiftCardOrderServiceV1RiseOrdersPostCreateOrderRequestBody | 

    try:
        api_response = api_instance.create_order(gift_card_order_gift_card_order_service_v1_rise_orders_post_create_order_request_body)
        print("The response of GiftCardOrderApi->create_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GiftCardOrderApi->create_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gift_card_order_gift_card_order_service_v1_rise_orders_post_create_order_request_body** | [**GiftCardOrderGiftCardOrderServiceV1RiseOrdersPostCreateOrderRequestBody**](GiftCardOrderGiftCardOrderServiceV1RiseOrdersPostCreateOrderRequestBody.md)|  | 

### Return type

[**CreateOrderResponse**](CreateOrderResponse.md)

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

# **fulfill_order**
> fulfill_order(gift_card_order_gift_card_order_service_v1_rise_orders_fulfill_post_fulfill_order_request_body)

Fulfills an order in an async manner.

### Example


```python
import openapi_client
from openapi_client.models.gift_card_order_gift_card_order_service_v1_rise_orders_fulfill_post_fulfill_order_request_body import GiftCardOrderGiftCardOrderServiceV1RiseOrdersFulfillPostFulfillOrderRequestBody
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
    api_instance = openapi_client.GiftCardOrderApi(api_client)
    gift_card_order_gift_card_order_service_v1_rise_orders_fulfill_post_fulfill_order_request_body = openapi_client.GiftCardOrderGiftCardOrderServiceV1RiseOrdersFulfillPostFulfillOrderRequestBody() # GiftCardOrderGiftCardOrderServiceV1RiseOrdersFulfillPostFulfillOrderRequestBody | 

    try:
        api_instance.fulfill_order(gift_card_order_gift_card_order_service_v1_rise_orders_fulfill_post_fulfill_order_request_body)
    except Exception as e:
        print("Exception when calling GiftCardOrderApi->fulfill_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gift_card_order_gift_card_order_service_v1_rise_orders_fulfill_post_fulfill_order_request_body** | [**GiftCardOrderGiftCardOrderServiceV1RiseOrdersFulfillPostFulfillOrderRequestBody**](GiftCardOrderGiftCardOrderServiceV1RiseOrdersFulfillPostFulfillOrderRequestBody.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an empty object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_orders**
> QueryOrdersResponse1 query_orders(gift_card_order_gift_card_order_service_v1_rise_orders_query_post_query_orders_request_body)

Retrieves a list of Orders, given the provided paging, filtering, and sorting].
Up to 1,000 Orders can be returned per request.
To learn how to query Orders, see [API Query Language](https://platform.rise.ai/docs/#tag/About-API-Query-Language).

### Example


```python
import openapi_client
from openapi_client.models.gift_card_order_gift_card_order_service_v1_rise_orders_query_post_query_orders_request_body import GiftCardOrderGiftCardOrderServiceV1RiseOrdersQueryPostQueryOrdersRequestBody
from openapi_client.models.query_orders_response1 import QueryOrdersResponse1
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
    api_instance = openapi_client.GiftCardOrderApi(api_client)
    gift_card_order_gift_card_order_service_v1_rise_orders_query_post_query_orders_request_body = openapi_client.GiftCardOrderGiftCardOrderServiceV1RiseOrdersQueryPostQueryOrdersRequestBody() # GiftCardOrderGiftCardOrderServiceV1RiseOrdersQueryPostQueryOrdersRequestBody | 

    try:
        api_response = api_instance.query_orders(gift_card_order_gift_card_order_service_v1_rise_orders_query_post_query_orders_request_body)
        print("The response of GiftCardOrderApi->query_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GiftCardOrderApi->query_orders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gift_card_order_gift_card_order_service_v1_rise_orders_query_post_query_orders_request_body** | [**GiftCardOrderGiftCardOrderServiceV1RiseOrdersQueryPostQueryOrdersRequestBody**](GiftCardOrderGiftCardOrderServiceV1RiseOrdersQueryPostQueryOrdersRequestBody.md)|  | 

### Return type

[**QueryOrdersResponse1**](QueryOrdersResponse1.md)

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

# **update_order**
> UpdateOrderResponse update_order(order_id, gift_card_order_gift_card_order_service_v1_rise_orders_order_id_patch_update_order_request_body)

Updates a Rise Gift Card Order.

### Example


```python
import openapi_client
from openapi_client.models.gift_card_order_gift_card_order_service_v1_rise_orders_order_id_patch_update_order_request_body import GiftCardOrderGiftCardOrderServiceV1RiseOrdersOrderIdPatchUpdateOrderRequestBody
from openapi_client.models.update_order_response import UpdateOrderResponse
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
    api_instance = openapi_client.GiftCardOrderApi(api_client)
    order_id = 'order_id_example' # str | Order ID.
    gift_card_order_gift_card_order_service_v1_rise_orders_order_id_patch_update_order_request_body = openapi_client.GiftCardOrderGiftCardOrderServiceV1RiseOrdersOrderIdPatchUpdateOrderRequestBody() # GiftCardOrderGiftCardOrderServiceV1RiseOrdersOrderIdPatchUpdateOrderRequestBody | 

    try:
        api_response = api_instance.update_order(order_id, gift_card_order_gift_card_order_service_v1_rise_orders_order_id_patch_update_order_request_body)
        print("The response of GiftCardOrderApi->update_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GiftCardOrderApi->update_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Order ID. | 
 **gift_card_order_gift_card_order_service_v1_rise_orders_order_id_patch_update_order_request_body** | [**GiftCardOrderGiftCardOrderServiceV1RiseOrdersOrderIdPatchUpdateOrderRequestBody**](GiftCardOrderGiftCardOrderServiceV1RiseOrdersOrderIdPatchUpdateOrderRequestBody.md)|  | 

### Return type

[**UpdateOrderResponse**](UpdateOrderResponse.md)

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

# **update_order_status**
> update_order_status(gift_card_order_gift_card_order_service_v1_rise_orders_status_post_update_order_status_request_body)

Updates order payment status and fulfills it accordingly, in an async manner.

### Example


```python
import openapi_client
from openapi_client.models.gift_card_order_gift_card_order_service_v1_rise_orders_status_post_update_order_status_request_body import GiftCardOrderGiftCardOrderServiceV1RiseOrdersStatusPostUpdateOrderStatusRequestBody
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
    api_instance = openapi_client.GiftCardOrderApi(api_client)
    gift_card_order_gift_card_order_service_v1_rise_orders_status_post_update_order_status_request_body = openapi_client.GiftCardOrderGiftCardOrderServiceV1RiseOrdersStatusPostUpdateOrderStatusRequestBody() # GiftCardOrderGiftCardOrderServiceV1RiseOrdersStatusPostUpdateOrderStatusRequestBody | 

    try:
        api_instance.update_order_status(gift_card_order_gift_card_order_service_v1_rise_orders_status_post_update_order_status_request_body)
    except Exception as e:
        print("Exception when calling GiftCardOrderApi->update_order_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gift_card_order_gift_card_order_service_v1_rise_orders_status_post_update_order_status_request_body** | [**GiftCardOrderGiftCardOrderServiceV1RiseOrdersStatusPostUpdateOrderStatusRequestBody**](GiftCardOrderGiftCardOrderServiceV1RiseOrdersStatusPostUpdateOrderStatusRequestBody.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an empty object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

