# digitalai.release.v1.FacetApi

All URIs are relative to *http://localhost:5516*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_facet**](FacetApi.md#create_facet) | **POST** /api/v1/facets | 
[**delete_facet**](FacetApi.md#delete_facet) | **DELETE** /api/v1/facets/{facetId} | 
[**get_facet**](FacetApi.md#get_facet) | **GET** /api/v1/facets/{facetId} | 
[**get_facet_types**](FacetApi.md#get_facet_types) | **GET** /api/v1/facets/types | 
[**search_facets**](FacetApi.md#search_facets) | **POST** /api/v1/facets/search | 
[**update_facet**](FacetApi.md#update_facet) | **PUT** /api/v1/facets/{facetId} | 


# **create_facet**
> Facet create_facet()



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import facet_api
from digitalai.release.v1.model.facet import Facet
from digitalai.release.v1.model.configuration_facet import ConfigurationFacet
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
    api_instance = facet_api.FacetApi(api_client)
    configuration_facet = ConfigurationFacet(
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
    ) # ConfigurationFacet |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_facet(configuration_facet=configuration_facet)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling FacetApi->create_facet: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_facet** | [**ConfigurationFacet**](ConfigurationFacet.md)|  | [optional]

### Return type

[**Facet**](Facet.md)

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

# **delete_facet**
> delete_facet(facet_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import facet_api
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
    api_instance = facet_api.FacetApi(api_client)
    facet_id = "jUR,rZ#UM/?R,Fp^l6$ARjFacetQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_facet(facet_id)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling FacetApi->delete_facet: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facet_id** | **str**|  |

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

# **get_facet**
> Facet get_facet(facet_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import facet_api
from digitalai.release.v1.model.facet import Facet
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
    api_instance = facet_api.FacetApi(api_client)
    facet_id = "jUR,rZ#UM/?R,Fp^l6$ARjFacet^" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_facet(facet_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling FacetApi->get_facet: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facet_id** | **str**|  |

### Return type

[**Facet**](Facet.md)

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

# **get_facet_types**
> [bool, date, datetime, dict, float, int, list, str, none_type] get_facet_types()



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import facet_api
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
    api_instance = facet_api.FacetApi(api_client)
    base_type = "baseType_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_facet_types(base_type=base_type)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling FacetApi->get_facet_types: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_type** | **str**|  | [optional]

### Return type

**[bool, date, datetime, dict, float, int, list, str, none_type]**

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

# **search_facets**
> [Facet] search_facets()



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import facet_api
from digitalai.release.v1.model.facet import Facet
from digitalai.release.v1.model.facet_filters import FacetFilters
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
    api_instance = facet_api.FacetApi(api_client)
    facet_filters = FacetFilters(
        parent_id="parent_id_example",
        target_id="target_id_example",
        types=[
            None,
        ],
    ) # FacetFilters |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.search_facets(facet_filters=facet_filters)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling FacetApi->search_facets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facet_filters** | [**FacetFilters**](FacetFilters.md)|  | [optional]

### Return type

[**[Facet]**](Facet.md)

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

# **update_facet**
> Facet update_facet(facet_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import facet_api
from digitalai.release.v1.model.facet import Facet
from digitalai.release.v1.model.configuration_facet import ConfigurationFacet
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
    api_instance = facet_api.FacetApi(api_client)
    facet_id = "jUR,rZ#UM/?R,Fp^l6$ARjFacetQ" # str | 
    configuration_facet = ConfigurationFacet(
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
    ) # ConfigurationFacet |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_facet(facet_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling FacetApi->update_facet: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_facet(facet_id, configuration_facet=configuration_facet)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling FacetApi->update_facet: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facet_id** | **str**|  |
 **configuration_facet** | [**ConfigurationFacet**](ConfigurationFacet.md)|  | [optional]

### Return type

[**Facet**](Facet.md)

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

