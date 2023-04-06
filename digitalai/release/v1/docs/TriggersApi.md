# digitalai.release.v1.TriggersApi

All URIs are relative to *http://localhost:5516*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_trigger**](TriggersApi.md#add_trigger) | **POST** /api/v1/triggers | 
[**disable_all_triggers**](TriggersApi.md#disable_all_triggers) | **POST** /api/v1/triggers/disable/all | 
[**disable_trigger**](TriggersApi.md#disable_trigger) | **PUT** /api/v1/triggers/{triggerId}/disable | 
[**disable_triggers**](TriggersApi.md#disable_triggers) | **POST** /api/v1/triggers/disable | 
[**enable_all_triggers**](TriggersApi.md#enable_all_triggers) | **POST** /api/v1/triggers/enable/all | 
[**enable_trigger**](TriggersApi.md#enable_trigger) | **PUT** /api/v1/triggers/{triggerId}/enable | 
[**enable_triggers**](TriggersApi.md#enable_triggers) | **POST** /api/v1/triggers/enable | 
[**get_trigger**](TriggersApi.md#get_trigger) | **GET** /api/v1/triggers/{triggerId} | 
[**get_types**](TriggersApi.md#get_types) | **GET** /api/v1/triggers/types | 
[**remove_trigger**](TriggersApi.md#remove_trigger) | **DELETE** /api/v1/triggers/{triggerId} | 
[**run_trigger**](TriggersApi.md#run_trigger) | **POST** /api/v1/triggers/{triggerId}/run | 
[**search_triggers**](TriggersApi.md#search_triggers) | **GET** /api/v1/triggers | 
[**update_trigger**](TriggersApi.md#update_trigger) | **PUT** /api/v1/triggers/{triggerId} | 


# **add_trigger**
> Trigger add_trigger()



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import triggers_api
from digitalai.release.v1.model.trigger import Trigger
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5516
# See configuration.py for a list of all supported configuration parameters.
configuration = digitalai.release.v1.Configuration(
    host = "http://localhost:5516"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = digitalai.release.v1.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: patAuth
configuration.api_key['patAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['patAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with digitalai.release.v1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = triggers_api.TriggersApi(api_client)
    trigger = Trigger(
        id="id_example",
        type="type_example",
        script="script_example",
        abort_script="abort_script_example",
        ci_uid=1,
        title="title_example",
        description="description_example",
        enabled=True,
        trigger_state="trigger_state_example",
        folder_id="folder_id_example",
        allow_parallel_execution=True,
        last_run_date=dateutil_parser('2023-03-20T02:07:00Z'),
        last_run_status=TriggerExecutionStatus("SUCCESS"),
        internal_properties=[
            "internal_properties_example",
        ],
        container_id="container_id_example",
    ) # Trigger |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.add_trigger(trigger=trigger)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling TriggersApi->add_trigger: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trigger** | [**Trigger**](Trigger.md)|  | [optional]

### Return type

[**Trigger**](Trigger.md)

### Authorization

[basicAuth](../README.md#basicAuth), [patAuth](../README.md#patAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_all_triggers**
> BulkActionResultView disable_all_triggers()



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import triggers_api
from digitalai.release.v1.model.bulk_action_result_view import BulkActionResultView
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5516
# See configuration.py for a list of all supported configuration parameters.
configuration = digitalai.release.v1.Configuration(
    host = "http://localhost:5516"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = digitalai.release.v1.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: patAuth
configuration.api_key['patAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['patAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with digitalai.release.v1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = triggers_api.TriggersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.disable_all_triggers()
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling TriggersApi->disable_all_triggers: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**BulkActionResultView**](BulkActionResultView.md)

### Authorization

[basicAuth](../README.md#basicAuth), [patAuth](../README.md#patAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_trigger**
> disable_trigger(trigger_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import triggers_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5516
# See configuration.py for a list of all supported configuration parameters.
configuration = digitalai.release.v1.Configuration(
    host = "http://localhost:5516"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = digitalai.release.v1.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: patAuth
configuration.api_key['patAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['patAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with digitalai.release.v1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = triggers_api.TriggersApi(api_client)
    trigger_id = "jUR,rZ#UM/?R,Fp^l6$ARj/TriggerQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.disable_trigger(trigger_id)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling TriggersApi->disable_trigger: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trigger_id** | **str**|  |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [patAuth](../README.md#patAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_triggers**
> BulkActionResultView disable_triggers()



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import triggers_api
from digitalai.release.v1.model.bulk_action_result_view import BulkActionResultView
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5516
# See configuration.py for a list of all supported configuration parameters.
configuration = digitalai.release.v1.Configuration(
    host = "http://localhost:5516"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = digitalai.release.v1.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: patAuth
configuration.api_key['patAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['patAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with digitalai.release.v1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = triggers_api.TriggersApi(api_client)
    request_body = [
        "request_body_example",
    ] # [str] |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.disable_triggers(request_body=request_body)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling TriggersApi->disable_triggers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | **[str]**|  | [optional]

### Return type

[**BulkActionResultView**](BulkActionResultView.md)

### Authorization

[basicAuth](../README.md#basicAuth), [patAuth](../README.md#patAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_all_triggers**
> BulkActionResultView enable_all_triggers()



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import triggers_api
from digitalai.release.v1.model.bulk_action_result_view import BulkActionResultView
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5516
# See configuration.py for a list of all supported configuration parameters.
configuration = digitalai.release.v1.Configuration(
    host = "http://localhost:5516"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = digitalai.release.v1.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: patAuth
configuration.api_key['patAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['patAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with digitalai.release.v1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = triggers_api.TriggersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.enable_all_triggers()
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling TriggersApi->enable_all_triggers: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**BulkActionResultView**](BulkActionResultView.md)

### Authorization

[basicAuth](../README.md#basicAuth), [patAuth](../README.md#patAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_trigger**
> enable_trigger(trigger_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import triggers_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5516
# See configuration.py for a list of all supported configuration parameters.
configuration = digitalai.release.v1.Configuration(
    host = "http://localhost:5516"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = digitalai.release.v1.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: patAuth
configuration.api_key['patAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['patAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with digitalai.release.v1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = triggers_api.TriggersApi(api_client)
    trigger_id = "jUR,rZ#UM/?R,Fp^l6$ARj/TriggerQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.enable_trigger(trigger_id)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling TriggersApi->enable_trigger: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trigger_id** | **str**|  |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [patAuth](../README.md#patAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_triggers**
> BulkActionResultView enable_triggers()



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import triggers_api
from digitalai.release.v1.model.bulk_action_result_view import BulkActionResultView
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5516
# See configuration.py for a list of all supported configuration parameters.
configuration = digitalai.release.v1.Configuration(
    host = "http://localhost:5516"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = digitalai.release.v1.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: patAuth
configuration.api_key['patAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['patAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with digitalai.release.v1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = triggers_api.TriggersApi(api_client)
    request_body = [
        "request_body_example",
    ] # [str] |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.enable_triggers(request_body=request_body)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling TriggersApi->enable_triggers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | **[str]**|  | [optional]

### Return type

[**BulkActionResultView**](BulkActionResultView.md)

### Authorization

[basicAuth](../README.md#basicAuth), [patAuth](../README.md#patAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trigger**
> Trigger get_trigger(trigger_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import triggers_api
from digitalai.release.v1.model.trigger import Trigger
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5516
# See configuration.py for a list of all supported configuration parameters.
configuration = digitalai.release.v1.Configuration(
    host = "http://localhost:5516"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = digitalai.release.v1.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: patAuth
configuration.api_key['patAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['patAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with digitalai.release.v1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = triggers_api.TriggersApi(api_client)
    trigger_id = "jUR,rZ#UM/?R,Fp^l6$ARjTrigger^" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_trigger(trigger_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling TriggersApi->get_trigger: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trigger_id** | **str**|  |

### Return type

[**Trigger**](Trigger.md)

### Authorization

[basicAuth](../README.md#basicAuth), [patAuth](../README.md#patAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_types**
> [bool, date, datetime, dict, float, int, list, str, none_type] get_types()



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import triggers_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5516
# See configuration.py for a list of all supported configuration parameters.
configuration = digitalai.release.v1.Configuration(
    host = "http://localhost:5516"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = digitalai.release.v1.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: patAuth
configuration.api_key['patAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['patAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with digitalai.release.v1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = triggers_api.TriggersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_types()
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling TriggersApi->get_types: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**[bool, date, datetime, dict, float, int, list, str, none_type]**

### Authorization

[basicAuth](../README.md#basicAuth), [patAuth](../README.md#patAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_trigger**
> remove_trigger(trigger_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import triggers_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5516
# See configuration.py for a list of all supported configuration parameters.
configuration = digitalai.release.v1.Configuration(
    host = "http://localhost:5516"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = digitalai.release.v1.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: patAuth
configuration.api_key['patAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['patAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with digitalai.release.v1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = triggers_api.TriggersApi(api_client)
    trigger_id = "jUR,rZ#UM/?R,Fp^l6$ARj/TriggerQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.remove_trigger(trigger_id)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling TriggersApi->remove_trigger: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trigger_id** | **str**|  |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [patAuth](../README.md#patAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_trigger**
> run_trigger(trigger_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import triggers_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5516
# See configuration.py for a list of all supported configuration parameters.
configuration = digitalai.release.v1.Configuration(
    host = "http://localhost:5516"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = digitalai.release.v1.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: patAuth
configuration.api_key['patAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['patAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with digitalai.release.v1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = triggers_api.TriggersApi(api_client)
    trigger_id = "jUR,rZ#UM/?R,Fp^l6$ARj/TriggerQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.run_trigger(trigger_id)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling TriggersApi->run_trigger: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trigger_id** | **str**|  |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [patAuth](../README.md#patAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_triggers**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} search_triggers()



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import triggers_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5516
# See configuration.py for a list of all supported configuration parameters.
configuration = digitalai.release.v1.Configuration(
    host = "http://localhost:5516"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = digitalai.release.v1.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: patAuth
configuration.api_key['patAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['patAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with digitalai.release.v1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = triggers_api.TriggersApi(api_client)
    folder_id = "folderId_example" # str |  (optional)
    folder_title = "folderTitle_example" # str |  (optional)
    page = 0 # int |  (optional) if omitted the server will use the default value of 0
    results_per_page = 100 # int |  (optional) if omitted the server will use the default value of 100
    template_id = "templateId_example" # str |  (optional)
    template_title = "templateTitle_example" # str |  (optional)
    trigger_title = "triggerTitle_example" # str |  (optional)
    trigger_type = [
        "triggerType_example",
    ] # [str] |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.search_triggers(folder_id=folder_id, folder_title=folder_title, page=page, results_per_page=results_per_page, template_id=template_id, template_title=template_title, trigger_title=trigger_title, trigger_type=trigger_type)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling TriggersApi->search_triggers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**|  | [optional]
 **folder_title** | **str**|  | [optional]
 **page** | **int**|  | [optional] if omitted the server will use the default value of 0
 **results_per_page** | **int**|  | [optional] if omitted the server will use the default value of 100
 **template_id** | **str**|  | [optional]
 **template_title** | **str**|  | [optional]
 **trigger_title** | **str**|  | [optional]
 **trigger_type** | **[str]**|  | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[basicAuth](../README.md#basicAuth), [patAuth](../README.md#patAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_trigger**
> Trigger update_trigger(trigger_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import triggers_api
from digitalai.release.v1.model.trigger import Trigger
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5516
# See configuration.py for a list of all supported configuration parameters.
configuration = digitalai.release.v1.Configuration(
    host = "http://localhost:5516"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = digitalai.release.v1.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: patAuth
configuration.api_key['patAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['patAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with digitalai.release.v1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = triggers_api.TriggersApi(api_client)
    trigger_id = "jUR,rZ#UM/?R,Fp^l6$ARjTrigger^" # str | 
    trigger = Trigger(
        id="id_example",
        type="type_example",
        script="script_example",
        abort_script="abort_script_example",
        ci_uid=1,
        title="title_example",
        description="description_example",
        enabled=True,
        trigger_state="trigger_state_example",
        folder_id="folder_id_example",
        allow_parallel_execution=True,
        last_run_date=dateutil_parser('2023-03-20T02:07:00Z'),
        last_run_status=TriggerExecutionStatus("SUCCESS"),
        internal_properties=[
            "internal_properties_example",
        ],
        container_id="container_id_example",
    ) # Trigger |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_trigger(trigger_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling TriggersApi->update_trigger: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_trigger(trigger_id, trigger=trigger)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling TriggersApi->update_trigger: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trigger_id** | **str**|  |
 **trigger** | [**Trigger**](Trigger.md)|  | [optional]

### Return type

[**Trigger**](Trigger.md)

### Authorization

[basicAuth](../README.md#basicAuth), [patAuth](../README.md#patAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

