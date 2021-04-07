# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from workspaces.models.base_model_ import Model
from workspaces import util


class VolumeStorage(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, name=None):  # noqa: E501
        """VolumeStorage - a model defined in OpenAPI

        :param id: The id of this VolumeStorage.  # noqa: E501
        :type id: int
        :param name: The name of this VolumeStorage.  # noqa: E501
        :type name: str
        """
        self.openapi_types = {
            'id': int,
            'name': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name'
        }

        self._id = id
        self._name = name

    @classmethod
    def from_dict(cls, dikt) -> 'VolumeStorage':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The VolumeStorage of this VolumeStorage.  # noqa: E501
        :rtype: VolumeStorage
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this VolumeStorage.


        :return: The id of this VolumeStorage.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VolumeStorage.


        :param id: The id of this VolumeStorage.
        :type id: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this VolumeStorage.

        StorageVolume name  # noqa: E501

        :return: The name of this VolumeStorage.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VolumeStorage.

        StorageVolume name  # noqa: E501

        :param name: The name of this VolumeStorage.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name