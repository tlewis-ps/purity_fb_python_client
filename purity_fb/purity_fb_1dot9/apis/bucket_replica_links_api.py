# coding: utf-8

"""
    Pure Storage FlashBlade REST 1.9 Python SDK

    Pure Storage FlashBlade REST 1.9 Python SDK, developed by [Pure Storage, Inc](http://www.purestorage.com/). Documentations can be found at [purity-fb.readthedocs.io](http://purity-fb.readthedocs.io/).

    OpenAPI spec version: 1.9
    Contact: info@purestorage.com
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


class BucketReplicaLinksApi(object):
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

    def create_bucket_replica_links(self, bucket_replica_link, **kwargs):
        """
        Create new bucket replica links.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_bucket_replica_links(bucket_replica_link, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param BucketReplicaLinkPost bucket_replica_link: Bucket replica link create parameters. (required)
        :param list[str] local_bucket_names: A comma-separated list of local bucket names. This cannot be provided together with `local_bucket_ids` query parameter.
        :param list[str] remote_bucket_names: A comma-separated list of remote bucket names.
        :param list[str] remote_credentials_names: A comma-separated list of remote credentials names.
        :return: BucketReplicaLinkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_bucket_replica_links_with_http_info(bucket_replica_link, **kwargs)
        else:
            (data) = self.create_bucket_replica_links_with_http_info(bucket_replica_link, **kwargs)
            return data

    def create_bucket_replica_links_with_http_info(self, bucket_replica_link, **kwargs):
        """
        Create new bucket replica links.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_bucket_replica_links_with_http_info(bucket_replica_link, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param BucketReplicaLinkPost bucket_replica_link: Bucket replica link create parameters. (required)
        :param list[str] local_bucket_names: A comma-separated list of local bucket names. This cannot be provided together with `local_bucket_ids` query parameter.
        :param list[str] remote_bucket_names: A comma-separated list of remote bucket names.
        :param list[str] remote_credentials_names: A comma-separated list of remote credentials names.
        :return: BucketReplicaLinkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bucket_replica_link', 'local_bucket_names', 'remote_bucket_names', 'remote_credentials_names']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_bucket_replica_links" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'bucket_replica_link' is set
        if ('bucket_replica_link' not in params) or (params['bucket_replica_link'] is None):
            raise ValueError("Missing the required parameter `bucket_replica_link` when calling `create_bucket_replica_links`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'local_bucket_names' in params:
            query_params.append(('local_bucket_names', params['local_bucket_names']))
            collection_formats['local_bucket_names'] = 'csv'
        if 'remote_bucket_names' in params:
            query_params.append(('remote_bucket_names', params['remote_bucket_names']))
            collection_formats['remote_bucket_names'] = 'csv'
        if 'remote_credentials_names' in params:
            query_params.append(('remote_credentials_names', params['remote_credentials_names']))
            collection_formats['remote_credentials_names'] = 'csv'

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'bucket_replica_link' in params:
            body_params = params['bucket_replica_link']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['AuthTokenHeader']

        return self.api_client.call_api('/1.9/bucket-replica-links', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='BucketReplicaLinkResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_bucket_replica_links(self, **kwargs):
        """
        Delete a bucket replica link.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_bucket_replica_links(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] local_bucket_ids: A comma-separated list of local bucket IDs. This cannot be provided together with the `local_bucket_names` query parameter.
        :param list[str] local_bucket_names: A comma-separated list of local bucket names. This cannot be provided together with `local_bucket_ids` query parameter.
        :param list[str] remote_bucket_names: A comma-separated list of remote bucket names.
        :param list[str] remote_ids: A comma-separated list of remote array IDs. This cannot be provided together with the `remote_names` query parameter.
        :param list[str] remote_names: A comma-separated list of remote array names. This cannot be provided together with `remote_ids` query parameter.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_bucket_replica_links_with_http_info(**kwargs)
        else:
            (data) = self.delete_bucket_replica_links_with_http_info(**kwargs)
            return data

    def delete_bucket_replica_links_with_http_info(self, **kwargs):
        """
        Delete a bucket replica link.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_bucket_replica_links_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] local_bucket_ids: A comma-separated list of local bucket IDs. This cannot be provided together with the `local_bucket_names` query parameter.
        :param list[str] local_bucket_names: A comma-separated list of local bucket names. This cannot be provided together with `local_bucket_ids` query parameter.
        :param list[str] remote_bucket_names: A comma-separated list of remote bucket names.
        :param list[str] remote_ids: A comma-separated list of remote array IDs. This cannot be provided together with the `remote_names` query parameter.
        :param list[str] remote_names: A comma-separated list of remote array names. This cannot be provided together with `remote_ids` query parameter.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['local_bucket_ids', 'local_bucket_names', 'remote_bucket_names', 'remote_ids', 'remote_names']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_bucket_replica_links" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'local_bucket_ids' in params:
            query_params.append(('local_bucket_ids', params['local_bucket_ids']))
            collection_formats['local_bucket_ids'] = 'csv'
        if 'local_bucket_names' in params:
            query_params.append(('local_bucket_names', params['local_bucket_names']))
            collection_formats['local_bucket_names'] = 'csv'
        if 'remote_bucket_names' in params:
            query_params.append(('remote_bucket_names', params['remote_bucket_names']))
            collection_formats['remote_bucket_names'] = 'csv'
        if 'remote_ids' in params:
            query_params.append(('remote_ids', params['remote_ids']))
            collection_formats['remote_ids'] = 'csv'
        if 'remote_names' in params:
            query_params.append(('remote_names', params['remote_names']))
            collection_formats['remote_names'] = 'csv'

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['AuthTokenHeader']

        return self.api_client.call_api('/1.9/bucket-replica-links', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def list_bucket_replica_links(self, **kwargs):
        """
        List bucket replica links.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_bucket_replica_links(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] ids: A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters.
        :param str filter: The filter to be used for query.
        :param int limit: limit, should be >= 0
        :param list[str] local_bucket_ids: A comma-separated list of local bucket IDs. This cannot be provided together with the `local_bucket_names` query parameter.
        :param list[str] local_bucket_names: A comma-separated list of local bucket names. This cannot be provided together with `local_bucket_ids` query parameter.
        :param list[str] remote_bucket_names: A comma-separated list of remote bucket names.
        :param list[str] remote_ids: A comma-separated list of remote array IDs. This cannot be provided together with the `remote_names` query parameter.
        :param list[str] remote_names: A comma-separated list of remote array names. This cannot be provided together with `remote_ids` query parameter.
        :param str sort: Sort the response by the specified fields (in descending order if '-' is appended to the field name).
        :param int start: The offset of the first resource to return from a collection.
        :param str token: An opaque token used to iterate over a collection. The token to use on the next request is returned in the `continuation_token` field of the result.
        :return: BucketReplicaLinkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_bucket_replica_links_with_http_info(**kwargs)
        else:
            (data) = self.list_bucket_replica_links_with_http_info(**kwargs)
            return data

    def list_bucket_replica_links_with_http_info(self, **kwargs):
        """
        List bucket replica links.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_bucket_replica_links_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] ids: A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters.
        :param str filter: The filter to be used for query.
        :param int limit: limit, should be >= 0
        :param list[str] local_bucket_ids: A comma-separated list of local bucket IDs. This cannot be provided together with the `local_bucket_names` query parameter.
        :param list[str] local_bucket_names: A comma-separated list of local bucket names. This cannot be provided together with `local_bucket_ids` query parameter.
        :param list[str] remote_bucket_names: A comma-separated list of remote bucket names.
        :param list[str] remote_ids: A comma-separated list of remote array IDs. This cannot be provided together with the `remote_names` query parameter.
        :param list[str] remote_names: A comma-separated list of remote array names. This cannot be provided together with `remote_ids` query parameter.
        :param str sort: Sort the response by the specified fields (in descending order if '-' is appended to the field name).
        :param int start: The offset of the first resource to return from a collection.
        :param str token: An opaque token used to iterate over a collection. The token to use on the next request is returned in the `continuation_token` field of the result.
        :return: BucketReplicaLinkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ids', 'filter', 'limit', 'local_bucket_ids', 'local_bucket_names', 'remote_bucket_names', 'remote_ids', 'remote_names', 'sort', 'start', 'token']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_bucket_replica_links" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'ids' in params:
            query_params.append(('ids', params['ids']))
            collection_formats['ids'] = 'csv'
        if 'filter' in params:
            query_params.append(('filter', params['filter']))
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'local_bucket_ids' in params:
            query_params.append(('local_bucket_ids', params['local_bucket_ids']))
            collection_formats['local_bucket_ids'] = 'csv'
        if 'local_bucket_names' in params:
            query_params.append(('local_bucket_names', params['local_bucket_names']))
            collection_formats['local_bucket_names'] = 'csv'
        if 'remote_bucket_names' in params:
            query_params.append(('remote_bucket_names', params['remote_bucket_names']))
            collection_formats['remote_bucket_names'] = 'csv'
        if 'remote_ids' in params:
            query_params.append(('remote_ids', params['remote_ids']))
            collection_formats['remote_ids'] = 'csv'
        if 'remote_names' in params:
            query_params.append(('remote_names', params['remote_names']))
            collection_formats['remote_names'] = 'csv'
        if 'sort' in params:
            query_params.append(('sort', params['sort']))
        if 'start' in params:
            query_params.append(('start', params['start']))
        if 'token' in params:
            query_params.append(('token', params['token']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['AuthTokenHeader']

        return self.api_client.call_api('/1.9/bucket-replica-links', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='BucketReplicaLinkResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_bucket_replica_links(self, bucket_replica_link, **kwargs):
        """
        Update bucket replica links.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_bucket_replica_links(bucket_replica_link, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param BucketReplicaLink bucket_replica_link: The attribute map used to update the bucket replica link. (required)
        :param list[str] local_bucket_ids: A comma-separated list of local bucket IDs. This cannot be provided together with the `local_bucket_names` query parameter.
        :param list[str] local_bucket_names: A comma-separated list of local bucket names. This cannot be provided together with `local_bucket_ids` query parameter.
        :param list[str] remote_bucket_names: A comma-separated list of remote bucket names.
        :param list[str] remote_ids: A comma-separated list of remote array IDs. This cannot be provided together with the `remote_names` query parameter.
        :param list[str] remote_names: A comma-separated list of remote array names. This cannot be provided together with `remote_ids` query parameter.
        :return: BucketReplicaLinkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_bucket_replica_links_with_http_info(bucket_replica_link, **kwargs)
        else:
            (data) = self.update_bucket_replica_links_with_http_info(bucket_replica_link, **kwargs)
            return data

    def update_bucket_replica_links_with_http_info(self, bucket_replica_link, **kwargs):
        """
        Update bucket replica links.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_bucket_replica_links_with_http_info(bucket_replica_link, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param BucketReplicaLink bucket_replica_link: The attribute map used to update the bucket replica link. (required)
        :param list[str] local_bucket_ids: A comma-separated list of local bucket IDs. This cannot be provided together with the `local_bucket_names` query parameter.
        :param list[str] local_bucket_names: A comma-separated list of local bucket names. This cannot be provided together with `local_bucket_ids` query parameter.
        :param list[str] remote_bucket_names: A comma-separated list of remote bucket names.
        :param list[str] remote_ids: A comma-separated list of remote array IDs. This cannot be provided together with the `remote_names` query parameter.
        :param list[str] remote_names: A comma-separated list of remote array names. This cannot be provided together with `remote_ids` query parameter.
        :return: BucketReplicaLinkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bucket_replica_link', 'local_bucket_ids', 'local_bucket_names', 'remote_bucket_names', 'remote_ids', 'remote_names']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_bucket_replica_links" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'bucket_replica_link' is set
        if ('bucket_replica_link' not in params) or (params['bucket_replica_link'] is None):
            raise ValueError("Missing the required parameter `bucket_replica_link` when calling `update_bucket_replica_links`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'local_bucket_ids' in params:
            query_params.append(('local_bucket_ids', params['local_bucket_ids']))
            collection_formats['local_bucket_ids'] = 'csv'
        if 'local_bucket_names' in params:
            query_params.append(('local_bucket_names', params['local_bucket_names']))
            collection_formats['local_bucket_names'] = 'csv'
        if 'remote_bucket_names' in params:
            query_params.append(('remote_bucket_names', params['remote_bucket_names']))
            collection_formats['remote_bucket_names'] = 'csv'
        if 'remote_ids' in params:
            query_params.append(('remote_ids', params['remote_ids']))
            collection_formats['remote_ids'] = 'csv'
        if 'remote_names' in params:
            query_params.append(('remote_names', params['remote_names']))
            collection_formats['remote_names'] = 'csv'

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'bucket_replica_link' in params:
            body_params = params['bucket_replica_link']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['AuthTokenHeader']

        return self.api_client.call_api('/1.9/bucket-replica-links', 'PATCH',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='BucketReplicaLinkResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
