# digitalai.release.v1.RiskAssessmentApi

All URIs are relative to *http://localhost:5516*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_assessment**](RiskAssessmentApi.md#get_assessment) | **GET** /api/v1/risks/assessments/{riskAssessmentId} | 


# **get_assessment**
> RiskAssessment get_assessment(risk_assessment_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import risk_assessment_api
from digitalai.release.v1.model.risk_assessment import RiskAssessment
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
    api_instance = risk_assessment_api.RiskAssessmentApi(api_client)
    risk_assessment_id = "jUR,rZ#UM/?R,Fp^l6$ARjRiskAssessment^" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_assessment(risk_assessment_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling RiskAssessmentApi->get_assessment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **risk_assessment_id** | **str**|  |

### Return type

[**RiskAssessment**](RiskAssessment.md)

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

