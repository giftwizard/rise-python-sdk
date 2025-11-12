# Trigger



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** | ID of the app that defines the trigger. | [optional] 
**trigger_key** | **str** | Trigger key. | [optional] 
**filters** | **List[object]** | List of filters on schema fields. In order for the automation to run, all filter expressions must evaluate to &#x60;true&#x60; for a given payload. | [optional] 
**scheduled_event_offset** | **object** | Defines the time offset between the trigger date and when the automation runs. | [optional] 
**rate_limit** | **object** | Limits the number of times an automation can be triggered. | [optional] 
**automation_config_mapping** | **object** | An optional configuration, per automation, of a schema that is optionally offered by the trigger provider to affect the behavior of the trigger. For example, a trigger provider may offer a schema that allows the user to configure the trigger to happen at a certain time of day, He would define a schema with a field called \&quot;startDate\&quot; and using this parameter the user can define his preferred startDate, per automation. | [optional] 
**override_schema** | **object** | Optional schema of the trigger. It will be used instead the trigger schema in case it&#39;s provided. | [optional] 

## Example

```python
from openapi_client.models.trigger import Trigger

# TODO update the JSON string below
json = "{}"
# create an instance of Trigger from a JSON string
trigger_instance = Trigger.from_json(json)
# print the JSON string representation of the object
print(Trigger.to_json())

# convert the object into a dict
trigger_dict = trigger_instance.to_dict()
# create an instance of Trigger from a dict
trigger_from_dict = Trigger.from_dict(trigger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


