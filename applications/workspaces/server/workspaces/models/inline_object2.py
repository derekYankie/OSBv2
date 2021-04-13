# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from workspaces.models.base_model_ import Model
from workspaces.models.repository_resource import RepositoryResource
from workspaces.models.resource_type import ResourceType
from workspaces import util

from workspaces.models.repository_resource import RepositoryResource  # noqa: E501
from workspaces.models.resource_type import ResourceType  # noqa: E501

class InlineObject2(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, folder=None, resource_type=None, workspace_id=None, origin=None):  # noqa: E501
        """InlineObject2 - a model defined in OpenAPI

        :param name: The name of this InlineObject2.  # noqa: E501
        :type name: str
        :param folder: The folder of this InlineObject2.  # noqa: E501
        :type folder: str
        :param resource_type: The resource_type of this InlineObject2.  # noqa: E501
        :type resource_type: ResourceType
        :param workspace_id: The workspace_id of this InlineObject2.  # noqa: E501
        :type workspace_id: int
        :param origin: The origin of this InlineObject2.  # noqa: E501
        :type origin: RepositoryResource
        """
        self.openapi_types = {
            'name': str,
            'folder': str,
            'resource_type': ResourceType,
            'workspace_id': int,
            'origin': RepositoryResource
        }

        self.attribute_map = {
            'name': 'name',
            'folder': 'folder',
            'resource_type': 'resource_type',
            'workspace_id': 'workspace_id',
            'origin': 'origin'
        }

        self._name = name
        self._folder = folder
        self._resource_type = resource_type
        self._workspace_id = workspace_id
        self._origin = origin

    @classmethod
    def from_dict(cls, dikt) -> 'InlineObject2':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_object_2 of this InlineObject2.  # noqa: E501
        :rtype: InlineObject2
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this InlineObject2.

        WorkspaceResource name  # noqa: E501

        :return: The name of this InlineObject2.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineObject2.

        WorkspaceResource name  # noqa: E501

        :param name: The name of this InlineObject2.
        :type name: str
        """

        self._name = name

    @property
    def folder(self):
        """Gets the folder of this InlineObject2.

        WorkspaceResource folder where the resource will stored in the pvc  # noqa: E501

        :return: The folder of this InlineObject2.
        :rtype: str
        """
        return self._folder

    @folder.setter
    def folder(self, folder):
        """Sets the folder of this InlineObject2.

        WorkspaceResource folder where the resource will stored in the pvc  # noqa: E501

        :param folder: The folder of this InlineObject2.
        :type folder: str
        """

        self._folder = folder

    @property
    def resource_type(self):
        """Gets the resource_type of this InlineObject2.


        :return: The resource_type of this InlineObject2.
        :rtype: ResourceType
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this InlineObject2.


        :param resource_type: The resource_type of this InlineObject2.
        :type resource_type: ResourceType
        """

        self._resource_type = resource_type

    @property
    def workspace_id(self):
        """Gets the workspace_id of this InlineObject2.

        workspace_id  # noqa: E501

        :return: The workspace_id of this InlineObject2.
        :rtype: int
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this InlineObject2.

        workspace_id  # noqa: E501

        :param workspace_id: The workspace_id of this InlineObject2.
        :type workspace_id: int
        """

        self._workspace_id = workspace_id

    @property
    def origin(self):
        """Gets the origin of this InlineObject2.


        :return: The origin of this InlineObject2.
        :rtype: RepositoryResource
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this InlineObject2.


        :param origin: The origin of this InlineObject2.
        :type origin: RepositoryResource
        """

        self._origin = origin