# CampaignOptionsCampaignOptions

Bulk Options. (**Deprecated**: Use `bulk_options` instead.)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_id** | **str** |  | [optional] 
**liability** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.campaign_options_campaign_options import CampaignOptionsCampaignOptions

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignOptionsCampaignOptions from a JSON string
campaign_options_campaign_options_instance = CampaignOptionsCampaignOptions.from_json(json)
# print the JSON string representation of the object
print(CampaignOptionsCampaignOptions.to_json())

# convert the object into a dict
campaign_options_campaign_options_dict = campaign_options_campaign_options_instance.to_dict()
# create an instance of CampaignOptionsCampaignOptions from a dict
campaign_options_campaign_options_from_dict = CampaignOptionsCampaignOptions.from_dict(campaign_options_campaign_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


