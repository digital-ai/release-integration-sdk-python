# digitalai.release.v1.EnvironmentReservationApi

All URIs are relative to *http://localhost:5516*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_application**](EnvironmentReservationApi.md#add_application) | **POST** /api/v1/environments/reservations/{environmentReservationId} | 
[**create_reservation**](EnvironmentReservationApi.md#create_reservation) | **POST** /api/v1/environments/reservations | 
[**delete_environment_reservation**](EnvironmentReservationApi.md#delete_environment_reservation) | **DELETE** /api/v1/environments/reservations/{environmentReservationId} | 
[**get_reservation**](EnvironmentReservationApi.md#get_reservation) | **GET** /api/v1/environments/reservations/{environmentReservationId} | 
[**search_reservations**](EnvironmentReservationApi.md#search_reservations) | **POST** /api/v1/environments/reservations/search | 
[**update_reservation**](EnvironmentReservationApi.md#update_reservation) | **PUT** /api/v1/environments/reservations/{environmentReservationId} | 


# **add_application**
> add_application(environment_reservation_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import environment_reservation_api
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
    api_instance = environment_reservation_api.EnvironmentReservationApi(api_client)
    environment_reservation_id = "jUR,rZ#UM/?R,Fp^l6$ARj/EnvironmentReservationQ" # str | 
    application_id = "applicationId_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.add_application(environment_reservation_id)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling EnvironmentReservationApi->add_application: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.add_application(environment_reservation_id, application_id=application_id)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling EnvironmentReservationApi->add_application: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_reservation_id** | **str**|  |
 **application_id** | **str**|  | [optional]

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

# **create_reservation**
> EnvironmentReservationView create_reservation()



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import environment_reservation_api
from digitalai.release.v1.model.environment_reservation_form import EnvironmentReservationForm
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
    api_instance = environment_reservation_api.EnvironmentReservationApi(api_client)
    environment_reservation_form = EnvironmentReservationForm(
        start_date=dateutil_parser('2023-03-20T02:07:00Z'),
        end_date=dateutil_parser('2023-03-20T02:07:00Z'),
        note="note_example",
        environment_id="environment_id_example",
        application_ids=[
            "application_ids_example",
        ],
    ) # EnvironmentReservationForm |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_reservation(environment_reservation_form=environment_reservation_form)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling EnvironmentReservationApi->create_reservation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_reservation_form** | [**EnvironmentReservationForm**](EnvironmentReservationForm.md)|  | [optional]

### Return type

[**EnvironmentReservationView**](EnvironmentReservationView.md)

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

# **delete_environment_reservation**
> delete_environment_reservation(environment_reservation_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import environment_reservation_api
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
    api_instance = environment_reservation_api.EnvironmentReservationApi(api_client)
    environment_reservation_id = "jUR,rZ#UM/?R,Fp^l6$ARj/EnvironmentReservationQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_environment_reservation(environment_reservation_id)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling EnvironmentReservationApi->delete_environment_reservation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_reservation_id** | **str**|  |

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

# **get_reservation**
> EnvironmentReservationView get_reservation(environment_reservation_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import environment_reservation_api
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
    api_instance = environment_reservation_api.EnvironmentReservationApi(api_client)
    environment_reservation_id = "jUR,rZ#UM/?R,Fp^l6$ARj/EnvironmentReservationQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_reservation(environment_reservation_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling EnvironmentReservationApi->get_reservation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_reservation_id** | **str**|  |

### Return type

[**EnvironmentReservationView**](EnvironmentReservationView.md)

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

# **search_reservations**
> [EnvironmentReservationSearchView] search_reservations()



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import environment_reservation_api
from digitalai.release.v1.model.environment_reservation_search_view import EnvironmentReservationSearchView
from digitalai.release.v1.model.reservation_filters import ReservationFilters
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
    api_instance = environment_reservation_api.EnvironmentReservationApi(api_client)
    reservation_filters = ReservationFilters(
        environment_title="environment_title_example",
        stages=[
            "stages_example",
        ],
        labels=[
            "labels_example",
        ],
        applications=[
            "applications_example",
        ],
        _from=dateutil_parser('2023-03-20T02:07:00Z'),
        to=dateutil_parser('2023-03-20T02:07:00Z'),
    ) # ReservationFilters |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.search_reservations(reservation_filters=reservation_filters)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling EnvironmentReservationApi->search_reservations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_filters** | [**ReservationFilters**](ReservationFilters.md)|  | [optional]

### Return type

[**[EnvironmentReservationSearchView]**](EnvironmentReservationSearchView.md)

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

# **update_reservation**
> EnvironmentReservationView update_reservation(environment_reservation_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import environment_reservation_api
from digitalai.release.v1.model.environment_reservation_form import EnvironmentReservationForm
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
    api_instance = environment_reservation_api.EnvironmentReservationApi(api_client)
    environment_reservation_id = "jUR,rZ#UM/?R,Fp^l6$ARj/EnvironmentReservationQ" # str | 
    environment_reservation_form = EnvironmentReservationForm(
        start_date=dateutil_parser('2023-03-20T02:07:00Z'),
        end_date=dateutil_parser('2023-03-20T02:07:00Z'),
        note="note_example",
        environment_id="environment_id_example",
        application_ids=[
            "application_ids_example",
        ],
    ) # EnvironmentReservationForm |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_reservation(environment_reservation_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling EnvironmentReservationApi->update_reservation: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_reservation(environment_reservation_id, environment_reservation_form=environment_reservation_form)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling EnvironmentReservationApi->update_reservation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_reservation_id** | **str**|  |
 **environment_reservation_form** | [**EnvironmentReservationForm**](EnvironmentReservationForm.md)|  | [optional]

### Return type

[**EnvironmentReservationView**](EnvironmentReservationView.md)

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

