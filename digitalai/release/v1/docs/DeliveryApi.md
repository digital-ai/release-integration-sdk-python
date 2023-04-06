# digitalai.release.v1.DeliveryApi

All URIs are relative to *http://localhost:5516*

Method | HTTP request | Description
------------- | ------------- | -------------
[**complete_stage**](DeliveryApi.md#complete_stage) | **POST** /api/v1/deliveries/{stageId}/complete | 
[**complete_tracked_item**](DeliveryApi.md#complete_tracked_item) | **PUT** /api/v1/deliveries/{stageId}/{itemId}/complete | 
[**complete_transition**](DeliveryApi.md#complete_transition) | **POST** /api/v1/deliveries/{transitionId}/complete | 
[**create_tracked_item_in_delivery**](DeliveryApi.md#create_tracked_item_in_delivery) | **POST** /api/v1/deliveries/{deliveryId}/tracked-items | 
[**delete_delivery**](DeliveryApi.md#delete_delivery) | **DELETE** /api/v1/deliveries/{deliveryId} | 
[**delete_tracked_item_delivery**](DeliveryApi.md#delete_tracked_item_delivery) | **DELETE** /api/v1/deliveries/{itemId} | 
[**descope_tracked_item**](DeliveryApi.md#descope_tracked_item) | **PUT** /api/v1/deliveries/{itemId}/descope | 
[**get_delivery**](DeliveryApi.md#get_delivery) | **GET** /api/v1/deliveries/{deliveryId} | 
[**get_delivery_timeline**](DeliveryApi.md#get_delivery_timeline) | **GET** /api/v1/deliveries/{deliveryId}/timeline | 
[**get_releases_for_delivery**](DeliveryApi.md#get_releases_for_delivery) | **GET** /api/v1/deliveries/{deliveryId}/releases | 
[**get_stages_in_delivery**](DeliveryApi.md#get_stages_in_delivery) | **GET** /api/v1/deliveries/{deliveryId}/stages | 
[**get_tracked_itemsin_delivery**](DeliveryApi.md#get_tracked_itemsin_delivery) | **GET** /api/v1/deliveries/{deliveryId}/tracked-items | 
[**reopen_stage**](DeliveryApi.md#reopen_stage) | **POST** /api/v1/deliveries/{stageId}/reopen | 
[**rescope_tracked_item**](DeliveryApi.md#rescope_tracked_item) | **PUT** /api/v1/deliveries/{itemId}/rescope | 
[**reset_tracked_item**](DeliveryApi.md#reset_tracked_item) | **PUT** /api/v1/deliveries/{stageId}/{itemId}/reset | 
[**search_deliveries**](DeliveryApi.md#search_deliveries) | **POST** /api/v1/deliveries/search | 
[**skip_tracked_item**](DeliveryApi.md#skip_tracked_item) | **PUT** /api/v1/deliveries/{stageId}/{itemId}/skip | 
[**update_delivery**](DeliveryApi.md#update_delivery) | **PUT** /api/v1/deliveries/{deliveryId} | 
[**update_stage_in_delivery**](DeliveryApi.md#update_stage_in_delivery) | **PUT** /api/v1/deliveries/{stageId} | 
[**update_tracked_item_in_delivery**](DeliveryApi.md#update_tracked_item_in_delivery) | **PUT** /api/v1/deliveries/{itemId} | 
[**update_transition_in_delivery**](DeliveryApi.md#update_transition_in_delivery) | **PUT** /api/v1/deliveries/{transitionId} | 


# **complete_stage**
> complete_stage(stage_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import delivery_api
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
    api_instance = delivery_api.DeliveryApi(api_client)
    stage_id = "jUR,rZ#UM/?R,Fp^l6$ARjStageQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.complete_stage(stage_id)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryApi->complete_stage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_id** | **str**|  |

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

# **complete_tracked_item**
> complete_tracked_item(item_id, stage_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import delivery_api
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
    api_instance = delivery_api.DeliveryApi(api_client)
    item_id = "jUR,rZ#UM/?R,Fp^l6$ARjTrackedItemQ" # str | 
    stage_id = "jUR,rZ#UM/?R,Fp^l6$ARjStageQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.complete_tracked_item(item_id, stage_id)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryApi->complete_tracked_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  |
 **stage_id** | **str**|  |

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

# **complete_transition**
> complete_transition(transition_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import delivery_api
from digitalai.release.v1.model.complete_transition import CompleteTransition
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
    api_instance = delivery_api.DeliveryApi(api_client)
    transition_id = "jUR,rZ#UM/?R,Fp^l6$ARjTransitionQ" # str | 
    complete_transition = CompleteTransition(
        transition_items=[
            "transition_items_example",
        ],
        close_stages=True,
    ) # CompleteTransition |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.complete_transition(transition_id)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryApi->complete_transition: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.complete_transition(transition_id, complete_transition=complete_transition)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryApi->complete_transition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transition_id** | **str**|  |
 **complete_transition** | [**CompleteTransition**](CompleteTransition.md)|  | [optional]

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

# **create_tracked_item_in_delivery**
> TrackedItem create_tracked_item_in_delivery(delivery_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import delivery_api
from digitalai.release.v1.model.tracked_item import TrackedItem
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
    api_instance = delivery_api.DeliveryApi(api_client)
    delivery_id = "jUR,rZ#UM/?R,Fp^l6$ARjDeliveryQ" # str | 
    tracked_item = TrackedItem(
        id="id_example",
        type="type_example",
        title="title_example",
        release_ids=[
            "release_ids_example",
        ],
        descoped=True,
        created_date=dateutil_parser('2023-03-20T02:07:00Z'),
        modified_date=dateutil_parser('2023-03-20T02:07:00Z'),
    ) # TrackedItem |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_tracked_item_in_delivery(delivery_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryApi->create_tracked_item_in_delivery: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_tracked_item_in_delivery(delivery_id, tracked_item=tracked_item)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryApi->create_tracked_item_in_delivery: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delivery_id** | **str**|  |
 **tracked_item** | [**TrackedItem**](TrackedItem.md)|  | [optional]

### Return type

[**TrackedItem**](TrackedItem.md)

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

# **delete_delivery**
> delete_delivery(delivery_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import delivery_api
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
    api_instance = delivery_api.DeliveryApi(api_client)
    delivery_id = "jUR,rZ#UM/?R,Fp^l6$ARjDeliveryQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_delivery(delivery_id)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryApi->delete_delivery: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delivery_id** | **str**|  |

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

# **delete_tracked_item_delivery**
> delete_tracked_item_delivery(item_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import delivery_api
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
    api_instance = delivery_api.DeliveryApi(api_client)
    item_id = "jUR,rZ#UM/?R,Fp^l6$ARjTrackedItemQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_tracked_item_delivery(item_id)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryApi->delete_tracked_item_delivery: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  |

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

# **descope_tracked_item**
> descope_tracked_item(item_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import delivery_api
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
    api_instance = delivery_api.DeliveryApi(api_client)
    item_id = "jUR,rZ#UM/?R,Fp^l6$ARjTrackedItemQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.descope_tracked_item(item_id)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryApi->descope_tracked_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  |

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

# **get_delivery**
> Delivery get_delivery(delivery_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import delivery_api
from digitalai.release.v1.model.delivery import Delivery
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
    api_instance = delivery_api.DeliveryApi(api_client)
    delivery_id = "jUR,rZ#UM/?R,Fp^l6$ARjDeliveryQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_delivery(delivery_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryApi->get_delivery: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delivery_id** | **str**|  |

### Return type

[**Delivery**](Delivery.md)

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

# **get_delivery_timeline**
> DeliveryTimeline get_delivery_timeline(delivery_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import delivery_api
from digitalai.release.v1.model.delivery_timeline import DeliveryTimeline
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
    api_instance = delivery_api.DeliveryApi(api_client)
    delivery_id = "jUR,rZ#UM/?R,Fp^l6$ARjDeliveryQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_delivery_timeline(delivery_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryApi->get_delivery_timeline: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delivery_id** | **str**|  |

### Return type

[**DeliveryTimeline**](DeliveryTimeline.md)

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

# **get_releases_for_delivery**
> [DeliveryFlowReleaseInfo] get_releases_for_delivery(delivery_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import delivery_api
from digitalai.release.v1.model.delivery_flow_release_info import DeliveryFlowReleaseInfo
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
    api_instance = delivery_api.DeliveryApi(api_client)
    delivery_id = "jUR,rZ#UM/?R,Fp^l6$ARjDeliveryQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_releases_for_delivery(delivery_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryApi->get_releases_for_delivery: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delivery_id** | **str**|  |

### Return type

[**[DeliveryFlowReleaseInfo]**](DeliveryFlowReleaseInfo.md)

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

# **get_stages_in_delivery**
> [Stage] get_stages_in_delivery(delivery_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import delivery_api
from digitalai.release.v1.model.stage import Stage
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
    api_instance = delivery_api.DeliveryApi(api_client)
    delivery_id = "jUR,rZ#UM/?R,Fp^l6$ARjDeliveryQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_stages_in_delivery(delivery_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryApi->get_stages_in_delivery: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delivery_id** | **str**|  |

### Return type

[**[Stage]**](Stage.md)

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

# **get_tracked_itemsin_delivery**
> [TrackedItem] get_tracked_itemsin_delivery(delivery_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import delivery_api
from digitalai.release.v1.model.tracked_item import TrackedItem
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
    api_instance = delivery_api.DeliveryApi(api_client)
    delivery_id = "jUR,rZ#UM/?R,Fp^l6$ARjDeliveryQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_tracked_itemsin_delivery(delivery_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryApi->get_tracked_itemsin_delivery: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delivery_id** | **str**|  |

### Return type

[**[TrackedItem]**](TrackedItem.md)

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

# **reopen_stage**
> reopen_stage(stage_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import delivery_api
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
    api_instance = delivery_api.DeliveryApi(api_client)
    stage_id = "jUR,rZ#UM/?R,Fp^l6$ARjStageQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.reopen_stage(stage_id)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryApi->reopen_stage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_id** | **str**|  |

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

# **rescope_tracked_item**
> rescope_tracked_item(item_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import delivery_api
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
    api_instance = delivery_api.DeliveryApi(api_client)
    item_id = "jUR,rZ#UM/?R,Fp^l6$ARjTrackedItemQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.rescope_tracked_item(item_id)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryApi->rescope_tracked_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  |

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

# **reset_tracked_item**
> reset_tracked_item(item_id, stage_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import delivery_api
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
    api_instance = delivery_api.DeliveryApi(api_client)
    item_id = "jUR,rZ#UM/?R,Fp^l6$ARjTrackedItemQ" # str | 
    stage_id = "jUR,rZ#UM/?R,Fp^l6$ARjStageQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.reset_tracked_item(item_id, stage_id)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryApi->reset_tracked_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  |
 **stage_id** | **str**|  |

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

# **search_deliveries**
> [Delivery] search_deliveries()



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import delivery_api
from digitalai.release.v1.model.delivery import Delivery
from digitalai.release.v1.model.delivery_filters import DeliveryFilters
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
    api_instance = delivery_api.DeliveryApi(api_client)
    order_by = None # bool, date, datetime, dict, float, int, list, str, none_type |  (optional)
    page = 0 # int |  (optional) if omitted the server will use the default value of 0
    results_per_page = 100 # int |  (optional) if omitted the server will use the default value of 100
    delivery_filters = DeliveryFilters(
        title="title_example",
        strict_title_match=True,
        tracked_item_title="tracked_item_title_example",
        strict_tracked_item_title_match=True,
        folder_id="folder_id_example",
        origin_pattern_id="origin_pattern_id_example",
        statuses=[
            DeliveryStatus("TEMPLATE"),
        ],
    ) # DeliveryFilters |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.search_deliveries(order_by=order_by, page=page, results_per_page=results_per_page, delivery_filters=delivery_filters)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryApi->search_deliveries: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_by** | **bool, date, datetime, dict, float, int, list, str, none_type**|  | [optional]
 **page** | **int**|  | [optional] if omitted the server will use the default value of 0
 **results_per_page** | **int**|  | [optional] if omitted the server will use the default value of 100
 **delivery_filters** | [**DeliveryFilters**](DeliveryFilters.md)|  | [optional]

### Return type

[**[Delivery]**](Delivery.md)

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

# **skip_tracked_item**
> skip_tracked_item(item_id, stage_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import delivery_api
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
    api_instance = delivery_api.DeliveryApi(api_client)
    item_id = "jUR,rZ#UM/?R,Fp^l6$ARjTrackedItemQ" # str | 
    stage_id = "jUR,rZ#UM/?R,Fp^l6$ARjStageQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.skip_tracked_item(item_id, stage_id)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryApi->skip_tracked_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  |
 **stage_id** | **str**|  |

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

# **update_delivery**
> Delivery update_delivery(delivery_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import delivery_api
from digitalai.release.v1.model.delivery import Delivery
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
    api_instance = delivery_api.DeliveryApi(api_client)
    delivery_id = "jUR,rZ#UM/?R,Fp^l6$ARjDeliveryQ" # str | 
    delivery = Delivery(
        metadata={
            "key": {},
        },
        title="title_example",
        description="description_example",
        status=DeliveryStatus("TEMPLATE"),
        start_date=dateutil_parser('2023-03-20T02:07:00Z'),
        end_date=dateutil_parser('2023-03-20T02:07:00Z'),
        planned_duration=1,
        release_ids=[
            "release_ids_example",
        ],
        folder_id="folder_id_example",
        origin_pattern_id="origin_pattern_id_example",
        stages=[
            Stage(
                id="id_example",
                type="type_example",
                title="title_example",
                status=StageStatus("OPEN"),
                items=[
                    StageTrackedItem(
                        tracked_item_id="tracked_item_id_example",
                        status=TrackedItemStatus("NOT_READY"),
                        release_ids=[
                            "release_ids_example",
                        ],
                    ),
                ],
                transition=Transition(
                    id="id_example",
                    type="type_example",
                    title="title_example",
                    stage=Stage(),
                    conditions=[
                        Condition(
                            id="id_example",
                            type="type_example",
                            satisfied=True,
                            satisfied_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            description="description_example",
                            active=True,
                            input_properties=[
                                None,
                            ],
                            leaf=True,
                            all_conditions=[],
                            leaf_conditions=[],
                        ),
                    ],
                    automated=True,
                    all_conditions=[
                        Condition(
                            id="id_example",
                            type="type_example",
                            satisfied=True,
                            satisfied_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            description="description_example",
                            active=True,
                            input_properties=[
                                None,
                            ],
                            leaf=True,
                            all_conditions=[],
                            leaf_conditions=[],
                        ),
                    ],
                    leaf_conditions=[
                        Condition(
                            id="id_example",
                            type="type_example",
                            satisfied=True,
                            satisfied_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            description="description_example",
                            active=True,
                            input_properties=[
                                None,
                            ],
                            leaf=True,
                            all_conditions=[],
                            leaf_conditions=[],
                        ),
                    ],
                    root_condition=Condition(
                        id="id_example",
                        type="type_example",
                        satisfied=True,
                        satisfied_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        description="description_example",
                        active=True,
                        input_properties=[
                            None,
                        ],
                        leaf=True,
                        all_conditions=[
                            Condition(),
                        ],
                        leaf_conditions=[
                            Condition(),
                        ],
                    ),
                ),
                owner="owner_example",
                team="team_example",
                open=True,
                closed=True,
            ),
        ],
        tracked_items=[
            TrackedItem(
                id="id_example",
                type="type_example",
                title="title_example",
                release_ids=[
                    "release_ids_example",
                ],
                descoped=True,
                created_date=dateutil_parser('2023-03-20T02:07:00Z'),
                modified_date=dateutil_parser('2023-03-20T02:07:00Z'),
            ),
        ],
        subscribers=[
            Subscriber(
                id="id_example",
                type="type_example",
                source_id="source_id_example",
            ),
        ],
        auto_complete=True,
        template=True,
        transitions=[
            Transition(
                id="id_example",
                type="type_example",
                title="title_example",
                stage=Stage(
                    id="id_example",
                    type="type_example",
                    title="title_example",
                    status=StageStatus("OPEN"),
                    items=[
                        StageTrackedItem(
                            tracked_item_id="tracked_item_id_example",
                            status=TrackedItemStatus("NOT_READY"),
                            release_ids=[
                                "release_ids_example",
                            ],
                        ),
                    ],
                    transition=Transition(),
                    owner="owner_example",
                    team="team_example",
                    open=True,
                    closed=True,
                ),
                conditions=[
                    Condition(
                        id="id_example",
                        type="type_example",
                        satisfied=True,
                        satisfied_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        description="description_example",
                        active=True,
                        input_properties=[
                            None,
                        ],
                        leaf=True,
                        all_conditions=[],
                        leaf_conditions=[],
                    ),
                ],
                automated=True,
                all_conditions=[
                    Condition(
                        id="id_example",
                        type="type_example",
                        satisfied=True,
                        satisfied_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        description="description_example",
                        active=True,
                        input_properties=[
                            None,
                        ],
                        leaf=True,
                        all_conditions=[],
                        leaf_conditions=[],
                    ),
                ],
                leaf_conditions=[
                    Condition(
                        id="id_example",
                        type="type_example",
                        satisfied=True,
                        satisfied_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        description="description_example",
                        active=True,
                        input_properties=[
                            None,
                        ],
                        leaf=True,
                        all_conditions=[],
                        leaf_conditions=[],
                    ),
                ],
                root_condition=Condition(
                    id="id_example",
                    type="type_example",
                    satisfied=True,
                    satisfied_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    description="description_example",
                    active=True,
                    input_properties=[
                        None,
                    ],
                    leaf=True,
                    all_conditions=[
                        Condition(),
                    ],
                    leaf_conditions=[
                        Condition(),
                    ],
                ),
            ),
        ],
        stages_before_first_open_transition=[
            Stage(
                id="id_example",
                type="type_example",
                title="title_example",
                status=StageStatus("OPEN"),
                items=[
                    StageTrackedItem(
                        tracked_item_id="tracked_item_id_example",
                        status=TrackedItemStatus("NOT_READY"),
                        release_ids=[
                            "release_ids_example",
                        ],
                    ),
                ],
                transition=Transition(
                    id="id_example",
                    type="type_example",
                    title="title_example",
                    stage=Stage(),
                    conditions=[
                        Condition(
                            id="id_example",
                            type="type_example",
                            satisfied=True,
                            satisfied_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            description="description_example",
                            active=True,
                            input_properties=[
                                None,
                            ],
                            leaf=True,
                            all_conditions=[],
                            leaf_conditions=[],
                        ),
                    ],
                    automated=True,
                    all_conditions=[
                        Condition(
                            id="id_example",
                            type="type_example",
                            satisfied=True,
                            satisfied_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            description="description_example",
                            active=True,
                            input_properties=[
                                None,
                            ],
                            leaf=True,
                            all_conditions=[],
                            leaf_conditions=[],
                        ),
                    ],
                    leaf_conditions=[
                        Condition(
                            id="id_example",
                            type="type_example",
                            satisfied=True,
                            satisfied_date=dateutil_parser('2023-03-20T02:07:00Z'),
                            description="description_example",
                            active=True,
                            input_properties=[
                                None,
                            ],
                            leaf=True,
                            all_conditions=[],
                            leaf_conditions=[],
                        ),
                    ],
                    root_condition=Condition(
                        id="id_example",
                        type="type_example",
                        satisfied=True,
                        satisfied_date=dateutil_parser('2023-03-20T02:07:00Z'),
                        description="description_example",
                        active=True,
                        input_properties=[
                            None,
                        ],
                        leaf=True,
                        all_conditions=[
                            Condition(),
                        ],
                        leaf_conditions=[
                            Condition(),
                        ],
                    ),
                ),
                owner="owner_example",
                team="team_example",
                open=True,
                closed=True,
            ),
        ],
        updatable=True,
    ) # Delivery |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_delivery(delivery_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryApi->update_delivery: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_delivery(delivery_id, delivery=delivery)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryApi->update_delivery: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delivery_id** | **str**|  |
 **delivery** | [**Delivery**](Delivery.md)|  | [optional]

### Return type

[**Delivery**](Delivery.md)

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

# **update_stage_in_delivery**
> Stage update_stage_in_delivery(stage_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import delivery_api
from digitalai.release.v1.model.stage import Stage
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
    api_instance = delivery_api.DeliveryApi(api_client)
    stage_id = "jUR,rZ#UM/?R,Fp^l6$ARjStageQ" # str | 
    stage = Stage(
        id="id_example",
        type="type_example",
        title="title_example",
        status=StageStatus("OPEN"),
        items=[
            StageTrackedItem(
                tracked_item_id="tracked_item_id_example",
                status=TrackedItemStatus("NOT_READY"),
                release_ids=[
                    "release_ids_example",
                ],
            ),
        ],
        transition=Transition(
            id="id_example",
            type="type_example",
            title="title_example",
            stage=Stage(),
            conditions=[
                Condition(
                    id="id_example",
                    type="type_example",
                    satisfied=True,
                    satisfied_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    description="description_example",
                    active=True,
                    input_properties=[
                        None,
                    ],
                    leaf=True,
                    all_conditions=[],
                    leaf_conditions=[],
                ),
            ],
            automated=True,
            all_conditions=[
                Condition(
                    id="id_example",
                    type="type_example",
                    satisfied=True,
                    satisfied_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    description="description_example",
                    active=True,
                    input_properties=[
                        None,
                    ],
                    leaf=True,
                    all_conditions=[],
                    leaf_conditions=[],
                ),
            ],
            leaf_conditions=[
                Condition(
                    id="id_example",
                    type="type_example",
                    satisfied=True,
                    satisfied_date=dateutil_parser('2023-03-20T02:07:00Z'),
                    description="description_example",
                    active=True,
                    input_properties=[
                        None,
                    ],
                    leaf=True,
                    all_conditions=[],
                    leaf_conditions=[],
                ),
            ],
            root_condition=Condition(
                id="id_example",
                type="type_example",
                satisfied=True,
                satisfied_date=dateutil_parser('2023-03-20T02:07:00Z'),
                description="description_example",
                active=True,
                input_properties=[
                    None,
                ],
                leaf=True,
                all_conditions=[
                    Condition(),
                ],
                leaf_conditions=[
                    Condition(),
                ],
            ),
        ),
        owner="owner_example",
        team="team_example",
        open=True,
        closed=True,
    ) # Stage |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_stage_in_delivery(stage_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryApi->update_stage_in_delivery: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_stage_in_delivery(stage_id, stage=stage)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryApi->update_stage_in_delivery: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_id** | **str**|  |
 **stage** | [**Stage**](Stage.md)|  | [optional]

### Return type

[**Stage**](Stage.md)

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

# **update_tracked_item_in_delivery**
> TrackedItem update_tracked_item_in_delivery(item_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import delivery_api
from digitalai.release.v1.model.tracked_item import TrackedItem
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
    api_instance = delivery_api.DeliveryApi(api_client)
    item_id = "jUR,rZ#UM/?R,Fp^l6$ARjTrackedItemQ" # str | 
    tracked_item = TrackedItem(
        id="id_example",
        type="type_example",
        title="title_example",
        release_ids=[
            "release_ids_example",
        ],
        descoped=True,
        created_date=dateutil_parser('2023-03-20T02:07:00Z'),
        modified_date=dateutil_parser('2023-03-20T02:07:00Z'),
    ) # TrackedItem |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_tracked_item_in_delivery(item_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryApi->update_tracked_item_in_delivery: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_tracked_item_in_delivery(item_id, tracked_item=tracked_item)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryApi->update_tracked_item_in_delivery: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  |
 **tracked_item** | [**TrackedItem**](TrackedItem.md)|  | [optional]

### Return type

[**TrackedItem**](TrackedItem.md)

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

# **update_transition_in_delivery**
> Transition update_transition_in_delivery(transition_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import delivery_api
from digitalai.release.v1.model.transition import Transition
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
    api_instance = delivery_api.DeliveryApi(api_client)
    transition_id = "jUR,rZ#UM/?R,Fp^l6$ARjTransitionQ" # str | 
    transition = Transition(
        id="id_example",
        type="type_example",
        title="title_example",
        stage=Stage(
            id="id_example",
            type="type_example",
            title="title_example",
            status=StageStatus("OPEN"),
            items=[
                StageTrackedItem(
                    tracked_item_id="tracked_item_id_example",
                    status=TrackedItemStatus("NOT_READY"),
                    release_ids=[
                        "release_ids_example",
                    ],
                ),
            ],
            transition=Transition(),
            owner="owner_example",
            team="team_example",
            open=True,
            closed=True,
        ),
        conditions=[
            Condition(
                id="id_example",
                type="type_example",
                satisfied=True,
                satisfied_date=dateutil_parser('2023-03-20T02:07:00Z'),
                description="description_example",
                active=True,
                input_properties=[
                    None,
                ],
                leaf=True,
                all_conditions=[],
                leaf_conditions=[],
            ),
        ],
        automated=True,
        all_conditions=[
            Condition(
                id="id_example",
                type="type_example",
                satisfied=True,
                satisfied_date=dateutil_parser('2023-03-20T02:07:00Z'),
                description="description_example",
                active=True,
                input_properties=[
                    None,
                ],
                leaf=True,
                all_conditions=[],
                leaf_conditions=[],
            ),
        ],
        leaf_conditions=[
            Condition(
                id="id_example",
                type="type_example",
                satisfied=True,
                satisfied_date=dateutil_parser('2023-03-20T02:07:00Z'),
                description="description_example",
                active=True,
                input_properties=[
                    None,
                ],
                leaf=True,
                all_conditions=[],
                leaf_conditions=[],
            ),
        ],
        root_condition=Condition(
            id="id_example",
            type="type_example",
            satisfied=True,
            satisfied_date=dateutil_parser('2023-03-20T02:07:00Z'),
            description="description_example",
            active=True,
            input_properties=[
                None,
            ],
            leaf=True,
            all_conditions=[
                Condition(),
            ],
            leaf_conditions=[
                Condition(),
            ],
        ),
    ) # Transition |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_transition_in_delivery(transition_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryApi->update_transition_in_delivery: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_transition_in_delivery(transition_id, transition=transition)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryApi->update_transition_in_delivery: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transition_id** | **str**|  |
 **transition** | [**Transition**](Transition.md)|  | [optional]

### Return type

[**Transition**](Transition.md)

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

