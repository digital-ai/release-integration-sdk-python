# digitalai.release.v1.RolesApi

All URIs are relative to *http://localhost:5516*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_roles**](RolesApi.md#create_roles) | **POST** /api/v1/roles | 
[**create_roles1**](RolesApi.md#create_roles1) | **POST** /api/v1/roles/{roleName} | 
[**delete_roles**](RolesApi.md#delete_roles) | **DELETE** /api/v1/roles/{roleName} | 
[**get_role**](RolesApi.md#get_role) | **GET** /api/v1/roles/{roleName} | 
[**get_roles**](RolesApi.md#get_roles) | **GET** /api/v1/roles | 
[**rename_roles**](RolesApi.md#rename_roles) | **POST** /api/v1/roles/{roleName}/rename | 
[**update_roles**](RolesApi.md#update_roles) | **PUT** /api/v1/roles | 
[**update_roles1**](RolesApi.md#update_roles1) | **PUT** /api/v1/roles/{roleName} | 


# **create_roles**
> create_roles()



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import roles_api
from digitalai.release.v1.model.role_view import RoleView
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
    api_instance = roles_api.RolesApi(api_client)
    role_view = [
        RoleView(
            name="name_example",
            id="id_example",
            permissions=[
                "permissions_example",
            ],
            principals=[
                PrincipalView(
                    username="username_example",
                    fullname="fullname_example",
                ),
            ],
        ),
    ] # [RoleView] |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.create_roles(role_view=role_view)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling RolesApi->create_roles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_view** | [**[RoleView]**](RoleView.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [patAuth](../README.md#patAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_roles1**
> create_roles1(role_name)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import roles_api
from digitalai.release.v1.model.role_view import RoleView
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
    api_instance = roles_api.RolesApi(api_client)
    role_name = "jUR,rZ#UM/?R,Fp^l6$ARjQ" # str | 
    role_view = RoleView(
        name="name_example",
        id="id_example",
        permissions=[
            "permissions_example",
        ],
        principals=[
            PrincipalView(
                username="username_example",
                fullname="fullname_example",
            ),
        ],
    ) # RoleView |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.create_roles1(role_name)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling RolesApi->create_roles1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.create_roles1(role_name, role_view=role_view)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling RolesApi->create_roles1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**|  |
 **role_view** | [**RoleView**](RoleView.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [patAuth](../README.md#patAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_roles**
> delete_roles(role_name)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import roles_api
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
    api_instance = roles_api.RolesApi(api_client)
    role_name = "jUR,rZ#UM/?R,Fp^l6$ARjQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_roles(role_name)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling RolesApi->delete_roles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**|  |

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

# **get_role**
> RoleView get_role(role_name)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import roles_api
from digitalai.release.v1.model.role_view import RoleView
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
    api_instance = roles_api.RolesApi(api_client)
    role_name = "jUR,rZ#UM/?R,Fp^l6$ARjQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_role(role_name)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling RolesApi->get_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**|  |

### Return type

[**RoleView**](RoleView.md)

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

# **get_roles**
> [RoleView] get_roles()



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import roles_api
from digitalai.release.v1.model.role_view import RoleView
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
    api_instance = roles_api.RolesApi(api_client)
    page = 0 # int |  (optional) if omitted the server will use the default value of 0
    results_per_page = 100 # int |  (optional) if omitted the server will use the default value of 100

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_roles(page=page, results_per_page=results_per_page)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling RolesApi->get_roles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] if omitted the server will use the default value of 0
 **results_per_page** | **int**|  | [optional] if omitted the server will use the default value of 100

### Return type

[**[RoleView]**](RoleView.md)

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

# **rename_roles**
> rename_roles(role_name)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import roles_api
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
    api_instance = roles_api.RolesApi(api_client)
    role_name = "jUR,rZ#UM/?R,Fp^l6$ARjQ" # str | 
    new_name = "newName_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.rename_roles(role_name)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling RolesApi->rename_roles: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.rename_roles(role_name, new_name=new_name)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling RolesApi->rename_roles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**|  |
 **new_name** | **str**|  | [optional]

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

# **update_roles**
> update_roles()



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import roles_api
from digitalai.release.v1.model.role_view import RoleView
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
    api_instance = roles_api.RolesApi(api_client)
    role_view = [
        RoleView(
            name="name_example",
            id="id_example",
            permissions=[
                "permissions_example",
            ],
            principals=[
                PrincipalView(
                    username="username_example",
                    fullname="fullname_example",
                ),
            ],
        ),
    ] # [RoleView] |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.update_roles(role_view=role_view)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling RolesApi->update_roles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_view** | [**[RoleView]**](RoleView.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [patAuth](../README.md#patAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_roles1**
> update_roles1(role_name)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import roles_api
from digitalai.release.v1.model.role_view import RoleView
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
    api_instance = roles_api.RolesApi(api_client)
    role_name = "jUR,rZ#UM/?R,Fp^l6$ARjQ" # str | 
    role_view = RoleView(
        name="name_example",
        id="id_example",
        permissions=[
            "permissions_example",
        ],
        principals=[
            PrincipalView(
                username="username_example",
                fullname="fullname_example",
            ),
        ],
    ) # RoleView |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.update_roles1(role_name)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling RolesApi->update_roles1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.update_roles1(role_name, role_view=role_view)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling RolesApi->update_roles1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**|  |
 **role_view** | [**RoleView**](RoleView.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [patAuth](../README.md#patAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

