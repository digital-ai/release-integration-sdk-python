# digitalai.release.v1.DslApi

All URIs are relative to *http://localhost:5516*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_template_to_x_file**](DslApi.md#export_template_to_x_file) | **GET** /api/v1/dsl/export/{templateId} | 
[**preview_export_template_to_x_file**](DslApi.md#preview_export_template_to_x_file) | **GET** /api/v1/dsl/preview/{templateId} | 


# **export_template_to_x_file**
> export_template_to_x_file(template_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import dsl_api
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
    api_instance = dsl_api.DslApi(api_client)
    template_id = "jUR,rZ#UM/?R,Fp^l6$ARjReleaseQ" # str | 
    export_template = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.export_template_to_x_file(template_id)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DslApi->export_template_to_x_file: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.export_template_to_x_file(template_id, export_template=export_template)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DslApi->export_template_to_x_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  |
 **export_template** | **bool**|  | [optional]

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

# **preview_export_template_to_x_file**
> preview_export_template_to_x_file(template_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import dsl_api
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
    api_instance = dsl_api.DslApi(api_client)
    template_id = "jUR,rZ#UM/?R,Fp^l6$ARjReleaseQ" # str | 
    export_template = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.preview_export_template_to_x_file(template_id)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DslApi->preview_export_template_to_x_file: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.preview_export_template_to_x_file(template_id, export_template=export_template)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DslApi->preview_export_template_to_x_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  |
 **export_template** | **bool**|  | [optional]

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

