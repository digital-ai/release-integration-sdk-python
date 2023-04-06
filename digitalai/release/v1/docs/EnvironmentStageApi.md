# digitalai.release.v1.EnvironmentStageApi

All URIs are relative to *http://localhost:5516*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_stage3**](EnvironmentStageApi.md#create_stage3) | **POST** /api/v1/environments/stages | 
[**delete_environment_stage**](EnvironmentStageApi.md#delete_environment_stage) | **DELETE** /api/v1/environments/stages/{environmentStageId} | 
[**get_stage_by_id**](EnvironmentStageApi.md#get_stage_by_id) | **GET** /api/v1/environments/stages/{environmentStageId} | 
[**search_stages**](EnvironmentStageApi.md#search_stages) | **POST** /api/v1/environments/stages/search | 
[**update_stage_in_environment**](EnvironmentStageApi.md#update_stage_in_environment) | **PUT** /api/v1/environments/stages/{environmentStageId} | 


# **create_stage3**
> EnvironmentStageView create_stage3()



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import environment_stage_api
from digitalai.release.v1.model.environment_stage_form import EnvironmentStageForm
from digitalai.release.v1.model.environment_stage_view import EnvironmentStageView
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
    api_instance = environment_stage_api.EnvironmentStageApi(api_client)
    environment_stage_form = EnvironmentStageForm(
        title="title_example",
    ) # EnvironmentStageForm |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_stage3(environment_stage_form=environment_stage_form)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling EnvironmentStageApi->create_stage3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_stage_form** | [**EnvironmentStageForm**](EnvironmentStageForm.md)|  | [optional]

### Return type

[**EnvironmentStageView**](EnvironmentStageView.md)

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

# **delete_environment_stage**
> delete_environment_stage(environment_stage_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import environment_stage_api
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
    api_instance = environment_stage_api.EnvironmentStageApi(api_client)
    environment_stage_id = "jUR,rZ#UM/?R,Fp^l6$ARj/EnvironmentStageQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_environment_stage(environment_stage_id)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling EnvironmentStageApi->delete_environment_stage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_stage_id** | **str**|  |

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

# **get_stage_by_id**
> EnvironmentStageView get_stage_by_id(environment_stage_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import environment_stage_api
from digitalai.release.v1.model.environment_stage_view import EnvironmentStageView
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
    api_instance = environment_stage_api.EnvironmentStageApi(api_client)
    environment_stage_id = "jUR,rZ#UM/?R,Fp^l6$ARj/EnvironmentStageQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_stage_by_id(environment_stage_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling EnvironmentStageApi->get_stage_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_stage_id** | **str**|  |

### Return type

[**EnvironmentStageView**](EnvironmentStageView.md)

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

# **search_stages**
> [EnvironmentStageView] search_stages()



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import environment_stage_api
from digitalai.release.v1.model.environment_stage_view import EnvironmentStageView
from digitalai.release.v1.model.environment_stage_filters import EnvironmentStageFilters
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
    api_instance = environment_stage_api.EnvironmentStageApi(api_client)
    environment_stage_filters = EnvironmentStageFilters(
        title="title_example",
    ) # EnvironmentStageFilters |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.search_stages(environment_stage_filters=environment_stage_filters)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling EnvironmentStageApi->search_stages: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_stage_filters** | [**EnvironmentStageFilters**](EnvironmentStageFilters.md)|  | [optional]

### Return type

[**[EnvironmentStageView]**](EnvironmentStageView.md)

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

# **update_stage_in_environment**
> EnvironmentStageView update_stage_in_environment(environment_stage_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import environment_stage_api
from digitalai.release.v1.model.environment_stage_form import EnvironmentStageForm
from digitalai.release.v1.model.environment_stage_view import EnvironmentStageView
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
    api_instance = environment_stage_api.EnvironmentStageApi(api_client)
    environment_stage_id = "jUR,rZ#UM/?R,Fp^l6$ARj/EnvironmentStageQ" # str | 
    environment_stage_form = EnvironmentStageForm(
        title="title_example",
    ) # EnvironmentStageForm |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_stage_in_environment(environment_stage_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling EnvironmentStageApi->update_stage_in_environment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_stage_in_environment(environment_stage_id, environment_stage_form=environment_stage_form)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling EnvironmentStageApi->update_stage_in_environment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_stage_id** | **str**|  |
 **environment_stage_form** | [**EnvironmentStageForm**](EnvironmentStageForm.md)|  | [optional]

### Return type

[**EnvironmentStageView**](EnvironmentStageView.md)

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

