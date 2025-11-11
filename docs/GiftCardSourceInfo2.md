# GiftCardSourceInfo2

Information about the source of the gift card.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The source type of the gift card. | 
**source_tenant_id** | **str** | The Tenant ID of the sales channel that is associated with the gift card creation (e.g. Shopify shop id). | [optional] 
**source_channel_id** | **str** | The Channel ID of the sales channel that is associated with the gift card creation (e.g. Shopify channel id). | [optional] 
**source_location_id** | **str** | The location ID that is associated with the action (supports POS cases). | [optional] 
**initiator** | [**ActionInitiator3**](ActionInitiator3.md) |  | [optional] 
**order_options** | [**OrderOptions1**](OrderOptions1.md) |  | [optional] 
**campaign_options** | [**CampaignOptions2**](CampaignOptions2.md) |  | [optional] 
**migration_options** | [**MigrationOptions2**](MigrationOptions2.md) |  | [optional] 
**store_credit_options** | [**StoreCreditOptions1**](StoreCreditOptions1.md) |  | [optional] 
**workflow_options** | [**WorkflowOptions1**](WorkflowOptions1.md) |  | [optional] 
**bulk_options** | [**BulkOptions2**](BulkOptions2.md) |  | [optional] 
**manual_options** | [**ManualOptions2**](ManualOptions2.md) |  | [optional] 

## Example

```python
from openapi_client.models.gift_card_source_info2 import GiftCardSourceInfo2

# TODO update the JSON string below
json = "{}"
# create an instance of GiftCardSourceInfo2 from a JSON string
gift_card_source_info2_instance = GiftCardSourceInfo2.from_json(json)
# print the JSON string representation of the object
print(GiftCardSourceInfo2.to_json())

# convert the object into a dict
gift_card_source_info2_dict = gift_card_source_info2_instance.to_dict()
# create an instance of GiftCardSourceInfo2 from a dict
gift_card_source_info2_from_dict = GiftCardSourceInfo2.from_dict(gift_card_source_info2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


