# UpdateOrderStatusRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **object** | Order ID or Source Identifiers of the Order whose status is to be updated. | [optional] 
**payment_status** | **str** | The new payment status of the order. | [optional] 
**skip_auto_fulfillment** | **bool** | Skip auto fulfillment of the gift card. Default is false. | [optional] 

## Example

```python
from openapi_client.models.update_order_status_request import UpdateOrderStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOrderStatusRequest from a JSON string
update_order_status_request_instance = UpdateOrderStatusRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateOrderStatusRequest.to_json())

# convert the object into a dict
update_order_status_request_dict = update_order_status_request_instance.to_dict()
# create an instance of UpdateOrderStatusRequest from a dict
update_order_status_request_from_dict = UpdateOrderStatusRequest.from_dict(update_order_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


