# FulfilledData1

Data about the gift cards that were already fulfilled for this Line Item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gift_card_ids** | **List[str]** | List of the IDs of the Gift Cards that were already fulfilled for this Line Item. | [optional] [readonly] 

## Example

```python
from openapi_client.models.fulfilled_data1 import FulfilledData1

# TODO update the JSON string below
json = "{}"
# create an instance of FulfilledData1 from a JSON string
fulfilled_data1_instance = FulfilledData1.from_json(json)
# print the JSON string representation of the object
print(FulfilledData1.to_json())

# convert the object into a dict
fulfilled_data1_dict = fulfilled_data1_instance.to_dict()
# create an instance of FulfilledData1 from a dict
fulfilled_data1_from_dict = FulfilledData1.from_dict(fulfilled_data1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


