# digitalai.release.v1.ReleaseGroupApi

All URIs are relative to *http://localhost:5516*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_members_to_group**](ReleaseGroupApi.md#add_members_to_group) | **POST** /api/v1/release-groups/{groupId}/members | 
[**create_group**](ReleaseGroupApi.md#create_group) | **POST** /api/v1/release-groups | 
[**delete_group**](ReleaseGroupApi.md#delete_group) | **DELETE** /api/v1/release-groups/{groupId} | 
[**get_group**](ReleaseGroupApi.md#get_group) | **GET** /api/v1/release-groups/{groupId} | 
[**get_members**](ReleaseGroupApi.md#get_members) | **GET** /api/v1/release-groups/{groupId}/members | 
[**get_release_group_timeline**](ReleaseGroupApi.md#get_release_group_timeline) | **GET** /api/v1/release-groups/{groupId}/timeline | 
[**remove_members_from_group**](ReleaseGroupApi.md#remove_members_from_group) | **DELETE** /api/v1/release-groups/{groupId}/members | 
[**search_groups**](ReleaseGroupApi.md#search_groups) | **POST** /api/v1/release-groups/search | 
[**update_group**](ReleaseGroupApi.md#update_group) | **PUT** /api/v1/release-groups/{groupId} | 


# **add_members_to_group**
> add_members_to_group(group_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import release_group_api
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
    api_instance = release_group_api.ReleaseGroupApi(api_client)
    group_id = "jUR,rZ#UM/?R,Fp^l6$ARjReleaseGroupQ" # str | 
    request_body = [
        "request_body_example",
    ] # [str] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.add_members_to_group(group_id)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ReleaseGroupApi->add_members_to_group: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.add_members_to_group(group_id, request_body=request_body)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ReleaseGroupApi->add_members_to_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  |
 **request_body** | **[str]**|  | [optional]

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

# **create_group**
> ReleaseGroup create_group()



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import release_group_api
from digitalai.release.v1.model.release_group import ReleaseGroup
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
    api_instance = release_group_api.ReleaseGroupApi(api_client)
    release_group = ReleaseGroup(
        id="id_example",
        type="type_example",
        metadata={
            "key": {},
        },
        title="title_example",
        status=ReleaseGroupStatus("PLANNED"),
        start_date=dateutil_parser('2023-03-20T02:07:00Z'),
        end_date=dateutil_parser('2023-03-20T02:07:00Z'),
        risk_score=1,
        release_ids=[
            "release_ids_example",
        ],
        progress=1,
        folder_id="folder_id_example",
        updatable=True,
    ) # ReleaseGroup |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_group(release_group=release_group)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ReleaseGroupApi->create_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release_group** | [**ReleaseGroup**](ReleaseGroup.md)|  | [optional]

### Return type

[**ReleaseGroup**](ReleaseGroup.md)

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

# **delete_group**
> delete_group(group_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import release_group_api
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
    api_instance = release_group_api.ReleaseGroupApi(api_client)
    group_id = "jUR,rZ#UM/?R,Fp^l6$ARjReleaseGroupQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_group(group_id)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ReleaseGroupApi->delete_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  |

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

# **get_group**
> ReleaseGroup get_group(group_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import release_group_api
from digitalai.release.v1.model.release_group import ReleaseGroup
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
    api_instance = release_group_api.ReleaseGroupApi(api_client)
    group_id = "jUR,rZ#UM/?R,Fp^l6$ARjReleaseGroupQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_group(group_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ReleaseGroupApi->get_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  |

### Return type

[**ReleaseGroup**](ReleaseGroup.md)

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

# **get_members**
> [str] get_members(group_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import release_group_api
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
    api_instance = release_group_api.ReleaseGroupApi(api_client)
    group_id = "jUR,rZ#UM/?R,Fp^l6$ARjReleaseGroupQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_members(group_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ReleaseGroupApi->get_members: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  |

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

# **get_release_group_timeline**
> ReleaseGroupTimeline get_release_group_timeline(group_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import release_group_api
from digitalai.release.v1.model.release_group_timeline import ReleaseGroupTimeline
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
    api_instance = release_group_api.ReleaseGroupApi(api_client)
    group_id = "jUR,rZ#UM/?R,Fp^l6$ARjReleaseGroupQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_release_group_timeline(group_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ReleaseGroupApi->get_release_group_timeline: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  |

### Return type

[**ReleaseGroupTimeline**](ReleaseGroupTimeline.md)

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

# **remove_members_from_group**
> remove_members_from_group(group_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import release_group_api
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
    api_instance = release_group_api.ReleaseGroupApi(api_client)
    group_id = "jUR,rZ#UM/?R,Fp^l6$ARjReleaseGroupQ" # str | 
    request_body = [
        "request_body_example",
    ] # [str] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.remove_members_from_group(group_id)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ReleaseGroupApi->remove_members_from_group: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.remove_members_from_group(group_id, request_body=request_body)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ReleaseGroupApi->remove_members_from_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  |
 **request_body** | **[str]**|  | [optional]

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

# **search_groups**
> [ReleaseGroup] search_groups()



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import release_group_api
from digitalai.release.v1.model.release_group_filters import ReleaseGroupFilters
from digitalai.release.v1.model.release_group import ReleaseGroup
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
    api_instance = release_group_api.ReleaseGroupApi(api_client)
    order_by = None # bool, date, datetime, dict, float, int, list, str, none_type |  (optional)
    page = 0 # int |  (optional) if omitted the server will use the default value of 0
    results_per_page = 100 # int |  (optional) if omitted the server will use the default value of 100
    release_group_filters = ReleaseGroupFilters(
        title="title_example",
        folder_id="folder_id_example",
        statuses=[
            ReleaseGroupStatus("PLANNED"),
        ],
    ) # ReleaseGroupFilters |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.search_groups(order_by=order_by, page=page, results_per_page=results_per_page, release_group_filters=release_group_filters)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ReleaseGroupApi->search_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_by** | **bool, date, datetime, dict, float, int, list, str, none_type**|  | [optional]
 **page** | **int**|  | [optional] if omitted the server will use the default value of 0
 **results_per_page** | **int**|  | [optional] if omitted the server will use the default value of 100
 **release_group_filters** | [**ReleaseGroupFilters**](ReleaseGroupFilters.md)|  | [optional]

### Return type

[**[ReleaseGroup]**](ReleaseGroup.md)

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

# **update_group**
> ReleaseGroup update_group(group_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import release_group_api
from digitalai.release.v1.model.release_group import ReleaseGroup
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
    api_instance = release_group_api.ReleaseGroupApi(api_client)
    group_id = "jUR,rZ#UM/?R,Fp^l6$ARjReleaseGroupQ" # str | 
    release_group = ReleaseGroup(
        id="id_example",
        type="type_example",
        metadata={
            "key": {},
        },
        title="title_example",
        status=ReleaseGroupStatus("PLANNED"),
        start_date=dateutil_parser('2023-03-20T02:07:00Z'),
        end_date=dateutil_parser('2023-03-20T02:07:00Z'),
        risk_score=1,
        release_ids=[
            "release_ids_example",
        ],
        progress=1,
        folder_id="folder_id_example",
        updatable=True,
    ) # ReleaseGroup |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_group(group_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ReleaseGroupApi->update_group: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_group(group_id, release_group=release_group)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ReleaseGroupApi->update_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  |
 **release_group** | [**ReleaseGroup**](ReleaseGroup.md)|  | [optional]

### Return type

[**ReleaseGroup**](ReleaseGroup.md)

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

