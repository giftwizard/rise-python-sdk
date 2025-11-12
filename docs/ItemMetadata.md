# ItemMetadata



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Item ID. Should always be available, unless it&#39;s impossible (for example, when failing to create an item). | [optional] 
**original_index** | **int** | Index of the item within the request array. Allows for correlation between request and response items. | [optional] 
**success** | **bool** | Whether the requested action was successful for this item. When &#x60;false&#x60;, the &#x60;error&#x60; field is populated. | [optional] 
**error** | **object** | Details about the error in case of failure. | [optional] 

## Example

```python
from openapi_client.models.item_metadata import ItemMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ItemMetadata from a JSON string
item_metadata_instance = ItemMetadata.from_json(json)
# print the JSON string representation of the object
print(ItemMetadata.to_json())

# convert the object into a dict
item_metadata_dict = item_metadata_instance.to_dict()
# create an instance of ItemMetadata from a dict
item_metadata_from_dict = ItemMetadata.from_dict(item_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


