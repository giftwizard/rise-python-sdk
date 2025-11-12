# PagingMetadataV2



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of items returned in the response. | [optional] 
**offset** | **int** | Offset that was requested. | [optional] 
**total** | **int** | Total number of items that match the query. Returned if offset paging is used and the &#x60;tooManyToCount&#x60; flag is not set. | [optional] 
**too_many_to_count** | **bool** | Flag that indicates the server failed to calculate the &#x60;total&#x60; field. | [optional] 
**cursors** | **object** | Cursors to navigate through the result pages using &#x60;next&#x60; and &#x60;prev&#x60;. Returned if cursor paging is used. | [optional] 

## Example

```python
from openapi_client.models.paging_metadata_v2 import PagingMetadataV2

# TODO update the JSON string below
json = "{}"
# create an instance of PagingMetadataV2 from a JSON string
paging_metadata_v2_instance = PagingMetadataV2.from_json(json)
# print the JSON string representation of the object
print(PagingMetadataV2.to_json())

# convert the object into a dict
paging_metadata_v2_dict = paging_metadata_v2_instance.to_dict()
# create an instance of PagingMetadataV2 from a dict
paging_metadata_v2_from_dict = PagingMetadataV2.from_dict(paging_metadata_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


