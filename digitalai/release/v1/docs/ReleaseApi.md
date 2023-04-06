# digitalai.release.v1.ReleaseApi

All URIs are relative to *http://localhost:5516*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abort**](ReleaseApi.md#abort) | **POST** /api/v1/releases/{releaseId}/abort | 
[**count_releases**](ReleaseApi.md#count_releases) | **POST** /api/v1/releases/count | 
[**create_release_variable**](ReleaseApi.md#create_release_variable) | **POST** /api/v1/releases/{releaseId}/variables | 
[**delete_release**](ReleaseApi.md#delete_release) | **DELETE** /api/v1/releases/{releaseId} | 
[**delete_release_variable**](ReleaseApi.md#delete_release_variable) | **DELETE** /api/v1/releases/{variableId} | 
[**download_attachment**](ReleaseApi.md#download_attachment) | **GET** /api/v1/releases/attachments/{attachmentId} | 
[**full_search_releases**](ReleaseApi.md#full_search_releases) | **POST** /api/v1/releases/fullSearch | 
[**get_active_tasks**](ReleaseApi.md#get_active_tasks) | **GET** /api/v1/releases/{releaseId}/active-tasks | 
[**get_archived_release**](ReleaseApi.md#get_archived_release) | **GET** /api/v1/releases/archived/{releaseId} | 
[**get_possible_release_variable_values**](ReleaseApi.md#get_possible_release_variable_values) | **GET** /api/v1/releases/{variableId}/possibleValues | 
[**get_release**](ReleaseApi.md#get_release) | **GET** /api/v1/releases/{releaseId} | 
[**get_release_permissions**](ReleaseApi.md#get_release_permissions) | **GET** /api/v1/releases/permissions | 
[**get_release_teams**](ReleaseApi.md#get_release_teams) | **GET** /api/v1/releases/{releaseId}/teams | 
[**get_release_variable**](ReleaseApi.md#get_release_variable) | **GET** /api/v1/releases/{variableId} | 
[**get_release_variables**](ReleaseApi.md#get_release_variables) | **GET** /api/v1/releases/{releaseId}/variables | 
[**get_releases**](ReleaseApi.md#get_releases) | **GET** /api/v1/releases | 
[**get_variable_values**](ReleaseApi.md#get_variable_values) | **GET** /api/v1/releases/{releaseId}/variableValues | 
[**is_variable_used_release**](ReleaseApi.md#is_variable_used_release) | **GET** /api/v1/releases/{variableId}/used | 
[**replace_release_variables**](ReleaseApi.md#replace_release_variables) | **POST** /api/v1/releases/{variableId}/replace | 
[**restart_phases**](ReleaseApi.md#restart_phases) | **POST** /api/v1/releases/{releaseId}/restart | 
[**resume**](ReleaseApi.md#resume) | **POST** /api/v1/releases/{releaseId}/resume | 
[**search_releases_by_title**](ReleaseApi.md#search_releases_by_title) | **GET** /api/v1/releases/byTitle | 
[**search_releases_release**](ReleaseApi.md#search_releases_release) | **POST** /api/v1/releases/search | 
[**set_release_teams**](ReleaseApi.md#set_release_teams) | **POST** /api/v1/releases/{releaseId}/teams | 
[**start_release**](ReleaseApi.md#start_release) | **POST** /api/v1/releases/{releaseId}/start | 
[**update_release**](ReleaseApi.md#update_release) | **PUT** /api/v1/releases/{releaseId} | 
[**update_release_variable**](ReleaseApi.md#update_release_variable) | **PUT** /api/v1/releases/{variableId} | 
[**update_release_variables**](ReleaseApi.md#update_release_variables) | **PUT** /api/v1/releases/{releaseId}/variables | 


# **abort**
> Release abort(release_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import release_api
from digitalai.release.v1.model.release import Release
from digitalai.release.v1.model.abort_release import AbortRelease
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
    api_instance = release_api.ReleaseApi(api_client)
    release_id = "jUR,rZ#UM/?R,Fp^l6$ARjReleaseQ" # str | 
    abort_release = AbortRelease(
        abort_comment="abort_comment_example",
    ) # AbortRelease |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.abort(release_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ReleaseApi->abort: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.abort(release_id, abort_release=abort_release)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ReleaseApi->abort: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release_id** | **str**|  |
 **abort_release** | [**AbortRelease**](AbortRelease.md)|  | [optional]

### Return type

[**Release**](Release.md)

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

# **count_releases**
> ReleaseCountResults count_releases()



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import release_api
from digitalai.release.v1.model.release_count_results import ReleaseCountResults
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
    api_instance = release_api.ReleaseApi(api_client)
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
    # and optional values
    try:
        api_response = api_instance.count_releases(releases_filters=releases_filters)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ReleaseApi->count_releases: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **releases_filters** | [**ReleasesFilters**](ReleasesFilters.md)|  | [optional]

### Return type

[**ReleaseCountResults**](ReleaseCountResults.md)

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

# **create_release_variable**
> Variable create_release_variable(release_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import release_api
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
    api_instance = release_api.ReleaseApi(api_client)
    release_id = "jUR,rZ#UM/?R,Fp^l6$ARj" # str | 
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
        api_response = api_instance.create_release_variable(release_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ReleaseApi->create_release_variable: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_release_variable(release_id, variable1=variable1)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ReleaseApi->create_release_variable: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release_id** | **str**|  |
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

# **delete_release**
> delete_release(release_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import release_api
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
    api_instance = release_api.ReleaseApi(api_client)
    release_id = "jUR,rZ#UM/?R,Fp^l6$ARjReleaseQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_release(release_id)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ReleaseApi->delete_release: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release_id** | **str**|  |

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

# **delete_release_variable**
> delete_release_variable(variable_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import release_api
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
    api_instance = release_api.ReleaseApi(api_client)
    variable_id = "jUR,rZ#UM/?R,Fp^l6$ARj/VariableQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_release_variable(variable_id)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ReleaseApi->delete_release_variable: %s\n" % e)
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

# **download_attachment**
> download_attachment(attachment_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import release_api
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
    api_instance = release_api.ReleaseApi(api_client)
    attachment_id = "jUR,rZ#UM/?R,Fp^l6$ARj/AttachmentQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.download_attachment(attachment_id)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ReleaseApi->download_attachment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | **str**|  |

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_search_releases**
> ReleaseFullSearchResult full_search_releases()



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import release_api
from digitalai.release.v1.model.release_full_search_result import ReleaseFullSearchResult
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
    api_instance = release_api.ReleaseApi(api_client)
    archive_page = 1 # int |  (optional)
    archive_results_per_page = 1 # int |  (optional)
    page = 1 # int |  (optional)
    results_per_page = 1 # int |  (optional)
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
    # and optional values
    try:
        api_response = api_instance.full_search_releases(archive_page=archive_page, archive_results_per_page=archive_results_per_page, page=page, results_per_page=results_per_page, releases_filters=releases_filters)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ReleaseApi->full_search_releases: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **archive_page** | **int**|  | [optional]
 **archive_results_per_page** | **int**|  | [optional]
 **page** | **int**|  | [optional]
 **results_per_page** | **int**|  | [optional]
 **releases_filters** | [**ReleasesFilters**](ReleasesFilters.md)|  | [optional]

### Return type

[**ReleaseFullSearchResult**](ReleaseFullSearchResult.md)

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

# **get_active_tasks**
> [Task] get_active_tasks(release_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import release_api
from digitalai.release.v1.model.task import Task
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
    api_instance = release_api.ReleaseApi(api_client)
    release_id = "jUR,rZ#UM/?R,Fp^l6$ARjReleaseQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_active_tasks(release_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ReleaseApi->get_active_tasks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release_id** | **str**|  |

### Return type

[**[Task]**](Task.md)

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

# **get_archived_release**
> Release get_archived_release(release_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import release_api
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
    api_instance = release_api.ReleaseApi(api_client)
    release_id = "jUR,rZ#UM/?R,Fp^l6$ARjReleaseQ" # str | 
    role_ids = False # bool |  (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_archived_release(release_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ReleaseApi->get_archived_release: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_archived_release(release_id, role_ids=role_ids)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ReleaseApi->get_archived_release: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release_id** | **str**|  |
 **role_ids** | **bool**|  | [optional] if omitted the server will use the default value of False

### Return type

[**Release**](Release.md)

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

# **get_possible_release_variable_values**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_possible_release_variable_values(variable_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import release_api
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
    api_instance = release_api.ReleaseApi(api_client)
    variable_id = "jUR,rZ#UM/?R,Fp^l6$ARj/VariableQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_possible_release_variable_values(variable_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ReleaseApi->get_possible_release_variable_values: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variable_id** | **str**|  |

### Return type

**[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]**

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

# **get_release**
> Release get_release(release_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import release_api
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
    api_instance = release_api.ReleaseApi(api_client)
    release_id = "jUR,rZ#UM/?R,Fp^l6$ARjbhJk C>i H'qT\{<?'es#)#iK.YM{Rag2/!KB!k@5oXh.:Ts";mGL,i&z5[P@M"lzfB+Y,Twzfu~N^z"mfqecVU{SmA{QA<Y8XX0<}J;Krm9W'g~?)DvDDLE7-'(u+-7Tfp&\`F+7-?{%@=iEPLVY*a@A[b_6cfy~~0GcD_@b4Y=U?otReleaseg" # str | 
    role_ids = False # bool |  (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_release(release_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ReleaseApi->get_release: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_release(release_id, role_ids=role_ids)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ReleaseApi->get_release: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release_id** | **str**|  |
 **role_ids** | **bool**|  | [optional] if omitted the server will use the default value of False

### Return type

[**Release**](Release.md)

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

# **get_release_permissions**
> [str] get_release_permissions()



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import release_api
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
    api_instance = release_api.ReleaseApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_release_permissions()
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ReleaseApi->get_release_permissions: %s\n" % e)
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

# **get_release_teams**
> [TeamView] get_release_teams(release_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import release_api
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
    api_instance = release_api.ReleaseApi(api_client)
    release_id = "jUR,rZ#UM/?R,Fp^l6$ARjReleaseQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_release_teams(release_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ReleaseApi->get_release_teams: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release_id** | **str**|  |

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

# **get_release_variable**
> Variable get_release_variable(variable_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import release_api
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
    api_instance = release_api.ReleaseApi(api_client)
    variable_id = "jUR,rZ#UM/?R,Fp^l6$ARj/VariableQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_release_variable(variable_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ReleaseApi->get_release_variable: %s\n" % e)
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

# **get_release_variables**
> [Variable] get_release_variables(release_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import release_api
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
    api_instance = release_api.ReleaseApi(api_client)
    release_id = "jUR,rZ#UM/?R,Fp^l6$ARjReleaseQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_release_variables(release_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ReleaseApi->get_release_variables: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release_id** | **str**|  |

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

# **get_releases**
> [Release] get_releases()



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import release_api
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
    api_instance = release_api.ReleaseApi(api_client)
    depth = 1 # int |  (optional) if omitted the server will use the default value of 1
    page = 0 # int |  (optional) if omitted the server will use the default value of 0
    results_per_page = 100 # int |  (optional) if omitted the server will use the default value of 100

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_releases(depth=depth, page=page, results_per_page=results_per_page)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ReleaseApi->get_releases: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **depth** | **int**|  | [optional] if omitted the server will use the default value of 1
 **page** | **int**|  | [optional] if omitted the server will use the default value of 0
 **results_per_page** | **int**|  | [optional] if omitted the server will use the default value of 100

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

# **get_variable_values**
> {str: (str,)} get_variable_values(release_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import release_api
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
    api_instance = release_api.ReleaseApi(api_client)
    release_id = "jUR,rZ#UM/?R,Fp^l6$ARjReleaseQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_variable_values(release_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ReleaseApi->get_variable_values: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release_id** | **str**|  |

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

# **is_variable_used_release**
> bool is_variable_used_release(variable_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import release_api
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
    api_instance = release_api.ReleaseApi(api_client)
    variable_id = "jUR,rZ#UM/?R,Fp^l6$ARj/VariableQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.is_variable_used_release(variable_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ReleaseApi->is_variable_used_release: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variable_id** | **str**|  |

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

# **replace_release_variables**
> replace_release_variables(variable_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import release_api
from digitalai.release.v1.model.variable_or_value import VariableOrValue
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
    api_instance = release_api.ReleaseApi(api_client)
    variable_id = "jUR,rZ#UM/?R,Fp^l6$ARj/VariableQ" # str | 
    variable_or_value = VariableOrValue(
        variable="variable_example",
        value=None,
    ) # VariableOrValue |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.replace_release_variables(variable_id)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ReleaseApi->replace_release_variables: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.replace_release_variables(variable_id, variable_or_value=variable_or_value)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ReleaseApi->replace_release_variables: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variable_id** | **str**|  |
 **variable_or_value** | [**VariableOrValue**](VariableOrValue.md)|  | [optional]

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

# **restart_phases**
> Release restart_phases(release_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import release_api
from digitalai.release.v1.model.release import Release
from digitalai.release.v1.model.phase_version import PhaseVersion
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
    api_instance = release_api.ReleaseApi(api_client)
    release_id = "jUR,rZ#UM/?R,Fp^l6$ARjReleaseQ" # str | 
    from_phase_id = "fromPhaseId_example" # str |  (optional)
    from_task_id = "fromTaskId_example" # str |  (optional)
    phase_version = PhaseVersion("LATEST") # PhaseVersion |  (optional)
    resume = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.restart_phases(release_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ReleaseApi->restart_phases: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.restart_phases(release_id, from_phase_id=from_phase_id, from_task_id=from_task_id, phase_version=phase_version, resume=resume)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ReleaseApi->restart_phases: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release_id** | **str**|  |
 **from_phase_id** | **str**|  | [optional]
 **from_task_id** | **str**|  | [optional]
 **phase_version** | **PhaseVersion**|  | [optional]
 **resume** | **bool**|  | [optional]

### Return type

[**Release**](Release.md)

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

# **resume**
> Release resume(release_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import release_api
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
    api_instance = release_api.ReleaseApi(api_client)
    release_id = "jUR,rZ#UM/?R,Fp^l6$ARjReleaseQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.resume(release_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ReleaseApi->resume: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release_id** | **str**|  |

### Return type

[**Release**](Release.md)

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

# **search_releases_by_title**
> [Release] search_releases_by_title()



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import release_api
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
    api_instance = release_api.ReleaseApi(api_client)
    release_title = "releaseTitle_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.search_releases_by_title(release_title=release_title)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ReleaseApi->search_releases_by_title: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release_title** | **str**|  | [optional]

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

# **search_releases_release**
> [Release] search_releases_release()



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import release_api
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
    api_instance = release_api.ReleaseApi(api_client)
    page = 0 # int |  (optional) if omitted the server will use the default value of 0
    page_is_offset = False # bool |  (optional) if omitted the server will use the default value of False
    results_per_page = 100 # int |  (optional) if omitted the server will use the default value of 100
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
    # and optional values
    try:
        api_response = api_instance.search_releases_release(page=page, page_is_offset=page_is_offset, results_per_page=results_per_page, releases_filters=releases_filters)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ReleaseApi->search_releases_release: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] if omitted the server will use the default value of 0
 **page_is_offset** | **bool**|  | [optional] if omitted the server will use the default value of False
 **results_per_page** | **int**|  | [optional] if omitted the server will use the default value of 100
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

# **set_release_teams**
> [TeamView] set_release_teams(release_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import release_api
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
    api_instance = release_api.ReleaseApi(api_client)
    release_id = "jUR,rZ#UM/?R,Fp^l6$ARjReleaseQ" # str | 
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
        api_response = api_instance.set_release_teams(release_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ReleaseApi->set_release_teams: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.set_release_teams(release_id, team_view=team_view)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ReleaseApi->set_release_teams: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release_id** | **str**|  |
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

# **start_release**
> Release start_release(release_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import release_api
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
    api_instance = release_api.ReleaseApi(api_client)
    release_id = "jUR,rZ#UM/?R,Fp^l6$ARjReleaseQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.start_release(release_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ReleaseApi->start_release: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release_id** | **str**|  |

### Return type

[**Release**](Release.md)

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

# **update_release**
> Release update_release(release_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import release_api
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
    api_instance = release_api.ReleaseApi(api_client)
    release_id = "jUR,rZ#UM/?R,Fp^l6$ARjReleaseQ" # str | 
    release = Release(
        id="id_example",
        type="type_example",
        start_date=dateutil_parser('2023-03-20T02:07:00Z'),
        scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
        end_date=dateutil_parser('2023-03-20T02:07:00Z'),
        due_date=dateutil_parser('2023-03-20T02:07:00Z'),
        title="title_example",
        description="description_example",
        owner="owner_example",
        planned_duration=1,
        flag_status=FlagStatus("OK"),
        flag_comment="flag_comment_example",
        overdue_notified=True,
        flagged=True,
        start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
        end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
        overdue=True,
        or_calculate_due_date="or_calculate_due_date_example",
        computed_planned_duration={},
        actual_duration={},
        root_release_id="root_release_id_example",
        max_concurrent_releases=1,
        release_triggers=[
            ReleaseTrigger(
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
                poll_type=PollType("REPEAT"),
                periodicity="periodicity_example",
                initial_fire=True,
                release_title="release_title_example",
                execution_id="execution_id_example",
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
                template="template_example",
                tags=[
                    "tags_example",
                ],
                release_folder="release_folder_example",
                internal_properties=[
                    "internal_properties_example",
                ],
                template_variables={
                    "key": "key_example",
                },
                template_password_variables={
                    "key": "key_example",
                },
                trigger_state_from_results="trigger_state_from_results_example",
                script_variable_names=[
                    "script_variable_names_example",
                ],
                script_variables_from_results={
                    "key": {},
                },
                string_script_variable_values={
                    "key": "key_example",
                },
                script_variable_values={
                    "key": {},
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
                container_id="container_id_example",
            ),
        ],
        teams=[
            Team(
                id="id_example",
                type="type_example",
                team_name="team_name_example",
                members=[
                    "members_example",
                ],
                roles=[
                    "roles_example",
                ],
                permissions=[
                    "permissions_example",
                ],
                release_admin_team=True,
                template_owner_team=True,
                folder_owner_team=True,
                folder_admin_team=True,
                system_team=True,
            ),
        ],
        member_viewers=[
            "member_viewers_example",
        ],
        role_viewers=[
            "role_viewers_example",
        ],
        attachments=[
            Attachment(
                id="id_example",
                type="type_example",
                file={},
                content_type="content_type_example",
                export_filename="export_filename_example",
                file_uri="file_uri_example",
                placeholders=[
                    "placeholders_example",
                ],
                text_file_names_regex="text_file_names_regex_example",
                exclude_file_names_regex="exclude_file_names_regex_example",
                file_encodings={
                    "key": "key_example",
                },
                checksum="checksum_example",
            ),
        ],
        phases=[
            Phase(
                id="id_example",
                type="type_example",
                locked=True,
                title="title_example",
                description="description_example",
                owner="owner_example",
                scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                planned_duration=1,
                flag_status=FlagStatus("OK"),
                flag_comment="flag_comment_example",
                overdue_notified=True,
                flagged=True,
                start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                overdue=True,
                or_calculate_due_date="or_calculate_due_date_example",
                computed_planned_duration={},
                actual_duration={},
                release_uid=1,
                tasks=[
                    Task(
                        id="id_example",
                        type="type_example",
                        scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        flag_status=FlagStatus("OK"),
                        title="title_example",
                        description="description_example",
                        owner="owner_example",
                        due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        planned_duration=1,
                        flag_comment="flag_comment_example",
                        overdue_notified=True,
                        flagged=True,
                        start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        overdue=True,
                        or_calculate_due_date="or_calculate_due_date_example",
                        computed_planned_duration={},
                        actual_duration={},
                        release_uid=1,
                        ci_uid=1,
                        comments=[
                            Comment(
                                id="id_example",
                                type="type_example",
                                text="text_example",
                                author="author_example",
                                date=dateutil_parser('2023-03-20T02:07:00Z'),
                                creation_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            ),
                        ],
                        container=None,
                        facets=[
                            Facet(
                                id="id_example",
                                type="type_example",
                                scope=FacetScope("TASK"),
                                target_id="target_id_example",
                                configuration_uri="configuration_uri_example",
                                variable_mapping={
                                    "key": "key_example",
                                },
                                variable_usages=[
                                    UsagePoint(
                                        target_property=CiProperty(
                                            wrapped=CiProperty(),
                                            last_property=ModelProperty(
                                                indexed_property_pattern="indexed_property_pattern_example",
                                                property_name="property_name_example",
                                                index=1,
                                                indexed=True,
                                            ),
                                            parent={},
                                            exists=True,
                                            property_name="property_name_example",
                                            value={},
                                            parent_ci={},
                                            descriptor={},
                                            kind={},
                                            category="category_example",
                                            password=True,
                                            indexed=True,
                                        ),
                                    ),
                                ],
                                properties_with_variables=[
                                    None,
                                ],
                            ),
                        ],
                        attachments=[
                            Attachment(
                                id="id_example",
                                type="type_example",
                                file={},
                                content_type="content_type_example",
                                export_filename="export_filename_example",
                                file_uri="file_uri_example",
                                placeholders=[
                                    "placeholders_example",
                                ],
                                text_file_names_regex="text_file_names_regex_example",
                                exclude_file_names_regex="exclude_file_names_regex_example",
                                file_encodings={
                                    "key": "key_example",
                                },
                                checksum="checksum_example",
                            ),
                        ],
                        status=TaskStatus("PLANNED"),
                        team="team_example",
                        watchers=[
                            "watchers_example",
                        ],
                        wait_for_scheduled_start_date=True,
                        delay_during_blackout=True,
                        postponed_due_to_blackout=True,
                        postponed_until_environments_are_reserved=True,
                        original_scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        has_been_flagged=True,
                        has_been_delayed=True,
                        precondition="precondition_example",
                        failure_handler="failure_handler_example",
                        task_failure_handler_enabled=True,
                        task_recover_op=TaskRecoverOp("SKIP_TASK"),
                        failures_count=1,
                        execution_id="execution_id_example",
                        variable_mapping={
                            "key": "key_example",
                        },
                        external_variable_mapping={
                            "key": "key_example",
                        },
                        max_comment_size=1,
                        tags=[
                            "tags_example",
                        ],
                        configuration_uri="configuration_uri_example",
                        due_soon_notified=True,
                        locked=True,
                        check_attributes=True,
                        abort_script="abort_script_example",
                        phase=Phase(),
                        blackout_metadata=BlackoutMetadata(
                            periods=[
                                BlackoutPeriod(
                                    start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                ),
                            ],
                        ),
                        flagged_count=1,
                        delayed_count=1,
                        done=True,
                        done_in_advance=True,
                        defunct=True,
                        updatable=True,
                        aborted=True,
                        not_yet_reached=True,
                        planned=True,
                        active=True,
                        in_progress=True,
                        pending=True,
                        waiting_for_input=True,
                        failed=True,
                        failing=True,
                        completed_in_advance=True,
                        skipped=True,
                        skipped_in_advance=True,
                        precondition_in_progress=True,
                        failure_handler_in_progress=True,
                        abort_script_in_progress=True,
                        facet_in_progress=True,
                        movable=True,
                        gate=True,
                        task_group=True,
                        parallel_group=True,
                        precondition_enabled=True,
                        failure_handler_enabled=True,
                        release=Release(),
                        display_path="display_path_example",
                        release_owner="release_owner_example",
                        all_tasks=[],
                        children=[
                            PlanItem(
                                id="id_example",
                                type="type_example",
                                title="title_example",
                                description="description_example",
                                owner="owner_example",
                                scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                planned_duration=1,
                                flag_status=FlagStatus("OK"),
                                flag_comment="flag_comment_example",
                                overdue_notified=True,
                                flagged=True,
                                start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                children=[],
                                overdue=True,
                                done=True,
                                release=Release(),
                                release_uid=1,
                                updatable=True,
                                display_path="display_path_example",
                                aborted=True,
                                active=True,
                                variable_usages=[
                                    UsagePoint(
                                        target_property=CiProperty(
                                            wrapped=CiProperty(),
                                            last_property=ModelProperty(
                                                indexed_property_pattern="indexed_property_pattern_example",
                                                property_name="property_name_example",
                                                index=1,
                                                indexed=True,
                                            ),
                                            parent={},
                                            exists=True,
                                            property_name="property_name_example",
                                            value={},
                                            parent_ci={},
                                            descriptor={},
                                            kind={},
                                            category="category_example",
                                            password=True,
                                            indexed=True,
                                        ),
                                    ),
                                ],
                                or_calculate_due_date="or_calculate_due_date_example",
                                computed_planned_duration={},
                                actual_duration={},
                            ),
                        ],
                        variable_usages=[
                            UsagePoint(
                                target_property=CiProperty(
                                    wrapped=CiProperty(),
                                    last_property=ModelProperty(
                                        indexed_property_pattern="indexed_property_pattern_example",
                                        property_name="property_name_example",
                                        index=1,
                                        indexed=True,
                                    ),
                                    parent={},
                                    exists=True,
                                    property_name="property_name_example",
                                    value={},
                                    parent_ci={},
                                    descriptor={},
                                    kind={},
                                    category="category_example",
                                    password=True,
                                    indexed=True,
                                ),
                            ),
                        ],
                        input_variables=[
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
                        referenced_variables=[
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
                        unbound_required_variables=[
                            "unbound_required_variables_example",
                        ],
                        automated=True,
                        task_type={},
                        due_soon=True,
                        elapsed_duration_fraction=3.14,
                        url="url_example",
                    ),
                ],
                release=None,
                status=PhaseStatus("PLANNED"),
                color="color_example",
                origin_id="origin_id_example",
                current_task=Task(
                    id="id_example",
                    type="type_example",
                    scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    flag_status=FlagStatus("OK"),
                    title="title_example",
                    description="description_example",
                    owner="owner_example",
                    due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    planned_duration=1,
                    flag_comment="flag_comment_example",
                    overdue_notified=True,
                    flagged=True,
                    start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    overdue=True,
                    or_calculate_due_date="or_calculate_due_date_example",
                    computed_planned_duration={},
                    actual_duration={},
                    release_uid=1,
                    ci_uid=1,
                    comments=[
                        Comment(
                            id="id_example",
                            type="type_example",
                            text="text_example",
                            author="author_example",
                            date=dateutil_parser('2023-03-20T02:07:00Z'),
                            creation_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        ),
                    ],
                    container=None,
                    facets=[
                        Facet(
                            id="id_example",
                            type="type_example",
                            scope=FacetScope("TASK"),
                            target_id="target_id_example",
                            configuration_uri="configuration_uri_example",
                            variable_mapping={
                                "key": "key_example",
                            },
                            variable_usages=[
                                UsagePoint(
                                    target_property=CiProperty(
                                        wrapped=CiProperty(),
                                        last_property=ModelProperty(
                                            indexed_property_pattern="indexed_property_pattern_example",
                                            property_name="property_name_example",
                                            index=1,
                                            indexed=True,
                                        ),
                                        parent={},
                                        exists=True,
                                        property_name="property_name_example",
                                        value={},
                                        parent_ci={},
                                        descriptor={},
                                        kind={},
                                        category="category_example",
                                        password=True,
                                        indexed=True,
                                    ),
                                ),
                            ],
                            properties_with_variables=[
                                None,
                            ],
                        ),
                    ],
                    attachments=[
                        Attachment(
                            id="id_example",
                            type="type_example",
                            file={},
                            content_type="content_type_example",
                            export_filename="export_filename_example",
                            file_uri="file_uri_example",
                            placeholders=[
                                "placeholders_example",
                            ],
                            text_file_names_regex="text_file_names_regex_example",
                            exclude_file_names_regex="exclude_file_names_regex_example",
                            file_encodings={
                                "key": "key_example",
                            },
                            checksum="checksum_example",
                        ),
                    ],
                    status=TaskStatus("PLANNED"),
                    team="team_example",
                    watchers=[
                        "watchers_example",
                    ],
                    wait_for_scheduled_start_date=True,
                    delay_during_blackout=True,
                    postponed_due_to_blackout=True,
                    postponed_until_environments_are_reserved=True,
                    original_scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    has_been_flagged=True,
                    has_been_delayed=True,
                    precondition="precondition_example",
                    failure_handler="failure_handler_example",
                    task_failure_handler_enabled=True,
                    task_recover_op=TaskRecoverOp("SKIP_TASK"),
                    failures_count=1,
                    execution_id="execution_id_example",
                    variable_mapping={
                        "key": "key_example",
                    },
                    external_variable_mapping={
                        "key": "key_example",
                    },
                    max_comment_size=1,
                    tags=[
                        "tags_example",
                    ],
                    configuration_uri="configuration_uri_example",
                    due_soon_notified=True,
                    locked=True,
                    check_attributes=True,
                    abort_script="abort_script_example",
                    phase=Phase(),
                    blackout_metadata=BlackoutMetadata(
                        periods=[
                            BlackoutPeriod(
                                start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            ),
                        ],
                    ),
                    flagged_count=1,
                    delayed_count=1,
                    done=True,
                    done_in_advance=True,
                    defunct=True,
                    updatable=True,
                    aborted=True,
                    not_yet_reached=True,
                    planned=True,
                    active=True,
                    in_progress=True,
                    pending=True,
                    waiting_for_input=True,
                    failed=True,
                    failing=True,
                    completed_in_advance=True,
                    skipped=True,
                    skipped_in_advance=True,
                    precondition_in_progress=True,
                    failure_handler_in_progress=True,
                    abort_script_in_progress=True,
                    facet_in_progress=True,
                    movable=True,
                    gate=True,
                    task_group=True,
                    parallel_group=True,
                    precondition_enabled=True,
                    failure_handler_enabled=True,
                    release=Release(),
                    display_path="display_path_example",
                    release_owner="release_owner_example",
                    all_tasks=[
                        Task(),
                    ],
                    children=[
                        PlanItem(
                            id="id_example",
                            type="type_example",
                            title="title_example",
                            description="description_example",
                            owner="owner_example",
                            scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            planned_duration=1,
                            flag_status=FlagStatus("OK"),
                            flag_comment="flag_comment_example",
                            overdue_notified=True,
                            flagged=True,
                            start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            children=[],
                            overdue=True,
                            done=True,
                            release=Release(),
                            release_uid=1,
                            updatable=True,
                            display_path="display_path_example",
                            aborted=True,
                            active=True,
                            variable_usages=[
                                UsagePoint(
                                    target_property=CiProperty(
                                        wrapped=CiProperty(),
                                        last_property=ModelProperty(
                                            indexed_property_pattern="indexed_property_pattern_example",
                                            property_name="property_name_example",
                                            index=1,
                                            indexed=True,
                                        ),
                                        parent={},
                                        exists=True,
                                        property_name="property_name_example",
                                        value={},
                                        parent_ci={},
                                        descriptor={},
                                        kind={},
                                        category="category_example",
                                        password=True,
                                        indexed=True,
                                    ),
                                ),
                            ],
                            or_calculate_due_date="or_calculate_due_date_example",
                            computed_planned_duration={},
                            actual_duration={},
                        ),
                    ],
                    variable_usages=[
                        UsagePoint(
                            target_property=CiProperty(
                                wrapped=CiProperty(),
                                last_property=ModelProperty(
                                    indexed_property_pattern="indexed_property_pattern_example",
                                    property_name="property_name_example",
                                    index=1,
                                    indexed=True,
                                ),
                                parent={},
                                exists=True,
                                property_name="property_name_example",
                                value={},
                                parent_ci={},
                                descriptor={},
                                kind={},
                                category="category_example",
                                password=True,
                                indexed=True,
                            ),
                        ),
                    ],
                    input_variables=[
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
                    referenced_variables=[
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
                    unbound_required_variables=[
                        "unbound_required_variables_example",
                    ],
                    automated=True,
                    task_type={},
                    due_soon=True,
                    elapsed_duration_fraction=3.14,
                    url="url_example",
                ),
                display_path="display_path_example",
                active=True,
                done=True,
                defunct=True,
                updatable=True,
                aborted=True,
                planned=True,
                failed=True,
                failing=True,
                release_owner="release_owner_example",
                all_gates=[
                    GateTask(
                        id="id_example",
                        type="type_example",
                        scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        flag_status=FlagStatus("OK"),
                        title="title_example",
                        description="description_example",
                        owner="owner_example",
                        due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        planned_duration=1,
                        flag_comment="flag_comment_example",
                        overdue_notified=True,
                        flagged=True,
                        start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        overdue=True,
                        or_calculate_due_date="or_calculate_due_date_example",
                        computed_planned_duration={},
                        actual_duration={},
                        release_uid=1,
                        ci_uid=1,
                        comments=[
                            Comment(
                                id="id_example",
                                type="type_example",
                                text="text_example",
                                author="author_example",
                                date=dateutil_parser('2023-03-20T02:07:00Z'),
                                creation_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            ),
                        ],
                        container=TaskContainer(
                            id="id_example",
                            type="type_example",
                            tasks=[
                                Task(
                                    id="id_example",
                                    type="type_example",
                                    scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    flag_status=FlagStatus("OK"),
                                    title="title_example",
                                    description="description_example",
                                    owner="owner_example",
                                    due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    planned_duration=1,
                                    flag_comment="flag_comment_example",
                                    overdue_notified=True,
                                    flagged=True,
                                    start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    overdue=True,
                                    or_calculate_due_date="or_calculate_due_date_example",
                                    computed_planned_duration={},
                                    actual_duration={},
                                    release_uid=1,
                                    ci_uid=1,
                                    comments=[
                                        Comment(
                                            id="id_example",
                                            type="type_example",
                                            text="text_example",
                                            author="author_example",
                                            date=dateutil_parser('2023-03-20T02:07:00Z'),
                                            creation_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        ),
                                    ],
                                    container=None,
                                    facets=[
                                        Facet(
                                            id="id_example",
                                            type="type_example",
                                            scope=FacetScope("TASK"),
                                            target_id="target_id_example",
                                            configuration_uri="configuration_uri_example",
                                            variable_mapping={
                                                "key": "key_example",
                                            },
                                            variable_usages=[
                                                UsagePoint(
                                                    target_property=CiProperty(
                                                        wrapped=CiProperty(),
                                                        last_property=ModelProperty(
                                                            indexed_property_pattern="indexed_property_pattern_example",
                                                            property_name="property_name_example",
                                                            index=1,
                                                            indexed=True,
                                                        ),
                                                        parent={},
                                                        exists=True,
                                                        property_name="property_name_example",
                                                        value={},
                                                        parent_ci={},
                                                        descriptor={},
                                                        kind={},
                                                        category="category_example",
                                                        password=True,
                                                        indexed=True,
                                                    ),
                                                ),
                                            ],
                                            properties_with_variables=[
                                                None,
                                            ],
                                        ),
                                    ],
                                    attachments=[
                                        Attachment(
                                            id="id_example",
                                            type="type_example",
                                            file={},
                                            content_type="content_type_example",
                                            export_filename="export_filename_example",
                                            file_uri="file_uri_example",
                                            placeholders=[
                                                "placeholders_example",
                                            ],
                                            text_file_names_regex="text_file_names_regex_example",
                                            exclude_file_names_regex="exclude_file_names_regex_example",
                                            file_encodings={
                                                "key": "key_example",
                                            },
                                            checksum="checksum_example",
                                        ),
                                    ],
                                    status=TaskStatus("PLANNED"),
                                    team="team_example",
                                    watchers=[
                                        "watchers_example",
                                    ],
                                    wait_for_scheduled_start_date=True,
                                    delay_during_blackout=True,
                                    postponed_due_to_blackout=True,
                                    postponed_until_environments_are_reserved=True,
                                    original_scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    has_been_flagged=True,
                                    has_been_delayed=True,
                                    precondition="precondition_example",
                                    failure_handler="failure_handler_example",
                                    task_failure_handler_enabled=True,
                                    task_recover_op=TaskRecoverOp("SKIP_TASK"),
                                    failures_count=1,
                                    execution_id="execution_id_example",
                                    variable_mapping={
                                        "key": "key_example",
                                    },
                                    external_variable_mapping={
                                        "key": "key_example",
                                    },
                                    max_comment_size=1,
                                    tags=[
                                        "tags_example",
                                    ],
                                    configuration_uri="configuration_uri_example",
                                    due_soon_notified=True,
                                    locked=True,
                                    check_attributes=True,
                                    abort_script="abort_script_example",
                                    phase=Phase(),
                                    blackout_metadata=BlackoutMetadata(
                                        periods=[
                                            BlackoutPeriod(
                                                start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                                end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                            ),
                                        ],
                                    ),
                                    flagged_count=1,
                                    delayed_count=1,
                                    done=True,
                                    done_in_advance=True,
                                    defunct=True,
                                    updatable=True,
                                    aborted=True,
                                    not_yet_reached=True,
                                    planned=True,
                                    active=True,
                                    in_progress=True,
                                    pending=True,
                                    waiting_for_input=True,
                                    failed=True,
                                    failing=True,
                                    completed_in_advance=True,
                                    skipped=True,
                                    skipped_in_advance=True,
                                    precondition_in_progress=True,
                                    failure_handler_in_progress=True,
                                    abort_script_in_progress=True,
                                    facet_in_progress=True,
                                    movable=True,
                                    gate=True,
                                    task_group=True,
                                    parallel_group=True,
                                    precondition_enabled=True,
                                    failure_handler_enabled=True,
                                    release=Release(),
                                    display_path="display_path_example",
                                    release_owner="release_owner_example",
                                    all_tasks=[],
                                    children=[
                                        PlanItem(
                                            id="id_example",
                                            type="type_example",
                                            title="title_example",
                                            description="description_example",
                                            owner="owner_example",
                                            scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                            due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                            start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                            end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                            planned_duration=1,
                                            flag_status=FlagStatus("OK"),
                                            flag_comment="flag_comment_example",
                                            overdue_notified=True,
                                            flagged=True,
                                            start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                            end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                            children=[],
                                            overdue=True,
                                            done=True,
                                            release=Release(),
                                            release_uid=1,
                                            updatable=True,
                                            display_path="display_path_example",
                                            aborted=True,
                                            active=True,
                                            variable_usages=[
                                                UsagePoint(
                                                    target_property=CiProperty(
                                                        wrapped=CiProperty(),
                                                        last_property=ModelProperty(
                                                            indexed_property_pattern="indexed_property_pattern_example",
                                                            property_name="property_name_example",
                                                            index=1,
                                                            indexed=True,
                                                        ),
                                                        parent={},
                                                        exists=True,
                                                        property_name="property_name_example",
                                                        value={},
                                                        parent_ci={},
                                                        descriptor={},
                                                        kind={},
                                                        category="category_example",
                                                        password=True,
                                                        indexed=True,
                                                    ),
                                                ),
                                            ],
                                            or_calculate_due_date="or_calculate_due_date_example",
                                            computed_planned_duration={},
                                            actual_duration={},
                                        ),
                                    ],
                                    variable_usages=[
                                        UsagePoint(
                                            target_property=CiProperty(
                                                wrapped=CiProperty(),
                                                last_property=ModelProperty(
                                                    indexed_property_pattern="indexed_property_pattern_example",
                                                    property_name="property_name_example",
                                                    index=1,
                                                    indexed=True,
                                                ),
                                                parent={},
                                                exists=True,
                                                property_name="property_name_example",
                                                value={},
                                                parent_ci={},
                                                descriptor={},
                                                kind={},
                                                category="category_example",
                                                password=True,
                                                indexed=True,
                                            ),
                                        ),
                                    ],
                                    input_variables=[
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
                                    referenced_variables=[
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
                                    unbound_required_variables=[
                                        "unbound_required_variables_example",
                                    ],
                                    automated=True,
                                    task_type={},
                                    due_soon=True,
                                    elapsed_duration_fraction=3.14,
                                    url="url_example",
                                ),
                            ],
                            locked=True,
                            title="title_example",
                        ),
                        facets=[
                            Facet(
                                id="id_example",
                                type="type_example",
                                scope=FacetScope("TASK"),
                                target_id="target_id_example",
                                configuration_uri="configuration_uri_example",
                                variable_mapping={
                                    "key": "key_example",
                                },
                                variable_usages=[
                                    UsagePoint(
                                        target_property=CiProperty(
                                            wrapped=CiProperty(),
                                            last_property=ModelProperty(
                                                indexed_property_pattern="indexed_property_pattern_example",
                                                property_name="property_name_example",
                                                index=1,
                                                indexed=True,
                                            ),
                                            parent={},
                                            exists=True,
                                            property_name="property_name_example",
                                            value={},
                                            parent_ci={},
                                            descriptor={},
                                            kind={},
                                            category="category_example",
                                            password=True,
                                            indexed=True,
                                        ),
                                    ),
                                ],
                                properties_with_variables=[
                                    None,
                                ],
                            ),
                        ],
                        attachments=[
                            Attachment(
                                id="id_example",
                                type="type_example",
                                file={},
                                content_type="content_type_example",
                                export_filename="export_filename_example",
                                file_uri="file_uri_example",
                                placeholders=[
                                    "placeholders_example",
                                ],
                                text_file_names_regex="text_file_names_regex_example",
                                exclude_file_names_regex="exclude_file_names_regex_example",
                                file_encodings={
                                    "key": "key_example",
                                },
                                checksum="checksum_example",
                            ),
                        ],
                        status=TaskStatus("PLANNED"),
                        team="team_example",
                        watchers=[
                            "watchers_example",
                        ],
                        wait_for_scheduled_start_date=True,
                        delay_during_blackout=True,
                        postponed_due_to_blackout=True,
                        postponed_until_environments_are_reserved=True,
                        original_scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        has_been_flagged=True,
                        has_been_delayed=True,
                        precondition="precondition_example",
                        failure_handler="failure_handler_example",
                        task_failure_handler_enabled=True,
                        task_recover_op=TaskRecoverOp("SKIP_TASK"),
                        failures_count=1,
                        execution_id="execution_id_example",
                        variable_mapping={
                            "key": "key_example",
                        },
                        external_variable_mapping={
                            "key": "key_example",
                        },
                        max_comment_size=1,
                        tags=[
                            "tags_example",
                        ],
                        configuration_uri="configuration_uri_example",
                        due_soon_notified=True,
                        locked=True,
                        check_attributes=True,
                        abort_script="abort_script_example",
                        phase=Phase(),
                        blackout_metadata=BlackoutMetadata(
                            periods=[
                                BlackoutPeriod(
                                    start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                ),
                            ],
                        ),
                        flagged_count=1,
                        delayed_count=1,
                        done=True,
                        done_in_advance=True,
                        defunct=True,
                        updatable=True,
                        aborted=True,
                        not_yet_reached=True,
                        planned=True,
                        active=True,
                        in_progress=True,
                        pending=True,
                        waiting_for_input=True,
                        failed=True,
                        failing=True,
                        completed_in_advance=True,
                        skipped=True,
                        skipped_in_advance=True,
                        precondition_in_progress=True,
                        failure_handler_in_progress=True,
                        abort_script_in_progress=True,
                        facet_in_progress=True,
                        movable=True,
                        gate=True,
                        task_group=True,
                        parallel_group=True,
                        precondition_enabled=True,
                        failure_handler_enabled=True,
                        release=Release(),
                        display_path="display_path_example",
                        release_owner="release_owner_example",
                        all_tasks=[
                            Task(
                                id="id_example",
                                type="type_example",
                                scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                flag_status=FlagStatus("OK"),
                                title="title_example",
                                description="description_example",
                                owner="owner_example",
                                due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                planned_duration=1,
                                flag_comment="flag_comment_example",
                                overdue_notified=True,
                                flagged=True,
                                start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                overdue=True,
                                or_calculate_due_date="or_calculate_due_date_example",
                                computed_planned_duration={},
                                actual_duration={},
                                release_uid=1,
                                ci_uid=1,
                                comments=[
                                    Comment(
                                        id="id_example",
                                        type="type_example",
                                        text="text_example",
                                        author="author_example",
                                        date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        creation_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    ),
                                ],
                                container=None,
                                facets=[
                                    Facet(
                                        id="id_example",
                                        type="type_example",
                                        scope=FacetScope("TASK"),
                                        target_id="target_id_example",
                                        configuration_uri="configuration_uri_example",
                                        variable_mapping={
                                            "key": "key_example",
                                        },
                                        variable_usages=[
                                            UsagePoint(
                                                target_property=CiProperty(
                                                    wrapped=CiProperty(),
                                                    last_property=ModelProperty(
                                                        indexed_property_pattern="indexed_property_pattern_example",
                                                        property_name="property_name_example",
                                                        index=1,
                                                        indexed=True,
                                                    ),
                                                    parent={},
                                                    exists=True,
                                                    property_name="property_name_example",
                                                    value={},
                                                    parent_ci={},
                                                    descriptor={},
                                                    kind={},
                                                    category="category_example",
                                                    password=True,
                                                    indexed=True,
                                                ),
                                            ),
                                        ],
                                        properties_with_variables=[
                                            None,
                                        ],
                                    ),
                                ],
                                attachments=[
                                    Attachment(
                                        id="id_example",
                                        type="type_example",
                                        file={},
                                        content_type="content_type_example",
                                        export_filename="export_filename_example",
                                        file_uri="file_uri_example",
                                        placeholders=[
                                            "placeholders_example",
                                        ],
                                        text_file_names_regex="text_file_names_regex_example",
                                        exclude_file_names_regex="exclude_file_names_regex_example",
                                        file_encodings={
                                            "key": "key_example",
                                        },
                                        checksum="checksum_example",
                                    ),
                                ],
                                status=TaskStatus("PLANNED"),
                                team="team_example",
                                watchers=[
                                    "watchers_example",
                                ],
                                wait_for_scheduled_start_date=True,
                                delay_during_blackout=True,
                                postponed_due_to_blackout=True,
                                postponed_until_environments_are_reserved=True,
                                original_scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                has_been_flagged=True,
                                has_been_delayed=True,
                                precondition="precondition_example",
                                failure_handler="failure_handler_example",
                                task_failure_handler_enabled=True,
                                task_recover_op=TaskRecoverOp("SKIP_TASK"),
                                failures_count=1,
                                execution_id="execution_id_example",
                                variable_mapping={
                                    "key": "key_example",
                                },
                                external_variable_mapping={
                                    "key": "key_example",
                                },
                                max_comment_size=1,
                                tags=[
                                    "tags_example",
                                ],
                                configuration_uri="configuration_uri_example",
                                due_soon_notified=True,
                                locked=True,
                                check_attributes=True,
                                abort_script="abort_script_example",
                                phase=Phase(),
                                blackout_metadata=BlackoutMetadata(
                                    periods=[
                                        BlackoutPeriod(
                                            start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                            end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        ),
                                    ],
                                ),
                                flagged_count=1,
                                delayed_count=1,
                                done=True,
                                done_in_advance=True,
                                defunct=True,
                                updatable=True,
                                aborted=True,
                                not_yet_reached=True,
                                planned=True,
                                active=True,
                                in_progress=True,
                                pending=True,
                                waiting_for_input=True,
                                failed=True,
                                failing=True,
                                completed_in_advance=True,
                                skipped=True,
                                skipped_in_advance=True,
                                precondition_in_progress=True,
                                failure_handler_in_progress=True,
                                abort_script_in_progress=True,
                                facet_in_progress=True,
                                movable=True,
                                gate=True,
                                task_group=True,
                                parallel_group=True,
                                precondition_enabled=True,
                                failure_handler_enabled=True,
                                release=Release(),
                                display_path="display_path_example",
                                release_owner="release_owner_example",
                                all_tasks=[],
                                children=[
                                    PlanItem(
                                        id="id_example",
                                        type="type_example",
                                        title="title_example",
                                        description="description_example",
                                        owner="owner_example",
                                        scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        planned_duration=1,
                                        flag_status=FlagStatus("OK"),
                                        flag_comment="flag_comment_example",
                                        overdue_notified=True,
                                        flagged=True,
                                        start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        children=[],
                                        overdue=True,
                                        done=True,
                                        release=Release(),
                                        release_uid=1,
                                        updatable=True,
                                        display_path="display_path_example",
                                        aborted=True,
                                        active=True,
                                        variable_usages=[
                                            UsagePoint(
                                                target_property=CiProperty(
                                                    wrapped=CiProperty(),
                                                    last_property=ModelProperty(
                                                        indexed_property_pattern="indexed_property_pattern_example",
                                                        property_name="property_name_example",
                                                        index=1,
                                                        indexed=True,
                                                    ),
                                                    parent={},
                                                    exists=True,
                                                    property_name="property_name_example",
                                                    value={},
                                                    parent_ci={},
                                                    descriptor={},
                                                    kind={},
                                                    category="category_example",
                                                    password=True,
                                                    indexed=True,
                                                ),
                                            ),
                                        ],
                                        or_calculate_due_date="or_calculate_due_date_example",
                                        computed_planned_duration={},
                                        actual_duration={},
                                    ),
                                ],
                                variable_usages=[
                                    UsagePoint(
                                        target_property=CiProperty(
                                            wrapped=CiProperty(),
                                            last_property=ModelProperty(
                                                indexed_property_pattern="indexed_property_pattern_example",
                                                property_name="property_name_example",
                                                index=1,
                                                indexed=True,
                                            ),
                                            parent={},
                                            exists=True,
                                            property_name="property_name_example",
                                            value={},
                                            parent_ci={},
                                            descriptor={},
                                            kind={},
                                            category="category_example",
                                            password=True,
                                            indexed=True,
                                        ),
                                    ),
                                ],
                                input_variables=[
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
                                referenced_variables=[
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
                                unbound_required_variables=[
                                    "unbound_required_variables_example",
                                ],
                                automated=True,
                                task_type={},
                                due_soon=True,
                                elapsed_duration_fraction=3.14,
                                url="url_example",
                            ),
                        ],
                        children=[
                            PlanItem(
                                id="id_example",
                                type="type_example",
                                title="title_example",
                                description="description_example",
                                owner="owner_example",
                                scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                planned_duration=1,
                                flag_status=FlagStatus("OK"),
                                flag_comment="flag_comment_example",
                                overdue_notified=True,
                                flagged=True,
                                start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                children=[],
                                overdue=True,
                                done=True,
                                release=Release(),
                                release_uid=1,
                                updatable=True,
                                display_path="display_path_example",
                                aborted=True,
                                active=True,
                                variable_usages=[
                                    UsagePoint(
                                        target_property=CiProperty(
                                            wrapped=CiProperty(),
                                            last_property=ModelProperty(
                                                indexed_property_pattern="indexed_property_pattern_example",
                                                property_name="property_name_example",
                                                index=1,
                                                indexed=True,
                                            ),
                                            parent={},
                                            exists=True,
                                            property_name="property_name_example",
                                            value={},
                                            parent_ci={},
                                            descriptor={},
                                            kind={},
                                            category="category_example",
                                            password=True,
                                            indexed=True,
                                        ),
                                    ),
                                ],
                                or_calculate_due_date="or_calculate_due_date_example",
                                computed_planned_duration={},
                                actual_duration={},
                            ),
                        ],
                        input_variables=[
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
                        referenced_variables=[
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
                        unbound_required_variables=[
                            "unbound_required_variables_example",
                        ],
                        automated=True,
                        task_type={},
                        due_soon=True,
                        elapsed_duration_fraction=3.14,
                        url="url_example",
                        conditions=[
                            GateCondition(
                                id="id_example",
                                type="type_example",
                                title="title_example",
                                checked=True,
                            ),
                        ],
                        dependencies=[
                            Dependency(
                                id="id_example",
                                type="type_example",
                                gate_task=GateTask(),
                                target=PlanItem(
                                    id="id_example",
                                    type="type_example",
                                    title="title_example",
                                    description="description_example",
                                    owner="owner_example",
                                    scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    planned_duration=1,
                                    flag_status=FlagStatus("OK"),
                                    flag_comment="flag_comment_example",
                                    overdue_notified=True,
                                    flagged=True,
                                    start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    children=[
                                        PlanItem(),
                                    ],
                                    overdue=True,
                                    done=True,
                                    release=Release(),
                                    release_uid=1,
                                    updatable=True,
                                    display_path="display_path_example",
                                    aborted=True,
                                    active=True,
                                    variable_usages=[
                                        UsagePoint(
                                            target_property=CiProperty(
                                                wrapped=CiProperty(),
                                                last_property=ModelProperty(
                                                    indexed_property_pattern="indexed_property_pattern_example",
                                                    property_name="property_name_example",
                                                    index=1,
                                                    indexed=True,
                                                ),
                                                parent={},
                                                exists=True,
                                                property_name="property_name_example",
                                                value={},
                                                parent_ci={},
                                                descriptor={},
                                                kind={},
                                                category="category_example",
                                                password=True,
                                                indexed=True,
                                            ),
                                        ),
                                    ],
                                    or_calculate_due_date="or_calculate_due_date_example",
                                    computed_planned_duration={},
                                    actual_duration={},
                                ),
                                target_id="target_id_example",
                                archived_target_title="archived_target_title_example",
                                archived_target_id="archived_target_id_example",
                                archived_as_resolved=True,
                                metadata={
                                    "key": {},
                                },
                                archived=True,
                                done=True,
                                aborted=True,
                                target_display_path="target_display_path_example",
                                target_title="target_title_example",
                                valid_allowed_plan_item_id=True,
                            ),
                        ],
                        open=True,
                        open_in_advance=True,
                        completable=True,
                        aborted_dependency_titles="aborted_dependency_titles_example",
                        variable_usages=[
                            UsagePoint(
                                target_property=CiProperty(
                                    wrapped=CiProperty(),
                                    last_property=ModelProperty(
                                        indexed_property_pattern="indexed_property_pattern_example",
                                        property_name="property_name_example",
                                        index=1,
                                        indexed=True,
                                    ),
                                    parent={},
                                    exists=True,
                                    property_name="property_name_example",
                                    value={},
                                    parent_ci={},
                                    descriptor={},
                                    kind={},
                                    category="category_example",
                                    password=True,
                                    indexed=True,
                                ),
                            ),
                        ],
                    ),
                ],
                all_tasks=[
                    Task(
                        id="id_example",
                        type="type_example",
                        scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        flag_status=FlagStatus("OK"),
                        title="title_example",
                        description="description_example",
                        owner="owner_example",
                        due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        planned_duration=1,
                        flag_comment="flag_comment_example",
                        overdue_notified=True,
                        flagged=True,
                        start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        overdue=True,
                        or_calculate_due_date="or_calculate_due_date_example",
                        computed_planned_duration={},
                        actual_duration={},
                        release_uid=1,
                        ci_uid=1,
                        comments=[
                            Comment(
                                id="id_example",
                                type="type_example",
                                text="text_example",
                                author="author_example",
                                date=dateutil_parser('2023-03-20T02:07:00Z'),
                                creation_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            ),
                        ],
                        container=None,
                        facets=[
                            Facet(
                                id="id_example",
                                type="type_example",
                                scope=FacetScope("TASK"),
                                target_id="target_id_example",
                                configuration_uri="configuration_uri_example",
                                variable_mapping={
                                    "key": "key_example",
                                },
                                variable_usages=[
                                    UsagePoint(
                                        target_property=CiProperty(
                                            wrapped=CiProperty(),
                                            last_property=ModelProperty(
                                                indexed_property_pattern="indexed_property_pattern_example",
                                                property_name="property_name_example",
                                                index=1,
                                                indexed=True,
                                            ),
                                            parent={},
                                            exists=True,
                                            property_name="property_name_example",
                                            value={},
                                            parent_ci={},
                                            descriptor={},
                                            kind={},
                                            category="category_example",
                                            password=True,
                                            indexed=True,
                                        ),
                                    ),
                                ],
                                properties_with_variables=[
                                    None,
                                ],
                            ),
                        ],
                        attachments=[
                            Attachment(
                                id="id_example",
                                type="type_example",
                                file={},
                                content_type="content_type_example",
                                export_filename="export_filename_example",
                                file_uri="file_uri_example",
                                placeholders=[
                                    "placeholders_example",
                                ],
                                text_file_names_regex="text_file_names_regex_example",
                                exclude_file_names_regex="exclude_file_names_regex_example",
                                file_encodings={
                                    "key": "key_example",
                                },
                                checksum="checksum_example",
                            ),
                        ],
                        status=TaskStatus("PLANNED"),
                        team="team_example",
                        watchers=[
                            "watchers_example",
                        ],
                        wait_for_scheduled_start_date=True,
                        delay_during_blackout=True,
                        postponed_due_to_blackout=True,
                        postponed_until_environments_are_reserved=True,
                        original_scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        has_been_flagged=True,
                        has_been_delayed=True,
                        precondition="precondition_example",
                        failure_handler="failure_handler_example",
                        task_failure_handler_enabled=True,
                        task_recover_op=TaskRecoverOp("SKIP_TASK"),
                        failures_count=1,
                        execution_id="execution_id_example",
                        variable_mapping={
                            "key": "key_example",
                        },
                        external_variable_mapping={
                            "key": "key_example",
                        },
                        max_comment_size=1,
                        tags=[
                            "tags_example",
                        ],
                        configuration_uri="configuration_uri_example",
                        due_soon_notified=True,
                        locked=True,
                        check_attributes=True,
                        abort_script="abort_script_example",
                        phase=Phase(),
                        blackout_metadata=BlackoutMetadata(
                            periods=[
                                BlackoutPeriod(
                                    start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                ),
                            ],
                        ),
                        flagged_count=1,
                        delayed_count=1,
                        done=True,
                        done_in_advance=True,
                        defunct=True,
                        updatable=True,
                        aborted=True,
                        not_yet_reached=True,
                        planned=True,
                        active=True,
                        in_progress=True,
                        pending=True,
                        waiting_for_input=True,
                        failed=True,
                        failing=True,
                        completed_in_advance=True,
                        skipped=True,
                        skipped_in_advance=True,
                        precondition_in_progress=True,
                        failure_handler_in_progress=True,
                        abort_script_in_progress=True,
                        facet_in_progress=True,
                        movable=True,
                        gate=True,
                        task_group=True,
                        parallel_group=True,
                        precondition_enabled=True,
                        failure_handler_enabled=True,
                        release=Release(),
                        display_path="display_path_example",
                        release_owner="release_owner_example",
                        all_tasks=[],
                        children=[
                            PlanItem(
                                id="id_example",
                                type="type_example",
                                title="title_example",
                                description="description_example",
                                owner="owner_example",
                                scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                planned_duration=1,
                                flag_status=FlagStatus("OK"),
                                flag_comment="flag_comment_example",
                                overdue_notified=True,
                                flagged=True,
                                start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                children=[],
                                overdue=True,
                                done=True,
                                release=Release(),
                                release_uid=1,
                                updatable=True,
                                display_path="display_path_example",
                                aborted=True,
                                active=True,
                                variable_usages=[
                                    UsagePoint(
                                        target_property=CiProperty(
                                            wrapped=CiProperty(),
                                            last_property=ModelProperty(
                                                indexed_property_pattern="indexed_property_pattern_example",
                                                property_name="property_name_example",
                                                index=1,
                                                indexed=True,
                                            ),
                                            parent={},
                                            exists=True,
                                            property_name="property_name_example",
                                            value={},
                                            parent_ci={},
                                            descriptor={},
                                            kind={},
                                            category="category_example",
                                            password=True,
                                            indexed=True,
                                        ),
                                    ),
                                ],
                                or_calculate_due_date="or_calculate_due_date_example",
                                computed_planned_duration={},
                                actual_duration={},
                            ),
                        ],
                        variable_usages=[
                            UsagePoint(
                                target_property=CiProperty(
                                    wrapped=CiProperty(),
                                    last_property=ModelProperty(
                                        indexed_property_pattern="indexed_property_pattern_example",
                                        property_name="property_name_example",
                                        index=1,
                                        indexed=True,
                                    ),
                                    parent={},
                                    exists=True,
                                    property_name="property_name_example",
                                    value={},
                                    parent_ci={},
                                    descriptor={},
                                    kind={},
                                    category="category_example",
                                    password=True,
                                    indexed=True,
                                ),
                            ),
                        ],
                        input_variables=[
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
                        referenced_variables=[
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
                        unbound_required_variables=[
                            "unbound_required_variables_example",
                        ],
                        automated=True,
                        task_type={},
                        due_soon=True,
                        elapsed_duration_fraction=3.14,
                        url="url_example",
                    ),
                ],
                children=[
                    PlanItem(
                        id="id_example",
                        type="type_example",
                        title="title_example",
                        description="description_example",
                        owner="owner_example",
                        scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        planned_duration=1,
                        flag_status=FlagStatus("OK"),
                        flag_comment="flag_comment_example",
                        overdue_notified=True,
                        flagged=True,
                        start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        children=[],
                        overdue=True,
                        done=True,
                        release=Release(),
                        release_uid=1,
                        updatable=True,
                        display_path="display_path_example",
                        aborted=True,
                        active=True,
                        variable_usages=[
                            UsagePoint(
                                target_property=CiProperty(
                                    wrapped=CiProperty(),
                                    last_property=ModelProperty(
                                        indexed_property_pattern="indexed_property_pattern_example",
                                        property_name="property_name_example",
                                        index=1,
                                        indexed=True,
                                    ),
                                    parent={},
                                    exists=True,
                                    property_name="property_name_example",
                                    value={},
                                    parent_ci={},
                                    descriptor={},
                                    kind={},
                                    category="category_example",
                                    password=True,
                                    indexed=True,
                                ),
                            ),
                        ],
                        or_calculate_due_date="or_calculate_due_date_example",
                        computed_planned_duration={},
                        actual_duration={},
                    ),
                ],
                variable_usages=[
                    UsagePoint(
                        target_property=CiProperty(
                            wrapped=CiProperty(),
                            last_property=ModelProperty(
                                indexed_property_pattern="indexed_property_pattern_example",
                                property_name="property_name_example",
                                index=1,
                                indexed=True,
                            ),
                            parent={},
                            exists=True,
                            property_name="property_name_example",
                            value={},
                            parent_ci={},
                            descriptor={},
                            kind={},
                            category="category_example",
                            password=True,
                            indexed=True,
                        ),
                    ),
                ],
                original=True,
                phase_copied=True,
                ancestor_id="ancestor_id_example",
                latest_copy=True,
            ),
        ],
        queryable_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
        queryable_end_date=dateutil_parser('2023-03-20T02:07:00Z'),
        real_flag_status=FlagStatus("OK"),
        status=ReleaseStatus("TEMPLATE"),
        tags=[
            "tags_example",
        ],
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
        calendar_link_token="calendar_link_token_example",
        calendar_published=True,
        tutorial=True,
        abort_on_failure=True,
        archive_release=True,
        allow_passwords_in_all_fields=True,
        disable_notifications=True,
        allow_concurrent_releases_from_trigger=True,
        origin_template_id="origin_template_id_example",
        created_from_trigger=True,
        script_username="script_username_example",
        script_user_password="script_user_password_example",
        extensions=[
            ReleaseExtension(
                id="id_example",
                type="type_example",
                variable_usages=[
                    UsagePoint(
                        target_property=CiProperty(
                            wrapped=CiProperty(),
                            last_property=ModelProperty(
                                indexed_property_pattern="indexed_property_pattern_example",
                                property_name="property_name_example",
                                index=1,
                                indexed=True,
                            ),
                            parent={},
                            exists=True,
                            property_name="property_name_example",
                            value={},
                            parent_ci={},
                            descriptor={},
                            kind={},
                            category="category_example",
                            password=True,
                            indexed=True,
                        ),
                    ),
                ],
            ),
        ],
        started_from_task_id="started_from_task_id_example",
        auto_start=True,
        automated_resume_count=1,
        max_automated_resumes=1,
        abort_comment="abort_comment_example",
        variable_mapping={
            "key": "key_example",
        },
        risk_profile=None,
        metadata={
            "key": {},
        },
        archived=True,
        ci_uid=1,
        variable_values={
            "key": {},
        },
        password_variable_values={
            "key": {},
        },
        ci_property_variables=[
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
        all_string_variable_values={
            "key": "key_example",
        },
        all_release_global_and_folder_variables=[
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
        all_variable_values_as_strings_with_interpolation_info={
            "key": ValueWithInterpolation(
                value="value_example",
                prevent_interpolation=True,
            ),
        },
        variables_keys_in_non_interpolatable_variable_values=[
            "variables_keys_in_non_interpolatable_variable_values_example",
        ],
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
        global_variables=GlobalVariables(
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
            string_variable_values={
                "key": "key_example",
            },
            password_variable_values={
                "key": "key_example",
            },
        ),
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
        admin_team=Team(
            id="id_example",
            type="type_example",
            team_name="team_name_example",
            members=[
                "members_example",
            ],
            roles=[
                "roles_example",
            ],
            permissions=[
                "permissions_example",
            ],
            release_admin_team=True,
            template_owner_team=True,
            folder_owner_team=True,
            folder_admin_team=True,
            system_team=True,
        ),
        release_attachments=[
            Attachment(
                id="id_example",
                type="type_example",
                file={},
                content_type="content_type_example",
                export_filename="export_filename_example",
                file_uri="file_uri_example",
                placeholders=[
                    "placeholders_example",
                ],
                text_file_names_regex="text_file_names_regex_example",
                exclude_file_names_regex="exclude_file_names_regex_example",
                file_encodings={
                    "key": "key_example",
                },
                checksum="checksum_example",
            ),
        ],
        current_phase=Phase(
            id="id_example",
            type="type_example",
            locked=True,
            title="title_example",
            description="description_example",
            owner="owner_example",
            scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
            due_date=dateutil_parser('2023-03-20T02:07:00Z'),
            start_date=dateutil_parser('2023-03-20T02:07:00Z'),
            end_date=dateutil_parser('2023-03-20T02:07:00Z'),
            planned_duration=1,
            flag_status=FlagStatus("OK"),
            flag_comment="flag_comment_example",
            overdue_notified=True,
            flagged=True,
            start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
            end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
            overdue=True,
            or_calculate_due_date="or_calculate_due_date_example",
            computed_planned_duration={},
            actual_duration={},
            release_uid=1,
            tasks=[
                Task(
                    id="id_example",
                    type="type_example",
                    scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    flag_status=FlagStatus("OK"),
                    title="title_example",
                    description="description_example",
                    owner="owner_example",
                    due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    planned_duration=1,
                    flag_comment="flag_comment_example",
                    overdue_notified=True,
                    flagged=True,
                    start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    overdue=True,
                    or_calculate_due_date="or_calculate_due_date_example",
                    computed_planned_duration={},
                    actual_duration={},
                    release_uid=1,
                    ci_uid=1,
                    comments=[
                        Comment(
                            id="id_example",
                            type="type_example",
                            text="text_example",
                            author="author_example",
                            date=dateutil_parser('2023-03-20T02:07:00Z'),
                            creation_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        ),
                    ],
                    container=None,
                    facets=[
                        Facet(
                            id="id_example",
                            type="type_example",
                            scope=FacetScope("TASK"),
                            target_id="target_id_example",
                            configuration_uri="configuration_uri_example",
                            variable_mapping={
                                "key": "key_example",
                            },
                            variable_usages=[
                                UsagePoint(
                                    target_property=CiProperty(
                                        wrapped=CiProperty(),
                                        last_property=ModelProperty(
                                            indexed_property_pattern="indexed_property_pattern_example",
                                            property_name="property_name_example",
                                            index=1,
                                            indexed=True,
                                        ),
                                        parent={},
                                        exists=True,
                                        property_name="property_name_example",
                                        value={},
                                        parent_ci={},
                                        descriptor={},
                                        kind={},
                                        category="category_example",
                                        password=True,
                                        indexed=True,
                                    ),
                                ),
                            ],
                            properties_with_variables=[
                                None,
                            ],
                        ),
                    ],
                    attachments=[
                        Attachment(
                            id="id_example",
                            type="type_example",
                            file={},
                            content_type="content_type_example",
                            export_filename="export_filename_example",
                            file_uri="file_uri_example",
                            placeholders=[
                                "placeholders_example",
                            ],
                            text_file_names_regex="text_file_names_regex_example",
                            exclude_file_names_regex="exclude_file_names_regex_example",
                            file_encodings={
                                "key": "key_example",
                            },
                            checksum="checksum_example",
                        ),
                    ],
                    status=TaskStatus("PLANNED"),
                    team="team_example",
                    watchers=[
                        "watchers_example",
                    ],
                    wait_for_scheduled_start_date=True,
                    delay_during_blackout=True,
                    postponed_due_to_blackout=True,
                    postponed_until_environments_are_reserved=True,
                    original_scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    has_been_flagged=True,
                    has_been_delayed=True,
                    precondition="precondition_example",
                    failure_handler="failure_handler_example",
                    task_failure_handler_enabled=True,
                    task_recover_op=TaskRecoverOp("SKIP_TASK"),
                    failures_count=1,
                    execution_id="execution_id_example",
                    variable_mapping={
                        "key": "key_example",
                    },
                    external_variable_mapping={
                        "key": "key_example",
                    },
                    max_comment_size=1,
                    tags=[
                        "tags_example",
                    ],
                    configuration_uri="configuration_uri_example",
                    due_soon_notified=True,
                    locked=True,
                    check_attributes=True,
                    abort_script="abort_script_example",
                    phase=Phase(),
                    blackout_metadata=BlackoutMetadata(
                        periods=[
                            BlackoutPeriod(
                                start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            ),
                        ],
                    ),
                    flagged_count=1,
                    delayed_count=1,
                    done=True,
                    done_in_advance=True,
                    defunct=True,
                    updatable=True,
                    aborted=True,
                    not_yet_reached=True,
                    planned=True,
                    active=True,
                    in_progress=True,
                    pending=True,
                    waiting_for_input=True,
                    failed=True,
                    failing=True,
                    completed_in_advance=True,
                    skipped=True,
                    skipped_in_advance=True,
                    precondition_in_progress=True,
                    failure_handler_in_progress=True,
                    abort_script_in_progress=True,
                    facet_in_progress=True,
                    movable=True,
                    gate=True,
                    task_group=True,
                    parallel_group=True,
                    precondition_enabled=True,
                    failure_handler_enabled=True,
                    release=Release(),
                    display_path="display_path_example",
                    release_owner="release_owner_example",
                    all_tasks=[],
                    children=[
                        PlanItem(
                            id="id_example",
                            type="type_example",
                            title="title_example",
                            description="description_example",
                            owner="owner_example",
                            scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            planned_duration=1,
                            flag_status=FlagStatus("OK"),
                            flag_comment="flag_comment_example",
                            overdue_notified=True,
                            flagged=True,
                            start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            children=[],
                            overdue=True,
                            done=True,
                            release=Release(),
                            release_uid=1,
                            updatable=True,
                            display_path="display_path_example",
                            aborted=True,
                            active=True,
                            variable_usages=[
                                UsagePoint(
                                    target_property=CiProperty(
                                        wrapped=CiProperty(),
                                        last_property=ModelProperty(
                                            indexed_property_pattern="indexed_property_pattern_example",
                                            property_name="property_name_example",
                                            index=1,
                                            indexed=True,
                                        ),
                                        parent={},
                                        exists=True,
                                        property_name="property_name_example",
                                        value={},
                                        parent_ci={},
                                        descriptor={},
                                        kind={},
                                        category="category_example",
                                        password=True,
                                        indexed=True,
                                    ),
                                ),
                            ],
                            or_calculate_due_date="or_calculate_due_date_example",
                            computed_planned_duration={},
                            actual_duration={},
                        ),
                    ],
                    variable_usages=[
                        UsagePoint(
                            target_property=CiProperty(
                                wrapped=CiProperty(),
                                last_property=ModelProperty(
                                    indexed_property_pattern="indexed_property_pattern_example",
                                    property_name="property_name_example",
                                    index=1,
                                    indexed=True,
                                ),
                                parent={},
                                exists=True,
                                property_name="property_name_example",
                                value={},
                                parent_ci={},
                                descriptor={},
                                kind={},
                                category="category_example",
                                password=True,
                                indexed=True,
                            ),
                        ),
                    ],
                    input_variables=[
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
                    referenced_variables=[
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
                    unbound_required_variables=[
                        "unbound_required_variables_example",
                    ],
                    automated=True,
                    task_type={},
                    due_soon=True,
                    elapsed_duration_fraction=3.14,
                    url="url_example",
                ),
            ],
            release=None,
            status=PhaseStatus("PLANNED"),
            color="color_example",
            origin_id="origin_id_example",
            current_task=Task(
                id="id_example",
                type="type_example",
                scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                flag_status=FlagStatus("OK"),
                title="title_example",
                description="description_example",
                owner="owner_example",
                due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                planned_duration=1,
                flag_comment="flag_comment_example",
                overdue_notified=True,
                flagged=True,
                start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                overdue=True,
                or_calculate_due_date="or_calculate_due_date_example",
                computed_planned_duration={},
                actual_duration={},
                release_uid=1,
                ci_uid=1,
                comments=[
                    Comment(
                        id="id_example",
                        type="type_example",
                        text="text_example",
                        author="author_example",
                        date=dateutil_parser('2023-03-20T02:07:00Z'),
                        creation_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    ),
                ],
                container=None,
                facets=[
                    Facet(
                        id="id_example",
                        type="type_example",
                        scope=FacetScope("TASK"),
                        target_id="target_id_example",
                        configuration_uri="configuration_uri_example",
                        variable_mapping={
                            "key": "key_example",
                        },
                        variable_usages=[
                            UsagePoint(
                                target_property=CiProperty(
                                    wrapped=CiProperty(),
                                    last_property=ModelProperty(
                                        indexed_property_pattern="indexed_property_pattern_example",
                                        property_name="property_name_example",
                                        index=1,
                                        indexed=True,
                                    ),
                                    parent={},
                                    exists=True,
                                    property_name="property_name_example",
                                    value={},
                                    parent_ci={},
                                    descriptor={},
                                    kind={},
                                    category="category_example",
                                    password=True,
                                    indexed=True,
                                ),
                            ),
                        ],
                        properties_with_variables=[
                            None,
                        ],
                    ),
                ],
                attachments=[
                    Attachment(
                        id="id_example",
                        type="type_example",
                        file={},
                        content_type="content_type_example",
                        export_filename="export_filename_example",
                        file_uri="file_uri_example",
                        placeholders=[
                            "placeholders_example",
                        ],
                        text_file_names_regex="text_file_names_regex_example",
                        exclude_file_names_regex="exclude_file_names_regex_example",
                        file_encodings={
                            "key": "key_example",
                        },
                        checksum="checksum_example",
                    ),
                ],
                status=TaskStatus("PLANNED"),
                team="team_example",
                watchers=[
                    "watchers_example",
                ],
                wait_for_scheduled_start_date=True,
                delay_during_blackout=True,
                postponed_due_to_blackout=True,
                postponed_until_environments_are_reserved=True,
                original_scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                has_been_flagged=True,
                has_been_delayed=True,
                precondition="precondition_example",
                failure_handler="failure_handler_example",
                task_failure_handler_enabled=True,
                task_recover_op=TaskRecoverOp("SKIP_TASK"),
                failures_count=1,
                execution_id="execution_id_example",
                variable_mapping={
                    "key": "key_example",
                },
                external_variable_mapping={
                    "key": "key_example",
                },
                max_comment_size=1,
                tags=[
                    "tags_example",
                ],
                configuration_uri="configuration_uri_example",
                due_soon_notified=True,
                locked=True,
                check_attributes=True,
                abort_script="abort_script_example",
                phase=Phase(),
                blackout_metadata=BlackoutMetadata(
                    periods=[
                        BlackoutPeriod(
                            start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        ),
                    ],
                ),
                flagged_count=1,
                delayed_count=1,
                done=True,
                done_in_advance=True,
                defunct=True,
                updatable=True,
                aborted=True,
                not_yet_reached=True,
                planned=True,
                active=True,
                in_progress=True,
                pending=True,
                waiting_for_input=True,
                failed=True,
                failing=True,
                completed_in_advance=True,
                skipped=True,
                skipped_in_advance=True,
                precondition_in_progress=True,
                failure_handler_in_progress=True,
                abort_script_in_progress=True,
                facet_in_progress=True,
                movable=True,
                gate=True,
                task_group=True,
                parallel_group=True,
                precondition_enabled=True,
                failure_handler_enabled=True,
                release=Release(),
                display_path="display_path_example",
                release_owner="release_owner_example",
                all_tasks=[
                    Task(),
                ],
                children=[
                    PlanItem(
                        id="id_example",
                        type="type_example",
                        title="title_example",
                        description="description_example",
                        owner="owner_example",
                        scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        planned_duration=1,
                        flag_status=FlagStatus("OK"),
                        flag_comment="flag_comment_example",
                        overdue_notified=True,
                        flagged=True,
                        start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        children=[],
                        overdue=True,
                        done=True,
                        release=Release(),
                        release_uid=1,
                        updatable=True,
                        display_path="display_path_example",
                        aborted=True,
                        active=True,
                        variable_usages=[
                            UsagePoint(
                                target_property=CiProperty(
                                    wrapped=CiProperty(),
                                    last_property=ModelProperty(
                                        indexed_property_pattern="indexed_property_pattern_example",
                                        property_name="property_name_example",
                                        index=1,
                                        indexed=True,
                                    ),
                                    parent={},
                                    exists=True,
                                    property_name="property_name_example",
                                    value={},
                                    parent_ci={},
                                    descriptor={},
                                    kind={},
                                    category="category_example",
                                    password=True,
                                    indexed=True,
                                ),
                            ),
                        ],
                        or_calculate_due_date="or_calculate_due_date_example",
                        computed_planned_duration={},
                        actual_duration={},
                    ),
                ],
                variable_usages=[
                    UsagePoint(
                        target_property=CiProperty(
                            wrapped=CiProperty(),
                            last_property=ModelProperty(
                                indexed_property_pattern="indexed_property_pattern_example",
                                property_name="property_name_example",
                                index=1,
                                indexed=True,
                            ),
                            parent={},
                            exists=True,
                            property_name="property_name_example",
                            value={},
                            parent_ci={},
                            descriptor={},
                            kind={},
                            category="category_example",
                            password=True,
                            indexed=True,
                        ),
                    ),
                ],
                input_variables=[
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
                referenced_variables=[
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
                unbound_required_variables=[
                    "unbound_required_variables_example",
                ],
                automated=True,
                task_type={},
                due_soon=True,
                elapsed_duration_fraction=3.14,
                url="url_example",
            ),
            display_path="display_path_example",
            active=True,
            done=True,
            defunct=True,
            updatable=True,
            aborted=True,
            planned=True,
            failed=True,
            failing=True,
            release_owner="release_owner_example",
            all_gates=[
                GateTask(
                    id="id_example",
                    type="type_example",
                    scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    flag_status=FlagStatus("OK"),
                    title="title_example",
                    description="description_example",
                    owner="owner_example",
                    due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    planned_duration=1,
                    flag_comment="flag_comment_example",
                    overdue_notified=True,
                    flagged=True,
                    start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    overdue=True,
                    or_calculate_due_date="or_calculate_due_date_example",
                    computed_planned_duration={},
                    actual_duration={},
                    release_uid=1,
                    ci_uid=1,
                    comments=[
                        Comment(
                            id="id_example",
                            type="type_example",
                            text="text_example",
                            author="author_example",
                            date=dateutil_parser('2023-03-20T02:07:00Z'),
                            creation_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        ),
                    ],
                    container=TaskContainer(
                        id="id_example",
                        type="type_example",
                        tasks=[
                            Task(
                                id="id_example",
                                type="type_example",
                                scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                flag_status=FlagStatus("OK"),
                                title="title_example",
                                description="description_example",
                                owner="owner_example",
                                due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                planned_duration=1,
                                flag_comment="flag_comment_example",
                                overdue_notified=True,
                                flagged=True,
                                start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                overdue=True,
                                or_calculate_due_date="or_calculate_due_date_example",
                                computed_planned_duration={},
                                actual_duration={},
                                release_uid=1,
                                ci_uid=1,
                                comments=[
                                    Comment(
                                        id="id_example",
                                        type="type_example",
                                        text="text_example",
                                        author="author_example",
                                        date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        creation_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    ),
                                ],
                                container=None,
                                facets=[
                                    Facet(
                                        id="id_example",
                                        type="type_example",
                                        scope=FacetScope("TASK"),
                                        target_id="target_id_example",
                                        configuration_uri="configuration_uri_example",
                                        variable_mapping={
                                            "key": "key_example",
                                        },
                                        variable_usages=[
                                            UsagePoint(
                                                target_property=CiProperty(
                                                    wrapped=CiProperty(),
                                                    last_property=ModelProperty(
                                                        indexed_property_pattern="indexed_property_pattern_example",
                                                        property_name="property_name_example",
                                                        index=1,
                                                        indexed=True,
                                                    ),
                                                    parent={},
                                                    exists=True,
                                                    property_name="property_name_example",
                                                    value={},
                                                    parent_ci={},
                                                    descriptor={},
                                                    kind={},
                                                    category="category_example",
                                                    password=True,
                                                    indexed=True,
                                                ),
                                            ),
                                        ],
                                        properties_with_variables=[
                                            None,
                                        ],
                                    ),
                                ],
                                attachments=[
                                    Attachment(
                                        id="id_example",
                                        type="type_example",
                                        file={},
                                        content_type="content_type_example",
                                        export_filename="export_filename_example",
                                        file_uri="file_uri_example",
                                        placeholders=[
                                            "placeholders_example",
                                        ],
                                        text_file_names_regex="text_file_names_regex_example",
                                        exclude_file_names_regex="exclude_file_names_regex_example",
                                        file_encodings={
                                            "key": "key_example",
                                        },
                                        checksum="checksum_example",
                                    ),
                                ],
                                status=TaskStatus("PLANNED"),
                                team="team_example",
                                watchers=[
                                    "watchers_example",
                                ],
                                wait_for_scheduled_start_date=True,
                                delay_during_blackout=True,
                                postponed_due_to_blackout=True,
                                postponed_until_environments_are_reserved=True,
                                original_scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                has_been_flagged=True,
                                has_been_delayed=True,
                                precondition="precondition_example",
                                failure_handler="failure_handler_example",
                                task_failure_handler_enabled=True,
                                task_recover_op=TaskRecoverOp("SKIP_TASK"),
                                failures_count=1,
                                execution_id="execution_id_example",
                                variable_mapping={
                                    "key": "key_example",
                                },
                                external_variable_mapping={
                                    "key": "key_example",
                                },
                                max_comment_size=1,
                                tags=[
                                    "tags_example",
                                ],
                                configuration_uri="configuration_uri_example",
                                due_soon_notified=True,
                                locked=True,
                                check_attributes=True,
                                abort_script="abort_script_example",
                                phase=Phase(),
                                blackout_metadata=BlackoutMetadata(
                                    periods=[
                                        BlackoutPeriod(
                                            start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                            end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        ),
                                    ],
                                ),
                                flagged_count=1,
                                delayed_count=1,
                                done=True,
                                done_in_advance=True,
                                defunct=True,
                                updatable=True,
                                aborted=True,
                                not_yet_reached=True,
                                planned=True,
                                active=True,
                                in_progress=True,
                                pending=True,
                                waiting_for_input=True,
                                failed=True,
                                failing=True,
                                completed_in_advance=True,
                                skipped=True,
                                skipped_in_advance=True,
                                precondition_in_progress=True,
                                failure_handler_in_progress=True,
                                abort_script_in_progress=True,
                                facet_in_progress=True,
                                movable=True,
                                gate=True,
                                task_group=True,
                                parallel_group=True,
                                precondition_enabled=True,
                                failure_handler_enabled=True,
                                release=Release(),
                                display_path="display_path_example",
                                release_owner="release_owner_example",
                                all_tasks=[],
                                children=[
                                    PlanItem(
                                        id="id_example",
                                        type="type_example",
                                        title="title_example",
                                        description="description_example",
                                        owner="owner_example",
                                        scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        planned_duration=1,
                                        flag_status=FlagStatus("OK"),
                                        flag_comment="flag_comment_example",
                                        overdue_notified=True,
                                        flagged=True,
                                        start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        children=[],
                                        overdue=True,
                                        done=True,
                                        release=Release(),
                                        release_uid=1,
                                        updatable=True,
                                        display_path="display_path_example",
                                        aborted=True,
                                        active=True,
                                        variable_usages=[
                                            UsagePoint(
                                                target_property=CiProperty(
                                                    wrapped=CiProperty(),
                                                    last_property=ModelProperty(
                                                        indexed_property_pattern="indexed_property_pattern_example",
                                                        property_name="property_name_example",
                                                        index=1,
                                                        indexed=True,
                                                    ),
                                                    parent={},
                                                    exists=True,
                                                    property_name="property_name_example",
                                                    value={},
                                                    parent_ci={},
                                                    descriptor={},
                                                    kind={},
                                                    category="category_example",
                                                    password=True,
                                                    indexed=True,
                                                ),
                                            ),
                                        ],
                                        or_calculate_due_date="or_calculate_due_date_example",
                                        computed_planned_duration={},
                                        actual_duration={},
                                    ),
                                ],
                                variable_usages=[
                                    UsagePoint(
                                        target_property=CiProperty(
                                            wrapped=CiProperty(),
                                            last_property=ModelProperty(
                                                indexed_property_pattern="indexed_property_pattern_example",
                                                property_name="property_name_example",
                                                index=1,
                                                indexed=True,
                                            ),
                                            parent={},
                                            exists=True,
                                            property_name="property_name_example",
                                            value={},
                                            parent_ci={},
                                            descriptor={},
                                            kind={},
                                            category="category_example",
                                            password=True,
                                            indexed=True,
                                        ),
                                    ),
                                ],
                                input_variables=[
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
                                referenced_variables=[
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
                                unbound_required_variables=[
                                    "unbound_required_variables_example",
                                ],
                                automated=True,
                                task_type={},
                                due_soon=True,
                                elapsed_duration_fraction=3.14,
                                url="url_example",
                            ),
                        ],
                        locked=True,
                        title="title_example",
                    ),
                    facets=[
                        Facet(
                            id="id_example",
                            type="type_example",
                            scope=FacetScope("TASK"),
                            target_id="target_id_example",
                            configuration_uri="configuration_uri_example",
                            variable_mapping={
                                "key": "key_example",
                            },
                            variable_usages=[
                                UsagePoint(
                                    target_property=CiProperty(
                                        wrapped=CiProperty(),
                                        last_property=ModelProperty(
                                            indexed_property_pattern="indexed_property_pattern_example",
                                            property_name="property_name_example",
                                            index=1,
                                            indexed=True,
                                        ),
                                        parent={},
                                        exists=True,
                                        property_name="property_name_example",
                                        value={},
                                        parent_ci={},
                                        descriptor={},
                                        kind={},
                                        category="category_example",
                                        password=True,
                                        indexed=True,
                                    ),
                                ),
                            ],
                            properties_with_variables=[
                                None,
                            ],
                        ),
                    ],
                    attachments=[
                        Attachment(
                            id="id_example",
                            type="type_example",
                            file={},
                            content_type="content_type_example",
                            export_filename="export_filename_example",
                            file_uri="file_uri_example",
                            placeholders=[
                                "placeholders_example",
                            ],
                            text_file_names_regex="text_file_names_regex_example",
                            exclude_file_names_regex="exclude_file_names_regex_example",
                            file_encodings={
                                "key": "key_example",
                            },
                            checksum="checksum_example",
                        ),
                    ],
                    status=TaskStatus("PLANNED"),
                    team="team_example",
                    watchers=[
                        "watchers_example",
                    ],
                    wait_for_scheduled_start_date=True,
                    delay_during_blackout=True,
                    postponed_due_to_blackout=True,
                    postponed_until_environments_are_reserved=True,
                    original_scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    has_been_flagged=True,
                    has_been_delayed=True,
                    precondition="precondition_example",
                    failure_handler="failure_handler_example",
                    task_failure_handler_enabled=True,
                    task_recover_op=TaskRecoverOp("SKIP_TASK"),
                    failures_count=1,
                    execution_id="execution_id_example",
                    variable_mapping={
                        "key": "key_example",
                    },
                    external_variable_mapping={
                        "key": "key_example",
                    },
                    max_comment_size=1,
                    tags=[
                        "tags_example",
                    ],
                    configuration_uri="configuration_uri_example",
                    due_soon_notified=True,
                    locked=True,
                    check_attributes=True,
                    abort_script="abort_script_example",
                    phase=Phase(),
                    blackout_metadata=BlackoutMetadata(
                        periods=[
                            BlackoutPeriod(
                                start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            ),
                        ],
                    ),
                    flagged_count=1,
                    delayed_count=1,
                    done=True,
                    done_in_advance=True,
                    defunct=True,
                    updatable=True,
                    aborted=True,
                    not_yet_reached=True,
                    planned=True,
                    active=True,
                    in_progress=True,
                    pending=True,
                    waiting_for_input=True,
                    failed=True,
                    failing=True,
                    completed_in_advance=True,
                    skipped=True,
                    skipped_in_advance=True,
                    precondition_in_progress=True,
                    failure_handler_in_progress=True,
                    abort_script_in_progress=True,
                    facet_in_progress=True,
                    movable=True,
                    gate=True,
                    task_group=True,
                    parallel_group=True,
                    precondition_enabled=True,
                    failure_handler_enabled=True,
                    release=Release(),
                    display_path="display_path_example",
                    release_owner="release_owner_example",
                    all_tasks=[
                        Task(
                            id="id_example",
                            type="type_example",
                            scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            flag_status=FlagStatus("OK"),
                            title="title_example",
                            description="description_example",
                            owner="owner_example",
                            due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            planned_duration=1,
                            flag_comment="flag_comment_example",
                            overdue_notified=True,
                            flagged=True,
                            start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            overdue=True,
                            or_calculate_due_date="or_calculate_due_date_example",
                            computed_planned_duration={},
                            actual_duration={},
                            release_uid=1,
                            ci_uid=1,
                            comments=[
                                Comment(
                                    id="id_example",
                                    type="type_example",
                                    text="text_example",
                                    author="author_example",
                                    date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    creation_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                ),
                            ],
                            container=None,
                            facets=[
                                Facet(
                                    id="id_example",
                                    type="type_example",
                                    scope=FacetScope("TASK"),
                                    target_id="target_id_example",
                                    configuration_uri="configuration_uri_example",
                                    variable_mapping={
                                        "key": "key_example",
                                    },
                                    variable_usages=[
                                        UsagePoint(
                                            target_property=CiProperty(
                                                wrapped=CiProperty(),
                                                last_property=ModelProperty(
                                                    indexed_property_pattern="indexed_property_pattern_example",
                                                    property_name="property_name_example",
                                                    index=1,
                                                    indexed=True,
                                                ),
                                                parent={},
                                                exists=True,
                                                property_name="property_name_example",
                                                value={},
                                                parent_ci={},
                                                descriptor={},
                                                kind={},
                                                category="category_example",
                                                password=True,
                                                indexed=True,
                                            ),
                                        ),
                                    ],
                                    properties_with_variables=[
                                        None,
                                    ],
                                ),
                            ],
                            attachments=[
                                Attachment(
                                    id="id_example",
                                    type="type_example",
                                    file={},
                                    content_type="content_type_example",
                                    export_filename="export_filename_example",
                                    file_uri="file_uri_example",
                                    placeholders=[
                                        "placeholders_example",
                                    ],
                                    text_file_names_regex="text_file_names_regex_example",
                                    exclude_file_names_regex="exclude_file_names_regex_example",
                                    file_encodings={
                                        "key": "key_example",
                                    },
                                    checksum="checksum_example",
                                ),
                            ],
                            status=TaskStatus("PLANNED"),
                            team="team_example",
                            watchers=[
                                "watchers_example",
                            ],
                            wait_for_scheduled_start_date=True,
                            delay_during_blackout=True,
                            postponed_due_to_blackout=True,
                            postponed_until_environments_are_reserved=True,
                            original_scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            has_been_flagged=True,
                            has_been_delayed=True,
                            precondition="precondition_example",
                            failure_handler="failure_handler_example",
                            task_failure_handler_enabled=True,
                            task_recover_op=TaskRecoverOp("SKIP_TASK"),
                            failures_count=1,
                            execution_id="execution_id_example",
                            variable_mapping={
                                "key": "key_example",
                            },
                            external_variable_mapping={
                                "key": "key_example",
                            },
                            max_comment_size=1,
                            tags=[
                                "tags_example",
                            ],
                            configuration_uri="configuration_uri_example",
                            due_soon_notified=True,
                            locked=True,
                            check_attributes=True,
                            abort_script="abort_script_example",
                            phase=Phase(),
                            blackout_metadata=BlackoutMetadata(
                                periods=[
                                    BlackoutPeriod(
                                        start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    ),
                                ],
                            ),
                            flagged_count=1,
                            delayed_count=1,
                            done=True,
                            done_in_advance=True,
                            defunct=True,
                            updatable=True,
                            aborted=True,
                            not_yet_reached=True,
                            planned=True,
                            active=True,
                            in_progress=True,
                            pending=True,
                            waiting_for_input=True,
                            failed=True,
                            failing=True,
                            completed_in_advance=True,
                            skipped=True,
                            skipped_in_advance=True,
                            precondition_in_progress=True,
                            failure_handler_in_progress=True,
                            abort_script_in_progress=True,
                            facet_in_progress=True,
                            movable=True,
                            gate=True,
                            task_group=True,
                            parallel_group=True,
                            precondition_enabled=True,
                            failure_handler_enabled=True,
                            release=Release(),
                            display_path="display_path_example",
                            release_owner="release_owner_example",
                            all_tasks=[],
                            children=[
                                PlanItem(
                                    id="id_example",
                                    type="type_example",
                                    title="title_example",
                                    description="description_example",
                                    owner="owner_example",
                                    scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    planned_duration=1,
                                    flag_status=FlagStatus("OK"),
                                    flag_comment="flag_comment_example",
                                    overdue_notified=True,
                                    flagged=True,
                                    start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    children=[],
                                    overdue=True,
                                    done=True,
                                    release=Release(),
                                    release_uid=1,
                                    updatable=True,
                                    display_path="display_path_example",
                                    aborted=True,
                                    active=True,
                                    variable_usages=[
                                        UsagePoint(
                                            target_property=CiProperty(
                                                wrapped=CiProperty(),
                                                last_property=ModelProperty(
                                                    indexed_property_pattern="indexed_property_pattern_example",
                                                    property_name="property_name_example",
                                                    index=1,
                                                    indexed=True,
                                                ),
                                                parent={},
                                                exists=True,
                                                property_name="property_name_example",
                                                value={},
                                                parent_ci={},
                                                descriptor={},
                                                kind={},
                                                category="category_example",
                                                password=True,
                                                indexed=True,
                                            ),
                                        ),
                                    ],
                                    or_calculate_due_date="or_calculate_due_date_example",
                                    computed_planned_duration={},
                                    actual_duration={},
                                ),
                            ],
                            variable_usages=[
                                UsagePoint(
                                    target_property=CiProperty(
                                        wrapped=CiProperty(),
                                        last_property=ModelProperty(
                                            indexed_property_pattern="indexed_property_pattern_example",
                                            property_name="property_name_example",
                                            index=1,
                                            indexed=True,
                                        ),
                                        parent={},
                                        exists=True,
                                        property_name="property_name_example",
                                        value={},
                                        parent_ci={},
                                        descriptor={},
                                        kind={},
                                        category="category_example",
                                        password=True,
                                        indexed=True,
                                    ),
                                ),
                            ],
                            input_variables=[
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
                            referenced_variables=[
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
                            unbound_required_variables=[
                                "unbound_required_variables_example",
                            ],
                            automated=True,
                            task_type={},
                            due_soon=True,
                            elapsed_duration_fraction=3.14,
                            url="url_example",
                        ),
                    ],
                    children=[
                        PlanItem(
                            id="id_example",
                            type="type_example",
                            title="title_example",
                            description="description_example",
                            owner="owner_example",
                            scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            planned_duration=1,
                            flag_status=FlagStatus("OK"),
                            flag_comment="flag_comment_example",
                            overdue_notified=True,
                            flagged=True,
                            start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            children=[],
                            overdue=True,
                            done=True,
                            release=Release(),
                            release_uid=1,
                            updatable=True,
                            display_path="display_path_example",
                            aborted=True,
                            active=True,
                            variable_usages=[
                                UsagePoint(
                                    target_property=CiProperty(
                                        wrapped=CiProperty(),
                                        last_property=ModelProperty(
                                            indexed_property_pattern="indexed_property_pattern_example",
                                            property_name="property_name_example",
                                            index=1,
                                            indexed=True,
                                        ),
                                        parent={},
                                        exists=True,
                                        property_name="property_name_example",
                                        value={},
                                        parent_ci={},
                                        descriptor={},
                                        kind={},
                                        category="category_example",
                                        password=True,
                                        indexed=True,
                                    ),
                                ),
                            ],
                            or_calculate_due_date="or_calculate_due_date_example",
                            computed_planned_duration={},
                            actual_duration={},
                        ),
                    ],
                    input_variables=[
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
                    referenced_variables=[
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
                    unbound_required_variables=[
                        "unbound_required_variables_example",
                    ],
                    automated=True,
                    task_type={},
                    due_soon=True,
                    elapsed_duration_fraction=3.14,
                    url="url_example",
                    conditions=[
                        GateCondition(
                            id="id_example",
                            type="type_example",
                            title="title_example",
                            checked=True,
                        ),
                    ],
                    dependencies=[
                        Dependency(
                            id="id_example",
                            type="type_example",
                            gate_task=GateTask(),
                            target=PlanItem(
                                id="id_example",
                                type="type_example",
                                title="title_example",
                                description="description_example",
                                owner="owner_example",
                                scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                planned_duration=1,
                                flag_status=FlagStatus("OK"),
                                flag_comment="flag_comment_example",
                                overdue_notified=True,
                                flagged=True,
                                start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                children=[
                                    PlanItem(),
                                ],
                                overdue=True,
                                done=True,
                                release=Release(),
                                release_uid=1,
                                updatable=True,
                                display_path="display_path_example",
                                aborted=True,
                                active=True,
                                variable_usages=[
                                    UsagePoint(
                                        target_property=CiProperty(
                                            wrapped=CiProperty(),
                                            last_property=ModelProperty(
                                                indexed_property_pattern="indexed_property_pattern_example",
                                                property_name="property_name_example",
                                                index=1,
                                                indexed=True,
                                            ),
                                            parent={},
                                            exists=True,
                                            property_name="property_name_example",
                                            value={},
                                            parent_ci={},
                                            descriptor={},
                                            kind={},
                                            category="category_example",
                                            password=True,
                                            indexed=True,
                                        ),
                                    ),
                                ],
                                or_calculate_due_date="or_calculate_due_date_example",
                                computed_planned_duration={},
                                actual_duration={},
                            ),
                            target_id="target_id_example",
                            archived_target_title="archived_target_title_example",
                            archived_target_id="archived_target_id_example",
                            archived_as_resolved=True,
                            metadata={
                                "key": {},
                            },
                            archived=True,
                            done=True,
                            aborted=True,
                            target_display_path="target_display_path_example",
                            target_title="target_title_example",
                            valid_allowed_plan_item_id=True,
                        ),
                    ],
                    open=True,
                    open_in_advance=True,
                    completable=True,
                    aborted_dependency_titles="aborted_dependency_titles_example",
                    variable_usages=[
                        UsagePoint(
                            target_property=CiProperty(
                                wrapped=CiProperty(),
                                last_property=ModelProperty(
                                    indexed_property_pattern="indexed_property_pattern_example",
                                    property_name="property_name_example",
                                    index=1,
                                    indexed=True,
                                ),
                                parent={},
                                exists=True,
                                property_name="property_name_example",
                                value={},
                                parent_ci={},
                                descriptor={},
                                kind={},
                                category="category_example",
                                password=True,
                                indexed=True,
                            ),
                        ),
                    ],
                ),
            ],
            all_tasks=[
                Task(
                    id="id_example",
                    type="type_example",
                    scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    flag_status=FlagStatus("OK"),
                    title="title_example",
                    description="description_example",
                    owner="owner_example",
                    due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    planned_duration=1,
                    flag_comment="flag_comment_example",
                    overdue_notified=True,
                    flagged=True,
                    start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    overdue=True,
                    or_calculate_due_date="or_calculate_due_date_example",
                    computed_planned_duration={},
                    actual_duration={},
                    release_uid=1,
                    ci_uid=1,
                    comments=[
                        Comment(
                            id="id_example",
                            type="type_example",
                            text="text_example",
                            author="author_example",
                            date=dateutil_parser('2023-03-20T02:07:00Z'),
                            creation_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        ),
                    ],
                    container=None,
                    facets=[
                        Facet(
                            id="id_example",
                            type="type_example",
                            scope=FacetScope("TASK"),
                            target_id="target_id_example",
                            configuration_uri="configuration_uri_example",
                            variable_mapping={
                                "key": "key_example",
                            },
                            variable_usages=[
                                UsagePoint(
                                    target_property=CiProperty(
                                        wrapped=CiProperty(),
                                        last_property=ModelProperty(
                                            indexed_property_pattern="indexed_property_pattern_example",
                                            property_name="property_name_example",
                                            index=1,
                                            indexed=True,
                                        ),
                                        parent={},
                                        exists=True,
                                        property_name="property_name_example",
                                        value={},
                                        parent_ci={},
                                        descriptor={},
                                        kind={},
                                        category="category_example",
                                        password=True,
                                        indexed=True,
                                    ),
                                ),
                            ],
                            properties_with_variables=[
                                None,
                            ],
                        ),
                    ],
                    attachments=[
                        Attachment(
                            id="id_example",
                            type="type_example",
                            file={},
                            content_type="content_type_example",
                            export_filename="export_filename_example",
                            file_uri="file_uri_example",
                            placeholders=[
                                "placeholders_example",
                            ],
                            text_file_names_regex="text_file_names_regex_example",
                            exclude_file_names_regex="exclude_file_names_regex_example",
                            file_encodings={
                                "key": "key_example",
                            },
                            checksum="checksum_example",
                        ),
                    ],
                    status=TaskStatus("PLANNED"),
                    team="team_example",
                    watchers=[
                        "watchers_example",
                    ],
                    wait_for_scheduled_start_date=True,
                    delay_during_blackout=True,
                    postponed_due_to_blackout=True,
                    postponed_until_environments_are_reserved=True,
                    original_scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    has_been_flagged=True,
                    has_been_delayed=True,
                    precondition="precondition_example",
                    failure_handler="failure_handler_example",
                    task_failure_handler_enabled=True,
                    task_recover_op=TaskRecoverOp("SKIP_TASK"),
                    failures_count=1,
                    execution_id="execution_id_example",
                    variable_mapping={
                        "key": "key_example",
                    },
                    external_variable_mapping={
                        "key": "key_example",
                    },
                    max_comment_size=1,
                    tags=[
                        "tags_example",
                    ],
                    configuration_uri="configuration_uri_example",
                    due_soon_notified=True,
                    locked=True,
                    check_attributes=True,
                    abort_script="abort_script_example",
                    phase=Phase(),
                    blackout_metadata=BlackoutMetadata(
                        periods=[
                            BlackoutPeriod(
                                start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            ),
                        ],
                    ),
                    flagged_count=1,
                    delayed_count=1,
                    done=True,
                    done_in_advance=True,
                    defunct=True,
                    updatable=True,
                    aborted=True,
                    not_yet_reached=True,
                    planned=True,
                    active=True,
                    in_progress=True,
                    pending=True,
                    waiting_for_input=True,
                    failed=True,
                    failing=True,
                    completed_in_advance=True,
                    skipped=True,
                    skipped_in_advance=True,
                    precondition_in_progress=True,
                    failure_handler_in_progress=True,
                    abort_script_in_progress=True,
                    facet_in_progress=True,
                    movable=True,
                    gate=True,
                    task_group=True,
                    parallel_group=True,
                    precondition_enabled=True,
                    failure_handler_enabled=True,
                    release=Release(),
                    display_path="display_path_example",
                    release_owner="release_owner_example",
                    all_tasks=[],
                    children=[
                        PlanItem(
                            id="id_example",
                            type="type_example",
                            title="title_example",
                            description="description_example",
                            owner="owner_example",
                            scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            planned_duration=1,
                            flag_status=FlagStatus("OK"),
                            flag_comment="flag_comment_example",
                            overdue_notified=True,
                            flagged=True,
                            start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            children=[],
                            overdue=True,
                            done=True,
                            release=Release(),
                            release_uid=1,
                            updatable=True,
                            display_path="display_path_example",
                            aborted=True,
                            active=True,
                            variable_usages=[
                                UsagePoint(
                                    target_property=CiProperty(
                                        wrapped=CiProperty(),
                                        last_property=ModelProperty(
                                            indexed_property_pattern="indexed_property_pattern_example",
                                            property_name="property_name_example",
                                            index=1,
                                            indexed=True,
                                        ),
                                        parent={},
                                        exists=True,
                                        property_name="property_name_example",
                                        value={},
                                        parent_ci={},
                                        descriptor={},
                                        kind={},
                                        category="category_example",
                                        password=True,
                                        indexed=True,
                                    ),
                                ),
                            ],
                            or_calculate_due_date="or_calculate_due_date_example",
                            computed_planned_duration={},
                            actual_duration={},
                        ),
                    ],
                    variable_usages=[
                        UsagePoint(
                            target_property=CiProperty(
                                wrapped=CiProperty(),
                                last_property=ModelProperty(
                                    indexed_property_pattern="indexed_property_pattern_example",
                                    property_name="property_name_example",
                                    index=1,
                                    indexed=True,
                                ),
                                parent={},
                                exists=True,
                                property_name="property_name_example",
                                value={},
                                parent_ci={},
                                descriptor={},
                                kind={},
                                category="category_example",
                                password=True,
                                indexed=True,
                            ),
                        ),
                    ],
                    input_variables=[
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
                    referenced_variables=[
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
                    unbound_required_variables=[
                        "unbound_required_variables_example",
                    ],
                    automated=True,
                    task_type={},
                    due_soon=True,
                    elapsed_duration_fraction=3.14,
                    url="url_example",
                ),
            ],
            children=[
                PlanItem(
                    id="id_example",
                    type="type_example",
                    title="title_example",
                    description="description_example",
                    owner="owner_example",
                    scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    planned_duration=1,
                    flag_status=FlagStatus("OK"),
                    flag_comment="flag_comment_example",
                    overdue_notified=True,
                    flagged=True,
                    start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    children=[],
                    overdue=True,
                    done=True,
                    release=Release(),
                    release_uid=1,
                    updatable=True,
                    display_path="display_path_example",
                    aborted=True,
                    active=True,
                    variable_usages=[
                        UsagePoint(
                            target_property=CiProperty(
                                wrapped=CiProperty(),
                                last_property=ModelProperty(
                                    indexed_property_pattern="indexed_property_pattern_example",
                                    property_name="property_name_example",
                                    index=1,
                                    indexed=True,
                                ),
                                parent={},
                                exists=True,
                                property_name="property_name_example",
                                value={},
                                parent_ci={},
                                descriptor={},
                                kind={},
                                category="category_example",
                                password=True,
                                indexed=True,
                            ),
                        ),
                    ],
                    or_calculate_due_date="or_calculate_due_date_example",
                    computed_planned_duration={},
                    actual_duration={},
                ),
            ],
            variable_usages=[
                UsagePoint(
                    target_property=CiProperty(
                        wrapped=CiProperty(),
                        last_property=ModelProperty(
                            indexed_property_pattern="indexed_property_pattern_example",
                            property_name="property_name_example",
                            index=1,
                            indexed=True,
                        ),
                        parent={},
                        exists=True,
                        property_name="property_name_example",
                        value={},
                        parent_ci={},
                        descriptor={},
                        kind={},
                        category="category_example",
                        password=True,
                        indexed=True,
                    ),
                ),
            ],
            original=True,
            phase_copied=True,
            ancestor_id="ancestor_id_example",
            latest_copy=True,
        ),
        current_task=Task(
            id="id_example",
            type="type_example",
            scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
            flag_status=FlagStatus("OK"),
            title="title_example",
            description="description_example",
            owner="owner_example",
            due_date=dateutil_parser('2023-03-20T02:07:00Z'),
            start_date=dateutil_parser('2023-03-20T02:07:00Z'),
            end_date=dateutil_parser('2023-03-20T02:07:00Z'),
            planned_duration=1,
            flag_comment="flag_comment_example",
            overdue_notified=True,
            flagged=True,
            start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
            end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
            overdue=True,
            or_calculate_due_date="or_calculate_due_date_example",
            computed_planned_duration={},
            actual_duration={},
            release_uid=1,
            ci_uid=1,
            comments=[
                Comment(
                    id="id_example",
                    type="type_example",
                    text="text_example",
                    author="author_example",
                    date=dateutil_parser('2023-03-20T02:07:00Z'),
                    creation_date=dateutil_parser('2023-03-20T02:07:00Z'),
                ),
            ],
            container=None,
            facets=[
                Facet(
                    id="id_example",
                    type="type_example",
                    scope=FacetScope("TASK"),
                    target_id="target_id_example",
                    configuration_uri="configuration_uri_example",
                    variable_mapping={
                        "key": "key_example",
                    },
                    variable_usages=[
                        UsagePoint(
                            target_property=CiProperty(
                                wrapped=CiProperty(),
                                last_property=ModelProperty(
                                    indexed_property_pattern="indexed_property_pattern_example",
                                    property_name="property_name_example",
                                    index=1,
                                    indexed=True,
                                ),
                                parent={},
                                exists=True,
                                property_name="property_name_example",
                                value={},
                                parent_ci={},
                                descriptor={},
                                kind={},
                                category="category_example",
                                password=True,
                                indexed=True,
                            ),
                        ),
                    ],
                    properties_with_variables=[
                        None,
                    ],
                ),
            ],
            attachments=[
                Attachment(
                    id="id_example",
                    type="type_example",
                    file={},
                    content_type="content_type_example",
                    export_filename="export_filename_example",
                    file_uri="file_uri_example",
                    placeholders=[
                        "placeholders_example",
                    ],
                    text_file_names_regex="text_file_names_regex_example",
                    exclude_file_names_regex="exclude_file_names_regex_example",
                    file_encodings={
                        "key": "key_example",
                    },
                    checksum="checksum_example",
                ),
            ],
            status=TaskStatus("PLANNED"),
            team="team_example",
            watchers=[
                "watchers_example",
            ],
            wait_for_scheduled_start_date=True,
            delay_during_blackout=True,
            postponed_due_to_blackout=True,
            postponed_until_environments_are_reserved=True,
            original_scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
            has_been_flagged=True,
            has_been_delayed=True,
            precondition="precondition_example",
            failure_handler="failure_handler_example",
            task_failure_handler_enabled=True,
            task_recover_op=TaskRecoverOp("SKIP_TASK"),
            failures_count=1,
            execution_id="execution_id_example",
            variable_mapping={
                "key": "key_example",
            },
            external_variable_mapping={
                "key": "key_example",
            },
            max_comment_size=1,
            tags=[
                "tags_example",
            ],
            configuration_uri="configuration_uri_example",
            due_soon_notified=True,
            locked=True,
            check_attributes=True,
            abort_script="abort_script_example",
            phase=Phase(
                id="id_example",
                type="type_example",
                locked=True,
                title="title_example",
                description="description_example",
                owner="owner_example",
                scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                planned_duration=1,
                flag_status=FlagStatus("OK"),
                flag_comment="flag_comment_example",
                overdue_notified=True,
                flagged=True,
                start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                overdue=True,
                or_calculate_due_date="or_calculate_due_date_example",
                computed_planned_duration={},
                actual_duration={},
                release_uid=1,
                tasks=[
                    Task(),
                ],
                release=None,
                status=PhaseStatus("PLANNED"),
                color="color_example",
                origin_id="origin_id_example",
                current_task=Task(),
                display_path="display_path_example",
                active=True,
                done=True,
                defunct=True,
                updatable=True,
                aborted=True,
                planned=True,
                failed=True,
                failing=True,
                release_owner="release_owner_example",
                all_gates=[
                    GateTask(
                        id="id_example",
                        type="type_example",
                        scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        flag_status=FlagStatus("OK"),
                        title="title_example",
                        description="description_example",
                        owner="owner_example",
                        due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        planned_duration=1,
                        flag_comment="flag_comment_example",
                        overdue_notified=True,
                        flagged=True,
                        start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        overdue=True,
                        or_calculate_due_date="or_calculate_due_date_example",
                        computed_planned_duration={},
                        actual_duration={},
                        release_uid=1,
                        ci_uid=1,
                        comments=[
                            Comment(
                                id="id_example",
                                type="type_example",
                                text="text_example",
                                author="author_example",
                                date=dateutil_parser('2023-03-20T02:07:00Z'),
                                creation_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            ),
                        ],
                        container=TaskContainer(
                            id="id_example",
                            type="type_example",
                            tasks=[
                                Task(),
                            ],
                            locked=True,
                            title="title_example",
                        ),
                        facets=[
                            Facet(
                                id="id_example",
                                type="type_example",
                                scope=FacetScope("TASK"),
                                target_id="target_id_example",
                                configuration_uri="configuration_uri_example",
                                variable_mapping={
                                    "key": "key_example",
                                },
                                variable_usages=[
                                    UsagePoint(
                                        target_property=CiProperty(
                                            wrapped=CiProperty(),
                                            last_property=ModelProperty(
                                                indexed_property_pattern="indexed_property_pattern_example",
                                                property_name="property_name_example",
                                                index=1,
                                                indexed=True,
                                            ),
                                            parent={},
                                            exists=True,
                                            property_name="property_name_example",
                                            value={},
                                            parent_ci={},
                                            descriptor={},
                                            kind={},
                                            category="category_example",
                                            password=True,
                                            indexed=True,
                                        ),
                                    ),
                                ],
                                properties_with_variables=[
                                    None,
                                ],
                            ),
                        ],
                        attachments=[
                            Attachment(
                                id="id_example",
                                type="type_example",
                                file={},
                                content_type="content_type_example",
                                export_filename="export_filename_example",
                                file_uri="file_uri_example",
                                placeholders=[
                                    "placeholders_example",
                                ],
                                text_file_names_regex="text_file_names_regex_example",
                                exclude_file_names_regex="exclude_file_names_regex_example",
                                file_encodings={
                                    "key": "key_example",
                                },
                                checksum="checksum_example",
                            ),
                        ],
                        status=TaskStatus("PLANNED"),
                        team="team_example",
                        watchers=[
                            "watchers_example",
                        ],
                        wait_for_scheduled_start_date=True,
                        delay_during_blackout=True,
                        postponed_due_to_blackout=True,
                        postponed_until_environments_are_reserved=True,
                        original_scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        has_been_flagged=True,
                        has_been_delayed=True,
                        precondition="precondition_example",
                        failure_handler="failure_handler_example",
                        task_failure_handler_enabled=True,
                        task_recover_op=TaskRecoverOp("SKIP_TASK"),
                        failures_count=1,
                        execution_id="execution_id_example",
                        variable_mapping={
                            "key": "key_example",
                        },
                        external_variable_mapping={
                            "key": "key_example",
                        },
                        max_comment_size=1,
                        tags=[
                            "tags_example",
                        ],
                        configuration_uri="configuration_uri_example",
                        due_soon_notified=True,
                        locked=True,
                        check_attributes=True,
                        abort_script="abort_script_example",
                        phase=Phase(),
                        blackout_metadata=BlackoutMetadata(
                            periods=[
                                BlackoutPeriod(
                                    start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                ),
                            ],
                        ),
                        flagged_count=1,
                        delayed_count=1,
                        done=True,
                        done_in_advance=True,
                        defunct=True,
                        updatable=True,
                        aborted=True,
                        not_yet_reached=True,
                        planned=True,
                        active=True,
                        in_progress=True,
                        pending=True,
                        waiting_for_input=True,
                        failed=True,
                        failing=True,
                        completed_in_advance=True,
                        skipped=True,
                        skipped_in_advance=True,
                        precondition_in_progress=True,
                        failure_handler_in_progress=True,
                        abort_script_in_progress=True,
                        facet_in_progress=True,
                        movable=True,
                        gate=True,
                        task_group=True,
                        parallel_group=True,
                        precondition_enabled=True,
                        failure_handler_enabled=True,
                        release=Release(),
                        display_path="display_path_example",
                        release_owner="release_owner_example",
                        all_tasks=[
                            Task(),
                        ],
                        children=[
                            PlanItem(
                                id="id_example",
                                type="type_example",
                                title="title_example",
                                description="description_example",
                                owner="owner_example",
                                scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                planned_duration=1,
                                flag_status=FlagStatus("OK"),
                                flag_comment="flag_comment_example",
                                overdue_notified=True,
                                flagged=True,
                                start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                children=[],
                                overdue=True,
                                done=True,
                                release=Release(),
                                release_uid=1,
                                updatable=True,
                                display_path="display_path_example",
                                aborted=True,
                                active=True,
                                variable_usages=[
                                    UsagePoint(
                                        target_property=CiProperty(
                                            wrapped=CiProperty(),
                                            last_property=ModelProperty(
                                                indexed_property_pattern="indexed_property_pattern_example",
                                                property_name="property_name_example",
                                                index=1,
                                                indexed=True,
                                            ),
                                            parent={},
                                            exists=True,
                                            property_name="property_name_example",
                                            value={},
                                            parent_ci={},
                                            descriptor={},
                                            kind={},
                                            category="category_example",
                                            password=True,
                                            indexed=True,
                                        ),
                                    ),
                                ],
                                or_calculate_due_date="or_calculate_due_date_example",
                                computed_planned_duration={},
                                actual_duration={},
                            ),
                        ],
                        input_variables=[
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
                        referenced_variables=[
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
                        unbound_required_variables=[
                            "unbound_required_variables_example",
                        ],
                        automated=True,
                        task_type={},
                        due_soon=True,
                        elapsed_duration_fraction=3.14,
                        url="url_example",
                        conditions=[
                            GateCondition(
                                id="id_example",
                                type="type_example",
                                title="title_example",
                                checked=True,
                            ),
                        ],
                        dependencies=[
                            Dependency(
                                id="id_example",
                                type="type_example",
                                gate_task=GateTask(),
                                target=PlanItem(
                                    id="id_example",
                                    type="type_example",
                                    title="title_example",
                                    description="description_example",
                                    owner="owner_example",
                                    scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    planned_duration=1,
                                    flag_status=FlagStatus("OK"),
                                    flag_comment="flag_comment_example",
                                    overdue_notified=True,
                                    flagged=True,
                                    start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    children=[
                                        PlanItem(),
                                    ],
                                    overdue=True,
                                    done=True,
                                    release=Release(),
                                    release_uid=1,
                                    updatable=True,
                                    display_path="display_path_example",
                                    aborted=True,
                                    active=True,
                                    variable_usages=[
                                        UsagePoint(
                                            target_property=CiProperty(
                                                wrapped=CiProperty(),
                                                last_property=ModelProperty(
                                                    indexed_property_pattern="indexed_property_pattern_example",
                                                    property_name="property_name_example",
                                                    index=1,
                                                    indexed=True,
                                                ),
                                                parent={},
                                                exists=True,
                                                property_name="property_name_example",
                                                value={},
                                                parent_ci={},
                                                descriptor={},
                                                kind={},
                                                category="category_example",
                                                password=True,
                                                indexed=True,
                                            ),
                                        ),
                                    ],
                                    or_calculate_due_date="or_calculate_due_date_example",
                                    computed_planned_duration={},
                                    actual_duration={},
                                ),
                                target_id="target_id_example",
                                archived_target_title="archived_target_title_example",
                                archived_target_id="archived_target_id_example",
                                archived_as_resolved=True,
                                metadata={
                                    "key": {},
                                },
                                archived=True,
                                done=True,
                                aborted=True,
                                target_display_path="target_display_path_example",
                                target_title="target_title_example",
                                valid_allowed_plan_item_id=True,
                            ),
                        ],
                        open=True,
                        open_in_advance=True,
                        completable=True,
                        aborted_dependency_titles="aborted_dependency_titles_example",
                        variable_usages=[
                            UsagePoint(
                                target_property=CiProperty(
                                    wrapped=CiProperty(),
                                    last_property=ModelProperty(
                                        indexed_property_pattern="indexed_property_pattern_example",
                                        property_name="property_name_example",
                                        index=1,
                                        indexed=True,
                                    ),
                                    parent={},
                                    exists=True,
                                    property_name="property_name_example",
                                    value={},
                                    parent_ci={},
                                    descriptor={},
                                    kind={},
                                    category="category_example",
                                    password=True,
                                    indexed=True,
                                ),
                            ),
                        ],
                    ),
                ],
                all_tasks=[
                    Task(),
                ],
                children=[
                    PlanItem(
                        id="id_example",
                        type="type_example",
                        title="title_example",
                        description="description_example",
                        owner="owner_example",
                        scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        planned_duration=1,
                        flag_status=FlagStatus("OK"),
                        flag_comment="flag_comment_example",
                        overdue_notified=True,
                        flagged=True,
                        start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        children=[],
                        overdue=True,
                        done=True,
                        release=Release(),
                        release_uid=1,
                        updatable=True,
                        display_path="display_path_example",
                        aborted=True,
                        active=True,
                        variable_usages=[
                            UsagePoint(
                                target_property=CiProperty(
                                    wrapped=CiProperty(),
                                    last_property=ModelProperty(
                                        indexed_property_pattern="indexed_property_pattern_example",
                                        property_name="property_name_example",
                                        index=1,
                                        indexed=True,
                                    ),
                                    parent={},
                                    exists=True,
                                    property_name="property_name_example",
                                    value={},
                                    parent_ci={},
                                    descriptor={},
                                    kind={},
                                    category="category_example",
                                    password=True,
                                    indexed=True,
                                ),
                            ),
                        ],
                        or_calculate_due_date="or_calculate_due_date_example",
                        computed_planned_duration={},
                        actual_duration={},
                    ),
                ],
                variable_usages=[
                    UsagePoint(
                        target_property=CiProperty(
                            wrapped=CiProperty(),
                            last_property=ModelProperty(
                                indexed_property_pattern="indexed_property_pattern_example",
                                property_name="property_name_example",
                                index=1,
                                indexed=True,
                            ),
                            parent={},
                            exists=True,
                            property_name="property_name_example",
                            value={},
                            parent_ci={},
                            descriptor={},
                            kind={},
                            category="category_example",
                            password=True,
                            indexed=True,
                        ),
                    ),
                ],
                original=True,
                phase_copied=True,
                ancestor_id="ancestor_id_example",
                latest_copy=True,
            ),
            blackout_metadata=BlackoutMetadata(
                periods=[
                    BlackoutPeriod(
                        start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    ),
                ],
            ),
            flagged_count=1,
            delayed_count=1,
            done=True,
            done_in_advance=True,
            defunct=True,
            updatable=True,
            aborted=True,
            not_yet_reached=True,
            planned=True,
            active=True,
            in_progress=True,
            pending=True,
            waiting_for_input=True,
            failed=True,
            failing=True,
            completed_in_advance=True,
            skipped=True,
            skipped_in_advance=True,
            precondition_in_progress=True,
            failure_handler_in_progress=True,
            abort_script_in_progress=True,
            facet_in_progress=True,
            movable=True,
            gate=True,
            task_group=True,
            parallel_group=True,
            precondition_enabled=True,
            failure_handler_enabled=True,
            release=Release(),
            display_path="display_path_example",
            release_owner="release_owner_example",
            all_tasks=[
                Task(),
            ],
            children=[
                PlanItem(
                    id="id_example",
                    type="type_example",
                    title="title_example",
                    description="description_example",
                    owner="owner_example",
                    scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    planned_duration=1,
                    flag_status=FlagStatus("OK"),
                    flag_comment="flag_comment_example",
                    overdue_notified=True,
                    flagged=True,
                    start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    children=[],
                    overdue=True,
                    done=True,
                    release=Release(),
                    release_uid=1,
                    updatable=True,
                    display_path="display_path_example",
                    aborted=True,
                    active=True,
                    variable_usages=[
                        UsagePoint(
                            target_property=CiProperty(
                                wrapped=CiProperty(),
                                last_property=ModelProperty(
                                    indexed_property_pattern="indexed_property_pattern_example",
                                    property_name="property_name_example",
                                    index=1,
                                    indexed=True,
                                ),
                                parent={},
                                exists=True,
                                property_name="property_name_example",
                                value={},
                                parent_ci={},
                                descriptor={},
                                kind={},
                                category="category_example",
                                password=True,
                                indexed=True,
                            ),
                        ),
                    ],
                    or_calculate_due_date="or_calculate_due_date_example",
                    computed_planned_duration={},
                    actual_duration={},
                ),
            ],
            variable_usages=[
                UsagePoint(
                    target_property=CiProperty(
                        wrapped=CiProperty(),
                        last_property=ModelProperty(
                            indexed_property_pattern="indexed_property_pattern_example",
                            property_name="property_name_example",
                            index=1,
                            indexed=True,
                        ),
                        parent={},
                        exists=True,
                        property_name="property_name_example",
                        value={},
                        parent_ci={},
                        descriptor={},
                        kind={},
                        category="category_example",
                        password=True,
                        indexed=True,
                    ),
                ),
            ],
            input_variables=[
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
            referenced_variables=[
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
            unbound_required_variables=[
                "unbound_required_variables_example",
            ],
            automated=True,
            task_type={},
            due_soon=True,
            elapsed_duration_fraction=3.14,
            url="url_example",
        ),
        all_tasks=[
            Task(
                id="id_example",
                type="type_example",
                scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                flag_status=FlagStatus("OK"),
                title="title_example",
                description="description_example",
                owner="owner_example",
                due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                planned_duration=1,
                flag_comment="flag_comment_example",
                overdue_notified=True,
                flagged=True,
                start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                overdue=True,
                or_calculate_due_date="or_calculate_due_date_example",
                computed_planned_duration={},
                actual_duration={},
                release_uid=1,
                ci_uid=1,
                comments=[
                    Comment(
                        id="id_example",
                        type="type_example",
                        text="text_example",
                        author="author_example",
                        date=dateutil_parser('2023-03-20T02:07:00Z'),
                        creation_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    ),
                ],
                container=None,
                facets=[
                    Facet(
                        id="id_example",
                        type="type_example",
                        scope=FacetScope("TASK"),
                        target_id="target_id_example",
                        configuration_uri="configuration_uri_example",
                        variable_mapping={
                            "key": "key_example",
                        },
                        variable_usages=[
                            UsagePoint(
                                target_property=CiProperty(
                                    wrapped=CiProperty(),
                                    last_property=ModelProperty(
                                        indexed_property_pattern="indexed_property_pattern_example",
                                        property_name="property_name_example",
                                        index=1,
                                        indexed=True,
                                    ),
                                    parent={},
                                    exists=True,
                                    property_name="property_name_example",
                                    value={},
                                    parent_ci={},
                                    descriptor={},
                                    kind={},
                                    category="category_example",
                                    password=True,
                                    indexed=True,
                                ),
                            ),
                        ],
                        properties_with_variables=[
                            None,
                        ],
                    ),
                ],
                attachments=[
                    Attachment(
                        id="id_example",
                        type="type_example",
                        file={},
                        content_type="content_type_example",
                        export_filename="export_filename_example",
                        file_uri="file_uri_example",
                        placeholders=[
                            "placeholders_example",
                        ],
                        text_file_names_regex="text_file_names_regex_example",
                        exclude_file_names_regex="exclude_file_names_regex_example",
                        file_encodings={
                            "key": "key_example",
                        },
                        checksum="checksum_example",
                    ),
                ],
                status=TaskStatus("PLANNED"),
                team="team_example",
                watchers=[
                    "watchers_example",
                ],
                wait_for_scheduled_start_date=True,
                delay_during_blackout=True,
                postponed_due_to_blackout=True,
                postponed_until_environments_are_reserved=True,
                original_scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                has_been_flagged=True,
                has_been_delayed=True,
                precondition="precondition_example",
                failure_handler="failure_handler_example",
                task_failure_handler_enabled=True,
                task_recover_op=TaskRecoverOp("SKIP_TASK"),
                failures_count=1,
                execution_id="execution_id_example",
                variable_mapping={
                    "key": "key_example",
                },
                external_variable_mapping={
                    "key": "key_example",
                },
                max_comment_size=1,
                tags=[
                    "tags_example",
                ],
                configuration_uri="configuration_uri_example",
                due_soon_notified=True,
                locked=True,
                check_attributes=True,
                abort_script="abort_script_example",
                phase=Phase(
                    id="id_example",
                    type="type_example",
                    locked=True,
                    title="title_example",
                    description="description_example",
                    owner="owner_example",
                    scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    planned_duration=1,
                    flag_status=FlagStatus("OK"),
                    flag_comment="flag_comment_example",
                    overdue_notified=True,
                    flagged=True,
                    start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    overdue=True,
                    or_calculate_due_date="or_calculate_due_date_example",
                    computed_planned_duration={},
                    actual_duration={},
                    release_uid=1,
                    tasks=[],
                    release=None,
                    status=PhaseStatus("PLANNED"),
                    color="color_example",
                    origin_id="origin_id_example",
                    current_task=Task(),
                    display_path="display_path_example",
                    active=True,
                    done=True,
                    defunct=True,
                    updatable=True,
                    aborted=True,
                    planned=True,
                    failed=True,
                    failing=True,
                    release_owner="release_owner_example",
                    all_gates=[
                        GateTask(
                            id="id_example",
                            type="type_example",
                            scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            flag_status=FlagStatus("OK"),
                            title="title_example",
                            description="description_example",
                            owner="owner_example",
                            due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            planned_duration=1,
                            flag_comment="flag_comment_example",
                            overdue_notified=True,
                            flagged=True,
                            start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            overdue=True,
                            or_calculate_due_date="or_calculate_due_date_example",
                            computed_planned_duration={},
                            actual_duration={},
                            release_uid=1,
                            ci_uid=1,
                            comments=[
                                Comment(
                                    id="id_example",
                                    type="type_example",
                                    text="text_example",
                                    author="author_example",
                                    date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    creation_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                ),
                            ],
                            container=TaskContainer(
                                id="id_example",
                                type="type_example",
                                tasks=[],
                                locked=True,
                                title="title_example",
                            ),
                            facets=[
                                Facet(
                                    id="id_example",
                                    type="type_example",
                                    scope=FacetScope("TASK"),
                                    target_id="target_id_example",
                                    configuration_uri="configuration_uri_example",
                                    variable_mapping={
                                        "key": "key_example",
                                    },
                                    variable_usages=[
                                        UsagePoint(
                                            target_property=CiProperty(
                                                wrapped=CiProperty(),
                                                last_property=ModelProperty(
                                                    indexed_property_pattern="indexed_property_pattern_example",
                                                    property_name="property_name_example",
                                                    index=1,
                                                    indexed=True,
                                                ),
                                                parent={},
                                                exists=True,
                                                property_name="property_name_example",
                                                value={},
                                                parent_ci={},
                                                descriptor={},
                                                kind={},
                                                category="category_example",
                                                password=True,
                                                indexed=True,
                                            ),
                                        ),
                                    ],
                                    properties_with_variables=[
                                        None,
                                    ],
                                ),
                            ],
                            attachments=[
                                Attachment(
                                    id="id_example",
                                    type="type_example",
                                    file={},
                                    content_type="content_type_example",
                                    export_filename="export_filename_example",
                                    file_uri="file_uri_example",
                                    placeholders=[
                                        "placeholders_example",
                                    ],
                                    text_file_names_regex="text_file_names_regex_example",
                                    exclude_file_names_regex="exclude_file_names_regex_example",
                                    file_encodings={
                                        "key": "key_example",
                                    },
                                    checksum="checksum_example",
                                ),
                            ],
                            status=TaskStatus("PLANNED"),
                            team="team_example",
                            watchers=[
                                "watchers_example",
                            ],
                            wait_for_scheduled_start_date=True,
                            delay_during_blackout=True,
                            postponed_due_to_blackout=True,
                            postponed_until_environments_are_reserved=True,
                            original_scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            has_been_flagged=True,
                            has_been_delayed=True,
                            precondition="precondition_example",
                            failure_handler="failure_handler_example",
                            task_failure_handler_enabled=True,
                            task_recover_op=TaskRecoverOp("SKIP_TASK"),
                            failures_count=1,
                            execution_id="execution_id_example",
                            variable_mapping={
                                "key": "key_example",
                            },
                            external_variable_mapping={
                                "key": "key_example",
                            },
                            max_comment_size=1,
                            tags=[
                                "tags_example",
                            ],
                            configuration_uri="configuration_uri_example",
                            due_soon_notified=True,
                            locked=True,
                            check_attributes=True,
                            abort_script="abort_script_example",
                            phase=Phase(),
                            blackout_metadata=BlackoutMetadata(
                                periods=[
                                    BlackoutPeriod(
                                        start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    ),
                                ],
                            ),
                            flagged_count=1,
                            delayed_count=1,
                            done=True,
                            done_in_advance=True,
                            defunct=True,
                            updatable=True,
                            aborted=True,
                            not_yet_reached=True,
                            planned=True,
                            active=True,
                            in_progress=True,
                            pending=True,
                            waiting_for_input=True,
                            failed=True,
                            failing=True,
                            completed_in_advance=True,
                            skipped=True,
                            skipped_in_advance=True,
                            precondition_in_progress=True,
                            failure_handler_in_progress=True,
                            abort_script_in_progress=True,
                            facet_in_progress=True,
                            movable=True,
                            gate=True,
                            task_group=True,
                            parallel_group=True,
                            precondition_enabled=True,
                            failure_handler_enabled=True,
                            release=Release(),
                            display_path="display_path_example",
                            release_owner="release_owner_example",
                            all_tasks=[],
                            children=[
                                PlanItem(
                                    id="id_example",
                                    type="type_example",
                                    title="title_example",
                                    description="description_example",
                                    owner="owner_example",
                                    scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    planned_duration=1,
                                    flag_status=FlagStatus("OK"),
                                    flag_comment="flag_comment_example",
                                    overdue_notified=True,
                                    flagged=True,
                                    start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    children=[],
                                    overdue=True,
                                    done=True,
                                    release=Release(),
                                    release_uid=1,
                                    updatable=True,
                                    display_path="display_path_example",
                                    aborted=True,
                                    active=True,
                                    variable_usages=[
                                        UsagePoint(
                                            target_property=CiProperty(
                                                wrapped=CiProperty(),
                                                last_property=ModelProperty(
                                                    indexed_property_pattern="indexed_property_pattern_example",
                                                    property_name="property_name_example",
                                                    index=1,
                                                    indexed=True,
                                                ),
                                                parent={},
                                                exists=True,
                                                property_name="property_name_example",
                                                value={},
                                                parent_ci={},
                                                descriptor={},
                                                kind={},
                                                category="category_example",
                                                password=True,
                                                indexed=True,
                                            ),
                                        ),
                                    ],
                                    or_calculate_due_date="or_calculate_due_date_example",
                                    computed_planned_duration={},
                                    actual_duration={},
                                ),
                            ],
                            input_variables=[
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
                            referenced_variables=[
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
                            unbound_required_variables=[
                                "unbound_required_variables_example",
                            ],
                            automated=True,
                            task_type={},
                            due_soon=True,
                            elapsed_duration_fraction=3.14,
                            url="url_example",
                            conditions=[
                                GateCondition(
                                    id="id_example",
                                    type="type_example",
                                    title="title_example",
                                    checked=True,
                                ),
                            ],
                            dependencies=[
                                Dependency(
                                    id="id_example",
                                    type="type_example",
                                    gate_task=GateTask(),
                                    target=PlanItem(
                                        id="id_example",
                                        type="type_example",
                                        title="title_example",
                                        description="description_example",
                                        owner="owner_example",
                                        scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        planned_duration=1,
                                        flag_status=FlagStatus("OK"),
                                        flag_comment="flag_comment_example",
                                        overdue_notified=True,
                                        flagged=True,
                                        start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        children=[
                                            PlanItem(),
                                        ],
                                        overdue=True,
                                        done=True,
                                        release=Release(),
                                        release_uid=1,
                                        updatable=True,
                                        display_path="display_path_example",
                                        aborted=True,
                                        active=True,
                                        variable_usages=[
                                            UsagePoint(
                                                target_property=CiProperty(
                                                    wrapped=CiProperty(),
                                                    last_property=ModelProperty(
                                                        indexed_property_pattern="indexed_property_pattern_example",
                                                        property_name="property_name_example",
                                                        index=1,
                                                        indexed=True,
                                                    ),
                                                    parent={},
                                                    exists=True,
                                                    property_name="property_name_example",
                                                    value={},
                                                    parent_ci={},
                                                    descriptor={},
                                                    kind={},
                                                    category="category_example",
                                                    password=True,
                                                    indexed=True,
                                                ),
                                            ),
                                        ],
                                        or_calculate_due_date="or_calculate_due_date_example",
                                        computed_planned_duration={},
                                        actual_duration={},
                                    ),
                                    target_id="target_id_example",
                                    archived_target_title="archived_target_title_example",
                                    archived_target_id="archived_target_id_example",
                                    archived_as_resolved=True,
                                    metadata={
                                        "key": {},
                                    },
                                    archived=True,
                                    done=True,
                                    aborted=True,
                                    target_display_path="target_display_path_example",
                                    target_title="target_title_example",
                                    valid_allowed_plan_item_id=True,
                                ),
                            ],
                            open=True,
                            open_in_advance=True,
                            completable=True,
                            aborted_dependency_titles="aborted_dependency_titles_example",
                            variable_usages=[
                                UsagePoint(
                                    target_property=CiProperty(
                                        wrapped=CiProperty(),
                                        last_property=ModelProperty(
                                            indexed_property_pattern="indexed_property_pattern_example",
                                            property_name="property_name_example",
                                            index=1,
                                            indexed=True,
                                        ),
                                        parent={},
                                        exists=True,
                                        property_name="property_name_example",
                                        value={},
                                        parent_ci={},
                                        descriptor={},
                                        kind={},
                                        category="category_example",
                                        password=True,
                                        indexed=True,
                                    ),
                                ),
                            ],
                        ),
                    ],
                    all_tasks=[],
                    children=[
                        PlanItem(
                            id="id_example",
                            type="type_example",
                            title="title_example",
                            description="description_example",
                            owner="owner_example",
                            scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            planned_duration=1,
                            flag_status=FlagStatus("OK"),
                            flag_comment="flag_comment_example",
                            overdue_notified=True,
                            flagged=True,
                            start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            children=[],
                            overdue=True,
                            done=True,
                            release=Release(),
                            release_uid=1,
                            updatable=True,
                            display_path="display_path_example",
                            aborted=True,
                            active=True,
                            variable_usages=[
                                UsagePoint(
                                    target_property=CiProperty(
                                        wrapped=CiProperty(),
                                        last_property=ModelProperty(
                                            indexed_property_pattern="indexed_property_pattern_example",
                                            property_name="property_name_example",
                                            index=1,
                                            indexed=True,
                                        ),
                                        parent={},
                                        exists=True,
                                        property_name="property_name_example",
                                        value={},
                                        parent_ci={},
                                        descriptor={},
                                        kind={},
                                        category="category_example",
                                        password=True,
                                        indexed=True,
                                    ),
                                ),
                            ],
                            or_calculate_due_date="or_calculate_due_date_example",
                            computed_planned_duration={},
                            actual_duration={},
                        ),
                    ],
                    variable_usages=[
                        UsagePoint(
                            target_property=CiProperty(
                                wrapped=CiProperty(),
                                last_property=ModelProperty(
                                    indexed_property_pattern="indexed_property_pattern_example",
                                    property_name="property_name_example",
                                    index=1,
                                    indexed=True,
                                ),
                                parent={},
                                exists=True,
                                property_name="property_name_example",
                                value={},
                                parent_ci={},
                                descriptor={},
                                kind={},
                                category="category_example",
                                password=True,
                                indexed=True,
                            ),
                        ),
                    ],
                    original=True,
                    phase_copied=True,
                    ancestor_id="ancestor_id_example",
                    latest_copy=True,
                ),
                blackout_metadata=BlackoutMetadata(
                    periods=[
                        BlackoutPeriod(
                            start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        ),
                    ],
                ),
                flagged_count=1,
                delayed_count=1,
                done=True,
                done_in_advance=True,
                defunct=True,
                updatable=True,
                aborted=True,
                not_yet_reached=True,
                planned=True,
                active=True,
                in_progress=True,
                pending=True,
                waiting_for_input=True,
                failed=True,
                failing=True,
                completed_in_advance=True,
                skipped=True,
                skipped_in_advance=True,
                precondition_in_progress=True,
                failure_handler_in_progress=True,
                abort_script_in_progress=True,
                facet_in_progress=True,
                movable=True,
                gate=True,
                task_group=True,
                parallel_group=True,
                precondition_enabled=True,
                failure_handler_enabled=True,
                release=Release(),
                display_path="display_path_example",
                release_owner="release_owner_example",
                all_tasks=[],
                children=[
                    PlanItem(
                        id="id_example",
                        type="type_example",
                        title="title_example",
                        description="description_example",
                        owner="owner_example",
                        scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        planned_duration=1,
                        flag_status=FlagStatus("OK"),
                        flag_comment="flag_comment_example",
                        overdue_notified=True,
                        flagged=True,
                        start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        children=[],
                        overdue=True,
                        done=True,
                        release=Release(),
                        release_uid=1,
                        updatable=True,
                        display_path="display_path_example",
                        aborted=True,
                        active=True,
                        variable_usages=[
                            UsagePoint(
                                target_property=CiProperty(
                                    wrapped=CiProperty(),
                                    last_property=ModelProperty(
                                        indexed_property_pattern="indexed_property_pattern_example",
                                        property_name="property_name_example",
                                        index=1,
                                        indexed=True,
                                    ),
                                    parent={},
                                    exists=True,
                                    property_name="property_name_example",
                                    value={},
                                    parent_ci={},
                                    descriptor={},
                                    kind={},
                                    category="category_example",
                                    password=True,
                                    indexed=True,
                                ),
                            ),
                        ],
                        or_calculate_due_date="or_calculate_due_date_example",
                        computed_planned_duration={},
                        actual_duration={},
                    ),
                ],
                variable_usages=[
                    UsagePoint(
                        target_property=CiProperty(
                            wrapped=CiProperty(),
                            last_property=ModelProperty(
                                indexed_property_pattern="indexed_property_pattern_example",
                                property_name="property_name_example",
                                index=1,
                                indexed=True,
                            ),
                            parent={},
                            exists=True,
                            property_name="property_name_example",
                            value={},
                            parent_ci={},
                            descriptor={},
                            kind={},
                            category="category_example",
                            password=True,
                            indexed=True,
                        ),
                    ),
                ],
                input_variables=[
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
                referenced_variables=[
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
                unbound_required_variables=[
                    "unbound_required_variables_example",
                ],
                automated=True,
                task_type={},
                due_soon=True,
                elapsed_duration_fraction=3.14,
                url="url_example",
            ),
        ],
        all_gates=[
            GateTask(
                id="id_example",
                type="type_example",
                scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                flag_status=FlagStatus("OK"),
                title="title_example",
                description="description_example",
                owner="owner_example",
                due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                planned_duration=1,
                flag_comment="flag_comment_example",
                overdue_notified=True,
                flagged=True,
                start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                overdue=True,
                or_calculate_due_date="or_calculate_due_date_example",
                computed_planned_duration={},
                actual_duration={},
                release_uid=1,
                ci_uid=1,
                comments=[
                    Comment(
                        id="id_example",
                        type="type_example",
                        text="text_example",
                        author="author_example",
                        date=dateutil_parser('2023-03-20T02:07:00Z'),
                        creation_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    ),
                ],
                container=TaskContainer(
                    id="id_example",
                    type="type_example",
                    tasks=[
                        Task(
                            id="id_example",
                            type="type_example",
                            scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            flag_status=FlagStatus("OK"),
                            title="title_example",
                            description="description_example",
                            owner="owner_example",
                            due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            planned_duration=1,
                            flag_comment="flag_comment_example",
                            overdue_notified=True,
                            flagged=True,
                            start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            overdue=True,
                            or_calculate_due_date="or_calculate_due_date_example",
                            computed_planned_duration={},
                            actual_duration={},
                            release_uid=1,
                            ci_uid=1,
                            comments=[
                                Comment(
                                    id="id_example",
                                    type="type_example",
                                    text="text_example",
                                    author="author_example",
                                    date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    creation_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                ),
                            ],
                            container=None,
                            facets=[
                                Facet(
                                    id="id_example",
                                    type="type_example",
                                    scope=FacetScope("TASK"),
                                    target_id="target_id_example",
                                    configuration_uri="configuration_uri_example",
                                    variable_mapping={
                                        "key": "key_example",
                                    },
                                    variable_usages=[
                                        UsagePoint(
                                            target_property=CiProperty(
                                                wrapped=CiProperty(),
                                                last_property=ModelProperty(
                                                    indexed_property_pattern="indexed_property_pattern_example",
                                                    property_name="property_name_example",
                                                    index=1,
                                                    indexed=True,
                                                ),
                                                parent={},
                                                exists=True,
                                                property_name="property_name_example",
                                                value={},
                                                parent_ci={},
                                                descriptor={},
                                                kind={},
                                                category="category_example",
                                                password=True,
                                                indexed=True,
                                            ),
                                        ),
                                    ],
                                    properties_with_variables=[
                                        None,
                                    ],
                                ),
                            ],
                            attachments=[
                                Attachment(
                                    id="id_example",
                                    type="type_example",
                                    file={},
                                    content_type="content_type_example",
                                    export_filename="export_filename_example",
                                    file_uri="file_uri_example",
                                    placeholders=[
                                        "placeholders_example",
                                    ],
                                    text_file_names_regex="text_file_names_regex_example",
                                    exclude_file_names_regex="exclude_file_names_regex_example",
                                    file_encodings={
                                        "key": "key_example",
                                    },
                                    checksum="checksum_example",
                                ),
                            ],
                            status=TaskStatus("PLANNED"),
                            team="team_example",
                            watchers=[
                                "watchers_example",
                            ],
                            wait_for_scheduled_start_date=True,
                            delay_during_blackout=True,
                            postponed_due_to_blackout=True,
                            postponed_until_environments_are_reserved=True,
                            original_scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            has_been_flagged=True,
                            has_been_delayed=True,
                            precondition="precondition_example",
                            failure_handler="failure_handler_example",
                            task_failure_handler_enabled=True,
                            task_recover_op=TaskRecoverOp("SKIP_TASK"),
                            failures_count=1,
                            execution_id="execution_id_example",
                            variable_mapping={
                                "key": "key_example",
                            },
                            external_variable_mapping={
                                "key": "key_example",
                            },
                            max_comment_size=1,
                            tags=[
                                "tags_example",
                            ],
                            configuration_uri="configuration_uri_example",
                            due_soon_notified=True,
                            locked=True,
                            check_attributes=True,
                            abort_script="abort_script_example",
                            phase=Phase(
                                id="id_example",
                                type="type_example",
                                locked=True,
                                title="title_example",
                                description="description_example",
                                owner="owner_example",
                                scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                planned_duration=1,
                                flag_status=FlagStatus("OK"),
                                flag_comment="flag_comment_example",
                                overdue_notified=True,
                                flagged=True,
                                start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                overdue=True,
                                or_calculate_due_date="or_calculate_due_date_example",
                                computed_planned_duration={},
                                actual_duration={},
                                release_uid=1,
                                tasks=[],
                                release=None,
                                status=PhaseStatus("PLANNED"),
                                color="color_example",
                                origin_id="origin_id_example",
                                current_task=Task(),
                                display_path="display_path_example",
                                active=True,
                                done=True,
                                defunct=True,
                                updatable=True,
                                aborted=True,
                                planned=True,
                                failed=True,
                                failing=True,
                                release_owner="release_owner_example",
                                all_gates=[],
                                all_tasks=[],
                                children=[
                                    PlanItem(
                                        id="id_example",
                                        type="type_example",
                                        title="title_example",
                                        description="description_example",
                                        owner="owner_example",
                                        scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        planned_duration=1,
                                        flag_status=FlagStatus("OK"),
                                        flag_comment="flag_comment_example",
                                        overdue_notified=True,
                                        flagged=True,
                                        start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        children=[],
                                        overdue=True,
                                        done=True,
                                        release=Release(),
                                        release_uid=1,
                                        updatable=True,
                                        display_path="display_path_example",
                                        aborted=True,
                                        active=True,
                                        variable_usages=[
                                            UsagePoint(
                                                target_property=CiProperty(
                                                    wrapped=CiProperty(),
                                                    last_property=ModelProperty(
                                                        indexed_property_pattern="indexed_property_pattern_example",
                                                        property_name="property_name_example",
                                                        index=1,
                                                        indexed=True,
                                                    ),
                                                    parent={},
                                                    exists=True,
                                                    property_name="property_name_example",
                                                    value={},
                                                    parent_ci={},
                                                    descriptor={},
                                                    kind={},
                                                    category="category_example",
                                                    password=True,
                                                    indexed=True,
                                                ),
                                            ),
                                        ],
                                        or_calculate_due_date="or_calculate_due_date_example",
                                        computed_planned_duration={},
                                        actual_duration={},
                                    ),
                                ],
                                variable_usages=[
                                    UsagePoint(
                                        target_property=CiProperty(
                                            wrapped=CiProperty(),
                                            last_property=ModelProperty(
                                                indexed_property_pattern="indexed_property_pattern_example",
                                                property_name="property_name_example",
                                                index=1,
                                                indexed=True,
                                            ),
                                            parent={},
                                            exists=True,
                                            property_name="property_name_example",
                                            value={},
                                            parent_ci={},
                                            descriptor={},
                                            kind={},
                                            category="category_example",
                                            password=True,
                                            indexed=True,
                                        ),
                                    ),
                                ],
                                original=True,
                                phase_copied=True,
                                ancestor_id="ancestor_id_example",
                                latest_copy=True,
                            ),
                            blackout_metadata=BlackoutMetadata(
                                periods=[
                                    BlackoutPeriod(
                                        start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    ),
                                ],
                            ),
                            flagged_count=1,
                            delayed_count=1,
                            done=True,
                            done_in_advance=True,
                            defunct=True,
                            updatable=True,
                            aborted=True,
                            not_yet_reached=True,
                            planned=True,
                            active=True,
                            in_progress=True,
                            pending=True,
                            waiting_for_input=True,
                            failed=True,
                            failing=True,
                            completed_in_advance=True,
                            skipped=True,
                            skipped_in_advance=True,
                            precondition_in_progress=True,
                            failure_handler_in_progress=True,
                            abort_script_in_progress=True,
                            facet_in_progress=True,
                            movable=True,
                            gate=True,
                            task_group=True,
                            parallel_group=True,
                            precondition_enabled=True,
                            failure_handler_enabled=True,
                            release=Release(),
                            display_path="display_path_example",
                            release_owner="release_owner_example",
                            all_tasks=[],
                            children=[
                                PlanItem(
                                    id="id_example",
                                    type="type_example",
                                    title="title_example",
                                    description="description_example",
                                    owner="owner_example",
                                    scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    planned_duration=1,
                                    flag_status=FlagStatus("OK"),
                                    flag_comment="flag_comment_example",
                                    overdue_notified=True,
                                    flagged=True,
                                    start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    children=[],
                                    overdue=True,
                                    done=True,
                                    release=Release(),
                                    release_uid=1,
                                    updatable=True,
                                    display_path="display_path_example",
                                    aborted=True,
                                    active=True,
                                    variable_usages=[
                                        UsagePoint(
                                            target_property=CiProperty(
                                                wrapped=CiProperty(),
                                                last_property=ModelProperty(
                                                    indexed_property_pattern="indexed_property_pattern_example",
                                                    property_name="property_name_example",
                                                    index=1,
                                                    indexed=True,
                                                ),
                                                parent={},
                                                exists=True,
                                                property_name="property_name_example",
                                                value={},
                                                parent_ci={},
                                                descriptor={},
                                                kind={},
                                                category="category_example",
                                                password=True,
                                                indexed=True,
                                            ),
                                        ),
                                    ],
                                    or_calculate_due_date="or_calculate_due_date_example",
                                    computed_planned_duration={},
                                    actual_duration={},
                                ),
                            ],
                            variable_usages=[
                                UsagePoint(
                                    target_property=CiProperty(
                                        wrapped=CiProperty(),
                                        last_property=ModelProperty(
                                            indexed_property_pattern="indexed_property_pattern_example",
                                            property_name="property_name_example",
                                            index=1,
                                            indexed=True,
                                        ),
                                        parent={},
                                        exists=True,
                                        property_name="property_name_example",
                                        value={},
                                        parent_ci={},
                                        descriptor={},
                                        kind={},
                                        category="category_example",
                                        password=True,
                                        indexed=True,
                                    ),
                                ),
                            ],
                            input_variables=[
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
                            referenced_variables=[
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
                            unbound_required_variables=[
                                "unbound_required_variables_example",
                            ],
                            automated=True,
                            task_type={},
                            due_soon=True,
                            elapsed_duration_fraction=3.14,
                            url="url_example",
                        ),
                    ],
                    locked=True,
                    title="title_example",
                ),
                facets=[
                    Facet(
                        id="id_example",
                        type="type_example",
                        scope=FacetScope("TASK"),
                        target_id="target_id_example",
                        configuration_uri="configuration_uri_example",
                        variable_mapping={
                            "key": "key_example",
                        },
                        variable_usages=[
                            UsagePoint(
                                target_property=CiProperty(
                                    wrapped=CiProperty(),
                                    last_property=ModelProperty(
                                        indexed_property_pattern="indexed_property_pattern_example",
                                        property_name="property_name_example",
                                        index=1,
                                        indexed=True,
                                    ),
                                    parent={},
                                    exists=True,
                                    property_name="property_name_example",
                                    value={},
                                    parent_ci={},
                                    descriptor={},
                                    kind={},
                                    category="category_example",
                                    password=True,
                                    indexed=True,
                                ),
                            ),
                        ],
                        properties_with_variables=[
                            None,
                        ],
                    ),
                ],
                attachments=[
                    Attachment(
                        id="id_example",
                        type="type_example",
                        file={},
                        content_type="content_type_example",
                        export_filename="export_filename_example",
                        file_uri="file_uri_example",
                        placeholders=[
                            "placeholders_example",
                        ],
                        text_file_names_regex="text_file_names_regex_example",
                        exclude_file_names_regex="exclude_file_names_regex_example",
                        file_encodings={
                            "key": "key_example",
                        },
                        checksum="checksum_example",
                    ),
                ],
                status=TaskStatus("PLANNED"),
                team="team_example",
                watchers=[
                    "watchers_example",
                ],
                wait_for_scheduled_start_date=True,
                delay_during_blackout=True,
                postponed_due_to_blackout=True,
                postponed_until_environments_are_reserved=True,
                original_scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                has_been_flagged=True,
                has_been_delayed=True,
                precondition="precondition_example",
                failure_handler="failure_handler_example",
                task_failure_handler_enabled=True,
                task_recover_op=TaskRecoverOp("SKIP_TASK"),
                failures_count=1,
                execution_id="execution_id_example",
                variable_mapping={
                    "key": "key_example",
                },
                external_variable_mapping={
                    "key": "key_example",
                },
                max_comment_size=1,
                tags=[
                    "tags_example",
                ],
                configuration_uri="configuration_uri_example",
                due_soon_notified=True,
                locked=True,
                check_attributes=True,
                abort_script="abort_script_example",
                phase=Phase(
                    id="id_example",
                    type="type_example",
                    locked=True,
                    title="title_example",
                    description="description_example",
                    owner="owner_example",
                    scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    planned_duration=1,
                    flag_status=FlagStatus("OK"),
                    flag_comment="flag_comment_example",
                    overdue_notified=True,
                    flagged=True,
                    start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    overdue=True,
                    or_calculate_due_date="or_calculate_due_date_example",
                    computed_planned_duration={},
                    actual_duration={},
                    release_uid=1,
                    tasks=[
                        Task(
                            id="id_example",
                            type="type_example",
                            scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            flag_status=FlagStatus("OK"),
                            title="title_example",
                            description="description_example",
                            owner="owner_example",
                            due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            planned_duration=1,
                            flag_comment="flag_comment_example",
                            overdue_notified=True,
                            flagged=True,
                            start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            overdue=True,
                            or_calculate_due_date="or_calculate_due_date_example",
                            computed_planned_duration={},
                            actual_duration={},
                            release_uid=1,
                            ci_uid=1,
                            comments=[
                                Comment(
                                    id="id_example",
                                    type="type_example",
                                    text="text_example",
                                    author="author_example",
                                    date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    creation_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                ),
                            ],
                            container=None,
                            facets=[
                                Facet(
                                    id="id_example",
                                    type="type_example",
                                    scope=FacetScope("TASK"),
                                    target_id="target_id_example",
                                    configuration_uri="configuration_uri_example",
                                    variable_mapping={
                                        "key": "key_example",
                                    },
                                    variable_usages=[
                                        UsagePoint(
                                            target_property=CiProperty(
                                                wrapped=CiProperty(),
                                                last_property=ModelProperty(
                                                    indexed_property_pattern="indexed_property_pattern_example",
                                                    property_name="property_name_example",
                                                    index=1,
                                                    indexed=True,
                                                ),
                                                parent={},
                                                exists=True,
                                                property_name="property_name_example",
                                                value={},
                                                parent_ci={},
                                                descriptor={},
                                                kind={},
                                                category="category_example",
                                                password=True,
                                                indexed=True,
                                            ),
                                        ),
                                    ],
                                    properties_with_variables=[
                                        None,
                                    ],
                                ),
                            ],
                            attachments=[
                                Attachment(
                                    id="id_example",
                                    type="type_example",
                                    file={},
                                    content_type="content_type_example",
                                    export_filename="export_filename_example",
                                    file_uri="file_uri_example",
                                    placeholders=[
                                        "placeholders_example",
                                    ],
                                    text_file_names_regex="text_file_names_regex_example",
                                    exclude_file_names_regex="exclude_file_names_regex_example",
                                    file_encodings={
                                        "key": "key_example",
                                    },
                                    checksum="checksum_example",
                                ),
                            ],
                            status=TaskStatus("PLANNED"),
                            team="team_example",
                            watchers=[
                                "watchers_example",
                            ],
                            wait_for_scheduled_start_date=True,
                            delay_during_blackout=True,
                            postponed_due_to_blackout=True,
                            postponed_until_environments_are_reserved=True,
                            original_scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            has_been_flagged=True,
                            has_been_delayed=True,
                            precondition="precondition_example",
                            failure_handler="failure_handler_example",
                            task_failure_handler_enabled=True,
                            task_recover_op=TaskRecoverOp("SKIP_TASK"),
                            failures_count=1,
                            execution_id="execution_id_example",
                            variable_mapping={
                                "key": "key_example",
                            },
                            external_variable_mapping={
                                "key": "key_example",
                            },
                            max_comment_size=1,
                            tags=[
                                "tags_example",
                            ],
                            configuration_uri="configuration_uri_example",
                            due_soon_notified=True,
                            locked=True,
                            check_attributes=True,
                            abort_script="abort_script_example",
                            phase=Phase(),
                            blackout_metadata=BlackoutMetadata(
                                periods=[
                                    BlackoutPeriod(
                                        start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    ),
                                ],
                            ),
                            flagged_count=1,
                            delayed_count=1,
                            done=True,
                            done_in_advance=True,
                            defunct=True,
                            updatable=True,
                            aborted=True,
                            not_yet_reached=True,
                            planned=True,
                            active=True,
                            in_progress=True,
                            pending=True,
                            waiting_for_input=True,
                            failed=True,
                            failing=True,
                            completed_in_advance=True,
                            skipped=True,
                            skipped_in_advance=True,
                            precondition_in_progress=True,
                            failure_handler_in_progress=True,
                            abort_script_in_progress=True,
                            facet_in_progress=True,
                            movable=True,
                            gate=True,
                            task_group=True,
                            parallel_group=True,
                            precondition_enabled=True,
                            failure_handler_enabled=True,
                            release=Release(),
                            display_path="display_path_example",
                            release_owner="release_owner_example",
                            all_tasks=[],
                            children=[
                                PlanItem(
                                    id="id_example",
                                    type="type_example",
                                    title="title_example",
                                    description="description_example",
                                    owner="owner_example",
                                    scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    planned_duration=1,
                                    flag_status=FlagStatus("OK"),
                                    flag_comment="flag_comment_example",
                                    overdue_notified=True,
                                    flagged=True,
                                    start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    children=[],
                                    overdue=True,
                                    done=True,
                                    release=Release(),
                                    release_uid=1,
                                    updatable=True,
                                    display_path="display_path_example",
                                    aborted=True,
                                    active=True,
                                    variable_usages=[
                                        UsagePoint(
                                            target_property=CiProperty(
                                                wrapped=CiProperty(),
                                                last_property=ModelProperty(
                                                    indexed_property_pattern="indexed_property_pattern_example",
                                                    property_name="property_name_example",
                                                    index=1,
                                                    indexed=True,
                                                ),
                                                parent={},
                                                exists=True,
                                                property_name="property_name_example",
                                                value={},
                                                parent_ci={},
                                                descriptor={},
                                                kind={},
                                                category="category_example",
                                                password=True,
                                                indexed=True,
                                            ),
                                        ),
                                    ],
                                    or_calculate_due_date="or_calculate_due_date_example",
                                    computed_planned_duration={},
                                    actual_duration={},
                                ),
                            ],
                            variable_usages=[
                                UsagePoint(
                                    target_property=CiProperty(
                                        wrapped=CiProperty(),
                                        last_property=ModelProperty(
                                            indexed_property_pattern="indexed_property_pattern_example",
                                            property_name="property_name_example",
                                            index=1,
                                            indexed=True,
                                        ),
                                        parent={},
                                        exists=True,
                                        property_name="property_name_example",
                                        value={},
                                        parent_ci={},
                                        descriptor={},
                                        kind={},
                                        category="category_example",
                                        password=True,
                                        indexed=True,
                                    ),
                                ),
                            ],
                            input_variables=[
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
                            referenced_variables=[
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
                            unbound_required_variables=[
                                "unbound_required_variables_example",
                            ],
                            automated=True,
                            task_type={},
                            due_soon=True,
                            elapsed_duration_fraction=3.14,
                            url="url_example",
                        ),
                    ],
                    release=None,
                    status=PhaseStatus("PLANNED"),
                    color="color_example",
                    origin_id="origin_id_example",
                    current_task=Task(
                        id="id_example",
                        type="type_example",
                        scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        flag_status=FlagStatus("OK"),
                        title="title_example",
                        description="description_example",
                        owner="owner_example",
                        due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        planned_duration=1,
                        flag_comment="flag_comment_example",
                        overdue_notified=True,
                        flagged=True,
                        start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        overdue=True,
                        or_calculate_due_date="or_calculate_due_date_example",
                        computed_planned_duration={},
                        actual_duration={},
                        release_uid=1,
                        ci_uid=1,
                        comments=[
                            Comment(
                                id="id_example",
                                type="type_example",
                                text="text_example",
                                author="author_example",
                                date=dateutil_parser('2023-03-20T02:07:00Z'),
                                creation_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            ),
                        ],
                        container=None,
                        facets=[
                            Facet(
                                id="id_example",
                                type="type_example",
                                scope=FacetScope("TASK"),
                                target_id="target_id_example",
                                configuration_uri="configuration_uri_example",
                                variable_mapping={
                                    "key": "key_example",
                                },
                                variable_usages=[
                                    UsagePoint(
                                        target_property=CiProperty(
                                            wrapped=CiProperty(),
                                            last_property=ModelProperty(
                                                indexed_property_pattern="indexed_property_pattern_example",
                                                property_name="property_name_example",
                                                index=1,
                                                indexed=True,
                                            ),
                                            parent={},
                                            exists=True,
                                            property_name="property_name_example",
                                            value={},
                                            parent_ci={},
                                            descriptor={},
                                            kind={},
                                            category="category_example",
                                            password=True,
                                            indexed=True,
                                        ),
                                    ),
                                ],
                                properties_with_variables=[
                                    None,
                                ],
                            ),
                        ],
                        attachments=[
                            Attachment(
                                id="id_example",
                                type="type_example",
                                file={},
                                content_type="content_type_example",
                                export_filename="export_filename_example",
                                file_uri="file_uri_example",
                                placeholders=[
                                    "placeholders_example",
                                ],
                                text_file_names_regex="text_file_names_regex_example",
                                exclude_file_names_regex="exclude_file_names_regex_example",
                                file_encodings={
                                    "key": "key_example",
                                },
                                checksum="checksum_example",
                            ),
                        ],
                        status=TaskStatus("PLANNED"),
                        team="team_example",
                        watchers=[
                            "watchers_example",
                        ],
                        wait_for_scheduled_start_date=True,
                        delay_during_blackout=True,
                        postponed_due_to_blackout=True,
                        postponed_until_environments_are_reserved=True,
                        original_scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        has_been_flagged=True,
                        has_been_delayed=True,
                        precondition="precondition_example",
                        failure_handler="failure_handler_example",
                        task_failure_handler_enabled=True,
                        task_recover_op=TaskRecoverOp("SKIP_TASK"),
                        failures_count=1,
                        execution_id="execution_id_example",
                        variable_mapping={
                            "key": "key_example",
                        },
                        external_variable_mapping={
                            "key": "key_example",
                        },
                        max_comment_size=1,
                        tags=[
                            "tags_example",
                        ],
                        configuration_uri="configuration_uri_example",
                        due_soon_notified=True,
                        locked=True,
                        check_attributes=True,
                        abort_script="abort_script_example",
                        phase=Phase(),
                        blackout_metadata=BlackoutMetadata(
                            periods=[
                                BlackoutPeriod(
                                    start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                ),
                            ],
                        ),
                        flagged_count=1,
                        delayed_count=1,
                        done=True,
                        done_in_advance=True,
                        defunct=True,
                        updatable=True,
                        aborted=True,
                        not_yet_reached=True,
                        planned=True,
                        active=True,
                        in_progress=True,
                        pending=True,
                        waiting_for_input=True,
                        failed=True,
                        failing=True,
                        completed_in_advance=True,
                        skipped=True,
                        skipped_in_advance=True,
                        precondition_in_progress=True,
                        failure_handler_in_progress=True,
                        abort_script_in_progress=True,
                        facet_in_progress=True,
                        movable=True,
                        gate=True,
                        task_group=True,
                        parallel_group=True,
                        precondition_enabled=True,
                        failure_handler_enabled=True,
                        release=Release(),
                        display_path="display_path_example",
                        release_owner="release_owner_example",
                        all_tasks=[
                            Task(),
                        ],
                        children=[
                            PlanItem(
                                id="id_example",
                                type="type_example",
                                title="title_example",
                                description="description_example",
                                owner="owner_example",
                                scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                planned_duration=1,
                                flag_status=FlagStatus("OK"),
                                flag_comment="flag_comment_example",
                                overdue_notified=True,
                                flagged=True,
                                start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                children=[],
                                overdue=True,
                                done=True,
                                release=Release(),
                                release_uid=1,
                                updatable=True,
                                display_path="display_path_example",
                                aborted=True,
                                active=True,
                                variable_usages=[
                                    UsagePoint(
                                        target_property=CiProperty(
                                            wrapped=CiProperty(),
                                            last_property=ModelProperty(
                                                indexed_property_pattern="indexed_property_pattern_example",
                                                property_name="property_name_example",
                                                index=1,
                                                indexed=True,
                                            ),
                                            parent={},
                                            exists=True,
                                            property_name="property_name_example",
                                            value={},
                                            parent_ci={},
                                            descriptor={},
                                            kind={},
                                            category="category_example",
                                            password=True,
                                            indexed=True,
                                        ),
                                    ),
                                ],
                                or_calculate_due_date="or_calculate_due_date_example",
                                computed_planned_duration={},
                                actual_duration={},
                            ),
                        ],
                        variable_usages=[
                            UsagePoint(
                                target_property=CiProperty(
                                    wrapped=CiProperty(),
                                    last_property=ModelProperty(
                                        indexed_property_pattern="indexed_property_pattern_example",
                                        property_name="property_name_example",
                                        index=1,
                                        indexed=True,
                                    ),
                                    parent={},
                                    exists=True,
                                    property_name="property_name_example",
                                    value={},
                                    parent_ci={},
                                    descriptor={},
                                    kind={},
                                    category="category_example",
                                    password=True,
                                    indexed=True,
                                ),
                            ),
                        ],
                        input_variables=[
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
                        referenced_variables=[
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
                        unbound_required_variables=[
                            "unbound_required_variables_example",
                        ],
                        automated=True,
                        task_type={},
                        due_soon=True,
                        elapsed_duration_fraction=3.14,
                        url="url_example",
                    ),
                    display_path="display_path_example",
                    active=True,
                    done=True,
                    defunct=True,
                    updatable=True,
                    aborted=True,
                    planned=True,
                    failed=True,
                    failing=True,
                    release_owner="release_owner_example",
                    all_gates=[],
                    all_tasks=[
                        Task(
                            id="id_example",
                            type="type_example",
                            scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            flag_status=FlagStatus("OK"),
                            title="title_example",
                            description="description_example",
                            owner="owner_example",
                            due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            planned_duration=1,
                            flag_comment="flag_comment_example",
                            overdue_notified=True,
                            flagged=True,
                            start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            overdue=True,
                            or_calculate_due_date="or_calculate_due_date_example",
                            computed_planned_duration={},
                            actual_duration={},
                            release_uid=1,
                            ci_uid=1,
                            comments=[
                                Comment(
                                    id="id_example",
                                    type="type_example",
                                    text="text_example",
                                    author="author_example",
                                    date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    creation_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                ),
                            ],
                            container=None,
                            facets=[
                                Facet(
                                    id="id_example",
                                    type="type_example",
                                    scope=FacetScope("TASK"),
                                    target_id="target_id_example",
                                    configuration_uri="configuration_uri_example",
                                    variable_mapping={
                                        "key": "key_example",
                                    },
                                    variable_usages=[
                                        UsagePoint(
                                            target_property=CiProperty(
                                                wrapped=CiProperty(),
                                                last_property=ModelProperty(
                                                    indexed_property_pattern="indexed_property_pattern_example",
                                                    property_name="property_name_example",
                                                    index=1,
                                                    indexed=True,
                                                ),
                                                parent={},
                                                exists=True,
                                                property_name="property_name_example",
                                                value={},
                                                parent_ci={},
                                                descriptor={},
                                                kind={},
                                                category="category_example",
                                                password=True,
                                                indexed=True,
                                            ),
                                        ),
                                    ],
                                    properties_with_variables=[
                                        None,
                                    ],
                                ),
                            ],
                            attachments=[
                                Attachment(
                                    id="id_example",
                                    type="type_example",
                                    file={},
                                    content_type="content_type_example",
                                    export_filename="export_filename_example",
                                    file_uri="file_uri_example",
                                    placeholders=[
                                        "placeholders_example",
                                    ],
                                    text_file_names_regex="text_file_names_regex_example",
                                    exclude_file_names_regex="exclude_file_names_regex_example",
                                    file_encodings={
                                        "key": "key_example",
                                    },
                                    checksum="checksum_example",
                                ),
                            ],
                            status=TaskStatus("PLANNED"),
                            team="team_example",
                            watchers=[
                                "watchers_example",
                            ],
                            wait_for_scheduled_start_date=True,
                            delay_during_blackout=True,
                            postponed_due_to_blackout=True,
                            postponed_until_environments_are_reserved=True,
                            original_scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            has_been_flagged=True,
                            has_been_delayed=True,
                            precondition="precondition_example",
                            failure_handler="failure_handler_example",
                            task_failure_handler_enabled=True,
                            task_recover_op=TaskRecoverOp("SKIP_TASK"),
                            failures_count=1,
                            execution_id="execution_id_example",
                            variable_mapping={
                                "key": "key_example",
                            },
                            external_variable_mapping={
                                "key": "key_example",
                            },
                            max_comment_size=1,
                            tags=[
                                "tags_example",
                            ],
                            configuration_uri="configuration_uri_example",
                            due_soon_notified=True,
                            locked=True,
                            check_attributes=True,
                            abort_script="abort_script_example",
                            phase=Phase(),
                            blackout_metadata=BlackoutMetadata(
                                periods=[
                                    BlackoutPeriod(
                                        start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    ),
                                ],
                            ),
                            flagged_count=1,
                            delayed_count=1,
                            done=True,
                            done_in_advance=True,
                            defunct=True,
                            updatable=True,
                            aborted=True,
                            not_yet_reached=True,
                            planned=True,
                            active=True,
                            in_progress=True,
                            pending=True,
                            waiting_for_input=True,
                            failed=True,
                            failing=True,
                            completed_in_advance=True,
                            skipped=True,
                            skipped_in_advance=True,
                            precondition_in_progress=True,
                            failure_handler_in_progress=True,
                            abort_script_in_progress=True,
                            facet_in_progress=True,
                            movable=True,
                            gate=True,
                            task_group=True,
                            parallel_group=True,
                            precondition_enabled=True,
                            failure_handler_enabled=True,
                            release=Release(),
                            display_path="display_path_example",
                            release_owner="release_owner_example",
                            all_tasks=[],
                            children=[
                                PlanItem(
                                    id="id_example",
                                    type="type_example",
                                    title="title_example",
                                    description="description_example",
                                    owner="owner_example",
                                    scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    planned_duration=1,
                                    flag_status=FlagStatus("OK"),
                                    flag_comment="flag_comment_example",
                                    overdue_notified=True,
                                    flagged=True,
                                    start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    children=[],
                                    overdue=True,
                                    done=True,
                                    release=Release(),
                                    release_uid=1,
                                    updatable=True,
                                    display_path="display_path_example",
                                    aborted=True,
                                    active=True,
                                    variable_usages=[
                                        UsagePoint(
                                            target_property=CiProperty(
                                                wrapped=CiProperty(),
                                                last_property=ModelProperty(
                                                    indexed_property_pattern="indexed_property_pattern_example",
                                                    property_name="property_name_example",
                                                    index=1,
                                                    indexed=True,
                                                ),
                                                parent={},
                                                exists=True,
                                                property_name="property_name_example",
                                                value={},
                                                parent_ci={},
                                                descriptor={},
                                                kind={},
                                                category="category_example",
                                                password=True,
                                                indexed=True,
                                            ),
                                        ),
                                    ],
                                    or_calculate_due_date="or_calculate_due_date_example",
                                    computed_planned_duration={},
                                    actual_duration={},
                                ),
                            ],
                            variable_usages=[
                                UsagePoint(
                                    target_property=CiProperty(
                                        wrapped=CiProperty(),
                                        last_property=ModelProperty(
                                            indexed_property_pattern="indexed_property_pattern_example",
                                            property_name="property_name_example",
                                            index=1,
                                            indexed=True,
                                        ),
                                        parent={},
                                        exists=True,
                                        property_name="property_name_example",
                                        value={},
                                        parent_ci={},
                                        descriptor={},
                                        kind={},
                                        category="category_example",
                                        password=True,
                                        indexed=True,
                                    ),
                                ),
                            ],
                            input_variables=[
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
                            referenced_variables=[
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
                            unbound_required_variables=[
                                "unbound_required_variables_example",
                            ],
                            automated=True,
                            task_type={},
                            due_soon=True,
                            elapsed_duration_fraction=3.14,
                            url="url_example",
                        ),
                    ],
                    children=[
                        PlanItem(
                            id="id_example",
                            type="type_example",
                            title="title_example",
                            description="description_example",
                            owner="owner_example",
                            scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            planned_duration=1,
                            flag_status=FlagStatus("OK"),
                            flag_comment="flag_comment_example",
                            overdue_notified=True,
                            flagged=True,
                            start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            children=[],
                            overdue=True,
                            done=True,
                            release=Release(),
                            release_uid=1,
                            updatable=True,
                            display_path="display_path_example",
                            aborted=True,
                            active=True,
                            variable_usages=[
                                UsagePoint(
                                    target_property=CiProperty(
                                        wrapped=CiProperty(),
                                        last_property=ModelProperty(
                                            indexed_property_pattern="indexed_property_pattern_example",
                                            property_name="property_name_example",
                                            index=1,
                                            indexed=True,
                                        ),
                                        parent={},
                                        exists=True,
                                        property_name="property_name_example",
                                        value={},
                                        parent_ci={},
                                        descriptor={},
                                        kind={},
                                        category="category_example",
                                        password=True,
                                        indexed=True,
                                    ),
                                ),
                            ],
                            or_calculate_due_date="or_calculate_due_date_example",
                            computed_planned_duration={},
                            actual_duration={},
                        ),
                    ],
                    variable_usages=[
                        UsagePoint(
                            target_property=CiProperty(
                                wrapped=CiProperty(),
                                last_property=ModelProperty(
                                    indexed_property_pattern="indexed_property_pattern_example",
                                    property_name="property_name_example",
                                    index=1,
                                    indexed=True,
                                ),
                                parent={},
                                exists=True,
                                property_name="property_name_example",
                                value={},
                                parent_ci={},
                                descriptor={},
                                kind={},
                                category="category_example",
                                password=True,
                                indexed=True,
                            ),
                        ),
                    ],
                    original=True,
                    phase_copied=True,
                    ancestor_id="ancestor_id_example",
                    latest_copy=True,
                ),
                blackout_metadata=BlackoutMetadata(
                    periods=[
                        BlackoutPeriod(
                            start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        ),
                    ],
                ),
                flagged_count=1,
                delayed_count=1,
                done=True,
                done_in_advance=True,
                defunct=True,
                updatable=True,
                aborted=True,
                not_yet_reached=True,
                planned=True,
                active=True,
                in_progress=True,
                pending=True,
                waiting_for_input=True,
                failed=True,
                failing=True,
                completed_in_advance=True,
                skipped=True,
                skipped_in_advance=True,
                precondition_in_progress=True,
                failure_handler_in_progress=True,
                abort_script_in_progress=True,
                facet_in_progress=True,
                movable=True,
                gate=True,
                task_group=True,
                parallel_group=True,
                precondition_enabled=True,
                failure_handler_enabled=True,
                release=Release(),
                display_path="display_path_example",
                release_owner="release_owner_example",
                all_tasks=[
                    Task(
                        id="id_example",
                        type="type_example",
                        scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        flag_status=FlagStatus("OK"),
                        title="title_example",
                        description="description_example",
                        owner="owner_example",
                        due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        planned_duration=1,
                        flag_comment="flag_comment_example",
                        overdue_notified=True,
                        flagged=True,
                        start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        overdue=True,
                        or_calculate_due_date="or_calculate_due_date_example",
                        computed_planned_duration={},
                        actual_duration={},
                        release_uid=1,
                        ci_uid=1,
                        comments=[
                            Comment(
                                id="id_example",
                                type="type_example",
                                text="text_example",
                                author="author_example",
                                date=dateutil_parser('2023-03-20T02:07:00Z'),
                                creation_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            ),
                        ],
                        container=None,
                        facets=[
                            Facet(
                                id="id_example",
                                type="type_example",
                                scope=FacetScope("TASK"),
                                target_id="target_id_example",
                                configuration_uri="configuration_uri_example",
                                variable_mapping={
                                    "key": "key_example",
                                },
                                variable_usages=[
                                    UsagePoint(
                                        target_property=CiProperty(
                                            wrapped=CiProperty(),
                                            last_property=ModelProperty(
                                                indexed_property_pattern="indexed_property_pattern_example",
                                                property_name="property_name_example",
                                                index=1,
                                                indexed=True,
                                            ),
                                            parent={},
                                            exists=True,
                                            property_name="property_name_example",
                                            value={},
                                            parent_ci={},
                                            descriptor={},
                                            kind={},
                                            category="category_example",
                                            password=True,
                                            indexed=True,
                                        ),
                                    ),
                                ],
                                properties_with_variables=[
                                    None,
                                ],
                            ),
                        ],
                        attachments=[
                            Attachment(
                                id="id_example",
                                type="type_example",
                                file={},
                                content_type="content_type_example",
                                export_filename="export_filename_example",
                                file_uri="file_uri_example",
                                placeholders=[
                                    "placeholders_example",
                                ],
                                text_file_names_regex="text_file_names_regex_example",
                                exclude_file_names_regex="exclude_file_names_regex_example",
                                file_encodings={
                                    "key": "key_example",
                                },
                                checksum="checksum_example",
                            ),
                        ],
                        status=TaskStatus("PLANNED"),
                        team="team_example",
                        watchers=[
                            "watchers_example",
                        ],
                        wait_for_scheduled_start_date=True,
                        delay_during_blackout=True,
                        postponed_due_to_blackout=True,
                        postponed_until_environments_are_reserved=True,
                        original_scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        has_been_flagged=True,
                        has_been_delayed=True,
                        precondition="precondition_example",
                        failure_handler="failure_handler_example",
                        task_failure_handler_enabled=True,
                        task_recover_op=TaskRecoverOp("SKIP_TASK"),
                        failures_count=1,
                        execution_id="execution_id_example",
                        variable_mapping={
                            "key": "key_example",
                        },
                        external_variable_mapping={
                            "key": "key_example",
                        },
                        max_comment_size=1,
                        tags=[
                            "tags_example",
                        ],
                        configuration_uri="configuration_uri_example",
                        due_soon_notified=True,
                        locked=True,
                        check_attributes=True,
                        abort_script="abort_script_example",
                        phase=Phase(
                            id="id_example",
                            type="type_example",
                            locked=True,
                            title="title_example",
                            description="description_example",
                            owner="owner_example",
                            scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            planned_duration=1,
                            flag_status=FlagStatus("OK"),
                            flag_comment="flag_comment_example",
                            overdue_notified=True,
                            flagged=True,
                            start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            overdue=True,
                            or_calculate_due_date="or_calculate_due_date_example",
                            computed_planned_duration={},
                            actual_duration={},
                            release_uid=1,
                            tasks=[],
                            release=None,
                            status=PhaseStatus("PLANNED"),
                            color="color_example",
                            origin_id="origin_id_example",
                            current_task=Task(),
                            display_path="display_path_example",
                            active=True,
                            done=True,
                            defunct=True,
                            updatable=True,
                            aborted=True,
                            planned=True,
                            failed=True,
                            failing=True,
                            release_owner="release_owner_example",
                            all_gates=[],
                            all_tasks=[],
                            children=[
                                PlanItem(
                                    id="id_example",
                                    type="type_example",
                                    title="title_example",
                                    description="description_example",
                                    owner="owner_example",
                                    scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    planned_duration=1,
                                    flag_status=FlagStatus("OK"),
                                    flag_comment="flag_comment_example",
                                    overdue_notified=True,
                                    flagged=True,
                                    start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    children=[],
                                    overdue=True,
                                    done=True,
                                    release=Release(),
                                    release_uid=1,
                                    updatable=True,
                                    display_path="display_path_example",
                                    aborted=True,
                                    active=True,
                                    variable_usages=[
                                        UsagePoint(
                                            target_property=CiProperty(
                                                wrapped=CiProperty(),
                                                last_property=ModelProperty(
                                                    indexed_property_pattern="indexed_property_pattern_example",
                                                    property_name="property_name_example",
                                                    index=1,
                                                    indexed=True,
                                                ),
                                                parent={},
                                                exists=True,
                                                property_name="property_name_example",
                                                value={},
                                                parent_ci={},
                                                descriptor={},
                                                kind={},
                                                category="category_example",
                                                password=True,
                                                indexed=True,
                                            ),
                                        ),
                                    ],
                                    or_calculate_due_date="or_calculate_due_date_example",
                                    computed_planned_duration={},
                                    actual_duration={},
                                ),
                            ],
                            variable_usages=[
                                UsagePoint(
                                    target_property=CiProperty(
                                        wrapped=CiProperty(),
                                        last_property=ModelProperty(
                                            indexed_property_pattern="indexed_property_pattern_example",
                                            property_name="property_name_example",
                                            index=1,
                                            indexed=True,
                                        ),
                                        parent={},
                                        exists=True,
                                        property_name="property_name_example",
                                        value={},
                                        parent_ci={},
                                        descriptor={},
                                        kind={},
                                        category="category_example",
                                        password=True,
                                        indexed=True,
                                    ),
                                ),
                            ],
                            original=True,
                            phase_copied=True,
                            ancestor_id="ancestor_id_example",
                            latest_copy=True,
                        ),
                        blackout_metadata=BlackoutMetadata(
                            periods=[
                                BlackoutPeriod(
                                    start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                ),
                            ],
                        ),
                        flagged_count=1,
                        delayed_count=1,
                        done=True,
                        done_in_advance=True,
                        defunct=True,
                        updatable=True,
                        aborted=True,
                        not_yet_reached=True,
                        planned=True,
                        active=True,
                        in_progress=True,
                        pending=True,
                        waiting_for_input=True,
                        failed=True,
                        failing=True,
                        completed_in_advance=True,
                        skipped=True,
                        skipped_in_advance=True,
                        precondition_in_progress=True,
                        failure_handler_in_progress=True,
                        abort_script_in_progress=True,
                        facet_in_progress=True,
                        movable=True,
                        gate=True,
                        task_group=True,
                        parallel_group=True,
                        precondition_enabled=True,
                        failure_handler_enabled=True,
                        release=Release(),
                        display_path="display_path_example",
                        release_owner="release_owner_example",
                        all_tasks=[],
                        children=[
                            PlanItem(
                                id="id_example",
                                type="type_example",
                                title="title_example",
                                description="description_example",
                                owner="owner_example",
                                scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                planned_duration=1,
                                flag_status=FlagStatus("OK"),
                                flag_comment="flag_comment_example",
                                overdue_notified=True,
                                flagged=True,
                                start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                children=[],
                                overdue=True,
                                done=True,
                                release=Release(),
                                release_uid=1,
                                updatable=True,
                                display_path="display_path_example",
                                aborted=True,
                                active=True,
                                variable_usages=[
                                    UsagePoint(
                                        target_property=CiProperty(
                                            wrapped=CiProperty(),
                                            last_property=ModelProperty(
                                                indexed_property_pattern="indexed_property_pattern_example",
                                                property_name="property_name_example",
                                                index=1,
                                                indexed=True,
                                            ),
                                            parent={},
                                            exists=True,
                                            property_name="property_name_example",
                                            value={},
                                            parent_ci={},
                                            descriptor={},
                                            kind={},
                                            category="category_example",
                                            password=True,
                                            indexed=True,
                                        ),
                                    ),
                                ],
                                or_calculate_due_date="or_calculate_due_date_example",
                                computed_planned_duration={},
                                actual_duration={},
                            ),
                        ],
                        variable_usages=[
                            UsagePoint(
                                target_property=CiProperty(
                                    wrapped=CiProperty(),
                                    last_property=ModelProperty(
                                        indexed_property_pattern="indexed_property_pattern_example",
                                        property_name="property_name_example",
                                        index=1,
                                        indexed=True,
                                    ),
                                    parent={},
                                    exists=True,
                                    property_name="property_name_example",
                                    value={},
                                    parent_ci={},
                                    descriptor={},
                                    kind={},
                                    category="category_example",
                                    password=True,
                                    indexed=True,
                                ),
                            ),
                        ],
                        input_variables=[
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
                        referenced_variables=[
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
                        unbound_required_variables=[
                            "unbound_required_variables_example",
                        ],
                        automated=True,
                        task_type={},
                        due_soon=True,
                        elapsed_duration_fraction=3.14,
                        url="url_example",
                    ),
                ],
                children=[
                    PlanItem(
                        id="id_example",
                        type="type_example",
                        title="title_example",
                        description="description_example",
                        owner="owner_example",
                        scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        planned_duration=1,
                        flag_status=FlagStatus("OK"),
                        flag_comment="flag_comment_example",
                        overdue_notified=True,
                        flagged=True,
                        start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        children=[],
                        overdue=True,
                        done=True,
                        release=Release(),
                        release_uid=1,
                        updatable=True,
                        display_path="display_path_example",
                        aborted=True,
                        active=True,
                        variable_usages=[
                            UsagePoint(
                                target_property=CiProperty(
                                    wrapped=CiProperty(),
                                    last_property=ModelProperty(
                                        indexed_property_pattern="indexed_property_pattern_example",
                                        property_name="property_name_example",
                                        index=1,
                                        indexed=True,
                                    ),
                                    parent={},
                                    exists=True,
                                    property_name="property_name_example",
                                    value={},
                                    parent_ci={},
                                    descriptor={},
                                    kind={},
                                    category="category_example",
                                    password=True,
                                    indexed=True,
                                ),
                            ),
                        ],
                        or_calculate_due_date="or_calculate_due_date_example",
                        computed_planned_duration={},
                        actual_duration={},
                    ),
                ],
                input_variables=[
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
                referenced_variables=[
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
                unbound_required_variables=[
                    "unbound_required_variables_example",
                ],
                automated=True,
                task_type={},
                due_soon=True,
                elapsed_duration_fraction=3.14,
                url="url_example",
                conditions=[
                    GateCondition(
                        id="id_example",
                        type="type_example",
                        title="title_example",
                        checked=True,
                    ),
                ],
                dependencies=[
                    Dependency(
                        id="id_example",
                        type="type_example",
                        gate_task=GateTask(),
                        target=PlanItem(
                            id="id_example",
                            type="type_example",
                            title="title_example",
                            description="description_example",
                            owner="owner_example",
                            scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            planned_duration=1,
                            flag_status=FlagStatus("OK"),
                            flag_comment="flag_comment_example",
                            overdue_notified=True,
                            flagged=True,
                            start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            children=[
                                PlanItem(),
                            ],
                            overdue=True,
                            done=True,
                            release=Release(),
                            release_uid=1,
                            updatable=True,
                            display_path="display_path_example",
                            aborted=True,
                            active=True,
                            variable_usages=[
                                UsagePoint(
                                    target_property=CiProperty(
                                        wrapped=CiProperty(),
                                        last_property=ModelProperty(
                                            indexed_property_pattern="indexed_property_pattern_example",
                                            property_name="property_name_example",
                                            index=1,
                                            indexed=True,
                                        ),
                                        parent={},
                                        exists=True,
                                        property_name="property_name_example",
                                        value={},
                                        parent_ci={},
                                        descriptor={},
                                        kind={},
                                        category="category_example",
                                        password=True,
                                        indexed=True,
                                    ),
                                ),
                            ],
                            or_calculate_due_date="or_calculate_due_date_example",
                            computed_planned_duration={},
                            actual_duration={},
                        ),
                        target_id="target_id_example",
                        archived_target_title="archived_target_title_example",
                        archived_target_id="archived_target_id_example",
                        archived_as_resolved=True,
                        metadata={
                            "key": {},
                        },
                        archived=True,
                        done=True,
                        aborted=True,
                        target_display_path="target_display_path_example",
                        target_title="target_title_example",
                        valid_allowed_plan_item_id=True,
                    ),
                ],
                open=True,
                open_in_advance=True,
                completable=True,
                aborted_dependency_titles="aborted_dependency_titles_example",
                variable_usages=[
                    UsagePoint(
                        target_property=CiProperty(
                            wrapped=CiProperty(),
                            last_property=ModelProperty(
                                indexed_property_pattern="indexed_property_pattern_example",
                                property_name="property_name_example",
                                index=1,
                                indexed=True,
                            ),
                            parent={},
                            exists=True,
                            property_name="property_name_example",
                            value={},
                            parent_ci={},
                            descriptor={},
                            kind={},
                            category="category_example",
                            password=True,
                            indexed=True,
                        ),
                    ),
                ],
            ),
        ],
        all_user_input_tasks=[
            UserInputTask(
                id="id_example",
                type="type_example",
                scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                flag_status=FlagStatus("OK"),
                title="title_example",
                description="description_example",
                owner="owner_example",
                due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                planned_duration=1,
                flag_comment="flag_comment_example",
                overdue_notified=True,
                flagged=True,
                start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                overdue=True,
                or_calculate_due_date="or_calculate_due_date_example",
                computed_planned_duration={},
                actual_duration={},
                release_uid=1,
                ci_uid=1,
                comments=[
                    Comment(
                        id="id_example",
                        type="type_example",
                        text="text_example",
                        author="author_example",
                        date=dateutil_parser('2023-03-20T02:07:00Z'),
                        creation_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    ),
                ],
                container=TaskContainer(
                    id="id_example",
                    type="type_example",
                    tasks=[
                        Task(
                            id="id_example",
                            type="type_example",
                            scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            flag_status=FlagStatus("OK"),
                            title="title_example",
                            description="description_example",
                            owner="owner_example",
                            due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            planned_duration=1,
                            flag_comment="flag_comment_example",
                            overdue_notified=True,
                            flagged=True,
                            start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            overdue=True,
                            or_calculate_due_date="or_calculate_due_date_example",
                            computed_planned_duration={},
                            actual_duration={},
                            release_uid=1,
                            ci_uid=1,
                            comments=[
                                Comment(
                                    id="id_example",
                                    type="type_example",
                                    text="text_example",
                                    author="author_example",
                                    date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    creation_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                ),
                            ],
                            container=None,
                            facets=[
                                Facet(
                                    id="id_example",
                                    type="type_example",
                                    scope=FacetScope("TASK"),
                                    target_id="target_id_example",
                                    configuration_uri="configuration_uri_example",
                                    variable_mapping={
                                        "key": "key_example",
                                    },
                                    variable_usages=[
                                        UsagePoint(
                                            target_property=CiProperty(
                                                wrapped=CiProperty(),
                                                last_property=ModelProperty(
                                                    indexed_property_pattern="indexed_property_pattern_example",
                                                    property_name="property_name_example",
                                                    index=1,
                                                    indexed=True,
                                                ),
                                                parent={},
                                                exists=True,
                                                property_name="property_name_example",
                                                value={},
                                                parent_ci={},
                                                descriptor={},
                                                kind={},
                                                category="category_example",
                                                password=True,
                                                indexed=True,
                                            ),
                                        ),
                                    ],
                                    properties_with_variables=[
                                        None,
                                    ],
                                ),
                            ],
                            attachments=[
                                Attachment(
                                    id="id_example",
                                    type="type_example",
                                    file={},
                                    content_type="content_type_example",
                                    export_filename="export_filename_example",
                                    file_uri="file_uri_example",
                                    placeholders=[
                                        "placeholders_example",
                                    ],
                                    text_file_names_regex="text_file_names_regex_example",
                                    exclude_file_names_regex="exclude_file_names_regex_example",
                                    file_encodings={
                                        "key": "key_example",
                                    },
                                    checksum="checksum_example",
                                ),
                            ],
                            status=TaskStatus("PLANNED"),
                            team="team_example",
                            watchers=[
                                "watchers_example",
                            ],
                            wait_for_scheduled_start_date=True,
                            delay_during_blackout=True,
                            postponed_due_to_blackout=True,
                            postponed_until_environments_are_reserved=True,
                            original_scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            has_been_flagged=True,
                            has_been_delayed=True,
                            precondition="precondition_example",
                            failure_handler="failure_handler_example",
                            task_failure_handler_enabled=True,
                            task_recover_op=TaskRecoverOp("SKIP_TASK"),
                            failures_count=1,
                            execution_id="execution_id_example",
                            variable_mapping={
                                "key": "key_example",
                            },
                            external_variable_mapping={
                                "key": "key_example",
                            },
                            max_comment_size=1,
                            tags=[
                                "tags_example",
                            ],
                            configuration_uri="configuration_uri_example",
                            due_soon_notified=True,
                            locked=True,
                            check_attributes=True,
                            abort_script="abort_script_example",
                            phase=Phase(
                                id="id_example",
                                type="type_example",
                                locked=True,
                                title="title_example",
                                description="description_example",
                                owner="owner_example",
                                scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                planned_duration=1,
                                flag_status=FlagStatus("OK"),
                                flag_comment="flag_comment_example",
                                overdue_notified=True,
                                flagged=True,
                                start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                overdue=True,
                                or_calculate_due_date="or_calculate_due_date_example",
                                computed_planned_duration={},
                                actual_duration={},
                                release_uid=1,
                                tasks=[],
                                release=None,
                                status=PhaseStatus("PLANNED"),
                                color="color_example",
                                origin_id="origin_id_example",
                                current_task=Task(),
                                display_path="display_path_example",
                                active=True,
                                done=True,
                                defunct=True,
                                updatable=True,
                                aborted=True,
                                planned=True,
                                failed=True,
                                failing=True,
                                release_owner="release_owner_example",
                                all_gates=[
                                    GateTask(
                                        id="id_example",
                                        type="type_example",
                                        scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        flag_status=FlagStatus("OK"),
                                        title="title_example",
                                        description="description_example",
                                        owner="owner_example",
                                        due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        planned_duration=1,
                                        flag_comment="flag_comment_example",
                                        overdue_notified=True,
                                        flagged=True,
                                        start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        overdue=True,
                                        or_calculate_due_date="or_calculate_due_date_example",
                                        computed_planned_duration={},
                                        actual_duration={},
                                        release_uid=1,
                                        ci_uid=1,
                                        comments=[
                                            Comment(
                                                id="id_example",
                                                type="type_example",
                                                text="text_example",
                                                author="author_example",
                                                date=dateutil_parser('2023-03-20T02:07:00Z'),
                                                creation_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                            ),
                                        ],
                                        container=TaskContainer(),
                                        facets=[
                                            Facet(
                                                id="id_example",
                                                type="type_example",
                                                scope=FacetScope("TASK"),
                                                target_id="target_id_example",
                                                configuration_uri="configuration_uri_example",
                                                variable_mapping={
                                                    "key": "key_example",
                                                },
                                                variable_usages=[
                                                    UsagePoint(
                                                        target_property=CiProperty(
                                                            wrapped=CiProperty(),
                                                            last_property=ModelProperty(
                                                                indexed_property_pattern="indexed_property_pattern_example",
                                                                property_name="property_name_example",
                                                                index=1,
                                                                indexed=True,
                                                            ),
                                                            parent={},
                                                            exists=True,
                                                            property_name="property_name_example",
                                                            value={},
                                                            parent_ci={},
                                                            descriptor={},
                                                            kind={},
                                                            category="category_example",
                                                            password=True,
                                                            indexed=True,
                                                        ),
                                                    ),
                                                ],
                                                properties_with_variables=[
                                                    None,
                                                ],
                                            ),
                                        ],
                                        attachments=[
                                            Attachment(
                                                id="id_example",
                                                type="type_example",
                                                file={},
                                                content_type="content_type_example",
                                                export_filename="export_filename_example",
                                                file_uri="file_uri_example",
                                                placeholders=[
                                                    "placeholders_example",
                                                ],
                                                text_file_names_regex="text_file_names_regex_example",
                                                exclude_file_names_regex="exclude_file_names_regex_example",
                                                file_encodings={
                                                    "key": "key_example",
                                                },
                                                checksum="checksum_example",
                                            ),
                                        ],
                                        status=TaskStatus("PLANNED"),
                                        team="team_example",
                                        watchers=[
                                            "watchers_example",
                                        ],
                                        wait_for_scheduled_start_date=True,
                                        delay_during_blackout=True,
                                        postponed_due_to_blackout=True,
                                        postponed_until_environments_are_reserved=True,
                                        original_scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        has_been_flagged=True,
                                        has_been_delayed=True,
                                        precondition="precondition_example",
                                        failure_handler="failure_handler_example",
                                        task_failure_handler_enabled=True,
                                        task_recover_op=TaskRecoverOp("SKIP_TASK"),
                                        failures_count=1,
                                        execution_id="execution_id_example",
                                        variable_mapping={
                                            "key": "key_example",
                                        },
                                        external_variable_mapping={
                                            "key": "key_example",
                                        },
                                        max_comment_size=1,
                                        tags=[
                                            "tags_example",
                                        ],
                                        configuration_uri="configuration_uri_example",
                                        due_soon_notified=True,
                                        locked=True,
                                        check_attributes=True,
                                        abort_script="abort_script_example",
                                        phase=Phase(),
                                        blackout_metadata=BlackoutMetadata(
                                            periods=[
                                                BlackoutPeriod(
                                                    start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                                    end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                                ),
                                            ],
                                        ),
                                        flagged_count=1,
                                        delayed_count=1,
                                        done=True,
                                        done_in_advance=True,
                                        defunct=True,
                                        updatable=True,
                                        aborted=True,
                                        not_yet_reached=True,
                                        planned=True,
                                        active=True,
                                        in_progress=True,
                                        pending=True,
                                        waiting_for_input=True,
                                        failed=True,
                                        failing=True,
                                        completed_in_advance=True,
                                        skipped=True,
                                        skipped_in_advance=True,
                                        precondition_in_progress=True,
                                        failure_handler_in_progress=True,
                                        abort_script_in_progress=True,
                                        facet_in_progress=True,
                                        movable=True,
                                        gate=True,
                                        task_group=True,
                                        parallel_group=True,
                                        precondition_enabled=True,
                                        failure_handler_enabled=True,
                                        release=Release(),
                                        display_path="display_path_example",
                                        release_owner="release_owner_example",
                                        all_tasks=[],
                                        children=[
                                            PlanItem(
                                                id="id_example",
                                                type="type_example",
                                                title="title_example",
                                                description="description_example",
                                                owner="owner_example",
                                                scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                                due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                                start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                                end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                                planned_duration=1,
                                                flag_status=FlagStatus("OK"),
                                                flag_comment="flag_comment_example",
                                                overdue_notified=True,
                                                flagged=True,
                                                start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                                end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                                children=[],
                                                overdue=True,
                                                done=True,
                                                release=Release(),
                                                release_uid=1,
                                                updatable=True,
                                                display_path="display_path_example",
                                                aborted=True,
                                                active=True,
                                                variable_usages=[
                                                    UsagePoint(
                                                        target_property=CiProperty(
                                                            wrapped=CiProperty(),
                                                            last_property=ModelProperty(
                                                                indexed_property_pattern="indexed_property_pattern_example",
                                                                property_name="property_name_example",
                                                                index=1,
                                                                indexed=True,
                                                            ),
                                                            parent={},
                                                            exists=True,
                                                            property_name="property_name_example",
                                                            value={},
                                                            parent_ci={},
                                                            descriptor={},
                                                            kind={},
                                                            category="category_example",
                                                            password=True,
                                                            indexed=True,
                                                        ),
                                                    ),
                                                ],
                                                or_calculate_due_date="or_calculate_due_date_example",
                                                computed_planned_duration={},
                                                actual_duration={},
                                            ),
                                        ],
                                        input_variables=[
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
                                        referenced_variables=[
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
                                        unbound_required_variables=[
                                            "unbound_required_variables_example",
                                        ],
                                        automated=True,
                                        task_type={},
                                        due_soon=True,
                                        elapsed_duration_fraction=3.14,
                                        url="url_example",
                                        conditions=[
                                            GateCondition(
                                                id="id_example",
                                                type="type_example",
                                                title="title_example",
                                                checked=True,
                                            ),
                                        ],
                                        dependencies=[
                                            Dependency(
                                                id="id_example",
                                                type="type_example",
                                                gate_task=GateTask(),
                                                target=PlanItem(
                                                    id="id_example",
                                                    type="type_example",
                                                    title="title_example",
                                                    description="description_example",
                                                    owner="owner_example",
                                                    scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                                    due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                                    start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                                    end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                                    planned_duration=1,
                                                    flag_status=FlagStatus("OK"),
                                                    flag_comment="flag_comment_example",
                                                    overdue_notified=True,
                                                    flagged=True,
                                                    start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                                    end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                                    children=[
                                                        PlanItem(),
                                                    ],
                                                    overdue=True,
                                                    done=True,
                                                    release=Release(),
                                                    release_uid=1,
                                                    updatable=True,
                                                    display_path="display_path_example",
                                                    aborted=True,
                                                    active=True,
                                                    variable_usages=[
                                                        UsagePoint(
                                                            target_property=CiProperty(
                                                                wrapped=CiProperty(),
                                                                last_property=ModelProperty(
                                                                    indexed_property_pattern="indexed_property_pattern_example",
                                                                    property_name="property_name_example",
                                                                    index=1,
                                                                    indexed=True,
                                                                ),
                                                                parent={},
                                                                exists=True,
                                                                property_name="property_name_example",
                                                                value={},
                                                                parent_ci={},
                                                                descriptor={},
                                                                kind={},
                                                                category="category_example",
                                                                password=True,
                                                                indexed=True,
                                                            ),
                                                        ),
                                                    ],
                                                    or_calculate_due_date="or_calculate_due_date_example",
                                                    computed_planned_duration={},
                                                    actual_duration={},
                                                ),
                                                target_id="target_id_example",
                                                archived_target_title="archived_target_title_example",
                                                archived_target_id="archived_target_id_example",
                                                archived_as_resolved=True,
                                                metadata={
                                                    "key": {},
                                                },
                                                archived=True,
                                                done=True,
                                                aborted=True,
                                                target_display_path="target_display_path_example",
                                                target_title="target_title_example",
                                                valid_allowed_plan_item_id=True,
                                            ),
                                        ],
                                        open=True,
                                        open_in_advance=True,
                                        completable=True,
                                        aborted_dependency_titles="aborted_dependency_titles_example",
                                        variable_usages=[
                                            UsagePoint(
                                                target_property=CiProperty(
                                                    wrapped=CiProperty(),
                                                    last_property=ModelProperty(
                                                        indexed_property_pattern="indexed_property_pattern_example",
                                                        property_name="property_name_example",
                                                        index=1,
                                                        indexed=True,
                                                    ),
                                                    parent={},
                                                    exists=True,
                                                    property_name="property_name_example",
                                                    value={},
                                                    parent_ci={},
                                                    descriptor={},
                                                    kind={},
                                                    category="category_example",
                                                    password=True,
                                                    indexed=True,
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                all_tasks=[],
                                children=[
                                    PlanItem(
                                        id="id_example",
                                        type="type_example",
                                        title="title_example",
                                        description="description_example",
                                        owner="owner_example",
                                        scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        planned_duration=1,
                                        flag_status=FlagStatus("OK"),
                                        flag_comment="flag_comment_example",
                                        overdue_notified=True,
                                        flagged=True,
                                        start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        children=[],
                                        overdue=True,
                                        done=True,
                                        release=Release(),
                                        release_uid=1,
                                        updatable=True,
                                        display_path="display_path_example",
                                        aborted=True,
                                        active=True,
                                        variable_usages=[
                                            UsagePoint(
                                                target_property=CiProperty(
                                                    wrapped=CiProperty(),
                                                    last_property=ModelProperty(
                                                        indexed_property_pattern="indexed_property_pattern_example",
                                                        property_name="property_name_example",
                                                        index=1,
                                                        indexed=True,
                                                    ),
                                                    parent={},
                                                    exists=True,
                                                    property_name="property_name_example",
                                                    value={},
                                                    parent_ci={},
                                                    descriptor={},
                                                    kind={},
                                                    category="category_example",
                                                    password=True,
                                                    indexed=True,
                                                ),
                                            ),
                                        ],
                                        or_calculate_due_date="or_calculate_due_date_example",
                                        computed_planned_duration={},
                                        actual_duration={},
                                    ),
                                ],
                                variable_usages=[
                                    UsagePoint(
                                        target_property=CiProperty(
                                            wrapped=CiProperty(),
                                            last_property=ModelProperty(
                                                indexed_property_pattern="indexed_property_pattern_example",
                                                property_name="property_name_example",
                                                index=1,
                                                indexed=True,
                                            ),
                                            parent={},
                                            exists=True,
                                            property_name="property_name_example",
                                            value={},
                                            parent_ci={},
                                            descriptor={},
                                            kind={},
                                            category="category_example",
                                            password=True,
                                            indexed=True,
                                        ),
                                    ),
                                ],
                                original=True,
                                phase_copied=True,
                                ancestor_id="ancestor_id_example",
                                latest_copy=True,
                            ),
                            blackout_metadata=BlackoutMetadata(
                                periods=[
                                    BlackoutPeriod(
                                        start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    ),
                                ],
                            ),
                            flagged_count=1,
                            delayed_count=1,
                            done=True,
                            done_in_advance=True,
                            defunct=True,
                            updatable=True,
                            aborted=True,
                            not_yet_reached=True,
                            planned=True,
                            active=True,
                            in_progress=True,
                            pending=True,
                            waiting_for_input=True,
                            failed=True,
                            failing=True,
                            completed_in_advance=True,
                            skipped=True,
                            skipped_in_advance=True,
                            precondition_in_progress=True,
                            failure_handler_in_progress=True,
                            abort_script_in_progress=True,
                            facet_in_progress=True,
                            movable=True,
                            gate=True,
                            task_group=True,
                            parallel_group=True,
                            precondition_enabled=True,
                            failure_handler_enabled=True,
                            release=Release(),
                            display_path="display_path_example",
                            release_owner="release_owner_example",
                            all_tasks=[],
                            children=[
                                PlanItem(
                                    id="id_example",
                                    type="type_example",
                                    title="title_example",
                                    description="description_example",
                                    owner="owner_example",
                                    scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    planned_duration=1,
                                    flag_status=FlagStatus("OK"),
                                    flag_comment="flag_comment_example",
                                    overdue_notified=True,
                                    flagged=True,
                                    start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    children=[],
                                    overdue=True,
                                    done=True,
                                    release=Release(),
                                    release_uid=1,
                                    updatable=True,
                                    display_path="display_path_example",
                                    aborted=True,
                                    active=True,
                                    variable_usages=[
                                        UsagePoint(
                                            target_property=CiProperty(
                                                wrapped=CiProperty(),
                                                last_property=ModelProperty(
                                                    indexed_property_pattern="indexed_property_pattern_example",
                                                    property_name="property_name_example",
                                                    index=1,
                                                    indexed=True,
                                                ),
                                                parent={},
                                                exists=True,
                                                property_name="property_name_example",
                                                value={},
                                                parent_ci={},
                                                descriptor={},
                                                kind={},
                                                category="category_example",
                                                password=True,
                                                indexed=True,
                                            ),
                                        ),
                                    ],
                                    or_calculate_due_date="or_calculate_due_date_example",
                                    computed_planned_duration={},
                                    actual_duration={},
                                ),
                            ],
                            variable_usages=[
                                UsagePoint(
                                    target_property=CiProperty(
                                        wrapped=CiProperty(),
                                        last_property=ModelProperty(
                                            indexed_property_pattern="indexed_property_pattern_example",
                                            property_name="property_name_example",
                                            index=1,
                                            indexed=True,
                                        ),
                                        parent={},
                                        exists=True,
                                        property_name="property_name_example",
                                        value={},
                                        parent_ci={},
                                        descriptor={},
                                        kind={},
                                        category="category_example",
                                        password=True,
                                        indexed=True,
                                    ),
                                ),
                            ],
                            input_variables=[
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
                            referenced_variables=[
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
                            unbound_required_variables=[
                                "unbound_required_variables_example",
                            ],
                            automated=True,
                            task_type={},
                            due_soon=True,
                            elapsed_duration_fraction=3.14,
                            url="url_example",
                        ),
                    ],
                    locked=True,
                    title="title_example",
                ),
                facets=[
                    Facet(
                        id="id_example",
                        type="type_example",
                        scope=FacetScope("TASK"),
                        target_id="target_id_example",
                        configuration_uri="configuration_uri_example",
                        variable_mapping={
                            "key": "key_example",
                        },
                        variable_usages=[
                            UsagePoint(
                                target_property=CiProperty(
                                    wrapped=CiProperty(),
                                    last_property=ModelProperty(
                                        indexed_property_pattern="indexed_property_pattern_example",
                                        property_name="property_name_example",
                                        index=1,
                                        indexed=True,
                                    ),
                                    parent={},
                                    exists=True,
                                    property_name="property_name_example",
                                    value={},
                                    parent_ci={},
                                    descriptor={},
                                    kind={},
                                    category="category_example",
                                    password=True,
                                    indexed=True,
                                ),
                            ),
                        ],
                        properties_with_variables=[
                            None,
                        ],
                    ),
                ],
                attachments=[
                    Attachment(
                        id="id_example",
                        type="type_example",
                        file={},
                        content_type="content_type_example",
                        export_filename="export_filename_example",
                        file_uri="file_uri_example",
                        placeholders=[
                            "placeholders_example",
                        ],
                        text_file_names_regex="text_file_names_regex_example",
                        exclude_file_names_regex="exclude_file_names_regex_example",
                        file_encodings={
                            "key": "key_example",
                        },
                        checksum="checksum_example",
                    ),
                ],
                status=TaskStatus("PLANNED"),
                team="team_example",
                watchers=[
                    "watchers_example",
                ],
                wait_for_scheduled_start_date=True,
                delay_during_blackout=True,
                postponed_due_to_blackout=True,
                postponed_until_environments_are_reserved=True,
                original_scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                has_been_flagged=True,
                has_been_delayed=True,
                precondition="precondition_example",
                failure_handler="failure_handler_example",
                task_failure_handler_enabled=True,
                task_recover_op=TaskRecoverOp("SKIP_TASK"),
                failures_count=1,
                execution_id="execution_id_example",
                variable_mapping={
                    "key": "key_example",
                },
                external_variable_mapping={
                    "key": "key_example",
                },
                max_comment_size=1,
                tags=[
                    "tags_example",
                ],
                configuration_uri="configuration_uri_example",
                due_soon_notified=True,
                locked=True,
                check_attributes=True,
                abort_script="abort_script_example",
                phase=Phase(
                    id="id_example",
                    type="type_example",
                    locked=True,
                    title="title_example",
                    description="description_example",
                    owner="owner_example",
                    scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    planned_duration=1,
                    flag_status=FlagStatus("OK"),
                    flag_comment="flag_comment_example",
                    overdue_notified=True,
                    flagged=True,
                    start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    overdue=True,
                    or_calculate_due_date="or_calculate_due_date_example",
                    computed_planned_duration={},
                    actual_duration={},
                    release_uid=1,
                    tasks=[
                        Task(
                            id="id_example",
                            type="type_example",
                            scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            flag_status=FlagStatus("OK"),
                            title="title_example",
                            description="description_example",
                            owner="owner_example",
                            due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            planned_duration=1,
                            flag_comment="flag_comment_example",
                            overdue_notified=True,
                            flagged=True,
                            start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            overdue=True,
                            or_calculate_due_date="or_calculate_due_date_example",
                            computed_planned_duration={},
                            actual_duration={},
                            release_uid=1,
                            ci_uid=1,
                            comments=[
                                Comment(
                                    id="id_example",
                                    type="type_example",
                                    text="text_example",
                                    author="author_example",
                                    date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    creation_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                ),
                            ],
                            container=None,
                            facets=[
                                Facet(
                                    id="id_example",
                                    type="type_example",
                                    scope=FacetScope("TASK"),
                                    target_id="target_id_example",
                                    configuration_uri="configuration_uri_example",
                                    variable_mapping={
                                        "key": "key_example",
                                    },
                                    variable_usages=[
                                        UsagePoint(
                                            target_property=CiProperty(
                                                wrapped=CiProperty(),
                                                last_property=ModelProperty(
                                                    indexed_property_pattern="indexed_property_pattern_example",
                                                    property_name="property_name_example",
                                                    index=1,
                                                    indexed=True,
                                                ),
                                                parent={},
                                                exists=True,
                                                property_name="property_name_example",
                                                value={},
                                                parent_ci={},
                                                descriptor={},
                                                kind={},
                                                category="category_example",
                                                password=True,
                                                indexed=True,
                                            ),
                                        ),
                                    ],
                                    properties_with_variables=[
                                        None,
                                    ],
                                ),
                            ],
                            attachments=[
                                Attachment(
                                    id="id_example",
                                    type="type_example",
                                    file={},
                                    content_type="content_type_example",
                                    export_filename="export_filename_example",
                                    file_uri="file_uri_example",
                                    placeholders=[
                                        "placeholders_example",
                                    ],
                                    text_file_names_regex="text_file_names_regex_example",
                                    exclude_file_names_regex="exclude_file_names_regex_example",
                                    file_encodings={
                                        "key": "key_example",
                                    },
                                    checksum="checksum_example",
                                ),
                            ],
                            status=TaskStatus("PLANNED"),
                            team="team_example",
                            watchers=[
                                "watchers_example",
                            ],
                            wait_for_scheduled_start_date=True,
                            delay_during_blackout=True,
                            postponed_due_to_blackout=True,
                            postponed_until_environments_are_reserved=True,
                            original_scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            has_been_flagged=True,
                            has_been_delayed=True,
                            precondition="precondition_example",
                            failure_handler="failure_handler_example",
                            task_failure_handler_enabled=True,
                            task_recover_op=TaskRecoverOp("SKIP_TASK"),
                            failures_count=1,
                            execution_id="execution_id_example",
                            variable_mapping={
                                "key": "key_example",
                            },
                            external_variable_mapping={
                                "key": "key_example",
                            },
                            max_comment_size=1,
                            tags=[
                                "tags_example",
                            ],
                            configuration_uri="configuration_uri_example",
                            due_soon_notified=True,
                            locked=True,
                            check_attributes=True,
                            abort_script="abort_script_example",
                            phase=Phase(),
                            blackout_metadata=BlackoutMetadata(
                                periods=[
                                    BlackoutPeriod(
                                        start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    ),
                                ],
                            ),
                            flagged_count=1,
                            delayed_count=1,
                            done=True,
                            done_in_advance=True,
                            defunct=True,
                            updatable=True,
                            aborted=True,
                            not_yet_reached=True,
                            planned=True,
                            active=True,
                            in_progress=True,
                            pending=True,
                            waiting_for_input=True,
                            failed=True,
                            failing=True,
                            completed_in_advance=True,
                            skipped=True,
                            skipped_in_advance=True,
                            precondition_in_progress=True,
                            failure_handler_in_progress=True,
                            abort_script_in_progress=True,
                            facet_in_progress=True,
                            movable=True,
                            gate=True,
                            task_group=True,
                            parallel_group=True,
                            precondition_enabled=True,
                            failure_handler_enabled=True,
                            release=Release(),
                            display_path="display_path_example",
                            release_owner="release_owner_example",
                            all_tasks=[],
                            children=[
                                PlanItem(
                                    id="id_example",
                                    type="type_example",
                                    title="title_example",
                                    description="description_example",
                                    owner="owner_example",
                                    scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    planned_duration=1,
                                    flag_status=FlagStatus("OK"),
                                    flag_comment="flag_comment_example",
                                    overdue_notified=True,
                                    flagged=True,
                                    start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    children=[],
                                    overdue=True,
                                    done=True,
                                    release=Release(),
                                    release_uid=1,
                                    updatable=True,
                                    display_path="display_path_example",
                                    aborted=True,
                                    active=True,
                                    variable_usages=[
                                        UsagePoint(
                                            target_property=CiProperty(
                                                wrapped=CiProperty(),
                                                last_property=ModelProperty(
                                                    indexed_property_pattern="indexed_property_pattern_example",
                                                    property_name="property_name_example",
                                                    index=1,
                                                    indexed=True,
                                                ),
                                                parent={},
                                                exists=True,
                                                property_name="property_name_example",
                                                value={},
                                                parent_ci={},
                                                descriptor={},
                                                kind={},
                                                category="category_example",
                                                password=True,
                                                indexed=True,
                                            ),
                                        ),
                                    ],
                                    or_calculate_due_date="or_calculate_due_date_example",
                                    computed_planned_duration={},
                                    actual_duration={},
                                ),
                            ],
                            variable_usages=[
                                UsagePoint(
                                    target_property=CiProperty(
                                        wrapped=CiProperty(),
                                        last_property=ModelProperty(
                                            indexed_property_pattern="indexed_property_pattern_example",
                                            property_name="property_name_example",
                                            index=1,
                                            indexed=True,
                                        ),
                                        parent={},
                                        exists=True,
                                        property_name="property_name_example",
                                        value={},
                                        parent_ci={},
                                        descriptor={},
                                        kind={},
                                        category="category_example",
                                        password=True,
                                        indexed=True,
                                    ),
                                ),
                            ],
                            input_variables=[
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
                            referenced_variables=[
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
                            unbound_required_variables=[
                                "unbound_required_variables_example",
                            ],
                            automated=True,
                            task_type={},
                            due_soon=True,
                            elapsed_duration_fraction=3.14,
                            url="url_example",
                        ),
                    ],
                    release=None,
                    status=PhaseStatus("PLANNED"),
                    color="color_example",
                    origin_id="origin_id_example",
                    current_task=Task(
                        id="id_example",
                        type="type_example",
                        scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        flag_status=FlagStatus("OK"),
                        title="title_example",
                        description="description_example",
                        owner="owner_example",
                        due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        planned_duration=1,
                        flag_comment="flag_comment_example",
                        overdue_notified=True,
                        flagged=True,
                        start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        overdue=True,
                        or_calculate_due_date="or_calculate_due_date_example",
                        computed_planned_duration={},
                        actual_duration={},
                        release_uid=1,
                        ci_uid=1,
                        comments=[
                            Comment(
                                id="id_example",
                                type="type_example",
                                text="text_example",
                                author="author_example",
                                date=dateutil_parser('2023-03-20T02:07:00Z'),
                                creation_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            ),
                        ],
                        container=None,
                        facets=[
                            Facet(
                                id="id_example",
                                type="type_example",
                                scope=FacetScope("TASK"),
                                target_id="target_id_example",
                                configuration_uri="configuration_uri_example",
                                variable_mapping={
                                    "key": "key_example",
                                },
                                variable_usages=[
                                    UsagePoint(
                                        target_property=CiProperty(
                                            wrapped=CiProperty(),
                                            last_property=ModelProperty(
                                                indexed_property_pattern="indexed_property_pattern_example",
                                                property_name="property_name_example",
                                                index=1,
                                                indexed=True,
                                            ),
                                            parent={},
                                            exists=True,
                                            property_name="property_name_example",
                                            value={},
                                            parent_ci={},
                                            descriptor={},
                                            kind={},
                                            category="category_example",
                                            password=True,
                                            indexed=True,
                                        ),
                                    ),
                                ],
                                properties_with_variables=[
                                    None,
                                ],
                            ),
                        ],
                        attachments=[
                            Attachment(
                                id="id_example",
                                type="type_example",
                                file={},
                                content_type="content_type_example",
                                export_filename="export_filename_example",
                                file_uri="file_uri_example",
                                placeholders=[
                                    "placeholders_example",
                                ],
                                text_file_names_regex="text_file_names_regex_example",
                                exclude_file_names_regex="exclude_file_names_regex_example",
                                file_encodings={
                                    "key": "key_example",
                                },
                                checksum="checksum_example",
                            ),
                        ],
                        status=TaskStatus("PLANNED"),
                        team="team_example",
                        watchers=[
                            "watchers_example",
                        ],
                        wait_for_scheduled_start_date=True,
                        delay_during_blackout=True,
                        postponed_due_to_blackout=True,
                        postponed_until_environments_are_reserved=True,
                        original_scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        has_been_flagged=True,
                        has_been_delayed=True,
                        precondition="precondition_example",
                        failure_handler="failure_handler_example",
                        task_failure_handler_enabled=True,
                        task_recover_op=TaskRecoverOp("SKIP_TASK"),
                        failures_count=1,
                        execution_id="execution_id_example",
                        variable_mapping={
                            "key": "key_example",
                        },
                        external_variable_mapping={
                            "key": "key_example",
                        },
                        max_comment_size=1,
                        tags=[
                            "tags_example",
                        ],
                        configuration_uri="configuration_uri_example",
                        due_soon_notified=True,
                        locked=True,
                        check_attributes=True,
                        abort_script="abort_script_example",
                        phase=Phase(),
                        blackout_metadata=BlackoutMetadata(
                            periods=[
                                BlackoutPeriod(
                                    start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                ),
                            ],
                        ),
                        flagged_count=1,
                        delayed_count=1,
                        done=True,
                        done_in_advance=True,
                        defunct=True,
                        updatable=True,
                        aborted=True,
                        not_yet_reached=True,
                        planned=True,
                        active=True,
                        in_progress=True,
                        pending=True,
                        waiting_for_input=True,
                        failed=True,
                        failing=True,
                        completed_in_advance=True,
                        skipped=True,
                        skipped_in_advance=True,
                        precondition_in_progress=True,
                        failure_handler_in_progress=True,
                        abort_script_in_progress=True,
                        facet_in_progress=True,
                        movable=True,
                        gate=True,
                        task_group=True,
                        parallel_group=True,
                        precondition_enabled=True,
                        failure_handler_enabled=True,
                        release=Release(),
                        display_path="display_path_example",
                        release_owner="release_owner_example",
                        all_tasks=[
                            Task(),
                        ],
                        children=[
                            PlanItem(
                                id="id_example",
                                type="type_example",
                                title="title_example",
                                description="description_example",
                                owner="owner_example",
                                scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                planned_duration=1,
                                flag_status=FlagStatus("OK"),
                                flag_comment="flag_comment_example",
                                overdue_notified=True,
                                flagged=True,
                                start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                children=[],
                                overdue=True,
                                done=True,
                                release=Release(),
                                release_uid=1,
                                updatable=True,
                                display_path="display_path_example",
                                aborted=True,
                                active=True,
                                variable_usages=[
                                    UsagePoint(
                                        target_property=CiProperty(
                                            wrapped=CiProperty(),
                                            last_property=ModelProperty(
                                                indexed_property_pattern="indexed_property_pattern_example",
                                                property_name="property_name_example",
                                                index=1,
                                                indexed=True,
                                            ),
                                            parent={},
                                            exists=True,
                                            property_name="property_name_example",
                                            value={},
                                            parent_ci={},
                                            descriptor={},
                                            kind={},
                                            category="category_example",
                                            password=True,
                                            indexed=True,
                                        ),
                                    ),
                                ],
                                or_calculate_due_date="or_calculate_due_date_example",
                                computed_planned_duration={},
                                actual_duration={},
                            ),
                        ],
                        variable_usages=[
                            UsagePoint(
                                target_property=CiProperty(
                                    wrapped=CiProperty(),
                                    last_property=ModelProperty(
                                        indexed_property_pattern="indexed_property_pattern_example",
                                        property_name="property_name_example",
                                        index=1,
                                        indexed=True,
                                    ),
                                    parent={},
                                    exists=True,
                                    property_name="property_name_example",
                                    value={},
                                    parent_ci={},
                                    descriptor={},
                                    kind={},
                                    category="category_example",
                                    password=True,
                                    indexed=True,
                                ),
                            ),
                        ],
                        input_variables=[
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
                        referenced_variables=[
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
                        unbound_required_variables=[
                            "unbound_required_variables_example",
                        ],
                        automated=True,
                        task_type={},
                        due_soon=True,
                        elapsed_duration_fraction=3.14,
                        url="url_example",
                    ),
                    display_path="display_path_example",
                    active=True,
                    done=True,
                    defunct=True,
                    updatable=True,
                    aborted=True,
                    planned=True,
                    failed=True,
                    failing=True,
                    release_owner="release_owner_example",
                    all_gates=[
                        GateTask(
                            id="id_example",
                            type="type_example",
                            scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            flag_status=FlagStatus("OK"),
                            title="title_example",
                            description="description_example",
                            owner="owner_example",
                            due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            planned_duration=1,
                            flag_comment="flag_comment_example",
                            overdue_notified=True,
                            flagged=True,
                            start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            overdue=True,
                            or_calculate_due_date="or_calculate_due_date_example",
                            computed_planned_duration={},
                            actual_duration={},
                            release_uid=1,
                            ci_uid=1,
                            comments=[
                                Comment(
                                    id="id_example",
                                    type="type_example",
                                    text="text_example",
                                    author="author_example",
                                    date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    creation_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                ),
                            ],
                            container=TaskContainer(
                                id="id_example",
                                type="type_example",
                                tasks=[
                                    Task(
                                        id="id_example",
                                        type="type_example",
                                        scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        flag_status=FlagStatus("OK"),
                                        title="title_example",
                                        description="description_example",
                                        owner="owner_example",
                                        due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        planned_duration=1,
                                        flag_comment="flag_comment_example",
                                        overdue_notified=True,
                                        flagged=True,
                                        start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        overdue=True,
                                        or_calculate_due_date="or_calculate_due_date_example",
                                        computed_planned_duration={},
                                        actual_duration={},
                                        release_uid=1,
                                        ci_uid=1,
                                        comments=[
                                            Comment(
                                                id="id_example",
                                                type="type_example",
                                                text="text_example",
                                                author="author_example",
                                                date=dateutil_parser('2023-03-20T02:07:00Z'),
                                                creation_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                            ),
                                        ],
                                        container=None,
                                        facets=[
                                            Facet(
                                                id="id_example",
                                                type="type_example",
                                                scope=FacetScope("TASK"),
                                                target_id="target_id_example",
                                                configuration_uri="configuration_uri_example",
                                                variable_mapping={
                                                    "key": "key_example",
                                                },
                                                variable_usages=[
                                                    UsagePoint(
                                                        target_property=CiProperty(
                                                            wrapped=CiProperty(),
                                                            last_property=ModelProperty(
                                                                indexed_property_pattern="indexed_property_pattern_example",
                                                                property_name="property_name_example",
                                                                index=1,
                                                                indexed=True,
                                                            ),
                                                            parent={},
                                                            exists=True,
                                                            property_name="property_name_example",
                                                            value={},
                                                            parent_ci={},
                                                            descriptor={},
                                                            kind={},
                                                            category="category_example",
                                                            password=True,
                                                            indexed=True,
                                                        ),
                                                    ),
                                                ],
                                                properties_with_variables=[
                                                    None,
                                                ],
                                            ),
                                        ],
                                        attachments=[
                                            Attachment(
                                                id="id_example",
                                                type="type_example",
                                                file={},
                                                content_type="content_type_example",
                                                export_filename="export_filename_example",
                                                file_uri="file_uri_example",
                                                placeholders=[
                                                    "placeholders_example",
                                                ],
                                                text_file_names_regex="text_file_names_regex_example",
                                                exclude_file_names_regex="exclude_file_names_regex_example",
                                                file_encodings={
                                                    "key": "key_example",
                                                },
                                                checksum="checksum_example",
                                            ),
                                        ],
                                        status=TaskStatus("PLANNED"),
                                        team="team_example",
                                        watchers=[
                                            "watchers_example",
                                        ],
                                        wait_for_scheduled_start_date=True,
                                        delay_during_blackout=True,
                                        postponed_due_to_blackout=True,
                                        postponed_until_environments_are_reserved=True,
                                        original_scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        has_been_flagged=True,
                                        has_been_delayed=True,
                                        precondition="precondition_example",
                                        failure_handler="failure_handler_example",
                                        task_failure_handler_enabled=True,
                                        task_recover_op=TaskRecoverOp("SKIP_TASK"),
                                        failures_count=1,
                                        execution_id="execution_id_example",
                                        variable_mapping={
                                            "key": "key_example",
                                        },
                                        external_variable_mapping={
                                            "key": "key_example",
                                        },
                                        max_comment_size=1,
                                        tags=[
                                            "tags_example",
                                        ],
                                        configuration_uri="configuration_uri_example",
                                        due_soon_notified=True,
                                        locked=True,
                                        check_attributes=True,
                                        abort_script="abort_script_example",
                                        phase=Phase(),
                                        blackout_metadata=BlackoutMetadata(
                                            periods=[
                                                BlackoutPeriod(
                                                    start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                                    end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                                ),
                                            ],
                                        ),
                                        flagged_count=1,
                                        delayed_count=1,
                                        done=True,
                                        done_in_advance=True,
                                        defunct=True,
                                        updatable=True,
                                        aborted=True,
                                        not_yet_reached=True,
                                        planned=True,
                                        active=True,
                                        in_progress=True,
                                        pending=True,
                                        waiting_for_input=True,
                                        failed=True,
                                        failing=True,
                                        completed_in_advance=True,
                                        skipped=True,
                                        skipped_in_advance=True,
                                        precondition_in_progress=True,
                                        failure_handler_in_progress=True,
                                        abort_script_in_progress=True,
                                        facet_in_progress=True,
                                        movable=True,
                                        gate=True,
                                        task_group=True,
                                        parallel_group=True,
                                        precondition_enabled=True,
                                        failure_handler_enabled=True,
                                        release=Release(),
                                        display_path="display_path_example",
                                        release_owner="release_owner_example",
                                        all_tasks=[],
                                        children=[
                                            PlanItem(
                                                id="id_example",
                                                type="type_example",
                                                title="title_example",
                                                description="description_example",
                                                owner="owner_example",
                                                scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                                due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                                start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                                end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                                planned_duration=1,
                                                flag_status=FlagStatus("OK"),
                                                flag_comment="flag_comment_example",
                                                overdue_notified=True,
                                                flagged=True,
                                                start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                                end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                                children=[],
                                                overdue=True,
                                                done=True,
                                                release=Release(),
                                                release_uid=1,
                                                updatable=True,
                                                display_path="display_path_example",
                                                aborted=True,
                                                active=True,
                                                variable_usages=[
                                                    UsagePoint(
                                                        target_property=CiProperty(
                                                            wrapped=CiProperty(),
                                                            last_property=ModelProperty(
                                                                indexed_property_pattern="indexed_property_pattern_example",
                                                                property_name="property_name_example",
                                                                index=1,
                                                                indexed=True,
                                                            ),
                                                            parent={},
                                                            exists=True,
                                                            property_name="property_name_example",
                                                            value={},
                                                            parent_ci={},
                                                            descriptor={},
                                                            kind={},
                                                            category="category_example",
                                                            password=True,
                                                            indexed=True,
                                                        ),
                                                    ),
                                                ],
                                                or_calculate_due_date="or_calculate_due_date_example",
                                                computed_planned_duration={},
                                                actual_duration={},
                                            ),
                                        ],
                                        variable_usages=[
                                            UsagePoint(
                                                target_property=CiProperty(
                                                    wrapped=CiProperty(),
                                                    last_property=ModelProperty(
                                                        indexed_property_pattern="indexed_property_pattern_example",
                                                        property_name="property_name_example",
                                                        index=1,
                                                        indexed=True,
                                                    ),
                                                    parent={},
                                                    exists=True,
                                                    property_name="property_name_example",
                                                    value={},
                                                    parent_ci={},
                                                    descriptor={},
                                                    kind={},
                                                    category="category_example",
                                                    password=True,
                                                    indexed=True,
                                                ),
                                            ),
                                        ],
                                        input_variables=[
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
                                        referenced_variables=[
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
                                        unbound_required_variables=[
                                            "unbound_required_variables_example",
                                        ],
                                        automated=True,
                                        task_type={},
                                        due_soon=True,
                                        elapsed_duration_fraction=3.14,
                                        url="url_example",
                                    ),
                                ],
                                locked=True,
                                title="title_example",
                            ),
                            facets=[
                                Facet(
                                    id="id_example",
                                    type="type_example",
                                    scope=FacetScope("TASK"),
                                    target_id="target_id_example",
                                    configuration_uri="configuration_uri_example",
                                    variable_mapping={
                                        "key": "key_example",
                                    },
                                    variable_usages=[
                                        UsagePoint(
                                            target_property=CiProperty(
                                                wrapped=CiProperty(),
                                                last_property=ModelProperty(
                                                    indexed_property_pattern="indexed_property_pattern_example",
                                                    property_name="property_name_example",
                                                    index=1,
                                                    indexed=True,
                                                ),
                                                parent={},
                                                exists=True,
                                                property_name="property_name_example",
                                                value={},
                                                parent_ci={},
                                                descriptor={},
                                                kind={},
                                                category="category_example",
                                                password=True,
                                                indexed=True,
                                            ),
                                        ),
                                    ],
                                    properties_with_variables=[
                                        None,
                                    ],
                                ),
                            ],
                            attachments=[
                                Attachment(
                                    id="id_example",
                                    type="type_example",
                                    file={},
                                    content_type="content_type_example",
                                    export_filename="export_filename_example",
                                    file_uri="file_uri_example",
                                    placeholders=[
                                        "placeholders_example",
                                    ],
                                    text_file_names_regex="text_file_names_regex_example",
                                    exclude_file_names_regex="exclude_file_names_regex_example",
                                    file_encodings={
                                        "key": "key_example",
                                    },
                                    checksum="checksum_example",
                                ),
                            ],
                            status=TaskStatus("PLANNED"),
                            team="team_example",
                            watchers=[
                                "watchers_example",
                            ],
                            wait_for_scheduled_start_date=True,
                            delay_during_blackout=True,
                            postponed_due_to_blackout=True,
                            postponed_until_environments_are_reserved=True,
                            original_scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            has_been_flagged=True,
                            has_been_delayed=True,
                            precondition="precondition_example",
                            failure_handler="failure_handler_example",
                            task_failure_handler_enabled=True,
                            task_recover_op=TaskRecoverOp("SKIP_TASK"),
                            failures_count=1,
                            execution_id="execution_id_example",
                            variable_mapping={
                                "key": "key_example",
                            },
                            external_variable_mapping={
                                "key": "key_example",
                            },
                            max_comment_size=1,
                            tags=[
                                "tags_example",
                            ],
                            configuration_uri="configuration_uri_example",
                            due_soon_notified=True,
                            locked=True,
                            check_attributes=True,
                            abort_script="abort_script_example",
                            phase=Phase(),
                            blackout_metadata=BlackoutMetadata(
                                periods=[
                                    BlackoutPeriod(
                                        start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    ),
                                ],
                            ),
                            flagged_count=1,
                            delayed_count=1,
                            done=True,
                            done_in_advance=True,
                            defunct=True,
                            updatable=True,
                            aborted=True,
                            not_yet_reached=True,
                            planned=True,
                            active=True,
                            in_progress=True,
                            pending=True,
                            waiting_for_input=True,
                            failed=True,
                            failing=True,
                            completed_in_advance=True,
                            skipped=True,
                            skipped_in_advance=True,
                            precondition_in_progress=True,
                            failure_handler_in_progress=True,
                            abort_script_in_progress=True,
                            facet_in_progress=True,
                            movable=True,
                            gate=True,
                            task_group=True,
                            parallel_group=True,
                            precondition_enabled=True,
                            failure_handler_enabled=True,
                            release=Release(),
                            display_path="display_path_example",
                            release_owner="release_owner_example",
                            all_tasks=[
                                Task(
                                    id="id_example",
                                    type="type_example",
                                    scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    flag_status=FlagStatus("OK"),
                                    title="title_example",
                                    description="description_example",
                                    owner="owner_example",
                                    due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    planned_duration=1,
                                    flag_comment="flag_comment_example",
                                    overdue_notified=True,
                                    flagged=True,
                                    start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    overdue=True,
                                    or_calculate_due_date="or_calculate_due_date_example",
                                    computed_planned_duration={},
                                    actual_duration={},
                                    release_uid=1,
                                    ci_uid=1,
                                    comments=[
                                        Comment(
                                            id="id_example",
                                            type="type_example",
                                            text="text_example",
                                            author="author_example",
                                            date=dateutil_parser('2023-03-20T02:07:00Z'),
                                            creation_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        ),
                                    ],
                                    container=None,
                                    facets=[
                                        Facet(
                                            id="id_example",
                                            type="type_example",
                                            scope=FacetScope("TASK"),
                                            target_id="target_id_example",
                                            configuration_uri="configuration_uri_example",
                                            variable_mapping={
                                                "key": "key_example",
                                            },
                                            variable_usages=[
                                                UsagePoint(
                                                    target_property=CiProperty(
                                                        wrapped=CiProperty(),
                                                        last_property=ModelProperty(
                                                            indexed_property_pattern="indexed_property_pattern_example",
                                                            property_name="property_name_example",
                                                            index=1,
                                                            indexed=True,
                                                        ),
                                                        parent={},
                                                        exists=True,
                                                        property_name="property_name_example",
                                                        value={},
                                                        parent_ci={},
                                                        descriptor={},
                                                        kind={},
                                                        category="category_example",
                                                        password=True,
                                                        indexed=True,
                                                    ),
                                                ),
                                            ],
                                            properties_with_variables=[
                                                None,
                                            ],
                                        ),
                                    ],
                                    attachments=[
                                        Attachment(
                                            id="id_example",
                                            type="type_example",
                                            file={},
                                            content_type="content_type_example",
                                            export_filename="export_filename_example",
                                            file_uri="file_uri_example",
                                            placeholders=[
                                                "placeholders_example",
                                            ],
                                            text_file_names_regex="text_file_names_regex_example",
                                            exclude_file_names_regex="exclude_file_names_regex_example",
                                            file_encodings={
                                                "key": "key_example",
                                            },
                                            checksum="checksum_example",
                                        ),
                                    ],
                                    status=TaskStatus("PLANNED"),
                                    team="team_example",
                                    watchers=[
                                        "watchers_example",
                                    ],
                                    wait_for_scheduled_start_date=True,
                                    delay_during_blackout=True,
                                    postponed_due_to_blackout=True,
                                    postponed_until_environments_are_reserved=True,
                                    original_scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    has_been_flagged=True,
                                    has_been_delayed=True,
                                    precondition="precondition_example",
                                    failure_handler="failure_handler_example",
                                    task_failure_handler_enabled=True,
                                    task_recover_op=TaskRecoverOp("SKIP_TASK"),
                                    failures_count=1,
                                    execution_id="execution_id_example",
                                    variable_mapping={
                                        "key": "key_example",
                                    },
                                    external_variable_mapping={
                                        "key": "key_example",
                                    },
                                    max_comment_size=1,
                                    tags=[
                                        "tags_example",
                                    ],
                                    configuration_uri="configuration_uri_example",
                                    due_soon_notified=True,
                                    locked=True,
                                    check_attributes=True,
                                    abort_script="abort_script_example",
                                    phase=Phase(),
                                    blackout_metadata=BlackoutMetadata(
                                        periods=[
                                            BlackoutPeriod(
                                                start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                                end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                            ),
                                        ],
                                    ),
                                    flagged_count=1,
                                    delayed_count=1,
                                    done=True,
                                    done_in_advance=True,
                                    defunct=True,
                                    updatable=True,
                                    aborted=True,
                                    not_yet_reached=True,
                                    planned=True,
                                    active=True,
                                    in_progress=True,
                                    pending=True,
                                    waiting_for_input=True,
                                    failed=True,
                                    failing=True,
                                    completed_in_advance=True,
                                    skipped=True,
                                    skipped_in_advance=True,
                                    precondition_in_progress=True,
                                    failure_handler_in_progress=True,
                                    abort_script_in_progress=True,
                                    facet_in_progress=True,
                                    movable=True,
                                    gate=True,
                                    task_group=True,
                                    parallel_group=True,
                                    precondition_enabled=True,
                                    failure_handler_enabled=True,
                                    release=Release(),
                                    display_path="display_path_example",
                                    release_owner="release_owner_example",
                                    all_tasks=[],
                                    children=[
                                        PlanItem(
                                            id="id_example",
                                            type="type_example",
                                            title="title_example",
                                            description="description_example",
                                            owner="owner_example",
                                            scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                            due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                            start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                            end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                            planned_duration=1,
                                            flag_status=FlagStatus("OK"),
                                            flag_comment="flag_comment_example",
                                            overdue_notified=True,
                                            flagged=True,
                                            start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                            end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                            children=[],
                                            overdue=True,
                                            done=True,
                                            release=Release(),
                                            release_uid=1,
                                            updatable=True,
                                            display_path="display_path_example",
                                            aborted=True,
                                            active=True,
                                            variable_usages=[
                                                UsagePoint(
                                                    target_property=CiProperty(
                                                        wrapped=CiProperty(),
                                                        last_property=ModelProperty(
                                                            indexed_property_pattern="indexed_property_pattern_example",
                                                            property_name="property_name_example",
                                                            index=1,
                                                            indexed=True,
                                                        ),
                                                        parent={},
                                                        exists=True,
                                                        property_name="property_name_example",
                                                        value={},
                                                        parent_ci={},
                                                        descriptor={},
                                                        kind={},
                                                        category="category_example",
                                                        password=True,
                                                        indexed=True,
                                                    ),
                                                ),
                                            ],
                                            or_calculate_due_date="or_calculate_due_date_example",
                                            computed_planned_duration={},
                                            actual_duration={},
                                        ),
                                    ],
                                    variable_usages=[
                                        UsagePoint(
                                            target_property=CiProperty(
                                                wrapped=CiProperty(),
                                                last_property=ModelProperty(
                                                    indexed_property_pattern="indexed_property_pattern_example",
                                                    property_name="property_name_example",
                                                    index=1,
                                                    indexed=True,
                                                ),
                                                parent={},
                                                exists=True,
                                                property_name="property_name_example",
                                                value={},
                                                parent_ci={},
                                                descriptor={},
                                                kind={},
                                                category="category_example",
                                                password=True,
                                                indexed=True,
                                            ),
                                        ),
                                    ],
                                    input_variables=[
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
                                    referenced_variables=[
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
                                    unbound_required_variables=[
                                        "unbound_required_variables_example",
                                    ],
                                    automated=True,
                                    task_type={},
                                    due_soon=True,
                                    elapsed_duration_fraction=3.14,
                                    url="url_example",
                                ),
                            ],
                            children=[
                                PlanItem(
                                    id="id_example",
                                    type="type_example",
                                    title="title_example",
                                    description="description_example",
                                    owner="owner_example",
                                    scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    planned_duration=1,
                                    flag_status=FlagStatus("OK"),
                                    flag_comment="flag_comment_example",
                                    overdue_notified=True,
                                    flagged=True,
                                    start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    children=[],
                                    overdue=True,
                                    done=True,
                                    release=Release(),
                                    release_uid=1,
                                    updatable=True,
                                    display_path="display_path_example",
                                    aborted=True,
                                    active=True,
                                    variable_usages=[
                                        UsagePoint(
                                            target_property=CiProperty(
                                                wrapped=CiProperty(),
                                                last_property=ModelProperty(
                                                    indexed_property_pattern="indexed_property_pattern_example",
                                                    property_name="property_name_example",
                                                    index=1,
                                                    indexed=True,
                                                ),
                                                parent={},
                                                exists=True,
                                                property_name="property_name_example",
                                                value={},
                                                parent_ci={},
                                                descriptor={},
                                                kind={},
                                                category="category_example",
                                                password=True,
                                                indexed=True,
                                            ),
                                        ),
                                    ],
                                    or_calculate_due_date="or_calculate_due_date_example",
                                    computed_planned_duration={},
                                    actual_duration={},
                                ),
                            ],
                            input_variables=[
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
                            referenced_variables=[
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
                            unbound_required_variables=[
                                "unbound_required_variables_example",
                            ],
                            automated=True,
                            task_type={},
                            due_soon=True,
                            elapsed_duration_fraction=3.14,
                            url="url_example",
                            conditions=[
                                GateCondition(
                                    id="id_example",
                                    type="type_example",
                                    title="title_example",
                                    checked=True,
                                ),
                            ],
                            dependencies=[
                                Dependency(
                                    id="id_example",
                                    type="type_example",
                                    gate_task=GateTask(),
                                    target=PlanItem(
                                        id="id_example",
                                        type="type_example",
                                        title="title_example",
                                        description="description_example",
                                        owner="owner_example",
                                        scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        planned_duration=1,
                                        flag_status=FlagStatus("OK"),
                                        flag_comment="flag_comment_example",
                                        overdue_notified=True,
                                        flagged=True,
                                        start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        children=[
                                            PlanItem(),
                                        ],
                                        overdue=True,
                                        done=True,
                                        release=Release(),
                                        release_uid=1,
                                        updatable=True,
                                        display_path="display_path_example",
                                        aborted=True,
                                        active=True,
                                        variable_usages=[
                                            UsagePoint(
                                                target_property=CiProperty(
                                                    wrapped=CiProperty(),
                                                    last_property=ModelProperty(
                                                        indexed_property_pattern="indexed_property_pattern_example",
                                                        property_name="property_name_example",
                                                        index=1,
                                                        indexed=True,
                                                    ),
                                                    parent={},
                                                    exists=True,
                                                    property_name="property_name_example",
                                                    value={},
                                                    parent_ci={},
                                                    descriptor={},
                                                    kind={},
                                                    category="category_example",
                                                    password=True,
                                                    indexed=True,
                                                ),
                                            ),
                                        ],
                                        or_calculate_due_date="or_calculate_due_date_example",
                                        computed_planned_duration={},
                                        actual_duration={},
                                    ),
                                    target_id="target_id_example",
                                    archived_target_title="archived_target_title_example",
                                    archived_target_id="archived_target_id_example",
                                    archived_as_resolved=True,
                                    metadata={
                                        "key": {},
                                    },
                                    archived=True,
                                    done=True,
                                    aborted=True,
                                    target_display_path="target_display_path_example",
                                    target_title="target_title_example",
                                    valid_allowed_plan_item_id=True,
                                ),
                            ],
                            open=True,
                            open_in_advance=True,
                            completable=True,
                            aborted_dependency_titles="aborted_dependency_titles_example",
                            variable_usages=[
                                UsagePoint(
                                    target_property=CiProperty(
                                        wrapped=CiProperty(),
                                        last_property=ModelProperty(
                                            indexed_property_pattern="indexed_property_pattern_example",
                                            property_name="property_name_example",
                                            index=1,
                                            indexed=True,
                                        ),
                                        parent={},
                                        exists=True,
                                        property_name="property_name_example",
                                        value={},
                                        parent_ci={},
                                        descriptor={},
                                        kind={},
                                        category="category_example",
                                        password=True,
                                        indexed=True,
                                    ),
                                ),
                            ],
                        ),
                    ],
                    all_tasks=[
                        Task(
                            id="id_example",
                            type="type_example",
                            scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            flag_status=FlagStatus("OK"),
                            title="title_example",
                            description="description_example",
                            owner="owner_example",
                            due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            planned_duration=1,
                            flag_comment="flag_comment_example",
                            overdue_notified=True,
                            flagged=True,
                            start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            overdue=True,
                            or_calculate_due_date="or_calculate_due_date_example",
                            computed_planned_duration={},
                            actual_duration={},
                            release_uid=1,
                            ci_uid=1,
                            comments=[
                                Comment(
                                    id="id_example",
                                    type="type_example",
                                    text="text_example",
                                    author="author_example",
                                    date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    creation_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                ),
                            ],
                            container=None,
                            facets=[
                                Facet(
                                    id="id_example",
                                    type="type_example",
                                    scope=FacetScope("TASK"),
                                    target_id="target_id_example",
                                    configuration_uri="configuration_uri_example",
                                    variable_mapping={
                                        "key": "key_example",
                                    },
                                    variable_usages=[
                                        UsagePoint(
                                            target_property=CiProperty(
                                                wrapped=CiProperty(),
                                                last_property=ModelProperty(
                                                    indexed_property_pattern="indexed_property_pattern_example",
                                                    property_name="property_name_example",
                                                    index=1,
                                                    indexed=True,
                                                ),
                                                parent={},
                                                exists=True,
                                                property_name="property_name_example",
                                                value={},
                                                parent_ci={},
                                                descriptor={},
                                                kind={},
                                                category="category_example",
                                                password=True,
                                                indexed=True,
                                            ),
                                        ),
                                    ],
                                    properties_with_variables=[
                                        None,
                                    ],
                                ),
                            ],
                            attachments=[
                                Attachment(
                                    id="id_example",
                                    type="type_example",
                                    file={},
                                    content_type="content_type_example",
                                    export_filename="export_filename_example",
                                    file_uri="file_uri_example",
                                    placeholders=[
                                        "placeholders_example",
                                    ],
                                    text_file_names_regex="text_file_names_regex_example",
                                    exclude_file_names_regex="exclude_file_names_regex_example",
                                    file_encodings={
                                        "key": "key_example",
                                    },
                                    checksum="checksum_example",
                                ),
                            ],
                            status=TaskStatus("PLANNED"),
                            team="team_example",
                            watchers=[
                                "watchers_example",
                            ],
                            wait_for_scheduled_start_date=True,
                            delay_during_blackout=True,
                            postponed_due_to_blackout=True,
                            postponed_until_environments_are_reserved=True,
                            original_scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            has_been_flagged=True,
                            has_been_delayed=True,
                            precondition="precondition_example",
                            failure_handler="failure_handler_example",
                            task_failure_handler_enabled=True,
                            task_recover_op=TaskRecoverOp("SKIP_TASK"),
                            failures_count=1,
                            execution_id="execution_id_example",
                            variable_mapping={
                                "key": "key_example",
                            },
                            external_variable_mapping={
                                "key": "key_example",
                            },
                            max_comment_size=1,
                            tags=[
                                "tags_example",
                            ],
                            configuration_uri="configuration_uri_example",
                            due_soon_notified=True,
                            locked=True,
                            check_attributes=True,
                            abort_script="abort_script_example",
                            phase=Phase(),
                            blackout_metadata=BlackoutMetadata(
                                periods=[
                                    BlackoutPeriod(
                                        start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    ),
                                ],
                            ),
                            flagged_count=1,
                            delayed_count=1,
                            done=True,
                            done_in_advance=True,
                            defunct=True,
                            updatable=True,
                            aborted=True,
                            not_yet_reached=True,
                            planned=True,
                            active=True,
                            in_progress=True,
                            pending=True,
                            waiting_for_input=True,
                            failed=True,
                            failing=True,
                            completed_in_advance=True,
                            skipped=True,
                            skipped_in_advance=True,
                            precondition_in_progress=True,
                            failure_handler_in_progress=True,
                            abort_script_in_progress=True,
                            facet_in_progress=True,
                            movable=True,
                            gate=True,
                            task_group=True,
                            parallel_group=True,
                            precondition_enabled=True,
                            failure_handler_enabled=True,
                            release=Release(),
                            display_path="display_path_example",
                            release_owner="release_owner_example",
                            all_tasks=[],
                            children=[
                                PlanItem(
                                    id="id_example",
                                    type="type_example",
                                    title="title_example",
                                    description="description_example",
                                    owner="owner_example",
                                    scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    planned_duration=1,
                                    flag_status=FlagStatus("OK"),
                                    flag_comment="flag_comment_example",
                                    overdue_notified=True,
                                    flagged=True,
                                    start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    children=[],
                                    overdue=True,
                                    done=True,
                                    release=Release(),
                                    release_uid=1,
                                    updatable=True,
                                    display_path="display_path_example",
                                    aborted=True,
                                    active=True,
                                    variable_usages=[
                                        UsagePoint(
                                            target_property=CiProperty(
                                                wrapped=CiProperty(),
                                                last_property=ModelProperty(
                                                    indexed_property_pattern="indexed_property_pattern_example",
                                                    property_name="property_name_example",
                                                    index=1,
                                                    indexed=True,
                                                ),
                                                parent={},
                                                exists=True,
                                                property_name="property_name_example",
                                                value={},
                                                parent_ci={},
                                                descriptor={},
                                                kind={},
                                                category="category_example",
                                                password=True,
                                                indexed=True,
                                            ),
                                        ),
                                    ],
                                    or_calculate_due_date="or_calculate_due_date_example",
                                    computed_planned_duration={},
                                    actual_duration={},
                                ),
                            ],
                            variable_usages=[
                                UsagePoint(
                                    target_property=CiProperty(
                                        wrapped=CiProperty(),
                                        last_property=ModelProperty(
                                            indexed_property_pattern="indexed_property_pattern_example",
                                            property_name="property_name_example",
                                            index=1,
                                            indexed=True,
                                        ),
                                        parent={},
                                        exists=True,
                                        property_name="property_name_example",
                                        value={},
                                        parent_ci={},
                                        descriptor={},
                                        kind={},
                                        category="category_example",
                                        password=True,
                                        indexed=True,
                                    ),
                                ),
                            ],
                            input_variables=[
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
                            referenced_variables=[
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
                            unbound_required_variables=[
                                "unbound_required_variables_example",
                            ],
                            automated=True,
                            task_type={},
                            due_soon=True,
                            elapsed_duration_fraction=3.14,
                            url="url_example",
                        ),
                    ],
                    children=[
                        PlanItem(
                            id="id_example",
                            type="type_example",
                            title="title_example",
                            description="description_example",
                            owner="owner_example",
                            scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            planned_duration=1,
                            flag_status=FlagStatus("OK"),
                            flag_comment="flag_comment_example",
                            overdue_notified=True,
                            flagged=True,
                            start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            children=[],
                            overdue=True,
                            done=True,
                            release=Release(),
                            release_uid=1,
                            updatable=True,
                            display_path="display_path_example",
                            aborted=True,
                            active=True,
                            variable_usages=[
                                UsagePoint(
                                    target_property=CiProperty(
                                        wrapped=CiProperty(),
                                        last_property=ModelProperty(
                                            indexed_property_pattern="indexed_property_pattern_example",
                                            property_name="property_name_example",
                                            index=1,
                                            indexed=True,
                                        ),
                                        parent={},
                                        exists=True,
                                        property_name="property_name_example",
                                        value={},
                                        parent_ci={},
                                        descriptor={},
                                        kind={},
                                        category="category_example",
                                        password=True,
                                        indexed=True,
                                    ),
                                ),
                            ],
                            or_calculate_due_date="or_calculate_due_date_example",
                            computed_planned_duration={},
                            actual_duration={},
                        ),
                    ],
                    variable_usages=[
                        UsagePoint(
                            target_property=CiProperty(
                                wrapped=CiProperty(),
                                last_property=ModelProperty(
                                    indexed_property_pattern="indexed_property_pattern_example",
                                    property_name="property_name_example",
                                    index=1,
                                    indexed=True,
                                ),
                                parent={},
                                exists=True,
                                property_name="property_name_example",
                                value={},
                                parent_ci={},
                                descriptor={},
                                kind={},
                                category="category_example",
                                password=True,
                                indexed=True,
                            ),
                        ),
                    ],
                    original=True,
                    phase_copied=True,
                    ancestor_id="ancestor_id_example",
                    latest_copy=True,
                ),
                blackout_metadata=BlackoutMetadata(
                    periods=[
                        BlackoutPeriod(
                            start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        ),
                    ],
                ),
                flagged_count=1,
                delayed_count=1,
                done=True,
                done_in_advance=True,
                defunct=True,
                updatable=True,
                aborted=True,
                not_yet_reached=True,
                planned=True,
                active=True,
                in_progress=True,
                pending=True,
                waiting_for_input=True,
                failed=True,
                failing=True,
                completed_in_advance=True,
                skipped=True,
                skipped_in_advance=True,
                precondition_in_progress=True,
                failure_handler_in_progress=True,
                abort_script_in_progress=True,
                facet_in_progress=True,
                movable=True,
                gate=True,
                task_group=True,
                parallel_group=True,
                precondition_enabled=True,
                failure_handler_enabled=True,
                release=Release(),
                display_path="display_path_example",
                release_owner="release_owner_example",
                all_tasks=[
                    Task(
                        id="id_example",
                        type="type_example",
                        scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        flag_status=FlagStatus("OK"),
                        title="title_example",
                        description="description_example",
                        owner="owner_example",
                        due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        planned_duration=1,
                        flag_comment="flag_comment_example",
                        overdue_notified=True,
                        flagged=True,
                        start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        overdue=True,
                        or_calculate_due_date="or_calculate_due_date_example",
                        computed_planned_duration={},
                        actual_duration={},
                        release_uid=1,
                        ci_uid=1,
                        comments=[
                            Comment(
                                id="id_example",
                                type="type_example",
                                text="text_example",
                                author="author_example",
                                date=dateutil_parser('2023-03-20T02:07:00Z'),
                                creation_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            ),
                        ],
                        container=None,
                        facets=[
                            Facet(
                                id="id_example",
                                type="type_example",
                                scope=FacetScope("TASK"),
                                target_id="target_id_example",
                                configuration_uri="configuration_uri_example",
                                variable_mapping={
                                    "key": "key_example",
                                },
                                variable_usages=[
                                    UsagePoint(
                                        target_property=CiProperty(
                                            wrapped=CiProperty(),
                                            last_property=ModelProperty(
                                                indexed_property_pattern="indexed_property_pattern_example",
                                                property_name="property_name_example",
                                                index=1,
                                                indexed=True,
                                            ),
                                            parent={},
                                            exists=True,
                                            property_name="property_name_example",
                                            value={},
                                            parent_ci={},
                                            descriptor={},
                                            kind={},
                                            category="category_example",
                                            password=True,
                                            indexed=True,
                                        ),
                                    ),
                                ],
                                properties_with_variables=[
                                    None,
                                ],
                            ),
                        ],
                        attachments=[
                            Attachment(
                                id="id_example",
                                type="type_example",
                                file={},
                                content_type="content_type_example",
                                export_filename="export_filename_example",
                                file_uri="file_uri_example",
                                placeholders=[
                                    "placeholders_example",
                                ],
                                text_file_names_regex="text_file_names_regex_example",
                                exclude_file_names_regex="exclude_file_names_regex_example",
                                file_encodings={
                                    "key": "key_example",
                                },
                                checksum="checksum_example",
                            ),
                        ],
                        status=TaskStatus("PLANNED"),
                        team="team_example",
                        watchers=[
                            "watchers_example",
                        ],
                        wait_for_scheduled_start_date=True,
                        delay_during_blackout=True,
                        postponed_due_to_blackout=True,
                        postponed_until_environments_are_reserved=True,
                        original_scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        has_been_flagged=True,
                        has_been_delayed=True,
                        precondition="precondition_example",
                        failure_handler="failure_handler_example",
                        task_failure_handler_enabled=True,
                        task_recover_op=TaskRecoverOp("SKIP_TASK"),
                        failures_count=1,
                        execution_id="execution_id_example",
                        variable_mapping={
                            "key": "key_example",
                        },
                        external_variable_mapping={
                            "key": "key_example",
                        },
                        max_comment_size=1,
                        tags=[
                            "tags_example",
                        ],
                        configuration_uri="configuration_uri_example",
                        due_soon_notified=True,
                        locked=True,
                        check_attributes=True,
                        abort_script="abort_script_example",
                        phase=Phase(
                            id="id_example",
                            type="type_example",
                            locked=True,
                            title="title_example",
                            description="description_example",
                            owner="owner_example",
                            scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            planned_duration=1,
                            flag_status=FlagStatus("OK"),
                            flag_comment="flag_comment_example",
                            overdue_notified=True,
                            flagged=True,
                            start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            overdue=True,
                            or_calculate_due_date="or_calculate_due_date_example",
                            computed_planned_duration={},
                            actual_duration={},
                            release_uid=1,
                            tasks=[],
                            release=None,
                            status=PhaseStatus("PLANNED"),
                            color="color_example",
                            origin_id="origin_id_example",
                            current_task=Task(),
                            display_path="display_path_example",
                            active=True,
                            done=True,
                            defunct=True,
                            updatable=True,
                            aborted=True,
                            planned=True,
                            failed=True,
                            failing=True,
                            release_owner="release_owner_example",
                            all_gates=[
                                GateTask(
                                    id="id_example",
                                    type="type_example",
                                    scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    flag_status=FlagStatus("OK"),
                                    title="title_example",
                                    description="description_example",
                                    owner="owner_example",
                                    due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    planned_duration=1,
                                    flag_comment="flag_comment_example",
                                    overdue_notified=True,
                                    flagged=True,
                                    start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    overdue=True,
                                    or_calculate_due_date="or_calculate_due_date_example",
                                    computed_planned_duration={},
                                    actual_duration={},
                                    release_uid=1,
                                    ci_uid=1,
                                    comments=[
                                        Comment(
                                            id="id_example",
                                            type="type_example",
                                            text="text_example",
                                            author="author_example",
                                            date=dateutil_parser('2023-03-20T02:07:00Z'),
                                            creation_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        ),
                                    ],
                                    container=TaskContainer(
                                        id="id_example",
                                        type="type_example",
                                        tasks=[],
                                        locked=True,
                                        title="title_example",
                                    ),
                                    facets=[
                                        Facet(
                                            id="id_example",
                                            type="type_example",
                                            scope=FacetScope("TASK"),
                                            target_id="target_id_example",
                                            configuration_uri="configuration_uri_example",
                                            variable_mapping={
                                                "key": "key_example",
                                            },
                                            variable_usages=[
                                                UsagePoint(
                                                    target_property=CiProperty(
                                                        wrapped=CiProperty(),
                                                        last_property=ModelProperty(
                                                            indexed_property_pattern="indexed_property_pattern_example",
                                                            property_name="property_name_example",
                                                            index=1,
                                                            indexed=True,
                                                        ),
                                                        parent={},
                                                        exists=True,
                                                        property_name="property_name_example",
                                                        value={},
                                                        parent_ci={},
                                                        descriptor={},
                                                        kind={},
                                                        category="category_example",
                                                        password=True,
                                                        indexed=True,
                                                    ),
                                                ),
                                            ],
                                            properties_with_variables=[
                                                None,
                                            ],
                                        ),
                                    ],
                                    attachments=[
                                        Attachment(
                                            id="id_example",
                                            type="type_example",
                                            file={},
                                            content_type="content_type_example",
                                            export_filename="export_filename_example",
                                            file_uri="file_uri_example",
                                            placeholders=[
                                                "placeholders_example",
                                            ],
                                            text_file_names_regex="text_file_names_regex_example",
                                            exclude_file_names_regex="exclude_file_names_regex_example",
                                            file_encodings={
                                                "key": "key_example",
                                            },
                                            checksum="checksum_example",
                                        ),
                                    ],
                                    status=TaskStatus("PLANNED"),
                                    team="team_example",
                                    watchers=[
                                        "watchers_example",
                                    ],
                                    wait_for_scheduled_start_date=True,
                                    delay_during_blackout=True,
                                    postponed_due_to_blackout=True,
                                    postponed_until_environments_are_reserved=True,
                                    original_scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    has_been_flagged=True,
                                    has_been_delayed=True,
                                    precondition="precondition_example",
                                    failure_handler="failure_handler_example",
                                    task_failure_handler_enabled=True,
                                    task_recover_op=TaskRecoverOp("SKIP_TASK"),
                                    failures_count=1,
                                    execution_id="execution_id_example",
                                    variable_mapping={
                                        "key": "key_example",
                                    },
                                    external_variable_mapping={
                                        "key": "key_example",
                                    },
                                    max_comment_size=1,
                                    tags=[
                                        "tags_example",
                                    ],
                                    configuration_uri="configuration_uri_example",
                                    due_soon_notified=True,
                                    locked=True,
                                    check_attributes=True,
                                    abort_script="abort_script_example",
                                    phase=Phase(),
                                    blackout_metadata=BlackoutMetadata(
                                        periods=[
                                            BlackoutPeriod(
                                                start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                                end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                            ),
                                        ],
                                    ),
                                    flagged_count=1,
                                    delayed_count=1,
                                    done=True,
                                    done_in_advance=True,
                                    defunct=True,
                                    updatable=True,
                                    aborted=True,
                                    not_yet_reached=True,
                                    planned=True,
                                    active=True,
                                    in_progress=True,
                                    pending=True,
                                    waiting_for_input=True,
                                    failed=True,
                                    failing=True,
                                    completed_in_advance=True,
                                    skipped=True,
                                    skipped_in_advance=True,
                                    precondition_in_progress=True,
                                    failure_handler_in_progress=True,
                                    abort_script_in_progress=True,
                                    facet_in_progress=True,
                                    movable=True,
                                    gate=True,
                                    task_group=True,
                                    parallel_group=True,
                                    precondition_enabled=True,
                                    failure_handler_enabled=True,
                                    release=Release(),
                                    display_path="display_path_example",
                                    release_owner="release_owner_example",
                                    all_tasks=[],
                                    children=[
                                        PlanItem(
                                            id="id_example",
                                            type="type_example",
                                            title="title_example",
                                            description="description_example",
                                            owner="owner_example",
                                            scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                            due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                            start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                            end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                            planned_duration=1,
                                            flag_status=FlagStatus("OK"),
                                            flag_comment="flag_comment_example",
                                            overdue_notified=True,
                                            flagged=True,
                                            start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                            end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                            children=[],
                                            overdue=True,
                                            done=True,
                                            release=Release(),
                                            release_uid=1,
                                            updatable=True,
                                            display_path="display_path_example",
                                            aborted=True,
                                            active=True,
                                            variable_usages=[
                                                UsagePoint(
                                                    target_property=CiProperty(
                                                        wrapped=CiProperty(),
                                                        last_property=ModelProperty(
                                                            indexed_property_pattern="indexed_property_pattern_example",
                                                            property_name="property_name_example",
                                                            index=1,
                                                            indexed=True,
                                                        ),
                                                        parent={},
                                                        exists=True,
                                                        property_name="property_name_example",
                                                        value={},
                                                        parent_ci={},
                                                        descriptor={},
                                                        kind={},
                                                        category="category_example",
                                                        password=True,
                                                        indexed=True,
                                                    ),
                                                ),
                                            ],
                                            or_calculate_due_date="or_calculate_due_date_example",
                                            computed_planned_duration={},
                                            actual_duration={},
                                        ),
                                    ],
                                    input_variables=[
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
                                    referenced_variables=[
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
                                    unbound_required_variables=[
                                        "unbound_required_variables_example",
                                    ],
                                    automated=True,
                                    task_type={},
                                    due_soon=True,
                                    elapsed_duration_fraction=3.14,
                                    url="url_example",
                                    conditions=[
                                        GateCondition(
                                            id="id_example",
                                            type="type_example",
                                            title="title_example",
                                            checked=True,
                                        ),
                                    ],
                                    dependencies=[
                                        Dependency(
                                            id="id_example",
                                            type="type_example",
                                            gate_task=GateTask(),
                                            target=PlanItem(
                                                id="id_example",
                                                type="type_example",
                                                title="title_example",
                                                description="description_example",
                                                owner="owner_example",
                                                scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                                due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                                start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                                end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                                planned_duration=1,
                                                flag_status=FlagStatus("OK"),
                                                flag_comment="flag_comment_example",
                                                overdue_notified=True,
                                                flagged=True,
                                                start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                                end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                                children=[
                                                    PlanItem(),
                                                ],
                                                overdue=True,
                                                done=True,
                                                release=Release(),
                                                release_uid=1,
                                                updatable=True,
                                                display_path="display_path_example",
                                                aborted=True,
                                                active=True,
                                                variable_usages=[
                                                    UsagePoint(
                                                        target_property=CiProperty(
                                                            wrapped=CiProperty(),
                                                            last_property=ModelProperty(
                                                                indexed_property_pattern="indexed_property_pattern_example",
                                                                property_name="property_name_example",
                                                                index=1,
                                                                indexed=True,
                                                            ),
                                                            parent={},
                                                            exists=True,
                                                            property_name="property_name_example",
                                                            value={},
                                                            parent_ci={},
                                                            descriptor={},
                                                            kind={},
                                                            category="category_example",
                                                            password=True,
                                                            indexed=True,
                                                        ),
                                                    ),
                                                ],
                                                or_calculate_due_date="or_calculate_due_date_example",
                                                computed_planned_duration={},
                                                actual_duration={},
                                            ),
                                            target_id="target_id_example",
                                            archived_target_title="archived_target_title_example",
                                            archived_target_id="archived_target_id_example",
                                            archived_as_resolved=True,
                                            metadata={
                                                "key": {},
                                            },
                                            archived=True,
                                            done=True,
                                            aborted=True,
                                            target_display_path="target_display_path_example",
                                            target_title="target_title_example",
                                            valid_allowed_plan_item_id=True,
                                        ),
                                    ],
                                    open=True,
                                    open_in_advance=True,
                                    completable=True,
                                    aborted_dependency_titles="aborted_dependency_titles_example",
                                    variable_usages=[
                                        UsagePoint(
                                            target_property=CiProperty(
                                                wrapped=CiProperty(),
                                                last_property=ModelProperty(
                                                    indexed_property_pattern="indexed_property_pattern_example",
                                                    property_name="property_name_example",
                                                    index=1,
                                                    indexed=True,
                                                ),
                                                parent={},
                                                exists=True,
                                                property_name="property_name_example",
                                                value={},
                                                parent_ci={},
                                                descriptor={},
                                                kind={},
                                                category="category_example",
                                                password=True,
                                                indexed=True,
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            all_tasks=[],
                            children=[
                                PlanItem(
                                    id="id_example",
                                    type="type_example",
                                    title="title_example",
                                    description="description_example",
                                    owner="owner_example",
                                    scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    planned_duration=1,
                                    flag_status=FlagStatus("OK"),
                                    flag_comment="flag_comment_example",
                                    overdue_notified=True,
                                    flagged=True,
                                    start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    children=[],
                                    overdue=True,
                                    done=True,
                                    release=Release(),
                                    release_uid=1,
                                    updatable=True,
                                    display_path="display_path_example",
                                    aborted=True,
                                    active=True,
                                    variable_usages=[
                                        UsagePoint(
                                            target_property=CiProperty(
                                                wrapped=CiProperty(),
                                                last_property=ModelProperty(
                                                    indexed_property_pattern="indexed_property_pattern_example",
                                                    property_name="property_name_example",
                                                    index=1,
                                                    indexed=True,
                                                ),
                                                parent={},
                                                exists=True,
                                                property_name="property_name_example",
                                                value={},
                                                parent_ci={},
                                                descriptor={},
                                                kind={},
                                                category="category_example",
                                                password=True,
                                                indexed=True,
                                            ),
                                        ),
                                    ],
                                    or_calculate_due_date="or_calculate_due_date_example",
                                    computed_planned_duration={},
                                    actual_duration={},
                                ),
                            ],
                            variable_usages=[
                                UsagePoint(
                                    target_property=CiProperty(
                                        wrapped=CiProperty(),
                                        last_property=ModelProperty(
                                            indexed_property_pattern="indexed_property_pattern_example",
                                            property_name="property_name_example",
                                            index=1,
                                            indexed=True,
                                        ),
                                        parent={},
                                        exists=True,
                                        property_name="property_name_example",
                                        value={},
                                        parent_ci={},
                                        descriptor={},
                                        kind={},
                                        category="category_example",
                                        password=True,
                                        indexed=True,
                                    ),
                                ),
                            ],
                            original=True,
                            phase_copied=True,
                            ancestor_id="ancestor_id_example",
                            latest_copy=True,
                        ),
                        blackout_metadata=BlackoutMetadata(
                            periods=[
                                BlackoutPeriod(
                                    start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                ),
                            ],
                        ),
                        flagged_count=1,
                        delayed_count=1,
                        done=True,
                        done_in_advance=True,
                        defunct=True,
                        updatable=True,
                        aborted=True,
                        not_yet_reached=True,
                        planned=True,
                        active=True,
                        in_progress=True,
                        pending=True,
                        waiting_for_input=True,
                        failed=True,
                        failing=True,
                        completed_in_advance=True,
                        skipped=True,
                        skipped_in_advance=True,
                        precondition_in_progress=True,
                        failure_handler_in_progress=True,
                        abort_script_in_progress=True,
                        facet_in_progress=True,
                        movable=True,
                        gate=True,
                        task_group=True,
                        parallel_group=True,
                        precondition_enabled=True,
                        failure_handler_enabled=True,
                        release=Release(),
                        display_path="display_path_example",
                        release_owner="release_owner_example",
                        all_tasks=[],
                        children=[
                            PlanItem(
                                id="id_example",
                                type="type_example",
                                title="title_example",
                                description="description_example",
                                owner="owner_example",
                                scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                planned_duration=1,
                                flag_status=FlagStatus("OK"),
                                flag_comment="flag_comment_example",
                                overdue_notified=True,
                                flagged=True,
                                start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                children=[],
                                overdue=True,
                                done=True,
                                release=Release(),
                                release_uid=1,
                                updatable=True,
                                display_path="display_path_example",
                                aborted=True,
                                active=True,
                                variable_usages=[
                                    UsagePoint(
                                        target_property=CiProperty(
                                            wrapped=CiProperty(),
                                            last_property=ModelProperty(
                                                indexed_property_pattern="indexed_property_pattern_example",
                                                property_name="property_name_example",
                                                index=1,
                                                indexed=True,
                                            ),
                                            parent={},
                                            exists=True,
                                            property_name="property_name_example",
                                            value={},
                                            parent_ci={},
                                            descriptor={},
                                            kind={},
                                            category="category_example",
                                            password=True,
                                            indexed=True,
                                        ),
                                    ),
                                ],
                                or_calculate_due_date="or_calculate_due_date_example",
                                computed_planned_duration={},
                                actual_duration={},
                            ),
                        ],
                        variable_usages=[
                            UsagePoint(
                                target_property=CiProperty(
                                    wrapped=CiProperty(),
                                    last_property=ModelProperty(
                                        indexed_property_pattern="indexed_property_pattern_example",
                                        property_name="property_name_example",
                                        index=1,
                                        indexed=True,
                                    ),
                                    parent={},
                                    exists=True,
                                    property_name="property_name_example",
                                    value={},
                                    parent_ci={},
                                    descriptor={},
                                    kind={},
                                    category="category_example",
                                    password=True,
                                    indexed=True,
                                ),
                            ),
                        ],
                        input_variables=[
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
                        referenced_variables=[
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
                        unbound_required_variables=[
                            "unbound_required_variables_example",
                        ],
                        automated=True,
                        task_type={},
                        due_soon=True,
                        elapsed_duration_fraction=3.14,
                        url="url_example",
                    ),
                ],
                children=[
                    PlanItem(
                        id="id_example",
                        type="type_example",
                        title="title_example",
                        description="description_example",
                        owner="owner_example",
                        scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        planned_duration=1,
                        flag_status=FlagStatus("OK"),
                        flag_comment="flag_comment_example",
                        overdue_notified=True,
                        flagged=True,
                        start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        children=[],
                        overdue=True,
                        done=True,
                        release=Release(),
                        release_uid=1,
                        updatable=True,
                        display_path="display_path_example",
                        aborted=True,
                        active=True,
                        variable_usages=[
                            UsagePoint(
                                target_property=CiProperty(
                                    wrapped=CiProperty(),
                                    last_property=ModelProperty(
                                        indexed_property_pattern="indexed_property_pattern_example",
                                        property_name="property_name_example",
                                        index=1,
                                        indexed=True,
                                    ),
                                    parent={},
                                    exists=True,
                                    property_name="property_name_example",
                                    value={},
                                    parent_ci={},
                                    descriptor={},
                                    kind={},
                                    category="category_example",
                                    password=True,
                                    indexed=True,
                                ),
                            ),
                        ],
                        or_calculate_due_date="or_calculate_due_date_example",
                        computed_planned_duration={},
                        actual_duration={},
                    ),
                ],
                input_variables=[
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
                unbound_required_variables=[
                    "unbound_required_variables_example",
                ],
                automated=True,
                task_type={},
                due_soon=True,
                elapsed_duration_fraction=3.14,
                url="url_example",
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
                referenced_variables=[
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
                variable_usages=[
                    UsagePoint(
                        target_property=CiProperty(
                            wrapped=CiProperty(),
                            last_property=ModelProperty(
                                indexed_property_pattern="indexed_property_pattern_example",
                                property_name="property_name_example",
                                index=1,
                                indexed=True,
                            ),
                            parent={},
                            exists=True,
                            property_name="property_name_example",
                            value={},
                            parent_ci={},
                            descriptor={},
                            kind={},
                            category="category_example",
                            password=True,
                            indexed=True,
                        ),
                    ),
                ],
            ),
        ],
        done=True,
        planned_or_active=True,
        active=True,
        defunct=True,
        updatable=True,
        aborted=True,
        failing=True,
        failed=True,
        paused=True,
        template=True,
        planned=True,
        in_progress=True,
        release=Release(),
        release_uid=1,
        display_path="display_path_example",
        children=[
            PlanItem(
                id="id_example",
                type="type_example",
                title="title_example",
                description="description_example",
                owner="owner_example",
                scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                planned_duration=1,
                flag_status=FlagStatus("OK"),
                flag_comment="flag_comment_example",
                overdue_notified=True,
                flagged=True,
                start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                children=[],
                overdue=True,
                done=True,
                release=Release(),
                release_uid=1,
                updatable=True,
                display_path="display_path_example",
                aborted=True,
                active=True,
                variable_usages=[
                    UsagePoint(
                        target_property=CiProperty(
                            wrapped=CiProperty(),
                            last_property=ModelProperty(
                                indexed_property_pattern="indexed_property_pattern_example",
                                property_name="property_name_example",
                                index=1,
                                indexed=True,
                            ),
                            parent={},
                            exists=True,
                            property_name="property_name_example",
                            value={},
                            parent_ci={},
                            descriptor={},
                            kind={},
                            category="category_example",
                            password=True,
                            indexed=True,
                        ),
                    ),
                ],
                or_calculate_due_date="or_calculate_due_date_example",
                computed_planned_duration={},
                actual_duration={},
            ),
        ],
        all_plan_items=[
            PlanItem(
                id="id_example",
                type="type_example",
                title="title_example",
                description="description_example",
                owner="owner_example",
                scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                planned_duration=1,
                flag_status=FlagStatus("OK"),
                flag_comment="flag_comment_example",
                overdue_notified=True,
                flagged=True,
                start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                children=[],
                overdue=True,
                done=True,
                release=Release(),
                release_uid=1,
                updatable=True,
                display_path="display_path_example",
                aborted=True,
                active=True,
                variable_usages=[
                    UsagePoint(
                        target_property=CiProperty(
                            wrapped=CiProperty(),
                            last_property=ModelProperty(
                                indexed_property_pattern="indexed_property_pattern_example",
                                property_name="property_name_example",
                                index=1,
                                indexed=True,
                            ),
                            parent={},
                            exists=True,
                            property_name="property_name_example",
                            value={},
                            parent_ci={},
                            descriptor={},
                            kind={},
                            category="category_example",
                            password=True,
                            indexed=True,
                        ),
                    ),
                ],
                or_calculate_due_date="or_calculate_due_date_example",
                computed_planned_duration={},
                actual_duration={},
            ),
        ],
        url="url_example",
        active_tasks=[
            Task(
                id="id_example",
                type="type_example",
                scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                flag_status=FlagStatus("OK"),
                title="title_example",
                description="description_example",
                owner="owner_example",
                due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                planned_duration=1,
                flag_comment="flag_comment_example",
                overdue_notified=True,
                flagged=True,
                start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                overdue=True,
                or_calculate_due_date="or_calculate_due_date_example",
                computed_planned_duration={},
                actual_duration={},
                release_uid=1,
                ci_uid=1,
                comments=[
                    Comment(
                        id="id_example",
                        type="type_example",
                        text="text_example",
                        author="author_example",
                        date=dateutil_parser('2023-03-20T02:07:00Z'),
                        creation_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    ),
                ],
                container=None,
                facets=[
                    Facet(
                        id="id_example",
                        type="type_example",
                        scope=FacetScope("TASK"),
                        target_id="target_id_example",
                        configuration_uri="configuration_uri_example",
                        variable_mapping={
                            "key": "key_example",
                        },
                        variable_usages=[
                            UsagePoint(
                                target_property=CiProperty(
                                    wrapped=CiProperty(),
                                    last_property=ModelProperty(
                                        indexed_property_pattern="indexed_property_pattern_example",
                                        property_name="property_name_example",
                                        index=1,
                                        indexed=True,
                                    ),
                                    parent={},
                                    exists=True,
                                    property_name="property_name_example",
                                    value={},
                                    parent_ci={},
                                    descriptor={},
                                    kind={},
                                    category="category_example",
                                    password=True,
                                    indexed=True,
                                ),
                            ),
                        ],
                        properties_with_variables=[
                            None,
                        ],
                    ),
                ],
                attachments=[
                    Attachment(
                        id="id_example",
                        type="type_example",
                        file={},
                        content_type="content_type_example",
                        export_filename="export_filename_example",
                        file_uri="file_uri_example",
                        placeholders=[
                            "placeholders_example",
                        ],
                        text_file_names_regex="text_file_names_regex_example",
                        exclude_file_names_regex="exclude_file_names_regex_example",
                        file_encodings={
                            "key": "key_example",
                        },
                        checksum="checksum_example",
                    ),
                ],
                status=TaskStatus("PLANNED"),
                team="team_example",
                watchers=[
                    "watchers_example",
                ],
                wait_for_scheduled_start_date=True,
                delay_during_blackout=True,
                postponed_due_to_blackout=True,
                postponed_until_environments_are_reserved=True,
                original_scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                has_been_flagged=True,
                has_been_delayed=True,
                precondition="precondition_example",
                failure_handler="failure_handler_example",
                task_failure_handler_enabled=True,
                task_recover_op=TaskRecoverOp("SKIP_TASK"),
                failures_count=1,
                execution_id="execution_id_example",
                variable_mapping={
                    "key": "key_example",
                },
                external_variable_mapping={
                    "key": "key_example",
                },
                max_comment_size=1,
                tags=[
                    "tags_example",
                ],
                configuration_uri="configuration_uri_example",
                due_soon_notified=True,
                locked=True,
                check_attributes=True,
                abort_script="abort_script_example",
                phase=Phase(
                    id="id_example",
                    type="type_example",
                    locked=True,
                    title="title_example",
                    description="description_example",
                    owner="owner_example",
                    scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    planned_duration=1,
                    flag_status=FlagStatus("OK"),
                    flag_comment="flag_comment_example",
                    overdue_notified=True,
                    flagged=True,
                    start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    overdue=True,
                    or_calculate_due_date="or_calculate_due_date_example",
                    computed_planned_duration={},
                    actual_duration={},
                    release_uid=1,
                    tasks=[],
                    release=None,
                    status=PhaseStatus("PLANNED"),
                    color="color_example",
                    origin_id="origin_id_example",
                    current_task=Task(),
                    display_path="display_path_example",
                    active=True,
                    done=True,
                    defunct=True,
                    updatable=True,
                    aborted=True,
                    planned=True,
                    failed=True,
                    failing=True,
                    release_owner="release_owner_example",
                    all_gates=[
                        GateTask(
                            id="id_example",
                            type="type_example",
                            scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            flag_status=FlagStatus("OK"),
                            title="title_example",
                            description="description_example",
                            owner="owner_example",
                            due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            planned_duration=1,
                            flag_comment="flag_comment_example",
                            overdue_notified=True,
                            flagged=True,
                            start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            overdue=True,
                            or_calculate_due_date="or_calculate_due_date_example",
                            computed_planned_duration={},
                            actual_duration={},
                            release_uid=1,
                            ci_uid=1,
                            comments=[
                                Comment(
                                    id="id_example",
                                    type="type_example",
                                    text="text_example",
                                    author="author_example",
                                    date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    creation_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                ),
                            ],
                            container=TaskContainer(
                                id="id_example",
                                type="type_example",
                                tasks=[],
                                locked=True,
                                title="title_example",
                            ),
                            facets=[
                                Facet(
                                    id="id_example",
                                    type="type_example",
                                    scope=FacetScope("TASK"),
                                    target_id="target_id_example",
                                    configuration_uri="configuration_uri_example",
                                    variable_mapping={
                                        "key": "key_example",
                                    },
                                    variable_usages=[
                                        UsagePoint(
                                            target_property=CiProperty(
                                                wrapped=CiProperty(),
                                                last_property=ModelProperty(
                                                    indexed_property_pattern="indexed_property_pattern_example",
                                                    property_name="property_name_example",
                                                    index=1,
                                                    indexed=True,
                                                ),
                                                parent={},
                                                exists=True,
                                                property_name="property_name_example",
                                                value={},
                                                parent_ci={},
                                                descriptor={},
                                                kind={},
                                                category="category_example",
                                                password=True,
                                                indexed=True,
                                            ),
                                        ),
                                    ],
                                    properties_with_variables=[
                                        None,
                                    ],
                                ),
                            ],
                            attachments=[
                                Attachment(
                                    id="id_example",
                                    type="type_example",
                                    file={},
                                    content_type="content_type_example",
                                    export_filename="export_filename_example",
                                    file_uri="file_uri_example",
                                    placeholders=[
                                        "placeholders_example",
                                    ],
                                    text_file_names_regex="text_file_names_regex_example",
                                    exclude_file_names_regex="exclude_file_names_regex_example",
                                    file_encodings={
                                        "key": "key_example",
                                    },
                                    checksum="checksum_example",
                                ),
                            ],
                            status=TaskStatus("PLANNED"),
                            team="team_example",
                            watchers=[
                                "watchers_example",
                            ],
                            wait_for_scheduled_start_date=True,
                            delay_during_blackout=True,
                            postponed_due_to_blackout=True,
                            postponed_until_environments_are_reserved=True,
                            original_scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            has_been_flagged=True,
                            has_been_delayed=True,
                            precondition="precondition_example",
                            failure_handler="failure_handler_example",
                            task_failure_handler_enabled=True,
                            task_recover_op=TaskRecoverOp("SKIP_TASK"),
                            failures_count=1,
                            execution_id="execution_id_example",
                            variable_mapping={
                                "key": "key_example",
                            },
                            external_variable_mapping={
                                "key": "key_example",
                            },
                            max_comment_size=1,
                            tags=[
                                "tags_example",
                            ],
                            configuration_uri="configuration_uri_example",
                            due_soon_notified=True,
                            locked=True,
                            check_attributes=True,
                            abort_script="abort_script_example",
                            phase=Phase(),
                            blackout_metadata=BlackoutMetadata(
                                periods=[
                                    BlackoutPeriod(
                                        start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    ),
                                ],
                            ),
                            flagged_count=1,
                            delayed_count=1,
                            done=True,
                            done_in_advance=True,
                            defunct=True,
                            updatable=True,
                            aborted=True,
                            not_yet_reached=True,
                            planned=True,
                            active=True,
                            in_progress=True,
                            pending=True,
                            waiting_for_input=True,
                            failed=True,
                            failing=True,
                            completed_in_advance=True,
                            skipped=True,
                            skipped_in_advance=True,
                            precondition_in_progress=True,
                            failure_handler_in_progress=True,
                            abort_script_in_progress=True,
                            facet_in_progress=True,
                            movable=True,
                            gate=True,
                            task_group=True,
                            parallel_group=True,
                            precondition_enabled=True,
                            failure_handler_enabled=True,
                            release=Release(),
                            display_path="display_path_example",
                            release_owner="release_owner_example",
                            all_tasks=[],
                            children=[
                                PlanItem(
                                    id="id_example",
                                    type="type_example",
                                    title="title_example",
                                    description="description_example",
                                    owner="owner_example",
                                    scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    planned_duration=1,
                                    flag_status=FlagStatus("OK"),
                                    flag_comment="flag_comment_example",
                                    overdue_notified=True,
                                    flagged=True,
                                    start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                    children=[],
                                    overdue=True,
                                    done=True,
                                    release=Release(),
                                    release_uid=1,
                                    updatable=True,
                                    display_path="display_path_example",
                                    aborted=True,
                                    active=True,
                                    variable_usages=[
                                        UsagePoint(
                                            target_property=CiProperty(
                                                wrapped=CiProperty(),
                                                last_property=ModelProperty(
                                                    indexed_property_pattern="indexed_property_pattern_example",
                                                    property_name="property_name_example",
                                                    index=1,
                                                    indexed=True,
                                                ),
                                                parent={},
                                                exists=True,
                                                property_name="property_name_example",
                                                value={},
                                                parent_ci={},
                                                descriptor={},
                                                kind={},
                                                category="category_example",
                                                password=True,
                                                indexed=True,
                                            ),
                                        ),
                                    ],
                                    or_calculate_due_date="or_calculate_due_date_example",
                                    computed_planned_duration={},
                                    actual_duration={},
                                ),
                            ],
                            input_variables=[
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
                            referenced_variables=[
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
                            unbound_required_variables=[
                                "unbound_required_variables_example",
                            ],
                            automated=True,
                            task_type={},
                            due_soon=True,
                            elapsed_duration_fraction=3.14,
                            url="url_example",
                            conditions=[
                                GateCondition(
                                    id="id_example",
                                    type="type_example",
                                    title="title_example",
                                    checked=True,
                                ),
                            ],
                            dependencies=[
                                Dependency(
                                    id="id_example",
                                    type="type_example",
                                    gate_task=GateTask(),
                                    target=PlanItem(
                                        id="id_example",
                                        type="type_example",
                                        title="title_example",
                                        description="description_example",
                                        owner="owner_example",
                                        scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        planned_duration=1,
                                        flag_status=FlagStatus("OK"),
                                        flag_comment="flag_comment_example",
                                        overdue_notified=True,
                                        flagged=True,
                                        start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                                        children=[
                                            PlanItem(),
                                        ],
                                        overdue=True,
                                        done=True,
                                        release=Release(),
                                        release_uid=1,
                                        updatable=True,
                                        display_path="display_path_example",
                                        aborted=True,
                                        active=True,
                                        variable_usages=[
                                            UsagePoint(
                                                target_property=CiProperty(
                                                    wrapped=CiProperty(),
                                                    last_property=ModelProperty(
                                                        indexed_property_pattern="indexed_property_pattern_example",
                                                        property_name="property_name_example",
                                                        index=1,
                                                        indexed=True,
                                                    ),
                                                    parent={},
                                                    exists=True,
                                                    property_name="property_name_example",
                                                    value={},
                                                    parent_ci={},
                                                    descriptor={},
                                                    kind={},
                                                    category="category_example",
                                                    password=True,
                                                    indexed=True,
                                                ),
                                            ),
                                        ],
                                        or_calculate_due_date="or_calculate_due_date_example",
                                        computed_planned_duration={},
                                        actual_duration={},
                                    ),
                                    target_id="target_id_example",
                                    archived_target_title="archived_target_title_example",
                                    archived_target_id="archived_target_id_example",
                                    archived_as_resolved=True,
                                    metadata={
                                        "key": {},
                                    },
                                    archived=True,
                                    done=True,
                                    aborted=True,
                                    target_display_path="target_display_path_example",
                                    target_title="target_title_example",
                                    valid_allowed_plan_item_id=True,
                                ),
                            ],
                            open=True,
                            open_in_advance=True,
                            completable=True,
                            aborted_dependency_titles="aborted_dependency_titles_example",
                            variable_usages=[
                                UsagePoint(
                                    target_property=CiProperty(
                                        wrapped=CiProperty(),
                                        last_property=ModelProperty(
                                            indexed_property_pattern="indexed_property_pattern_example",
                                            property_name="property_name_example",
                                            index=1,
                                            indexed=True,
                                        ),
                                        parent={},
                                        exists=True,
                                        property_name="property_name_example",
                                        value={},
                                        parent_ci={},
                                        descriptor={},
                                        kind={},
                                        category="category_example",
                                        password=True,
                                        indexed=True,
                                    ),
                                ),
                            ],
                        ),
                    ],
                    all_tasks=[],
                    children=[
                        PlanItem(
                            id="id_example",
                            type="type_example",
                            title="title_example",
                            description="description_example",
                            owner="owner_example",
                            scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            planned_duration=1,
                            flag_status=FlagStatus("OK"),
                            flag_comment="flag_comment_example",
                            overdue_notified=True,
                            flagged=True,
                            start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            children=[],
                            overdue=True,
                            done=True,
                            release=Release(),
                            release_uid=1,
                            updatable=True,
                            display_path="display_path_example",
                            aborted=True,
                            active=True,
                            variable_usages=[
                                UsagePoint(
                                    target_property=CiProperty(
                                        wrapped=CiProperty(),
                                        last_property=ModelProperty(
                                            indexed_property_pattern="indexed_property_pattern_example",
                                            property_name="property_name_example",
                                            index=1,
                                            indexed=True,
                                        ),
                                        parent={},
                                        exists=True,
                                        property_name="property_name_example",
                                        value={},
                                        parent_ci={},
                                        descriptor={},
                                        kind={},
                                        category="category_example",
                                        password=True,
                                        indexed=True,
                                    ),
                                ),
                            ],
                            or_calculate_due_date="or_calculate_due_date_example",
                            computed_planned_duration={},
                            actual_duration={},
                        ),
                    ],
                    variable_usages=[
                        UsagePoint(
                            target_property=CiProperty(
                                wrapped=CiProperty(),
                                last_property=ModelProperty(
                                    indexed_property_pattern="indexed_property_pattern_example",
                                    property_name="property_name_example",
                                    index=1,
                                    indexed=True,
                                ),
                                parent={},
                                exists=True,
                                property_name="property_name_example",
                                value={},
                                parent_ci={},
                                descriptor={},
                                kind={},
                                category="category_example",
                                password=True,
                                indexed=True,
                            ),
                        ),
                    ],
                    original=True,
                    phase_copied=True,
                    ancestor_id="ancestor_id_example",
                    latest_copy=True,
                ),
                blackout_metadata=BlackoutMetadata(
                    periods=[
                        BlackoutPeriod(
                            start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        ),
                    ],
                ),
                flagged_count=1,
                delayed_count=1,
                done=True,
                done_in_advance=True,
                defunct=True,
                updatable=True,
                aborted=True,
                not_yet_reached=True,
                planned=True,
                active=True,
                in_progress=True,
                pending=True,
                waiting_for_input=True,
                failed=True,
                failing=True,
                completed_in_advance=True,
                skipped=True,
                skipped_in_advance=True,
                precondition_in_progress=True,
                failure_handler_in_progress=True,
                abort_script_in_progress=True,
                facet_in_progress=True,
                movable=True,
                gate=True,
                task_group=True,
                parallel_group=True,
                precondition_enabled=True,
                failure_handler_enabled=True,
                release=Release(),
                display_path="display_path_example",
                release_owner="release_owner_example",
                all_tasks=[],
                children=[
                    PlanItem(
                        id="id_example",
                        type="type_example",
                        title="title_example",
                        description="description_example",
                        owner="owner_example",
                        scheduled_start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        start_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        end_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        planned_duration=1,
                        flag_status=FlagStatus("OK"),
                        flag_comment="flag_comment_example",
                        overdue_notified=True,
                        flagged=True,
                        start_or_scheduled_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        end_or_due_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        children=[],
                        overdue=True,
                        done=True,
                        release=Release(),
                        release_uid=1,
                        updatable=True,
                        display_path="display_path_example",
                        aborted=True,
                        active=True,
                        variable_usages=[
                            UsagePoint(
                                target_property=CiProperty(
                                    wrapped=CiProperty(),
                                    last_property=ModelProperty(
                                        indexed_property_pattern="indexed_property_pattern_example",
                                        property_name="property_name_example",
                                        index=1,
                                        indexed=True,
                                    ),
                                    parent={},
                                    exists=True,
                                    property_name="property_name_example",
                                    value={},
                                    parent_ci={},
                                    descriptor={},
                                    kind={},
                                    category="category_example",
                                    password=True,
                                    indexed=True,
                                ),
                            ),
                        ],
                        or_calculate_due_date="or_calculate_due_date_example",
                        computed_planned_duration={},
                        actual_duration={},
                    ),
                ],
                variable_usages=[
                    UsagePoint(
                        target_property=CiProperty(
                            wrapped=CiProperty(),
                            last_property=ModelProperty(
                                indexed_property_pattern="indexed_property_pattern_example",
                                property_name="property_name_example",
                                index=1,
                                indexed=True,
                            ),
                            parent={},
                            exists=True,
                            property_name="property_name_example",
                            value={},
                            parent_ci={},
                            descriptor={},
                            kind={},
                            category="category_example",
                            password=True,
                            indexed=True,
                        ),
                    ),
                ],
                input_variables=[
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
                referenced_variables=[
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
                unbound_required_variables=[
                    "unbound_required_variables_example",
                ],
                automated=True,
                task_type={},
                due_soon=True,
                elapsed_duration_fraction=3.14,
                url="url_example",
            ),
        ],
        variable_usages=[
            UsagePoint(
                target_property=CiProperty(
                    wrapped=CiProperty(),
                    last_property=ModelProperty(
                        indexed_property_pattern="indexed_property_pattern_example",
                        property_name="property_name_example",
                        index=1,
                        indexed=True,
                    ),
                    parent={},
                    exists=True,
                    property_name="property_name_example",
                    value={},
                    parent_ci={},
                    descriptor={},
                    kind={},
                    category="category_example",
                    password=True,
                    indexed=True,
                ),
            ),
        ],
        pending=True,
    ) # Release |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_release(release_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ReleaseApi->update_release: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_release(release_id, release=release)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ReleaseApi->update_release: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release_id** | **str**|  |
 **release** | [**Release**](Release.md)|  | [optional]

### Return type

[**Release**](Release.md)

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

# **update_release_variable**
> Variable update_release_variable(variable_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import release_api
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
    api_instance = release_api.ReleaseApi(api_client)
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
        api_response = api_instance.update_release_variable(variable_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ReleaseApi->update_release_variable: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_release_variable(variable_id, variable=variable)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ReleaseApi->update_release_variable: %s\n" % e)
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

# **update_release_variables**
> [Variable] update_release_variables(release_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import release_api
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
    api_instance = release_api.ReleaseApi(api_client)
    release_id = "jUR,rZ#UM/?R,Fp^l6$ARj" # str | 
    variable = [
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
    ] # [Variable] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_release_variables(release_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ReleaseApi->update_release_variables: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_release_variables(release_id, variable=variable)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling ReleaseApi->update_release_variables: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release_id** | **str**|  |
 **variable** | [**[Variable]**](Variable.md)|  | [optional]

### Return type

[**[Variable]**](Variable.md)

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

