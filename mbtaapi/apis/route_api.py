# coding: utf-8

"""
    MBTA

    MBTA service API. https://www.mbta.com

    OpenAPI spec version: 3.0
    Contact: developer@mbta.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class RouteApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def api_web_route_controller_index(self, **kwargs):
        """
        
        List of routes.  ## Names and Descriptions  There are 3 attributes with increasing details for naming and describing the route.  1. `/data/{index}/attributes/short_name` 2. `/data/{index}/attributes/long_name` 3. `/data/{index}/attributes/description`  ## Directions  `/data/{index}/attributes/direction_names` is the only place to convert the `direction_id` used throughout the rest of the API to human-readable names.  ## Type  `/data/{index}/attributes/type` corresponds to [GTFS `routes.txt` `route_type`](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#routestxt).  | Value | Name          | Example    | |-------|---------------|------------| | `0`   | Light Rail    | Green Line | | `1`   | Heavy Rail    | Red Line   | | `2`   | Commuter Rail |            | | `3`   | Bus           |            | | `4`   | Ferry         |            |   
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.api_web_route_controller_index(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page_offset: Offset (0-based) of first element in the page
        :param int page_limit: Max number of elements to return
        :param str sort: Results can be [sorted](http://jsonapi.org/format/#fetching-sorting) by the id or any `/data/{index}/attributes` key. Assumes ascending; may be prefixed with '-' for descending  | JSON pointer | Direction | `sort`     | |--------------|-----------|------------| | `/data/{index}/attributes/description` | ascending | `description` | | `/data/{index}/attributes/description` | descending | `-description` | | `/data/{index}/attributes/direction_names` | ascending | `direction_names` | | `/data/{index}/attributes/direction_names` | descending | `-direction_names` | | `/data/{index}/attributes/long_name` | ascending | `long_name` | | `/data/{index}/attributes/long_name` | descending | `-long_name` | | `/data/{index}/attributes/short_name` | ascending | `short_name` | | `/data/{index}/attributes/short_name` | descending | `-short_name` | | `/data/{index}/attributes/sort_order` | ascending | `sort_order` | | `/data/{index}/attributes/sort_order` | descending | `-sort_order` | | `/data/{index}/attributes/type` | ascending | `type` | | `/data/{index}/attributes/type` | descending | `-type` |  
        :param str api_key: Key for API access.  Without api_key, requests will be tracked by IP address and have stricter rate limit. [Register for a key](/register) 
        :param str include: Relationships to include.  * `stop`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)  include=stop only works when `filter[stop]` is also used 
        :param str filter_stop: Filter by `/data/{index}/relationships/stop/data/id`. Must filter by stop in order to include stop with response
        :param str filter_type: | Value | Name          | Example    | |-------|---------------|------------| | `0`   | Light Rail    | Green Line | | `1`   | Heavy Rail    | Red Line   | | `2`   | Commuter Rail |            | | `3`   | Bus           |            | | `4`   | Ferry         |            | 
        :param str filter_direction_id: Filter by direction of travel along the route.  The meaning of `direction_id` varies based on the route. You can programmatically get the direction names from `/routes` `/data/{index}/attributes/direction_names` or `/routes/{id}` `/data/attributes/direction_names`.   When combined with stop_id, filters by routes which stop at that stop when traveling in a particular direction 
        :param date filter_date: Filter by date that route is active YYYY-MM-DD
        :return: Routes
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.api_web_route_controller_index_with_http_info(**kwargs)
        else:
            (data) = self.api_web_route_controller_index_with_http_info(**kwargs)
            return data

    def api_web_route_controller_index_with_http_info(self, **kwargs):
        """
        
        List of routes.  ## Names and Descriptions  There are 3 attributes with increasing details for naming and describing the route.  1. `/data/{index}/attributes/short_name` 2. `/data/{index}/attributes/long_name` 3. `/data/{index}/attributes/description`  ## Directions  `/data/{index}/attributes/direction_names` is the only place to convert the `direction_id` used throughout the rest of the API to human-readable names.  ## Type  `/data/{index}/attributes/type` corresponds to [GTFS `routes.txt` `route_type`](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#routestxt).  | Value | Name          | Example    | |-------|---------------|------------| | `0`   | Light Rail    | Green Line | | `1`   | Heavy Rail    | Red Line   | | `2`   | Commuter Rail |            | | `3`   | Bus           |            | | `4`   | Ferry         |            |   
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.api_web_route_controller_index_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page_offset: Offset (0-based) of first element in the page
        :param int page_limit: Max number of elements to return
        :param str sort: Results can be [sorted](http://jsonapi.org/format/#fetching-sorting) by the id or any `/data/{index}/attributes` key. Assumes ascending; may be prefixed with '-' for descending  | JSON pointer | Direction | `sort`     | |--------------|-----------|------------| | `/data/{index}/attributes/description` | ascending | `description` | | `/data/{index}/attributes/description` | descending | `-description` | | `/data/{index}/attributes/direction_names` | ascending | `direction_names` | | `/data/{index}/attributes/direction_names` | descending | `-direction_names` | | `/data/{index}/attributes/long_name` | ascending | `long_name` | | `/data/{index}/attributes/long_name` | descending | `-long_name` | | `/data/{index}/attributes/short_name` | ascending | `short_name` | | `/data/{index}/attributes/short_name` | descending | `-short_name` | | `/data/{index}/attributes/sort_order` | ascending | `sort_order` | | `/data/{index}/attributes/sort_order` | descending | `-sort_order` | | `/data/{index}/attributes/type` | ascending | `type` | | `/data/{index}/attributes/type` | descending | `-type` |  
        :param str api_key: Key for API access.  Without api_key, requests will be tracked by IP address and have stricter rate limit. [Register for a key](/register) 
        :param str include: Relationships to include.  * `stop`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)  include=stop only works when `filter[stop]` is also used 
        :param str filter_stop: Filter by `/data/{index}/relationships/stop/data/id`. Must filter by stop in order to include stop with response
        :param str filter_type: | Value | Name          | Example    | |-------|---------------|------------| | `0`   | Light Rail    | Green Line | | `1`   | Heavy Rail    | Red Line   | | `2`   | Commuter Rail |            | | `3`   | Bus           |            | | `4`   | Ferry         |            | 
        :param str filter_direction_id: Filter by direction of travel along the route.  The meaning of `direction_id` varies based on the route. You can programmatically get the direction names from `/routes` `/data/{index}/attributes/direction_names` or `/routes/{id}` `/data/attributes/direction_names`.   When combined with stop_id, filters by routes which stop at that stop when traveling in a particular direction 
        :param date filter_date: Filter by date that route is active YYYY-MM-DD
        :return: Routes
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_offset', 'page_limit', 'sort', 'api_key', 'include', 'filter_stop', 'filter_type', 'filter_direction_id', 'filter_date']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_web_route_controller_index" % key
                )
            params[key] = val
        del params['kwargs']

        if 'page_offset' in params and params['page_offset'] < 0:
            raise ValueError("Invalid value for parameter `page_offset` when calling `api_web_route_controller_index`, must be a value greater than or equal to `0`")
        if 'page_limit' in params and params['page_limit'] < 1:
            raise ValueError("Invalid value for parameter `page_limit` when calling `api_web_route_controller_index`, must be a value greater than or equal to `1`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_offset' in params:
            query_params.append(('page[offset]', params['page_offset']))
        if 'page_limit' in params:
            query_params.append(('page[limit]', params['page_limit']))
        if 'sort' in params:
            query_params.append(('sort', params['sort']))
        if 'api_key' in params:
            query_params.append(('api_key', params['api_key']))
        if 'include' in params:
            query_params.append(('include', params['include']))
        if 'filter_stop' in params:
            query_params.append(('filter[stop]', params['filter_stop']))
        if 'filter_type' in params:
            query_params.append(('filter[type]', params['filter_type']))
        if 'filter_direction_id' in params:
            query_params.append(('filter[direction_id]', params['filter_direction_id']))
        if 'filter_date' in params:
            query_params.append(('filter[date]', params['filter_date']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/vnd.api+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/vnd.api+json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/routes', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Routes',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def api_web_route_controller_show(self, id, **kwargs):
        """
        
        Show a particular route by the route's id.  ## Names and Descriptions  There are 3 attributes with increasing details for naming and describing the route.  1. `/data/attributes/short_name` 2. `/data/attributes/long_name` 3. `/data/attributes/description`  ## Directions  `/data/attributes/direction_names` is the only place to convert the `direction_id` used throughout the rest of the API to human-readable names.  ## Type  `/data/attributes/type` corresponds to [GTFS `routes.txt` `route_type`](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#routestxt).  | Value | Name          | Example    | |-------|---------------|------------| | `0`   | Light Rail    | Green Line | | `1`   | Heavy Rail    | Red Line   | | `2`   | Commuter Rail |            | | `3`   | Bus           |            | | `4`   | Ferry         |            |   
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.api_web_route_controller_show(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: Unique identifier for route (required)
        :param str api_key: Key for API access.  Without api_key, requests will be tracked by IP address and have stricter rate limit. [Register for a key](/register) 
        :param str include: Relationships to include.  * `stop`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)   
        :return: Route
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.api_web_route_controller_show_with_http_info(id, **kwargs)
        else:
            (data) = self.api_web_route_controller_show_with_http_info(id, **kwargs)
            return data

    def api_web_route_controller_show_with_http_info(self, id, **kwargs):
        """
        
        Show a particular route by the route's id.  ## Names and Descriptions  There are 3 attributes with increasing details for naming and describing the route.  1. `/data/attributes/short_name` 2. `/data/attributes/long_name` 3. `/data/attributes/description`  ## Directions  `/data/attributes/direction_names` is the only place to convert the `direction_id` used throughout the rest of the API to human-readable names.  ## Type  `/data/attributes/type` corresponds to [GTFS `routes.txt` `route_type`](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#routestxt).  | Value | Name          | Example    | |-------|---------------|------------| | `0`   | Light Rail    | Green Line | | `1`   | Heavy Rail    | Red Line   | | `2`   | Commuter Rail |            | | `3`   | Bus           |            | | `4`   | Ferry         |            |   
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.api_web_route_controller_show_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: Unique identifier for route (required)
        :param str api_key: Key for API access.  Without api_key, requests will be tracked by IP address and have stricter rate limit. [Register for a key](/register) 
        :param str include: Relationships to include.  * `stop`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)   
        :return: Route
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'api_key', 'include']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_web_route_controller_show" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `api_web_route_controller_show`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = []
        if 'api_key' in params:
            query_params.append(('api_key', params['api_key']))
        if 'include' in params:
            query_params.append(('include', params['include']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/vnd.api+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/vnd.api+json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/routes/{id}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Route',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
