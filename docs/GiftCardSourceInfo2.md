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
**order_options** | [**OrderOptionsOrderOptions**](OrderOptionsOrderOptions.md) |  | [optional] 
**campaign_options** | [**CampaignOptionsCampaignOptions**](CampaignOptionsCampaignOptions.md) |  | [optional] 
**migration_options** | [**MigrationOptionsMigrationOptions**](MigrationOptionsMigrationOptions.md) |  | [optional] 
**store_credit_options** | [**StoreCreditOptionsStoreCreditOptions**](StoreCreditOptionsStoreCreditOptions.md) |  | [optional] 
**workflow_options** | [**WorkflowOptionsWorkflowOptions**](WorkflowOptionsWorkflowOptions.md) |  | [optional] 
**bulk_options** | [**BulkOptionsBulkOptions**](BulkOptionsBulkOptions.md) |  | [optional] 
**manual_options** | [**ManualOptionsManualOptions**](ManualOptionsManualOptions.md) |  | [optional] 

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


