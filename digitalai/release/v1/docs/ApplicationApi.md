# digitalai.release.v1.ApplicationApi

All URIs are relative to *http://localhost:5516*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_application**](ApplicationApi.md#create_application) | **POST** /api/v1/applications | 
[**delete_application**](ApplicationApi.md#delete_application) | **DELETE** /api/v1/applications/{applicationId} | 
[**get_application**](ApplicationApi.md#get_application) | **GET** /api/v1/applications/{applicationId} | 
[**search_applications**](ApplicationApi.md#search_applications) | **POST** /api/v1/applications/search | 
[**update_application**](ApplicationApi.md#update_application) | **PUT** /api/v1/applications/{applicationId} | 


# **create_application**
> ApplicationView create_application()



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import application_api
from digitalai.release.v1.model.application_view import ApplicationView
from digitalai.release.v1.model.application_form import ApplicationForm
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
    api_instance = application_api.ApplicationApi(api_client)
    application_form = ApplicationForm(
        title="title_example",
        environment_ids=[
            "environment_ids_example",
        ],
    ) # ApplicationForm |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_application(application_form=application_form)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ApplicationApi->create_application: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_form** | [**ApplicationForm**](ApplicationForm.md)|  | [optional]

### Return type

[**ApplicationView**](ApplicationView.md)

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

# **delete_application**
> delete_application(application_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import application_api
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
    api_instance = application_api.ApplicationApi(api_client)
    application_id = "jUR,rZ#UM/?R,Fp^l6$ARj/ApplicationQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_application(application_id)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ApplicationApi->delete_application: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  |

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

# **get_application**
> ApplicationView get_application(application_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import application_api
from digitalai.release.v1.model.application_view import ApplicationView
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
    api_instance = application_api.ApplicationApi(api_client)
    application_id = "jUR,rZ#UM/?R,Fp^l6$ARj/ApplicationQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_application(application_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ApplicationApi->get_application: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  |

### Return type

[**ApplicationView**](ApplicationView.md)

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

# **search_applications**
> [ApplicationView] search_applications()



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import application_api
from digitalai.release.v1.model.application_view import ApplicationView
from digitalai.release.v1.model.application_filters import ApplicationFilters
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
    api_instance = application_api.ApplicationApi(api_client)
    application_filters = ApplicationFilters(
        title="title_example",
        environments=[
            "environments_example",
        ],
    ) # ApplicationFilters |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.search_applications(application_filters=application_filters)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ApplicationApi->search_applications: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_filters** | [**ApplicationFilters**](ApplicationFilters.md)|  | [optional]

### Return type

[**[ApplicationView]**](ApplicationView.md)

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

# **update_application**
> ApplicationView update_application(application_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import application_api
from digitalai.release.v1.model.application_view import ApplicationView
from digitalai.release.v1.model.application_form import ApplicationForm
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
    api_instance = application_api.ApplicationApi(api_client)
    application_id = "jUR,rZ#UM/?R,Fp^l6$ARj/ApplicationQ" # str | 
    application_form = ApplicationForm(
        title="title_example",
        environment_ids=[
            "environment_ids_example",
        ],
    ) # ApplicationForm |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_application(application_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ApplicationApi->update_application: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_application(application_id, application_form=application_form)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ApplicationApi->update_application: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  |
 **application_form** | [**ApplicationForm**](ApplicationForm.md)|  | [optional]

### Return type

[**ApplicationView**](ApplicationView.md)

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

