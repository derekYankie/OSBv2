# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from workspaces.models.base_model_ import Model
from workspaces.models.osb_repository_resource_all_of import OSBRepositoryResourceAllOf
from workspaces.models.repository_resource import RepositoryResource
from workspaces import util

from workspaces.models.osb_repository_resource_all_of import OSBRepositoryResourceAllOf  # noqa: E501
from workspaces.models.repository_resource import RepositoryResource  # noqa: E501

class OSBRepositoryResource(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, uid=None, id=None):  # noqa: E501
        """OSBRepositoryResource - a model defined in OpenAPI

        :param name: The name of this OSBRepositoryResource.  # noqa: E501
        :type name: str
        :param uid: The uid of this OSBRepositoryResource.  # noqa: E501
        :type uid: str
        :param id: The id of this OSBRepositoryResource.  # noqa: E501
        :type id: int
        """
        self.openapi_types = {
            'name': str,
            'uid': str,
            'id': int
        }

        self.attribute_map = {
            'name': 'name',
            'uid': 'uid',
            'id': 'id'
        }

        self._name = name
        self._uid = uid
        self._id = id

    @classmethod
    def from_dict(cls, dikt) -> 'OSBRepositoryResource':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The OSBRepositoryResource of this OSBRepositoryResource.  # noqa: E501
        :rtype: OSBRepositoryResource
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this OSBRepositoryResource.

        folder/file name  # noqa: E501

        :return: The name of this OSBRepositoryResource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OSBRepositoryResource.

        folder/file name  # noqa: E501

        :param name: The name of this OSBRepositoryResource.
        :type name: str
        """

        self._name = name

    @property
    def uid(self):
        """Gets the uid of this OSBRepositoryResource.

        unique identifier for the resource in the (external) repository  # noqa: E501

        :return: The uid of this OSBRepositoryResource.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this OSBRepositoryResource.

        unique identifier for the resource in the (external) repository  # noqa: E501

        :param uid: The uid of this OSBRepositoryResource.
        :type uid: str
        """

        self._uid = uid

    @property
    def id(self):
        """Gets the id of this OSBRepositoryResource.


        :return: The id of this OSBRepositoryResource.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OSBRepositoryResource.


        :param id: The id of this OSBRepositoryResource.
        :type id: int
        """

        self._id = id
