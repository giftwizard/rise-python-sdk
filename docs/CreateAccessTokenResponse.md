# CreateAccessTokenResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | Created access token. | [optional] 
**token_type** | **str** | Type of the created access token. Always &#x60;”Bearer”&#x60;. | [optional] 
**expires_in** | **int** | Time the access token expires in seconds. Always &#x60;14400&#x60; (4 hours). | [optional] 

## Example

```python
from openapi_client.models.create_access_token_response import CreateAccessTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAccessTokenResponse from a JSON string
create_access_token_response_instance = CreateAccessTokenResponse.from_json(json)
# print the JSON string representation of the object
print(CreateAccessTokenResponse.to_json())

# convert the object into a dict
create_access_token_response_dict = create_access_token_response_instance.to_dict()
# create an instance of CreateAccessTokenResponse from a dict
create_access_token_response_from_dict = CreateAccessTokenResponse.from_dict(create_access_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


