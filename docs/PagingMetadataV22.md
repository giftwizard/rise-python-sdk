# PagingMetadataV22



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of items returned in the response. | [optional] 
**offset** | **int** | Offset that was requested. | [optional] 
**total** | **int** | Total number of items that match the query. Returned if offset paging is used and the &#x60;tooManyToCount&#x60; flag is not set. | [optional] 
**too_many_to_count** | **bool** | Flag that indicates the server failed to calculate the &#x60;total&#x60; field. | [optional] 
**cursors** | [**Cursors3**](Cursors3.md) |  | [optional] 

## Example

```python
from openapi_client.models.paging_metadata_v22 import PagingMetadataV22

# TODO update the JSON string below
json = "{}"
# create an instance of PagingMetadataV22 from a JSON string
paging_metadata_v22_instance = PagingMetadataV22.from_json(json)
# print the JSON string representation of the object
print(PagingMetadataV22.to_json())

# convert the object into a dict
paging_metadata_v22_dict = paging_metadata_v22_instance.to_dict()
# create an instance of PagingMetadataV22 from a dict
paging_metadata_v22_from_dict = PagingMetadataV22.from_dict(paging_metadata_v22_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


