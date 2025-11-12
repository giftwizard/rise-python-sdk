# FulfilledData

Data about the gift cards that were already fulfilled for this Line Item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gift_card_ids** | **List[str]** | List of the IDs of the Gift Cards that were already fulfilled for this Line Item. | [optional] [readonly] 

## Example

```python
from openapi_client.models.fulfilled_data import FulfilledData

# TODO update the JSON string below
json = "{}"
# create an instance of FulfilledData from a JSON string
fulfilled_data_instance = FulfilledData.from_json(json)
# print the JSON string representation of the object
print(FulfilledData.to_json())

# convert the object into a dict
fulfilled_data_dict = fulfilled_data_instance.to_dict()
# create an instance of FulfilledData from a dict
fulfilled_data_from_dict = FulfilledData.from_dict(fulfilled_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


