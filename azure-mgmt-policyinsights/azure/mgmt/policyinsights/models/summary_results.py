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

from msrest.serialization import Model


class SummaryResults(Model):
    """Non-compliance summary on a particular summary level.

    :param query_results_uri: HTTP POST URI for queryResults action on
     Microsoft.PolicyInsights to retrieve raw results for the non-compliance
     summary.
    :type query_results_uri: str
    :param non_compliant_resources: Number of non-compliant resources.
    :type non_compliant_resources: int
    :param non_compliant_policies: Number of non-compliant policies.
    :type non_compliant_policies: int
    """

    _validation = {
        'non_compliant_resources': {'minimum': 0},
        'non_compliant_policies': {'minimum': 0},
    }

    _attribute_map = {
        'query_results_uri': {'key': 'queryResultsUri', 'type': 'str'},
        'non_compliant_resources': {'key': 'nonCompliantResources', 'type': 'int'},
        'non_compliant_policies': {'key': 'nonCompliantPolicies', 'type': 'int'},
    }

    def __init__(self, query_results_uri=None, non_compliant_resources=None, non_compliant_policies=None):
        super(SummaryResults, self).__init__()
        self.query_results_uri = query_results_uri
        self.non_compliant_resources = non_compliant_resources
        self.non_compliant_policies = non_compliant_policies
