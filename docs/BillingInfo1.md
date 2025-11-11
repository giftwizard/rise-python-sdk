# BillingInfo1

Billing information of the buyer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address1** | **str** | The street address of the billing address. | [optional] 
**address2** | **str** | An optional additional field for the street address of the billing address.address | [optional] 
**city** | **str** | The city of the billing address. | [optional] 
**company** | **str** | The company of the person associated with the billing address. | [optional] 
**country** | **str** | The name of the country of the billing address. | [optional] 
**state** | **str** | The name of the region of the billing address. | [optional] 
**zip** | **str** | The postal code of the billing address. | [optional] 
**state_code** | **str** | province code of the billing address. | [optional] 
**country_code** | **str** | country code of the billing address. | [optional] 
**latitude** | **str** | The latitude of the billing address. | [optional] 
**longitude** | **str** | The longitude of the billing address. | [optional] 

## Example

```python
from openapi_client.models.billing_info1 import BillingInfo1

# TODO update the JSON string below
json = "{}"
# create an instance of BillingInfo1 from a JSON string
billing_info1_instance = BillingInfo1.from_json(json)
# print the JSON string representation of the object
print(BillingInfo1.to_json())

# convert the object into a dict
billing_info1_dict = billing_info1_instance.to_dict()
# create an instance of BillingInfo1 from a dict
billing_info1_from_dict = BillingInfo1.from_dict(billing_info1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


