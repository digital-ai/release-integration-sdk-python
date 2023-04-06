# digitalai.release.v1.RiskApi

All URIs are relative to *http://localhost:5516*

Method | HTTP request | Description
------------- | ------------- | -------------
[**copy_risk_profile**](RiskApi.md#copy_risk_profile) | **POST** /api/v1/risks/profiles/{riskProfileId}/copy | 
[**create_risk_profile**](RiskApi.md#create_risk_profile) | **POST** /api/v1/risks/profiles | 
[**delete_risk_profile**](RiskApi.md#delete_risk_profile) | **DELETE** /api/v1/risks/profiles/{riskProfileId} | 
[**get_all_risk_assessors**](RiskApi.md#get_all_risk_assessors) | **GET** /api/v1/risks/assessors | 
[**get_risk**](RiskApi.md#get_risk) | **GET** /api/v1/risks/{riskId} | 
[**get_risk_global_thresholds**](RiskApi.md#get_risk_global_thresholds) | **GET** /api/v1/risks/config | 
[**get_risk_profile**](RiskApi.md#get_risk_profile) | **GET** /api/v1/risks/profiles/{riskProfileId} | 
[**get_risk_profiles**](RiskApi.md#get_risk_profiles) | **GET** /api/v1/risks/profiles | 
[**update_risk_global_thresholds**](RiskApi.md#update_risk_global_thresholds) | **PUT** /api/v1/risks/config | 
[**update_risk_profile**](RiskApi.md#update_risk_profile) | **PUT** /api/v1/risks/profiles/{riskProfileId} | 


# **copy_risk_profile**
> RiskProfile copy_risk_profile(risk_profile_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import risk_api
from digitalai.release.v1.model.risk_profile import RiskProfile
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
    api_instance = risk_api.RiskApi(api_client)
    risk_profile_id = "jUR,rZ#UM/?R,Fp^l6$ARj/RiskProfileQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.copy_risk_profile(risk_profile_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling RiskApi->copy_risk_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **risk_profile_id** | **str**|  |

### Return type

[**RiskProfile**](RiskProfile.md)

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

# **create_risk_profile**
> RiskProfile create_risk_profile()



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import risk_api
from digitalai.release.v1.model.risk_profile import RiskProfile
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
    api_instance = risk_api.RiskApi(api_client)
    risk_profile = RiskProfile(
        id="id_example",
        type="type_example",
        folder_id="folder_id_example",
        title="title_example",
        default_profile=True,
        risk_profile_assessors={
            "key": "key_example",
        },
    ) # RiskProfile |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_risk_profile(risk_profile=risk_profile)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling RiskApi->create_risk_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **risk_profile** | [**RiskProfile**](RiskProfile.md)|  | [optional]

### Return type

[**RiskProfile**](RiskProfile.md)

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

# **delete_risk_profile**
> delete_risk_profile(risk_profile_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import risk_api
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
    api_instance = risk_api.RiskApi(api_client)
    risk_profile_id = "jUR,rZ#UM/?R,Fp^l6$ARj/RiskProfileQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_risk_profile(risk_profile_id)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling RiskApi->delete_risk_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **risk_profile_id** | **str**|  |

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

# **get_all_risk_assessors**
> [RiskAssessor] get_all_risk_assessors()



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import risk_api
from digitalai.release.v1.model.risk_assessor import RiskAssessor
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
    api_instance = risk_api.RiskApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_all_risk_assessors()
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling RiskApi->get_all_risk_assessors: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[RiskAssessor]**](RiskAssessor.md)

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

# **get_risk**
> Risk get_risk(risk_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import risk_api
from digitalai.release.v1.model.risk import Risk
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
    api_instance = risk_api.RiskApi(api_client)
    risk_id = "jUR,rZ#UM/?R,Fp^l6$ARj/Ris" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_risk(risk_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling RiskApi->get_risk: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **risk_id** | **str**|  |

### Return type

[**Risk**](Risk.md)

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

# **get_risk_global_thresholds**
> RiskGlobalThresholds get_risk_global_thresholds()



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import risk_api
from digitalai.release.v1.model.risk_global_thresholds import RiskGlobalThresholds
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
    api_instance = risk_api.RiskApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_risk_global_thresholds()
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling RiskApi->get_risk_global_thresholds: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**RiskGlobalThresholds**](RiskGlobalThresholds.md)

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

# **get_risk_profile**
> RiskProfile get_risk_profile(risk_profile_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import risk_api
from digitalai.release.v1.model.risk_profile import RiskProfile
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
    api_instance = risk_api.RiskApi(api_client)
    risk_profile_id = "ne" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_risk_profile(risk_profile_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling RiskApi->get_risk_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **risk_profile_id** | **str**|  |

### Return type

[**RiskProfile**](RiskProfile.md)

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

# **get_risk_profiles**
> [RiskProfile] get_risk_profiles()



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import risk_api
from digitalai.release.v1.model.risk_profile import RiskProfile
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
    api_instance = risk_api.RiskApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_risk_profiles()
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling RiskApi->get_risk_profiles: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[RiskProfile]**](RiskProfile.md)

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

# **update_risk_global_thresholds**
> RiskGlobalThresholds update_risk_global_thresholds()



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import risk_api
from digitalai.release.v1.model.risk_global_thresholds import RiskGlobalThresholds
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
    api_instance = risk_api.RiskApi(api_client)
    risk_global_thresholds = RiskGlobalThresholds(
        id="id_example",
        type="type_example",
        folder_id="folder_id_example",
        title="title_example",
        at_risk_from=1,
        attention_needed_from=1,
    ) # RiskGlobalThresholds |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_risk_global_thresholds(risk_global_thresholds=risk_global_thresholds)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling RiskApi->update_risk_global_thresholds: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **risk_global_thresholds** | [**RiskGlobalThresholds**](RiskGlobalThresholds.md)|  | [optional]

### Return type

[**RiskGlobalThresholds**](RiskGlobalThresholds.md)

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

# **update_risk_profile**
> RiskProfile update_risk_profile(risk_profile_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import risk_api
from digitalai.release.v1.model.risk_profile import RiskProfile
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
    api_instance = risk_api.RiskApi(api_client)
    risk_profile_id = "jUR,rZ#UM/?R,Fp^l6$ARj/RiskProfileQ" # str | 
    risk_profile = RiskProfile(
        id="id_example",
        type="type_example",
        folder_id="folder_id_example",
        title="title_example",
        default_profile=True,
        risk_profile_assessors={
            "key": "key_example",
        },
    ) # RiskProfile |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_risk_profile(risk_profile_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling RiskApi->update_risk_profile: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_risk_profile(risk_profile_id, risk_profile=risk_profile)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling RiskApi->update_risk_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **risk_profile_id** | **str**|  |
 **risk_profile** | [**RiskProfile**](RiskProfile.md)|  | [optional]

### Return type

[**RiskProfile**](RiskProfile.md)

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

