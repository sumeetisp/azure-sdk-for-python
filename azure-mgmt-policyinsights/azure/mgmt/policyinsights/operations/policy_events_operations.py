# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import uuid
from msrest.pipeline import ClientRawResponse

from .. import models


class PolicyEventsOperations(object):
    """PolicyEventsOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar policy_events_resource: The name of the virtual resource under PolicyEvents resource type; only "default" is allowed. Constant value: "default".
    :ivar api_version: API version to use with the client requests. Constant value: "2017-12-12-preview".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.policy_events_resource = "default"
        self.api_version = "2017-12-12-preview"

        self.config = config

    def list_query_results_for_management_group(
            self, management_group_id, query_options=None, custom_headers=None, raw=False, **operation_config):
        """Queries policy events for the resources under the management group.

        :param management_group_id: Management group ID, e.g.
         /providers/Microsoft.Management/managementGroups/{name}.
        :type management_group_id: str
        :param query_options: Additional parameters for the operation
        :type query_options: ~azure.mgmt.policyinsights.models.QueryOptions
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PolicyEventsQueryResults or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.policyinsights.models.PolicyEventsQueryResults or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`QueryFailureException<azure.mgmt.policyinsights.models.QueryFailureException>`
        """
        top = None
        if query_options is not None:
            top = query_options.top
        order_by = None
        if query_options is not None:
            order_by = query_options.order_by
        select = None
        if query_options is not None:
            select = query_options.select
        from_parameter = None
        if query_options is not None:
            from_parameter = query_options.from_property
        to = None
        if query_options is not None:
            to = query_options.to
        filter = None
        if query_options is not None:
            filter = query_options.filter
        apply = None
        if query_options is not None:
            apply = query_options.apply

        # Construct URL
        url = self.list_query_results_for_management_group.metadata['url']
        path_format_arguments = {
            'policyEventsResource': self._serialize.url("self.policy_events_resource", self.policy_events_resource, 'str'),
            'managementGroupId': self._serialize.url("management_group_id", management_group_id, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
        if top is not None:
            query_parameters['$top'] = self._serialize.query("top", top, 'int', minimum=0)
        if order_by is not None:
            query_parameters['$orderby'] = self._serialize.query("order_by", order_by, 'str')
        if select is not None:
            query_parameters['$select'] = self._serialize.query("select", select, 'str')
        if from_parameter is not None:
            query_parameters['$from'] = self._serialize.query("from_parameter", from_parameter, 'iso-8601')
        if to is not None:
            query_parameters['$to'] = self._serialize.query("to", to, 'iso-8601')
        if filter is not None:
            query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
        if apply is not None:
            query_parameters['$apply'] = self._serialize.query("apply", apply, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.QueryFailureException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('PolicyEventsQueryResults', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list_query_results_for_management_group.metadata = {'url': '/{managementGroupId}/providers/Microsoft.PolicyInsights/policyEvents/{policyEventsResource}/queryResults'}

    def list_query_results_for_subscription(
            self, subscription_id, query_options=None, custom_headers=None, raw=False, **operation_config):
        """Queries policy events for the resources under the subscription.

        :param subscription_id: Microsoft Azure subscription ID.
        :type subscription_id: str
        :param query_options: Additional parameters for the operation
        :type query_options: ~azure.mgmt.policyinsights.models.QueryOptions
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PolicyEventsQueryResults or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.policyinsights.models.PolicyEventsQueryResults or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`QueryFailureException<azure.mgmt.policyinsights.models.QueryFailureException>`
        """
        top = None
        if query_options is not None:
            top = query_options.top
        order_by = None
        if query_options is not None:
            order_by = query_options.order_by
        select = None
        if query_options is not None:
            select = query_options.select
        from_parameter = None
        if query_options is not None:
            from_parameter = query_options.from_property
        to = None
        if query_options is not None:
            to = query_options.to
        filter = None
        if query_options is not None:
            filter = query_options.filter
        apply = None
        if query_options is not None:
            apply = query_options.apply

        # Construct URL
        url = self.list_query_results_for_subscription.metadata['url']
        path_format_arguments = {
            'policyEventsResource': self._serialize.url("self.policy_events_resource", self.policy_events_resource, 'str'),
            'subscriptionId': self._serialize.url("subscription_id", subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
        if top is not None:
            query_parameters['$top'] = self._serialize.query("top", top, 'int', minimum=0)
        if order_by is not None:
            query_parameters['$orderby'] = self._serialize.query("order_by", order_by, 'str')
        if select is not None:
            query_parameters['$select'] = self._serialize.query("select", select, 'str')
        if from_parameter is not None:
            query_parameters['$from'] = self._serialize.query("from_parameter", from_parameter, 'iso-8601')
        if to is not None:
            query_parameters['$to'] = self._serialize.query("to", to, 'iso-8601')
        if filter is not None:
            query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
        if apply is not None:
            query_parameters['$apply'] = self._serialize.query("apply", apply, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.QueryFailureException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('PolicyEventsQueryResults', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list_query_results_for_subscription.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.PolicyInsights/policyEvents/{policyEventsResource}/queryResults'}

    def list_query_results_for_resource_group(
            self, subscription_id, resource_group_name, query_options=None, custom_headers=None, raw=False, **operation_config):
        """Queries policy events for the resources under the resource group.

        :param subscription_id: Microsoft Azure subscription ID.
        :type subscription_id: str
        :param resource_group_name: Resource group name.
        :type resource_group_name: str
        :param query_options: Additional parameters for the operation
        :type query_options: ~azure.mgmt.policyinsights.models.QueryOptions
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PolicyEventsQueryResults or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.policyinsights.models.PolicyEventsQueryResults or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`QueryFailureException<azure.mgmt.policyinsights.models.QueryFailureException>`
        """
        top = None
        if query_options is not None:
            top = query_options.top
        order_by = None
        if query_options is not None:
            order_by = query_options.order_by
        select = None
        if query_options is not None:
            select = query_options.select
        from_parameter = None
        if query_options is not None:
            from_parameter = query_options.from_property
        to = None
        if query_options is not None:
            to = query_options.to
        filter = None
        if query_options is not None:
            filter = query_options.filter
        apply = None
        if query_options is not None:
            apply = query_options.apply

        # Construct URL
        url = self.list_query_results_for_resource_group.metadata['url']
        path_format_arguments = {
            'policyEventsResource': self._serialize.url("self.policy_events_resource", self.policy_events_resource, 'str'),
            'subscriptionId': self._serialize.url("subscription_id", subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
        if top is not None:
            query_parameters['$top'] = self._serialize.query("top", top, 'int', minimum=0)
        if order_by is not None:
            query_parameters['$orderby'] = self._serialize.query("order_by", order_by, 'str')
        if select is not None:
            query_parameters['$select'] = self._serialize.query("select", select, 'str')
        if from_parameter is not None:
            query_parameters['$from'] = self._serialize.query("from_parameter", from_parameter, 'iso-8601')
        if to is not None:
            query_parameters['$to'] = self._serialize.query("to", to, 'iso-8601')
        if filter is not None:
            query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
        if apply is not None:
            query_parameters['$apply'] = self._serialize.query("apply", apply, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.QueryFailureException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('PolicyEventsQueryResults', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list_query_results_for_resource_group.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PolicyInsights/policyEvents/{policyEventsResource}/queryResults'}

    def list_query_results_for_resource(
            self, resource_id, query_options=None, custom_headers=None, raw=False, **operation_config):
        """Queries policy events for the resource.

        :param resource_id: Resource ID.
        :type resource_id: str
        :param query_options: Additional parameters for the operation
        :type query_options: ~azure.mgmt.policyinsights.models.QueryOptions
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PolicyEventsQueryResults or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.policyinsights.models.PolicyEventsQueryResults or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`QueryFailureException<azure.mgmt.policyinsights.models.QueryFailureException>`
        """
        top = None
        if query_options is not None:
            top = query_options.top
        order_by = None
        if query_options is not None:
            order_by = query_options.order_by
        select = None
        if query_options is not None:
            select = query_options.select
        from_parameter = None
        if query_options is not None:
            from_parameter = query_options.from_property
        to = None
        if query_options is not None:
            to = query_options.to
        filter = None
        if query_options is not None:
            filter = query_options.filter
        apply = None
        if query_options is not None:
            apply = query_options.apply

        # Construct URL
        url = self.list_query_results_for_resource.metadata['url']
        path_format_arguments = {
            'policyEventsResource': self._serialize.url("self.policy_events_resource", self.policy_events_resource, 'str'),
            'resourceId': self._serialize.url("resource_id", resource_id, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
        if top is not None:
            query_parameters['$top'] = self._serialize.query("top", top, 'int', minimum=0)
        if order_by is not None:
            query_parameters['$orderby'] = self._serialize.query("order_by", order_by, 'str')
        if select is not None:
            query_parameters['$select'] = self._serialize.query("select", select, 'str')
        if from_parameter is not None:
            query_parameters['$from'] = self._serialize.query("from_parameter", from_parameter, 'iso-8601')
        if to is not None:
            query_parameters['$to'] = self._serialize.query("to", to, 'iso-8601')
        if filter is not None:
            query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
        if apply is not None:
            query_parameters['$apply'] = self._serialize.query("apply", apply, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.QueryFailureException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('PolicyEventsQueryResults', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list_query_results_for_resource.metadata = {'url': '/{resourceId}/providers/Microsoft.PolicyInsights/policyEvents/{policyEventsResource}/queryResults'}

    def list_query_results_for_policy_set_definition(
            self, policy_set_definition_id, query_options=None, custom_headers=None, raw=False, **operation_config):
        """Queries policy events for the policy set definition.

        :param policy_set_definition_id: Subscription level policy set
         definition ID.
        :type policy_set_definition_id: str
        :param query_options: Additional parameters for the operation
        :type query_options: ~azure.mgmt.policyinsights.models.QueryOptions
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PolicyEventsQueryResults or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.policyinsights.models.PolicyEventsQueryResults or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`QueryFailureException<azure.mgmt.policyinsights.models.QueryFailureException>`
        """
        top = None
        if query_options is not None:
            top = query_options.top
        order_by = None
        if query_options is not None:
            order_by = query_options.order_by
        select = None
        if query_options is not None:
            select = query_options.select
        from_parameter = None
        if query_options is not None:
            from_parameter = query_options.from_property
        to = None
        if query_options is not None:
            to = query_options.to
        filter = None
        if query_options is not None:
            filter = query_options.filter
        apply = None
        if query_options is not None:
            apply = query_options.apply

        # Construct URL
        url = self.list_query_results_for_policy_set_definition.metadata['url']
        path_format_arguments = {
            'policyEventsResource': self._serialize.url("self.policy_events_resource", self.policy_events_resource, 'str'),
            'policySetDefinitionId': self._serialize.url("policy_set_definition_id", policy_set_definition_id, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
        if top is not None:
            query_parameters['$top'] = self._serialize.query("top", top, 'int', minimum=0)
        if order_by is not None:
            query_parameters['$orderby'] = self._serialize.query("order_by", order_by, 'str')
        if select is not None:
            query_parameters['$select'] = self._serialize.query("select", select, 'str')
        if from_parameter is not None:
            query_parameters['$from'] = self._serialize.query("from_parameter", from_parameter, 'iso-8601')
        if to is not None:
            query_parameters['$to'] = self._serialize.query("to", to, 'iso-8601')
        if filter is not None:
            query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
        if apply is not None:
            query_parameters['$apply'] = self._serialize.query("apply", apply, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.QueryFailureException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('PolicyEventsQueryResults', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list_query_results_for_policy_set_definition.metadata = {'url': '/{policySetDefinitionId}/providers/Microsoft.PolicyInsights/policyEvents/{policyEventsResource}/queryResults'}

    def list_query_results_for_policy_definition(
            self, policy_definition_id, query_options=None, custom_headers=None, raw=False, **operation_config):
        """Queries policy events for the policy definition.

        :param policy_definition_id: Subscription level policy definition ID.
        :type policy_definition_id: str
        :param query_options: Additional parameters for the operation
        :type query_options: ~azure.mgmt.policyinsights.models.QueryOptions
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PolicyEventsQueryResults or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.policyinsights.models.PolicyEventsQueryResults or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`QueryFailureException<azure.mgmt.policyinsights.models.QueryFailureException>`
        """
        top = None
        if query_options is not None:
            top = query_options.top
        order_by = None
        if query_options is not None:
            order_by = query_options.order_by
        select = None
        if query_options is not None:
            select = query_options.select
        from_parameter = None
        if query_options is not None:
            from_parameter = query_options.from_property
        to = None
        if query_options is not None:
            to = query_options.to
        filter = None
        if query_options is not None:
            filter = query_options.filter
        apply = None
        if query_options is not None:
            apply = query_options.apply

        # Construct URL
        url = self.list_query_results_for_policy_definition.metadata['url']
        path_format_arguments = {
            'policyEventsResource': self._serialize.url("self.policy_events_resource", self.policy_events_resource, 'str'),
            'policyDefinitionId': self._serialize.url("policy_definition_id", policy_definition_id, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
        if top is not None:
            query_parameters['$top'] = self._serialize.query("top", top, 'int', minimum=0)
        if order_by is not None:
            query_parameters['$orderby'] = self._serialize.query("order_by", order_by, 'str')
        if select is not None:
            query_parameters['$select'] = self._serialize.query("select", select, 'str')
        if from_parameter is not None:
            query_parameters['$from'] = self._serialize.query("from_parameter", from_parameter, 'iso-8601')
        if to is not None:
            query_parameters['$to'] = self._serialize.query("to", to, 'iso-8601')
        if filter is not None:
            query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
        if apply is not None:
            query_parameters['$apply'] = self._serialize.query("apply", apply, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.QueryFailureException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('PolicyEventsQueryResults', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list_query_results_for_policy_definition.metadata = {'url': '/{policyDefinitionId}/providers/Microsoft.PolicyInsights/policyEvents/{policyEventsResource}/queryResults'}

    def list_query_results_for_policy_assignment(
            self, policy_assignment_id, query_options=None, custom_headers=None, raw=False, **operation_config):
        """Queries policy events for the policy assignment.

        :param policy_assignment_id: Subscription level or a resource group
         level policy assignment ID.
        :type policy_assignment_id: str
        :param query_options: Additional parameters for the operation
        :type query_options: ~azure.mgmt.policyinsights.models.QueryOptions
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PolicyEventsQueryResults or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.policyinsights.models.PolicyEventsQueryResults or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`QueryFailureException<azure.mgmt.policyinsights.models.QueryFailureException>`
        """
        top = None
        if query_options is not None:
            top = query_options.top
        order_by = None
        if query_options is not None:
            order_by = query_options.order_by
        select = None
        if query_options is not None:
            select = query_options.select
        from_parameter = None
        if query_options is not None:
            from_parameter = query_options.from_property
        to = None
        if query_options is not None:
            to = query_options.to
        filter = None
        if query_options is not None:
            filter = query_options.filter
        apply = None
        if query_options is not None:
            apply = query_options.apply

        # Construct URL
        url = self.list_query_results_for_policy_assignment.metadata['url']
        path_format_arguments = {
            'policyEventsResource': self._serialize.url("self.policy_events_resource", self.policy_events_resource, 'str'),
            'policyAssignmentId': self._serialize.url("policy_assignment_id", policy_assignment_id, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
        if top is not None:
            query_parameters['$top'] = self._serialize.query("top", top, 'int', minimum=0)
        if order_by is not None:
            query_parameters['$orderby'] = self._serialize.query("order_by", order_by, 'str')
        if select is not None:
            query_parameters['$select'] = self._serialize.query("select", select, 'str')
        if from_parameter is not None:
            query_parameters['$from'] = self._serialize.query("from_parameter", from_parameter, 'iso-8601')
        if to is not None:
            query_parameters['$to'] = self._serialize.query("to", to, 'iso-8601')
        if filter is not None:
            query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
        if apply is not None:
            query_parameters['$apply'] = self._serialize.query("apply", apply, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.QueryFailureException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('PolicyEventsQueryResults', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list_query_results_for_policy_assignment.metadata = {'url': '/{policyAssignmentId}/providers/Microsoft.PolicyInsights/policyEvents/{policyEventsResource}/queryResults'}

    def get_metadata(
            self, scope, custom_headers=None, raw=False, **operation_config):
        """Gets OData metadata XML document.

        :param scope: A valid scope, i.e. management group, subscription,
         resource group, or resource ID. Scope used has no effect on metadata
         returned.
        :type scope: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: str or ClientRawResponse if raw=true
        :rtype: str or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`QueryFailureException<azure.mgmt.policyinsights.models.QueryFailureException>`
        """
        # Construct URL
        url = self.get_metadata.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.QueryFailureException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('str', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_metadata.metadata = {'url': '/{scope}/providers/Microsoft.PolicyInsights/policyEvents/$metadata'}
