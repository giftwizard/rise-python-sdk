# Wallet2

The retrieved Wallet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Wallet ID. | [optional] [readonly] 
**revision** | **str** | Represents the current state of an item. Each time the item is modified, its &#x60;revision&#x60; changes. for an update operation to succeed, you MUST pass the latest revision. | [optional] [readonly] 
**gift_card_id** | **str** | ID of the Gift Card associated with this Wallet. | [optional] [readonly] 
**customer_references** | [**List[CustomerReference1]**](CustomerReference1.md) | List of references to the customer in specific source channels. See definition below. | [optional] [readonly] 
**created_date** | **datetime** | The time this Wallet was created. | [optional] [readonly] 
**updated_date** | **datetime** | The time this Wallet was last updated. | [optional] [readonly] 
**gift_card_info** | [**GiftCardInfo1**](GiftCardInfo1.md) |  | [optional] 
**primary_contact_details** | [**ContactDetails1**](ContactDetails1.md) |  | [optional] 

## Example

```python
from openapi_client.models.wallet2 import Wallet2

# TODO update the JSON string below
json = "{}"
# create an instance of Wallet2 from a JSON string
wallet2_instance = Wallet2.from_json(json)
# print the JSON string representation of the object
print(Wallet2.to_json())

# convert the object into a dict
wallet2_dict = wallet2_instance.to_dict()
# create an instance of Wallet2 from a dict
wallet2_from_dict = Wallet2.from_dict(wallet2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


