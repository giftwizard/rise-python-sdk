# ProduceTransactionAddedEventRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.produce_transaction_added_event_request import ProduceTransactionAddedEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProduceTransactionAddedEventRequest from a JSON string
produce_transaction_added_event_request_instance = ProduceTransactionAddedEventRequest.from_json(json)
# print the JSON string representation of the object
print(ProduceTransactionAddedEventRequest.to_json())

# convert the object into a dict
produce_transaction_added_event_request_dict = produce_transaction_added_event_request_instance.to_dict()
# create an instance of ProduceTransactionAddedEventRequest from a dict
produce_transaction_added_event_request_from_dict = ProduceTransactionAddedEventRequest.from_dict(produce_transaction_added_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


