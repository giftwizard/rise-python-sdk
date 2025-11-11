# Wallet

A wallet represents a customer who has Store Credits. It contains information about the Gift Card associated with this wallet. It also contains a list of references to the customer in specific source channels (see CustomerReference object definition below).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Wallet ID. | [optional] [readonly] 
**revision** | **str** | Represents the current state of an item. Each time the item is modified, its &#x60;revision&#x60; changes. for an update operation to succeed, you MUST pass the latest revision. | [optional] [readonly] 
**gift_card_id** | **str** | ID of the Gift Card associated with this Wallet. | [optional] [readonly] 
**customer_references** | **List[object]** | List of references to the customer in specific source channels. See definition below. | [optional] [readonly] 
**created_date** | **datetime** | The time this Wallet was created. | [optional] [readonly] 
**updated_date** | **datetime** | The time this Wallet was last updated. | [optional] [readonly] 
**gift_card_info** | **object** | Information about the Gift Card associated with this Wallet. | [optional] [readonly] 
**primary_contact_details** | **object** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.wallet import Wallet

# TODO update the JSON string below
json = "{}"
# create an instance of Wallet from a JSON string
wallet_instance = Wallet.from_json(json)
# print the JSON string representation of the object
print(Wallet.to_json())

# convert the object into a dict
wallet_dict = wallet_instance.to_dict()
# create an instance of Wallet from a dict
wallet_from_dict = Wallet.from_dict(wallet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


