# digitalai.release.v1.FolderApi

All URIs are relative to *http://localhost:5516*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_folder**](FolderApi.md#add_folder) | **POST** /api/v1/folders/{folderId} | 
[**create_folder_variable**](FolderApi.md#create_folder_variable) | **POST** /api/v1/folders/{folderId}/variables | 
[**delete_folder**](FolderApi.md#delete_folder) | **DELETE** /api/v1/folders/{folderId} | 
[**delete_folder_variable**](FolderApi.md#delete_folder_variable) | **DELETE** /api/v1/folders/{folderId}/{variableId} | 
[**find**](FolderApi.md#find) | **GET** /api/v1/folders/find | 
[**get_folder**](FolderApi.md#get_folder) | **GET** /api/v1/folders/{folderId} | 
[**get_folder_permissions**](FolderApi.md#get_folder_permissions) | **GET** /api/v1/folders/permissions | 
[**get_folder_teams**](FolderApi.md#get_folder_teams) | **GET** /api/v1/folders/{folderId}/teams | 
[**get_folder_templates**](FolderApi.md#get_folder_templates) | **GET** /api/v1/folders/{folderId}/templates | 
[**get_folder_variable**](FolderApi.md#get_folder_variable) | **GET** /api/v1/folders/{folderId}/{variableId} | 
[**is_folder_owner**](FolderApi.md#is_folder_owner) | **GET** /api/v1/folders/{folderId}/folderOwner | 
[**list**](FolderApi.md#list) | **GET** /api/v1/folders/{folderId}/list | 
[**list_root**](FolderApi.md#list_root) | **GET** /api/v1/folders/list | 
[**list_variable_values**](FolderApi.md#list_variable_values) | **GET** /api/v1/folders/{folderId}/variableValues | 
[**list_variables**](FolderApi.md#list_variables) | **GET** /api/v1/folders/{folderId}/variables | 
[**move**](FolderApi.md#move) | **POST** /api/v1/folders/{folderId}/move | 
[**move_template**](FolderApi.md#move_template) | **POST** /api/v1/folders/{folderId}/templates/{templateId} | 
[**rename_folder**](FolderApi.md#rename_folder) | **POST** /api/v1/folders/{folderId}/rename | 
[**search_releases_folder**](FolderApi.md#search_releases_folder) | **POST** /api/v1/folders/{folderId}/releases | 
[**set_folder_teams**](FolderApi.md#set_folder_teams) | **POST** /api/v1/folders/{folderId}/teams | 
[**update_folder_variable**](FolderApi.md#update_folder_variable) | **PUT** /api/v1/folders/{folderId}/{variableId} | 


# **add_folder**
> Folder add_folder(folder_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import folder_api
from digitalai.release.v1.model.folder import Folder
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
    api_instance = folder_api.FolderApi(api_client)
    folder_id = "jUR,rZ#UM/?R,Fp^l6$ARjFolder&6`$cClu+k& &su[-lzF6V+V6rEtCO?%28nxs"k8z(!\6\$TMxo:,sWVoim9gsbE`buHkrTt{qxXp~hu~%,Dc'g" # str | 
    folder = Folder(
        id="id_example",
        type="type_example",
        title="title_example",
        children=[
            Folder(),
        ],
        metadata={
            "key": {},
        },
        all_variables=[
            Variable(
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
            ),
        ],
        folder_variables=FolderVariables(
            id="id_example",
            type="type_example",
            variables=[
                Variable(
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
                ),
            ],
            string_variable_values={
                "key": "key_example",
            },
            password_variable_values={
                "key": "key_example",
            },
            variables_by_keys={
                "key": Variable(
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
                ),
            },
        ),
    ) # Folder |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.add_folder(folder_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling FolderApi->add_folder: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.add_folder(folder_id, folder=folder)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling FolderApi->add_folder: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**|  |
 **folder** | [**Folder**](Folder.md)|  | [optional]

### Return type

[**Folder**](Folder.md)

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

# **create_folder_variable**
> Variable create_folder_variable(folder_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import folder_api
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
    api_instance = folder_api.FolderApi(api_client)
    folder_id = "jUR,rZ#UM/?R,Fp^l6$ARjFolder&6`$cClu+k& &su[-lzF6V+V6rEtCO?%28nxs"k8z(!\6\$TMxo:,sWVoim9gsbE`buHkrTt{qxXp~hu~%,Dc'g" # str | 
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
    try:
        api_response = api_instance.create_folder_variable(folder_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling FolderApi->create_folder_variable: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_folder_variable(folder_id, variable1=variable1)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling FolderApi->create_folder_variable: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**|  |
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

# **delete_folder**
> delete_folder(folder_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import folder_api
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
    api_instance = folder_api.FolderApi(api_client)
    folder_id = "jUR,rZ#UM/?R,Fp^l6$ARjFolder&6`$cClu+k& &su[-lzF6V+V6rEtCO?%28nxs"k8z(!\6\$TMxo:,sWVoim9gsbE`buHkrTt{qxXp~hu~%,Dc'g" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_folder(folder_id)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling FolderApi->delete_folder: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**|  |

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

# **delete_folder_variable**
> delete_folder_variable(folder_id, variable_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import folder_api
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
    api_instance = folder_api.FolderApi(api_client)
    folder_id = "jUR,rZ#UM/?R,Fp^l6$ARjFolder&6`$cClu+k& &su[-lzF6V+V6rEtCO?%28nxs"k8z(!\6\$TMxo:,sWVoim9gsbE`buHkrTt{qxXp~hu~%,Dc'g" # str | 
    variable_id = "jUR,rZ#UM/?R,Fp^l6$ARjVariableQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_folder_variable(folder_id, variable_id)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling FolderApi->delete_folder_variable: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**|  |
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

# **find**
> Folder find()



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import folder_api
from digitalai.release.v1.model.folder import Folder
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
    api_instance = folder_api.FolderApi(api_client)
    by_path = "byPath_example" # str |  (optional)
    depth = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.find(by_path=by_path, depth=depth)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling FolderApi->find: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **by_path** | **str**|  | [optional]
 **depth** | **int**|  | [optional]

### Return type

[**Folder**](Folder.md)

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

# **get_folder**
> Folder get_folder(folder_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import folder_api
from digitalai.release.v1.model.folder import Folder
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
    api_instance = folder_api.FolderApi(api_client)
    folder_id = "jUR,rZ#UM/?R,Fp^l6$ARjFolder&6`$cClu+k& &su[-lzF6V+V6rEtCO?%28nxs"k8z(!\6\$TMxo:,sWVoim9gsbE`buHkrTt{qxXp~hu~%,Dc'g" # str | 
    depth = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_folder(folder_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling FolderApi->get_folder: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_folder(folder_id, depth=depth)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling FolderApi->get_folder: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**|  |
 **depth** | **int**|  | [optional]

### Return type

[**Folder**](Folder.md)

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

# **get_folder_permissions**
> [str] get_folder_permissions()



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import folder_api
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
    api_instance = folder_api.FolderApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_folder_permissions()
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling FolderApi->get_folder_permissions: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**[str]**

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

# **get_folder_teams**
> [TeamView] get_folder_teams(folder_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import folder_api
from digitalai.release.v1.model.team_view import TeamView
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
    api_instance = folder_api.FolderApi(api_client)
    folder_id = "jUR,rZ#UM/?R,Fp^l6$ARjFolder&6`$cClu+k& &su[-lzF6V+V6rEtCO?%28nxs"k8z(!\6\$TMxo:,sWVoim9gsbE`buHkrTt{qxXp~hu~%,Dc'g" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_folder_teams(folder_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling FolderApi->get_folder_teams: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**|  |

### Return type

[**[TeamView]**](TeamView.md)

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

# **get_folder_templates**
> [Release] get_folder_templates(folder_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import folder_api
from digitalai.release.v1.model.release import Release
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
    api_instance = folder_api.FolderApi(api_client)
    folder_id = "jUR,rZ#UM/?R,Fp^l6$ARjFolder&6`$cClu+k& &su[-lzF6V+V6rEtCO?%28nxs"k8z(!\6\$TMxo:,sWVoim9gsbE`buHkrTt{qxXp~hu~%,Dc'g" # str | 
    depth = 1 # int |  (optional)
    page = 1 # int |  (optional)
    results_per_page = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_folder_templates(folder_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling FolderApi->get_folder_templates: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_folder_templates(folder_id, depth=depth, page=page, results_per_page=results_per_page)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling FolderApi->get_folder_templates: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**|  |
 **depth** | **int**|  | [optional]
 **page** | **int**|  | [optional]
 **results_per_page** | **int**|  | [optional]

### Return type

[**[Release]**](Release.md)

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

# **get_folder_variable**
> Variable get_folder_variable(folder_id, variable_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import folder_api
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
    api_instance = folder_api.FolderApi(api_client)
    folder_id = "jUR,rZ#UM/?R,Fp^l6$ARjFolder&6`$cClu+k& &su[-lzF6V+V6rEtCO?%28nxs"k8z(!\6\$TMxo:,sWVoim9gsbE`buHkrTt{qxXp~hu~%,Dc'g" # str | 
    variable_id = "jUR,rZ#UM/?R,Fp^l6$ARjVariableQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_folder_variable(folder_id, variable_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling FolderApi->get_folder_variable: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**|  |
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

# **is_folder_owner**
> bool is_folder_owner(folder_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import folder_api
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
    api_instance = folder_api.FolderApi(api_client)
    folder_id = "jUR,rZ#UM/?R,Fp^l6$ARjFolder&6`$cClu+k& &su[-lzF6V+V6rEtCO?%28nxs"k8z(!\6\$TMxo:,sWVoim9gsbE`buHkrTt{qxXp~hu~%,Dc'g" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.is_folder_owner(folder_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling FolderApi->is_folder_owner: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**|  |

### Return type

**bool**

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

# **list**
> [Folder] list(folder_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import folder_api
from digitalai.release.v1.model.folder import Folder
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
    api_instance = folder_api.FolderApi(api_client)
    folder_id = "jUR,rZ#UM/?R,Fp^l6$ARjFolder&6`$cClu+k& &su[-lzF6V+V6rEtCO?%28nxs"k8z(!\6\$TMxo:,sWVoim9gsbE`buHkrTt{qxXp~hu~%,Dc'g" # str | 
    depth = 1 # int |  (optional)
    page = 1 # int |  (optional)
    permissions = True # bool |  (optional)
    results_per_page = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list(folder_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling FolderApi->list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list(folder_id, depth=depth, page=page, permissions=permissions, results_per_page=results_per_page)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling FolderApi->list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**|  |
 **depth** | **int**|  | [optional]
 **page** | **int**|  | [optional]
 **permissions** | **bool**|  | [optional]
 **results_per_page** | **int**|  | [optional]

### Return type

[**[Folder]**](Folder.md)

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

# **list_root**
> [Folder] list_root()



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import folder_api
from digitalai.release.v1.model.folder import Folder
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
    api_instance = folder_api.FolderApi(api_client)
    depth = 1 # int |  (optional)
    page = 1 # int |  (optional)
    permissions = True # bool |  (optional)
    results_per_page = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_root(depth=depth, page=page, permissions=permissions, results_per_page=results_per_page)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling FolderApi->list_root: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **depth** | **int**|  | [optional]
 **page** | **int**|  | [optional]
 **permissions** | **bool**|  | [optional]
 **results_per_page** | **int**|  | [optional]

### Return type

[**[Folder]**](Folder.md)

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

# **list_variable_values**
> {str: (str,)} list_variable_values(folder_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import folder_api
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
    api_instance = folder_api.FolderApi(api_client)
    folder_id = "jUR,rZ#UM/?R,Fp^l6$ARjFolder&6`$cClu+k& &su[-lzF6V+V6rEtCO?%28nxs"k8z(!\6\$TMxo:,sWVoim9gsbE`buHkrTt{qxXp~hu~%,Dc'g" # str | 
    folder_only = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_variable_values(folder_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling FolderApi->list_variable_values: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_variable_values(folder_id, folder_only=folder_only)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling FolderApi->list_variable_values: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**|  |
 **folder_only** | **bool**|  | [optional]

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

# **list_variables**
> [Variable] list_variables(folder_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import folder_api
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
    api_instance = folder_api.FolderApi(api_client)
    folder_id = "jUR,rZ#UM/?R,Fp^l6$ARjFolder&6`$cClu+k& &su[-lzF6V+V6rEtCO?%28nxs"k8z(!\6\$TMxo:,sWVoim9gsbE`buHkrTt{qxXp~hu~%,Dc'g" # str | 
    folder_only = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_variables(folder_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling FolderApi->list_variables: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_variables(folder_id, folder_only=folder_only)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling FolderApi->list_variables: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**|  |
 **folder_only** | **bool**|  | [optional]

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

# **move**
> move(folder_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import folder_api
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
    api_instance = folder_api.FolderApi(api_client)
    folder_id = "jUR,rZ#UM/?R,Fp^l6$ARjFolder&6`$cClu+k& &su[-lzF6V+V6rEtCO?%28nxs"k8z(!\6\$TMxo:,sWVoim9gsbE`buHkrTt{qxXp~hu~%,Dc'g" # str | 
    new_parent_id = "newParentId_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.move(folder_id)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling FolderApi->move: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.move(folder_id, new_parent_id=new_parent_id)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling FolderApi->move: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**|  |
 **new_parent_id** | **str**|  | [optional]

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

# **move_template**
> move_template(folder_id, template_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import folder_api
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
    api_instance = folder_api.FolderApi(api_client)
    folder_id = "jUR,rZ#UM/?R,Fp^l6$ARjFolder&6`$cClu+k& &su[-lzF6V+V6rEtCO?%28nxs"k8z(!\6\$TMxo:,sWVoim9gsbE`buHkrTt{qxXp~hu~%,Dc'g" # str | 
    template_id = "jUR,rZ#UM/?R,Fp^l6$ARjReleaseQ" # str | 
    merge_permissions = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.move_template(folder_id, template_id)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling FolderApi->move_template: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.move_template(folder_id, template_id, merge_permissions=merge_permissions)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling FolderApi->move_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**|  |
 **template_id** | **str**|  |
 **merge_permissions** | **bool**|  | [optional]

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

# **rename_folder**
> rename_folder(folder_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import folder_api
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
    api_instance = folder_api.FolderApi(api_client)
    folder_id = "jUR,rZ#UM/?R,Fp^l6$ARjFolder&6`$cClu+k& &su[-lzF6V+V6rEtCO?%28nxs"k8z(!\6\$TMxo:,sWVoim9gsbE`buHkrTt{qxXp~hu~%,Dc'g" # str | 
    new_name = "newName_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.rename_folder(folder_id)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling FolderApi->rename_folder: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.rename_folder(folder_id, new_name=new_name)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling FolderApi->rename_folder: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**|  |
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

# **search_releases_folder**
> [Release] search_releases_folder(folder_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import folder_api
from digitalai.release.v1.model.release import Release
from digitalai.release.v1.model.releases_filters import ReleasesFilters
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
    api_instance = folder_api.FolderApi(api_client)
    folder_id = "jUR,rZ#UM/?R,Fp^l6$ARjFolder&6`$cClu+k& &su[-lzF6V+V6rEtCO?%28nxs"k8z(!\6\$TMxo:,sWVoim9gsbE`buHkrTt{qxXp~hu~%,Dc'g" # str | 
    depth = 1 # int |  (optional)
    numberbypage = 1 # int |  (optional)
    page = 1 # int |  (optional)
    releases_filters = ReleasesFilters(
        title="title_example",
        tags=[
            "tags_example",
        ],
        task_tags=[
            "task_tags_example",
        ],
        time_frame=TimeFrame("LAST_SEVEN_DAYS"),
        _from=dateutil_parser('2023-03-20T02:07:00Z'),
        to=dateutil_parser('2023-03-20T02:07:00Z'),
        active=True,
        planned=True,
        in_progress=True,
        paused=True,
        failing=True,
        failed=True,
        inactive=True,
        completed=True,
        aborted=True,
        only_mine=True,
        only_flagged=True,
        only_archived=True,
        parent_id="parent_id_example",
        order_by=ReleaseOrderMode("risk"),
        order_direction=ReleaseOrderDirection("ASC"),
        risk_status_with_thresholds=RiskStatusWithThresholds(
            risk_status=RiskStatus("OK"),
            attention_needed_from=1,
            at_risk_from=1,
        ),
        query_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
        query_end_date=dateutil_parser('2023-03-20T02:07:00Z'),
        statuses=[
            ReleaseStatus("TEMPLATE"),
        ],
    ) # ReleasesFilters |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.search_releases_folder(folder_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling FolderApi->search_releases_folder: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.search_releases_folder(folder_id, depth=depth, numberbypage=numberbypage, page=page, releases_filters=releases_filters)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling FolderApi->search_releases_folder: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**|  |
 **depth** | **int**|  | [optional]
 **numberbypage** | **int**|  | [optional]
 **page** | **int**|  | [optional]
 **releases_filters** | [**ReleasesFilters**](ReleasesFilters.md)|  | [optional]

### Return type

[**[Release]**](Release.md)

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

# **set_folder_teams**
> [TeamView] set_folder_teams(folder_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import folder_api
from digitalai.release.v1.model.team_view import TeamView
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
    api_instance = folder_api.FolderApi(api_client)
    folder_id = "jUR,rZ#UM/?R,Fp^l6$ARjFolder&6`$cClu+k& &su[-lzF6V+V6rEtCO?%28nxs"k8z(!\6\$TMxo:,sWVoim9gsbE`buHkrTt{qxXp~hu~%,Dc'g" # str | 
    team_view = [
        TeamView(
            id="id_example",
            team_name="team_name_example",
            members=[
                TeamMemberView(
                    name="name_example",
                    full_name="full_name_example",
                    type=MemberType("PRINCIPAL"),
                    role_id="role_id_example",
                ),
            ],
            permissions=[
                "permissions_example",
            ],
            system_team=True,
        ),
    ] # [TeamView] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.set_folder_teams(folder_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling FolderApi->set_folder_teams: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.set_folder_teams(folder_id, team_view=team_view)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling FolderApi->set_folder_teams: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**|  |
 **team_view** | [**[TeamView]**](TeamView.md)|  | [optional]

### Return type

[**[TeamView]**](TeamView.md)

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

# **update_folder_variable**
> Variable update_folder_variable(folder_id, variable_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import folder_api
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
    api_instance = folder_api.FolderApi(api_client)
    folder_id = "jUR,rZ#UM/?R,Fp^l6$ARjFolder&6`$cClu+k& &su[-lzF6V+V6rEtCO?%28nxs"k8z(!\6\$TMxo:,sWVoim9gsbE`buHkrTt{qxXp~hu~%,Dc'g" # str | 
    variable_id = "jUR,rZ#UM/?R,Fp^l6$ARjVariableQ" # str | 
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
        api_response = api_instance.update_folder_variable(folder_id, variable_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling FolderApi->update_folder_variable: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_folder_variable(folder_id, variable_id, variable=variable)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling FolderApi->update_folder_variable: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**|  |
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

