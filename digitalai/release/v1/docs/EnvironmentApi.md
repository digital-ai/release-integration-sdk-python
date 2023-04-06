# digitalai.release.v1.EnvironmentApi

All URIs are relative to *http://localhost:5516*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_environment**](EnvironmentApi.md#create_environment) | **POST** /api/v1/environments | 
[**delete_environment**](EnvironmentApi.md#delete_environment) | **DELETE** /api/v1/environments/{environmentId} | 
[**get_deployable_applications_for_environment**](EnvironmentApi.md#get_deployable_applications_for_environment) | **GET** /api/v1/environments/{environmentId}/applications | 
[**get_environment**](EnvironmentApi.md#get_environment) | **GET** /api/v1/environments/{environmentId} | 
[**get_reservations_for_environment**](EnvironmentApi.md#get_reservations_for_environment) | **GET** /api/v1/environments/{environmentId}/reservations | 
[**search_environments**](EnvironmentApi.md#search_environments) | **POST** /api/v1/environments/search | 
[**update_environment**](EnvironmentApi.md#update_environment) | **PUT** /api/v1/environments/{environmentId} | 


# **create_environment**
> EnvironmentView create_environment()



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import environment_api
from digitalai.release.v1.model.environment_view import EnvironmentView
from digitalai.release.v1.model.environment_form import EnvironmentForm
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
    api_instance = environment_api.EnvironmentApi(api_client)
    environment_form = EnvironmentForm(
        title="title_example",
        description="description_example",
        stage_id="stage_id_example",
        label_ids=[
            "label_ids_example",
        ],
    ) # EnvironmentForm |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_environment(environment_form=environment_form)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling EnvironmentApi->create_environment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_form** | [**EnvironmentForm**](EnvironmentForm.md)|  | [optional]

### Return type

[**EnvironmentView**](EnvironmentView.md)

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

# **delete_environment**
> delete_environment(environment_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import environment_api
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
    api_instance = environment_api.EnvironmentApi(api_client)
    environment_id = "jUR,rZ#UM/?R,Fp^l6$ARj/EnvironmentQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_environment(environment_id)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling EnvironmentApi->delete_environment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**|  |

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

# **get_deployable_applications_for_environment**
> [BaseApplicationView] get_deployable_applications_for_environment(environment_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import environment_api
from digitalai.release.v1.model.base_application_view import BaseApplicationView
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
    api_instance = environment_api.EnvironmentApi(api_client)
    environment_id = "jUR,rZ#UM/?R,Fp^l6$ARj/EnvironmentQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_deployable_applications_for_environment(environment_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling EnvironmentApi->get_deployable_applications_for_environment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**|  |

### Return type

[**[BaseApplicationView]**](BaseApplicationView.md)

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

# **get_environment**
> EnvironmentView get_environment(environment_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import environment_api
from digitalai.release.v1.model.environment_view import EnvironmentView
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
    api_instance = environment_api.EnvironmentApi(api_client)
    environment_id = "jUR,rZ#UM/?R,Fp^l6$ARj/EnvironmentQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_environment(environment_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling EnvironmentApi->get_environment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**|  |

### Return type

[**EnvironmentView**](EnvironmentView.md)

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

# **get_reservations_for_environment**
> [EnvironmentReservationView] get_reservations_for_environment(environment_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import environment_api
from digitalai.release.v1.model.environment_reservation_view import EnvironmentReservationView
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
    api_instance = environment_api.EnvironmentApi(api_client)
    environment_id = "jUR,rZ#UM/?R,Fp^l6$ARj/EnvironmentQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_reservations_for_environment(environment_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling EnvironmentApi->get_reservations_for_environment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**|  |

### Return type

[**[EnvironmentReservationView]**](EnvironmentReservationView.md)

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

# **search_environments**
> [EnvironmentView] search_environments()



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import environment_api
from digitalai.release.v1.model.environment_view import EnvironmentView
from digitalai.release.v1.model.environment_filters import EnvironmentFilters
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
    api_instance = environment_api.EnvironmentApi(api_client)
    environment_filters = EnvironmentFilters(
        title="title_example",
        stage="stage_example",
        labels=[
            "labels_example",
        ],
    ) # EnvironmentFilters |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.search_environments(environment_filters=environment_filters)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling EnvironmentApi->search_environments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_filters** | [**EnvironmentFilters**](EnvironmentFilters.md)|  | [optional]

### Return type

[**[EnvironmentView]**](EnvironmentView.md)

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

# **update_environment**
> EnvironmentView update_environment(environment_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import environment_api
from digitalai.release.v1.model.environment_view import EnvironmentView
from digitalai.release.v1.model.environment_form import EnvironmentForm
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
    api_instance = environment_api.EnvironmentApi(api_client)
    environment_id = "jUR,rZ#UM/?R,Fp^l6$ARj/EnvironmentQ" # str | 
    environment_form = EnvironmentForm(
        title="title_example",
        description="description_example",
        stage_id="stage_id_example",
        label_ids=[
            "label_ids_example",
        ],
    ) # EnvironmentForm |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_environment(environment_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling EnvironmentApi->update_environment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_environment(environment_id, environment_form=environment_form)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling EnvironmentApi->update_environment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**|  |
 **environment_form** | [**EnvironmentForm**](EnvironmentForm.md)|  | [optional]

### Return type

[**EnvironmentView**](EnvironmentView.md)

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

