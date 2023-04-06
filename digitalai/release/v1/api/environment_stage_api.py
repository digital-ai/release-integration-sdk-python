"""
    Digital.ai Release API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from digitalai.release.v1.api_client import ApiClient, Endpoint as _Endpoint
from digitalai.release.v1.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from digitalai.release.v1.model.environment_stage_filters import EnvironmentStageFilters
from digitalai.release.v1.model.environment_stage_form import EnvironmentStageForm
from digitalai.release.v1.model.environment_stage_view import EnvironmentStageView


class EnvironmentStageApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_stage3_endpoint = _Endpoint(
            settings={
                'response_type': (EnvironmentStageView,),
                'auth': [
                    'basicAuth',
                    'patAuth'
                ],
                'endpoint_path': '/api/v1/environments/stages',
                'operation_id': 'create_stage3',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'environment_stage_form',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'environment_stage_form':
                        (EnvironmentStageForm,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'environment_stage_form': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.delete_environment_stage_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'basicAuth',
                    'patAuth'
                ],
                'endpoint_path': '/api/v1/environments/stages/{environmentStageId}',
                'operation_id': 'delete_environment_stage',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'environment_stage_id',
                ],
                'required': [
                    'environment_stage_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'environment_stage_id',
                ]
            },
            root_map={
                'validations': {
                    ('environment_stage_id',): {

                        'regex': {
                            'pattern': r'.*\/EnvironmentStage[^\/]*',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'environment_stage_id':
                        (str,),
                },
                'attribute_map': {
                    'environment_stage_id': 'environmentStageId',
                },
                'location_map': {
                    'environment_stage_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_stage_by_id_endpoint = _Endpoint(
            settings={
                'response_type': (EnvironmentStageView,),
                'auth': [
                    'basicAuth',
                    'patAuth'
                ],
                'endpoint_path': '/api/v1/environments/stages/{environmentStageId}',
                'operation_id': 'get_stage_by_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'environment_stage_id',
                ],
                'required': [
                    'environment_stage_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'environment_stage_id',
                ]
            },
            root_map={
                'validations': {
                    ('environment_stage_id',): {

                        'regex': {
                            'pattern': r'.*\/EnvironmentStage[^\/]*',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'environment_stage_id':
                        (str,),
                },
                'attribute_map': {
                    'environment_stage_id': 'environmentStageId',
                },
                'location_map': {
                    'environment_stage_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.search_stages_endpoint = _Endpoint(
            settings={
                'response_type': ([EnvironmentStageView],),
                'auth': [
                    'basicAuth',
                    'patAuth'
                ],
                'endpoint_path': '/api/v1/environments/stages/search',
                'operation_id': 'search_stages',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'environment_stage_filters',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'environment_stage_filters':
                        (EnvironmentStageFilters,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'environment_stage_filters': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.update_stage_in_environment_endpoint = _Endpoint(
            settings={
                'response_type': (EnvironmentStageView,),
                'auth': [
                    'basicAuth',
                    'patAuth'
                ],
                'endpoint_path': '/api/v1/environments/stages/{environmentStageId}',
                'operation_id': 'update_stage_in_environment',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'environment_stage_id',
                    'environment_stage_form',
                ],
                'required': [
                    'environment_stage_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'environment_stage_id',
                ]
            },
            root_map={
                'validations': {
                    ('environment_stage_id',): {

                        'regex': {
                            'pattern': r'.*\/EnvironmentStage[^\/]*',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'environment_stage_id':
                        (str,),
                    'environment_stage_form':
                        (EnvironmentStageForm,),
                },
                'attribute_map': {
                    'environment_stage_id': 'environmentStageId',
                },
                'location_map': {
                    'environment_stage_id': 'path',
                    'environment_stage_form': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def create_stage3(
        self,
        **kwargs
    ):
        """create_stage3  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_stage3(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            environment_stage_form (EnvironmentStageForm): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            EnvironmentStageView
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.create_stage3_endpoint.call_with_http_info(**kwargs)

    def delete_environment_stage(
        self,
        environment_stage_id,
        **kwargs
    ):
        """delete_environment_stage  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_environment_stage(environment_stage_id, async_req=True)
        >>> result = thread.get()

        Args:
            environment_stage_id (str):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['environment_stage_id'] = \
            environment_stage_id
        return self.delete_environment_stage_endpoint.call_with_http_info(**kwargs)

    def get_stage_by_id(
        self,
        environment_stage_id,
        **kwargs
    ):
        """get_stage_by_id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_stage_by_id(environment_stage_id, async_req=True)
        >>> result = thread.get()

        Args:
            environment_stage_id (str):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            EnvironmentStageView
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['environment_stage_id'] = \
            environment_stage_id
        return self.get_stage_by_id_endpoint.call_with_http_info(**kwargs)

    def search_stages(
        self,
        **kwargs
    ):
        """search_stages  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_stages(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            environment_stage_filters (EnvironmentStageFilters): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            [EnvironmentStageView]
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.search_stages_endpoint.call_with_http_info(**kwargs)

    def update_stage_in_environment(
        self,
        environment_stage_id,
        **kwargs
    ):
        """update_stage_in_environment  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_stage_in_environment(environment_stage_id, async_req=True)
        >>> result = thread.get()

        Args:
            environment_stage_id (str):

        Keyword Args:
            environment_stage_form (EnvironmentStageForm): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            EnvironmentStageView
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['environment_stage_id'] = \
            environment_stage_id
        return self.update_stage_in_environment_endpoint.call_with_http_info(**kwargs)

