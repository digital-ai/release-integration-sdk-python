# digitalai.release.v1.EnvironmentLabelApi

All URIs are relative to *http://localhost:5516*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_label**](EnvironmentLabelApi.md#create_label) | **POST** /api/v1/environments/labels | 
[**delete_environment_label**](EnvironmentLabelApi.md#delete_environment_label) | **DELETE** /api/v1/environments/labels/{environmentLabelId} | 
[**get_label_by_id**](EnvironmentLabelApi.md#get_label_by_id) | **GET** /api/v1/environments/labels/{environmentLabelId} | 
[**search_labels**](EnvironmentLabelApi.md#search_labels) | **POST** /api/v1/environments/labels/search | 
[**update_label**](EnvironmentLabelApi.md#update_label) | **PUT** /api/v1/environments/labels/{environmentLabelId} | 


# **create_label**
> EnvironmentLabelView create_label()



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import environment_label_api
from digitalai.release.v1.model.environment_label_view import EnvironmentLabelView
from digitalai.release.v1.model.environment_label_form import EnvironmentLabelForm
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
    api_instance = environment_label_api.EnvironmentLabelApi(api_client)
    environment_label_form = EnvironmentLabelForm(
        title="title_example",
        color="color_example",
    ) # EnvironmentLabelForm |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_label(environment_label_form=environment_label_form)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling EnvironmentLabelApi->create_label: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_label_form** | [**EnvironmentLabelForm**](EnvironmentLabelForm.md)|  | [optional]

### Return type

[**EnvironmentLabelView**](EnvironmentLabelView.md)

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

# **delete_environment_label**
> delete_environment_label(environment_label_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import environment_label_api
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
    api_instance = environment_label_api.EnvironmentLabelApi(api_client)
    environment_label_id = "jUR,rZ#UM/?R,Fp^l6$ARj/EnvironmentLabelQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_environment_label(environment_label_id)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling EnvironmentLabelApi->delete_environment_label: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_label_id** | **str**|  |

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

# **get_label_by_id**
> EnvironmentLabelView get_label_by_id(environment_label_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import environment_label_api
from digitalai.release.v1.model.environment_label_view import EnvironmentLabelView
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
    api_instance = environment_label_api.EnvironmentLabelApi(api_client)
    environment_label_id = "jUR,rZ#UM/?R,Fp^l6$ARj/EnvironmentLabelQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_label_by_id(environment_label_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling EnvironmentLabelApi->get_label_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_label_id** | **str**|  |

### Return type

[**EnvironmentLabelView**](EnvironmentLabelView.md)

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

# **search_labels**
> [EnvironmentLabelView] search_labels()



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import environment_label_api
from digitalai.release.v1.model.environment_label_view import EnvironmentLabelView
from digitalai.release.v1.model.environment_label_filters import EnvironmentLabelFilters
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
    api_instance = environment_label_api.EnvironmentLabelApi(api_client)
    environment_label_filters = EnvironmentLabelFilters(
        title="title_example",
    ) # EnvironmentLabelFilters |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.search_labels(environment_label_filters=environment_label_filters)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling EnvironmentLabelApi->search_labels: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_label_filters** | [**EnvironmentLabelFilters**](EnvironmentLabelFilters.md)|  | [optional]

### Return type

[**[EnvironmentLabelView]**](EnvironmentLabelView.md)

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

# **update_label**
> EnvironmentLabelView update_label(environment_label_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import environment_label_api
from digitalai.release.v1.model.environment_label_view import EnvironmentLabelView
from digitalai.release.v1.model.environment_label_form import EnvironmentLabelForm
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
    api_instance = environment_label_api.EnvironmentLabelApi(api_client)
    environment_label_id = "jUR,rZ#UM/?R,Fp^l6$ARj/EnvironmentLabelQ" # str | 
    environment_label_form = EnvironmentLabelForm(
        title="title_example",
        color="color_example",
    ) # EnvironmentLabelForm |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_label(environment_label_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling EnvironmentLabelApi->update_label: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_label(environment_label_id, environment_label_form=environment_label_form)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling EnvironmentLabelApi->update_label: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_label_id** | **str**|  |
 **environment_label_form** | [**EnvironmentLabelForm**](EnvironmentLabelForm.md)|  | [optional]

### Return type

[**EnvironmentLabelView**](EnvironmentLabelView.md)

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

