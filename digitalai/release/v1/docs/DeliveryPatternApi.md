# digitalai.release.v1.DeliveryPatternApi

All URIs are relative to *http://localhost:5516*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_title**](DeliveryPatternApi.md#check_title) | **POST** /api/v1/delivery-patterns/checkTitle | 
[**create_delivery_from_pattern**](DeliveryPatternApi.md#create_delivery_from_pattern) | **POST** /api/v1/delivery-patterns/{patternId}/create | 
[**create_pattern**](DeliveryPatternApi.md#create_pattern) | **POST** /api/v1/delivery-patterns | 
[**create_stage**](DeliveryPatternApi.md#create_stage) | **POST** /api/v1/delivery-patterns/{patternId}/createStage | 
[**create_stage1**](DeliveryPatternApi.md#create_stage1) | **POST** /api/v1/delivery-patterns/{patternId}/stages | 
[**create_stage2**](DeliveryPatternApi.md#create_stage2) | **POST** /api/v1/delivery-patterns/{patternId}/stages/{position} | 
[**create_tracked_item_in_pattern**](DeliveryPatternApi.md#create_tracked_item_in_pattern) | **POST** /api/v1/delivery-patterns/{patternId}/tracked-items | 
[**create_transition**](DeliveryPatternApi.md#create_transition) | **POST** /api/v1/delivery-patterns/{stageId}/transitions | 
[**delete_pattern**](DeliveryPatternApi.md#delete_pattern) | **DELETE** /api/v1/delivery-patterns/{patternId} | 
[**delete_stage**](DeliveryPatternApi.md#delete_stage) | **DELETE** /api/v1/delivery-patterns/{stageId} | 
[**delete_tracked_item_delivery_pattern**](DeliveryPatternApi.md#delete_tracked_item_delivery_pattern) | **DELETE** /api/v1/delivery-patterns/{itemId} | 
[**delete_transition**](DeliveryPatternApi.md#delete_transition) | **DELETE** /api/v1/delivery-patterns/{transitionId} | 
[**duplicate_pattern**](DeliveryPatternApi.md#duplicate_pattern) | **POST** /api/v1/delivery-patterns/{patternId}/duplicate | 
[**get_pattern**](DeliveryPatternApi.md#get_pattern) | **GET** /api/v1/delivery-patterns/{patternId} | 
[**get_pattern_by_id_or_title**](DeliveryPatternApi.md#get_pattern_by_id_or_title) | **GET** /api/v1/delivery-patterns/{patternIdOrTitle} | 
[**get_stages_in_pattern**](DeliveryPatternApi.md#get_stages_in_pattern) | **GET** /api/v1/delivery-patterns/{patternId}/stages | 
[**get_tracked_items_in_pattern**](DeliveryPatternApi.md#get_tracked_items_in_pattern) | **GET** /api/v1/delivery-patterns/{patternId}/tracked-items | 
[**search_patterns**](DeliveryPatternApi.md#search_patterns) | **POST** /api/v1/delivery-patterns/search | 
[**update_pattern**](DeliveryPatternApi.md#update_pattern) | **PUT** /api/v1/delivery-patterns/{patternId} | 
[**update_stage_from_batch**](DeliveryPatternApi.md#update_stage_from_batch) | **PUT** /api/v1/delivery-patterns/{stageId}/batched | 
[**update_stage_in_pattern**](DeliveryPatternApi.md#update_stage_in_pattern) | **PUT** /api/v1/delivery-patterns/{stageId} | 
[**update_tracked_item_in_pattern**](DeliveryPatternApi.md#update_tracked_item_in_pattern) | **PUT** /api/v1/delivery-patterns/{itemId} | 
[**update_transition_in_pattern**](DeliveryPatternApi.md#update_transition_in_pattern) | **PUT** /api/v1/delivery-patterns/{transitionId} | 


# **check_title**
> bool check_title()



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import delivery_pattern_api
from digitalai.release.v1.model.validate_pattern import ValidatePattern
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
    api_instance = delivery_pattern_api.DeliveryPatternApi(api_client)
    validate_pattern = ValidatePattern(
        id="id_example",
        title="title_example",
    ) # ValidatePattern |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.check_title(validate_pattern=validate_pattern)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryPatternApi->check_title: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validate_pattern** | [**ValidatePattern**](ValidatePattern.md)|  | [optional]

### Return type

**bool**

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

# **create_delivery_from_pattern**
> Delivery create_delivery_from_pattern(pattern_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import delivery_pattern_api
from digitalai.release.v1.model.delivery import Delivery
from digitalai.release.v1.model.create_delivery import CreateDelivery
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
    api_instance = delivery_pattern_api.DeliveryPatternApi(api_client)
    pattern_id = "jUR,rZ#UM/?R,Fp^l6$ARjDeliveryQ" # str | 
    create_delivery = CreateDelivery(
        id="id_example",
        type="type_example",
        folder_id="folder_id_example",
        title="title_example",
        description="description_example",
        duration=1,
        start_date=dateutil_parser('2023-03-20T02:07:00Z'),
        end_date=dateutil_parser('2023-03-20T02:07:00Z'),
        auto_complete=True,
    ) # CreateDelivery |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_delivery_from_pattern(pattern_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryPatternApi->create_delivery_from_pattern: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_delivery_from_pattern(pattern_id, create_delivery=create_delivery)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryPatternApi->create_delivery_from_pattern: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pattern_id** | **str**|  |
 **create_delivery** | [**CreateDelivery**](CreateDelivery.md)|  | [optional]

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

# **create_pattern**
> Delivery create_pattern()



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import delivery_pattern_api
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
    api_instance = delivery_pattern_api.DeliveryPatternApi(api_client)
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
    # and optional values
    try:
        api_response = api_instance.create_pattern(delivery=delivery)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryPatternApi->create_pattern: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **create_stage**
> Stage create_stage(pattern_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import delivery_pattern_api
from digitalai.release.v1.model.create_delivery_stage import CreateDeliveryStage
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
    api_instance = delivery_pattern_api.DeliveryPatternApi(api_client)
    pattern_id = "jUR,rZ#UM/?R,Fp^l6$ARjDeliveryQ" # str | 
    create_delivery_stage = CreateDeliveryStage(
        after="after_example",
        before="before_example",
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
    ) # CreateDeliveryStage |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_stage(pattern_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryPatternApi->create_stage: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_stage(pattern_id, create_delivery_stage=create_delivery_stage)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryPatternApi->create_stage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pattern_id** | **str**|  |
 **create_delivery_stage** | [**CreateDeliveryStage**](CreateDeliveryStage.md)|  | [optional]

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

# **create_stage1**
> Stage create_stage1(pattern_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import delivery_pattern_api
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
    api_instance = delivery_pattern_api.DeliveryPatternApi(api_client)
    pattern_id = "jUR,rZ#UM/?R,Fp^l6$ARjDeliveryQ" # str | 
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
        api_response = api_instance.create_stage1(pattern_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryPatternApi->create_stage1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_stage1(pattern_id, stage=stage)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryPatternApi->create_stage1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pattern_id** | **str**|  |
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

# **create_stage2**
> Stage create_stage2(pattern_id, position)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import delivery_pattern_api
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
    api_instance = delivery_pattern_api.DeliveryPatternApi(api_client)
    pattern_id = "jUR,rZ#UM/?R,Fp^l6$ARjDeliveryQ" # str | 
    position = 1 # int | 
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
        api_response = api_instance.create_stage2(pattern_id, position)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryPatternApi->create_stage2: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_stage2(pattern_id, position, stage=stage)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryPatternApi->create_stage2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pattern_id** | **str**|  |
 **position** | **int**|  |
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

# **create_tracked_item_in_pattern**
> TrackedItem create_tracked_item_in_pattern(pattern_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import delivery_pattern_api
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
    api_instance = delivery_pattern_api.DeliveryPatternApi(api_client)
    pattern_id = "jUR,rZ#UM/?R,Fp^l6$ARjDeliveryQ" # str | 
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
        api_response = api_instance.create_tracked_item_in_pattern(pattern_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryPatternApi->create_tracked_item_in_pattern: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_tracked_item_in_pattern(pattern_id, tracked_item=tracked_item)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryPatternApi->create_tracked_item_in_pattern: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pattern_id** | **str**|  |
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

# **create_transition**
> Transition create_transition(stage_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import delivery_pattern_api
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
    api_instance = delivery_pattern_api.DeliveryPatternApi(api_client)
    stage_id = "jUR,rZ#UM/?R,Fp^l6$ARjStageQ" # str | 
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
        api_response = api_instance.create_transition(stage_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryPatternApi->create_transition: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_transition(stage_id, transition=transition)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryPatternApi->create_transition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage_id** | **str**|  |
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

# **delete_pattern**
> delete_pattern(pattern_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import delivery_pattern_api
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
    api_instance = delivery_pattern_api.DeliveryPatternApi(api_client)
    pattern_id = "jUR,rZ#UM/?R,Fp^l6$ARjDeliveryQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_pattern(pattern_id)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryPatternApi->delete_pattern: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pattern_id** | **str**|  |

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

# **delete_stage**
> delete_stage(stage_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import delivery_pattern_api
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
    api_instance = delivery_pattern_api.DeliveryPatternApi(api_client)
    stage_id = "jUR,rZ#UM/?R,Fp^l6$ARjStageQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_stage(stage_id)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryPatternApi->delete_stage: %s\n" % e)
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
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tracked_item_delivery_pattern**
> delete_tracked_item_delivery_pattern(item_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import delivery_pattern_api
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
    api_instance = delivery_pattern_api.DeliveryPatternApi(api_client)
    item_id = "jUR,rZ#UM/?R,Fp^l6$ARjTrackedItemQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_tracked_item_delivery_pattern(item_id)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryPatternApi->delete_tracked_item_delivery_pattern: %s\n" % e)
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

# **delete_transition**
> delete_transition(transition_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import delivery_pattern_api
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
    api_instance = delivery_pattern_api.DeliveryPatternApi(api_client)
    transition_id = "jUR,rZ#UM/?R,Fp^l6$ARjTransitionQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_transition(transition_id)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryPatternApi->delete_transition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transition_id** | **str**|  |

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

# **duplicate_pattern**
> Delivery duplicate_pattern(pattern_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import delivery_pattern_api
from digitalai.release.v1.model.delivery import Delivery
from digitalai.release.v1.model.duplicate_delivery_pattern import DuplicateDeliveryPattern
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
    api_instance = delivery_pattern_api.DeliveryPatternApi(api_client)
    pattern_id = "jUR,rZ#UM/?R,Fp^l6$ARjDeliveryQ" # str | 
    duplicate_delivery_pattern = DuplicateDeliveryPattern(
        title="title_example",
        description="description_example",
    ) # DuplicateDeliveryPattern |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.duplicate_pattern(pattern_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryPatternApi->duplicate_pattern: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.duplicate_pattern(pattern_id, duplicate_delivery_pattern=duplicate_delivery_pattern)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryPatternApi->duplicate_pattern: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pattern_id** | **str**|  |
 **duplicate_delivery_pattern** | [**DuplicateDeliveryPattern**](DuplicateDeliveryPattern.md)|  | [optional]

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

# **get_pattern**
> Delivery get_pattern(pattern_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import delivery_pattern_api
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
    api_instance = delivery_pattern_api.DeliveryPatternApi(api_client)
    pattern_id = "jUR,rZ#UM/?R,Fp^l6$ARjDeliveryQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_pattern(pattern_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryPatternApi->get_pattern: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pattern_id** | **str**|  |

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

# **get_pattern_by_id_or_title**
> Delivery get_pattern_by_id_or_title(pattern_id_or_title)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import delivery_pattern_api
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
    api_instance = delivery_pattern_api.DeliveryPatternApi(api_client)
    pattern_id_or_title = "patternIdOrTitle_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_pattern_by_id_or_title(pattern_id_or_title)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryPatternApi->get_pattern_by_id_or_title: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pattern_id_or_title** | **str**|  |

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

# **get_stages_in_pattern**
> [Stage] get_stages_in_pattern(pattern_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import delivery_pattern_api
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
    api_instance = delivery_pattern_api.DeliveryPatternApi(api_client)
    pattern_id = "jUR,rZ#UM/?R,Fp^l6$ARjDeliveryQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_stages_in_pattern(pattern_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryPatternApi->get_stages_in_pattern: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pattern_id** | **str**|  |

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

# **get_tracked_items_in_pattern**
> [TrackedItem] get_tracked_items_in_pattern(pattern_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import delivery_pattern_api
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
    api_instance = delivery_pattern_api.DeliveryPatternApi(api_client)
    pattern_id = "jUR,rZ#UM/?R,Fp^l6$ARjDeliveryQ" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_tracked_items_in_pattern(pattern_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryPatternApi->get_tracked_items_in_pattern: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pattern_id** | **str**|  |

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

# **search_patterns**
> [Delivery] search_patterns()



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import delivery_pattern_api
from digitalai.release.v1.model.delivery import Delivery
from digitalai.release.v1.model.delivery_pattern_filters import DeliveryPatternFilters
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
    api_instance = delivery_pattern_api.DeliveryPatternApi(api_client)
    page = 0 # int |  (optional) if omitted the server will use the default value of 0
    results_per_page = 100 # int |  (optional) if omitted the server will use the default value of 100
    delivery_pattern_filters = DeliveryPatternFilters(
        title="title_example",
        strict_title_match=True,
        tracked_item_title="tracked_item_title_example",
        strict_tracked_item_title_match=True,
        folder_id="folder_id_example",
        statuses=[
            DeliveryStatus("TEMPLATE"),
        ],
    ) # DeliveryPatternFilters |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.search_patterns(page=page, results_per_page=results_per_page, delivery_pattern_filters=delivery_pattern_filters)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryPatternApi->search_patterns: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] if omitted the server will use the default value of 0
 **results_per_page** | **int**|  | [optional] if omitted the server will use the default value of 100
 **delivery_pattern_filters** | [**DeliveryPatternFilters**](DeliveryPatternFilters.md)|  | [optional]

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

# **update_pattern**
> Delivery update_pattern(pattern_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import delivery_pattern_api
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
    api_instance = delivery_pattern_api.DeliveryPatternApi(api_client)
    pattern_id = "jUR,rZ#UM/?R,Fp^l6$ARjDeliveryQ" # str | 
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
        api_response = api_instance.update_pattern(pattern_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryPatternApi->update_pattern: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_pattern(pattern_id, delivery=delivery)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryPatternApi->update_pattern: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pattern_id** | **str**|  |
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

# **update_stage_from_batch**
> Stage update_stage_from_batch(stage_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import delivery_pattern_api
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
    api_instance = delivery_pattern_api.DeliveryPatternApi(api_client)
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
        api_response = api_instance.update_stage_from_batch(stage_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryPatternApi->update_stage_from_batch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_stage_from_batch(stage_id, stage=stage)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryPatternApi->update_stage_from_batch: %s\n" % e)
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

# **update_stage_in_pattern**
> Stage update_stage_in_pattern(stage_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import delivery_pattern_api
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
    api_instance = delivery_pattern_api.DeliveryPatternApi(api_client)
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
        api_response = api_instance.update_stage_in_pattern(stage_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryPatternApi->update_stage_in_pattern: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_stage_in_pattern(stage_id, stage=stage)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryPatternApi->update_stage_in_pattern: %s\n" % e)
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

# **update_tracked_item_in_pattern**
> TrackedItem update_tracked_item_in_pattern(item_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import delivery_pattern_api
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
    api_instance = delivery_pattern_api.DeliveryPatternApi(api_client)
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
        api_response = api_instance.update_tracked_item_in_pattern(item_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryPatternApi->update_tracked_item_in_pattern: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_tracked_item_in_pattern(item_id, tracked_item=tracked_item)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryPatternApi->update_tracked_item_in_pattern: %s\n" % e)
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

# **update_transition_in_pattern**
> Transition update_transition_in_pattern(transition_id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (patAuth):

```python
import time
import digitalai.release.v1
from digitalai.release.v1.api import delivery_pattern_api
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
    api_instance = delivery_pattern_api.DeliveryPatternApi(api_client)
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
        api_response = api_instance.update_transition_in_pattern(transition_id)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryPatternApi->update_transition_in_pattern: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_transition_in_pattern(transition_id, transition=transition)
        pprint(api_response)
    except digitalai.release.v1.ApiException as e:
        print("Exception when calling DeliveryPatternApi->update_transition_in_pattern: %s\n" % e)
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

