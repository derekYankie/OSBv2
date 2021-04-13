# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from workspaces.models.base_model_ import Model
from workspaces import util


class ResourceBase(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, path=None):  # noqa: E501
        """ResourceBase - a model defined in OpenAPI

        :param path: The path of this ResourceBase.  # noqa: E501
        :type path: str
        """
        self.openapi_types = {
            'path': str
        }

        self.attribute_map = {
            'path': 'path'
        }

        self._path = path

    @classmethod
    def from_dict(cls, dikt) -> 'ResourceBase':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ResourceBase of this ResourceBase.  # noqa: E501
        :rtype: ResourceBase
        """
        return util.deserialize_model(dikt, cls)

    @property
    def path(self):
        """Gets the path of this ResourceBase.

        Download URL of the Resource  # noqa: E501

        :return: The path of this ResourceBase.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ResourceBase.

        Download URL of the Resource  # noqa: E501

        :param path: The path of this ResourceBase.
        :type path: str
        """

        self._path = path