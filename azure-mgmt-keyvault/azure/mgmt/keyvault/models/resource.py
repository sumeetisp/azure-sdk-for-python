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


class Resource(Model):
    """Key Vault resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The Azure Resource Manager resource ID for the key vault.
    :vartype id: str
    :ivar name: The name of the key vault.
    :vartype name: str
    :ivar type: The resource type of the key vault.
    :vartype type: str
    :param location: The supported Azure location where the key vault should
     be created.
    :type location: str
    :param tags: The tags that will be assigned to the key vault.
    :type tags: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, location, tags=None):
        super(Resource, self).__init__()
        self.id = None
        self.name = None
        self.type = None
        self.location = location
        self.tags = tags
