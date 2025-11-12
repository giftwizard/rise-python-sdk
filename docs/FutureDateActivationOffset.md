# FutureDateActivationOffset



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pre_scheduled_event_offset_expression** | **str** | The offset value. The value is always taken as negative, so that the automation runs before the trigger date. To create an offset that causes the automation to run after the trigger date, use a delay action. | [optional] 
**scheduled_event_offset_time_unit** | **str** | Time unit for the scheduled event offset. | [optional] 

## Example

```python
from openapi_client.models.future_date_activation_offset import FutureDateActivationOffset

# TODO update the JSON string below
json = "{}"
# create an instance of FutureDateActivationOffset from a JSON string
future_date_activation_offset_instance = FutureDateActivationOffset.from_json(json)
# print the JSON string representation of the object
print(FutureDateActivationOffset.to_json())

# convert the object into a dict
future_date_activation_offset_dict = future_date_activation_offset_instance.to_dict()
# create an instance of FutureDateActivationOffset from a dict
future_date_activation_offset_from_dict = FutureDateActivationOffset.from_dict(future_date_activation_offset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


