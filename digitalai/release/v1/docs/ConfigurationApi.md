# digitalai.release.v1.ConfigurationApi

All URIs are relative to *http://localhost:5516*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_configuration**](ConfigurationApi.md#add_configuration) | **POST** /api/v1/config | 
[**add_global_variable**](ConfigurationApi.md#add_global_variable) | **POST** /api/v1/config/Configuration/variables/global | 
[**check_status**](ConfigurationApi.md#check_status) | **POST** /api/v1/config/status | 
[**check_status1**](ConfigurationApi.md#check_status1) | **POST** /api/v1/config/{configurationId}/status | 
[**delete_configuration**](ConfigurationApi.md#delete_configuration) | **DELETE** /api/v1/config/{configurationId} | 
[**delete_global_variable**](ConfigurationApi.md#delete_global_variable) | **DELETE** /api/v1/config/{variableId} | 
[**get_configuration**](ConfigurationApi.md#get_configuration) | **GET** /api/v1/config/{configurationId} | 
[**get_global_variable**](ConfigurationApi.md#get_global_variable) | **GET** /api/v1/config/{variableId} | 
[**get_global_variable_values**](ConfigurationApi.md#get_global_variable_values) | **GET** /api/v1/config/Configuration/variableValues/global | 
[**get_global_variables**](ConfigurationApi.md#get_global_variables) | **GET** /api/v1/config/Configuration/variables/global | 
[**get_system_message**](ConfigurationApi.md#get_system_message) | **GET** /api/v1/config/system-message | 
[**search_by_type_and_title**](ConfigurationApi.md#search_by_type_and_title) | **GET** /api/v1/config/byTypeAndTitle | 
[**update_configuration**](ConfigurationApi.md#update_configuration) | **PUT** /api/v1/config/{configurationId} | 
[**update_global_variable**](ConfigurationApi.md#update_global_variable) | **PUT** /api/v1/config/{variableId} | 
[**update_system_message**](ConfigurationApi.md#update_system_message) | **PUT** /api/v1/config/system-message | 


# **add_configuration**
> ReleaseConfiguration add_configuration()



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import configuration_api
from digitalai.release.v1.model.release_configuration import ReleaseConfiguration
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
    api_instance = configuration_api.ConfigurationApi(api_client)
    release_configuration = ReleaseConfiguration(
        folder_id="folder_id_example",
        title="title_example",
        variable_mapping={
            "key": "key_example",
        },
    ) # ReleaseConfiguration |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.add_configuration(release_configuration=release_configuration)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ConfigurationApi->add_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release_configuration** | [**ReleaseConfiguration**](ReleaseConfiguration.md)|  | [optional]

### Return type

[**ReleaseConfiguration**](ReleaseConfiguration.md)

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

# **add_global_variable**
> Variable add_global_variable()



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import configuration_api
from digitalai.release.v1.model.variable import Variable
from digitalai.release.v1.model.variable1 import Variable1
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
    api_instance = configuration_api.ConfigurationApi(api_client)
    variable1 = Variable1(
        id="id_example",
        key="key_example",
        type="type_example",
        requires_value=True,
        show_on_release_start=True,
        value=None,
        label="label_example",
        description="description_example",
        multiline=True,
        inherited=True,
        prevent_interpolation=True,
        external_variable_value=ExternalVariableValue(
            server="server_example",
            server_type="server_type_example",
            path="path_example",
            external_key="external_key_example",
        ),
        value_provider=ValueProviderConfiguration(
            id="id_example",
            type="type_example",
            variable=Variable(
                id="id_example",
                type="type_example",
                folder_id="folder_id_example",
                title="title_example",
                key="key_example",
                requires_value=True,
                show_on_release_start=True,
                label="label_example",
                description="description_example",
                value_provider=ValueProviderConfiguration(),
                inherited=True,
                value=None,
                empty_value={},
                value_empty=True,
                untyped_value={},
                password=True,
                value_as_string="value_as_string_example",
                empty_value_as_string="empty_value_as_string_example",
            ),
        ),
    ) # Variable1 |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.add_global_variable(variable1=variable1)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ConfigurationApi->add_global_variable: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variable1** | [**Variable1**](Variable1.md)|  | [optional]

### Return type

[**Variable**](Variable.md)

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

# **check_status**
> SharedConfigurationStatusResponse check_status()



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import configuration_api
from digitalai.release.v1.model.shared_configuration_status_response import SharedConfigurationStatusResponse
from digitalai.release.v1.model.configuration_view import ConfigurationView
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
    api_instance = configuration_api.ConfigurationApi(api_client)
    configuration_view = ConfigurationView(
        type="type_example",
        title="title_example",
        properties={
            "key": {},
        },
        id="id_example",
    ) # ConfigurationView |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.check_status(configuration_view=configuration_view)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ConfigurationApi->check_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_view** | [**ConfigurationView**](ConfigurationView.md)|  | [optional]

### Return type

[**SharedConfigurationStatusResponse**](SharedConfigurationStatusResponse.md)

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

# **check_status1**
> SharedConfigurationStatusResponse check_status1(configuration_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import configuration_api
from digitalai.release.v1.model.shared_configuration_status_response import SharedConfigurationStatusResponse
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
    api_instance = configuration_api.ConfigurationApi(api_client)
    configuration_id = "jUR,rZ#UM/?R,Fp^l6$ARj/ConfigurationQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.check_status1(configuration_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ConfigurationApi->check_status1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_id** | **str**|  |

### Return type

[**SharedConfigurationStatusResponse**](SharedConfigurationStatusResponse.md)

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

# **delete_configuration**
> delete_configuration(configuration_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import configuration_api
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
    api_instance = configuration_api.ConfigurationApi(api_client)
    configuration_id = "jUR,rZ#UM/?R,Fp^l6$ARj/ConfigurationQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_configuration(configuration_id)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ConfigurationApi->delete_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_id** | **str**|  |

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

# **delete_global_variable**
> delete_global_variable(variable_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import configuration_api
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
    api_instance = configuration_api.ConfigurationApi(api_client)
    variable_id = "jUR,rZ#UM/?R,Fp^l6$ARj/VariableQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_global_variable(variable_id)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ConfigurationApi->delete_global_variable: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variable_id** | **str**|  |

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

# **get_configuration**
> ReleaseConfiguration get_configuration(configuration_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import configuration_api
from digitalai.release.v1.model.release_configuration import ReleaseConfiguration
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
    api_instance = configuration_api.ConfigurationApi(api_client)
    configuration_id = "jUR,rZ#UM/?R,Fp^l6$ARj/ConfigurationQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_configuration(configuration_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ConfigurationApi->get_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_id** | **str**|  |

### Return type

[**ReleaseConfiguration**](ReleaseConfiguration.md)

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

# **get_global_variable**
> Variable get_global_variable(variable_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import configuration_api
from digitalai.release.v1.model.variable import Variable
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
    api_instance = configuration_api.ConfigurationApi(api_client)
    variable_id = "jUR,rZ#UM/?R,Fp^l6$ARj/VariableQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_global_variable(variable_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ConfigurationApi->get_global_variable: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variable_id** | **str**|  |

### Return type

[**Variable**](Variable.md)

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

# **get_global_variable_values**
> {str: (str,)} get_global_variable_values()



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import configuration_api
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
    api_instance = configuration_api.ConfigurationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_global_variable_values()
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ConfigurationApi->get_global_variable_values: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**{str: (str,)}**

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

# **get_global_variables**
> [Variable] get_global_variables()



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import configuration_api
from digitalai.release.v1.model.variable import Variable
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
    api_instance = configuration_api.ConfigurationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_global_variables()
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ConfigurationApi->get_global_variables: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Variable]**](Variable.md)

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

# **get_system_message**
> SystemMessageSettings get_system_message()



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import configuration_api
from digitalai.release.v1.model.system_message_settings import SystemMessageSettings
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
    api_instance = configuration_api.ConfigurationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_system_message()
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ConfigurationApi->get_system_message: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemMessageSettings**](SystemMessageSettings.md)

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

# **search_by_type_and_title**
> [ReleaseConfiguration] search_by_type_and_title()



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import configuration_api
from digitalai.release.v1.model.release_configuration import ReleaseConfiguration
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
    api_instance = configuration_api.ConfigurationApi(api_client)
    configuration_type = "configurationType_example" # str |  (optional)
    folder_id = "folderId_example" # str |  (optional)
    folder_only = True # bool |  (optional)
    title = "title_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.search_by_type_and_title(configuration_type=configuration_type, folder_id=folder_id, folder_only=folder_only, title=title)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ConfigurationApi->search_by_type_and_title: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_type** | **str**|  | [optional]
 **folder_id** | **str**|  | [optional]
 **folder_only** | **bool**|  | [optional]
 **title** | **str**|  | [optional]

### Return type

[**[ReleaseConfiguration]**](ReleaseConfiguration.md)

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

# **update_configuration**
> ReleaseConfiguration update_configuration(configuration_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import configuration_api
from digitalai.release.v1.model.release_configuration import ReleaseConfiguration
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
    api_instance = configuration_api.ConfigurationApi(api_client)
    configuration_id = "jUR,rZ#UM/?R,Fp^l6$ARj/ConfigurationQ" # str | 
    release_configuration = ReleaseConfiguration(
        folder_id="folder_id_example",
        title="title_example",
        variable_mapping={
            "key": "key_example",
        },
    ) # ReleaseConfiguration |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_configuration(configuration_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ConfigurationApi->update_configuration: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_configuration(configuration_id, release_configuration=release_configuration)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ConfigurationApi->update_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_id** | **str**|  |
 **release_configuration** | [**ReleaseConfiguration**](ReleaseConfiguration.md)|  | [optional]

### Return type

[**ReleaseConfiguration**](ReleaseConfiguration.md)

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

# **update_global_variable**
> Variable update_global_variable(variable_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import configuration_api
from digitalai.release.v1.model.variable import Variable
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
    api_instance = configuration_api.ConfigurationApi(api_client)
    variable_id = "jUR,rZ#UM/?R,Fp^l6$ARj/VariableQ" # str | 
    variable = Variable(
        id="id_example",
        type="type_example",
        folder_id="folder_id_example",
        title="title_example",
        key="key_example",
        requires_value=True,
        show_on_release_start=True,
        label="label_example",
        description="description_example",
        value_provider=ValueProviderConfiguration(
            id="id_example",
            type="type_example",
            variable=Variable(),
        ),
        inherited=True,
        value=None,
        empty_value={},
        value_empty=True,
        untyped_value={},
        password=True,
        value_as_string="value_as_string_example",
        empty_value_as_string="empty_value_as_string_example",
    ) # Variable |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_global_variable(variable_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ConfigurationApi->update_global_variable: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_global_variable(variable_id, variable=variable)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ConfigurationApi->update_global_variable: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variable_id** | **str**|  |
 **variable** | [**Variable**](Variable.md)|  | [optional]

### Return type

[**Variable**](Variable.md)

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

# **update_system_message**
> SystemMessageSettings update_system_message()



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import configuration_api
from digitalai.release.v1.model.system_message_settings import SystemMessageSettings
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
    api_instance = configuration_api.ConfigurationApi(api_client)
    system_message_settings = SystemMessageSettings(
        id="id_example",
        type="type_example",
        title="title_example",
        enabled=True,
        message="message_example",
        automated=True,
        start_date=dateutil_parser('2023-03-20T02:07:00Z'),
        end_date=dateutil_parser('2023-03-20T02:07:00Z'),
    ) # SystemMessageSettings |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_system_message(system_message_settings=system_message_settings)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ConfigurationApi->update_system_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_message_settings** | [**SystemMessageSettings**](SystemMessageSettings.md)|  | [optional]

### Return type

[**SystemMessageSettings**](SystemMessageSettings.md)

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

