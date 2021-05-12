# coding: utf-8

from __future__ import absolute_import

from datetime import date, datetime  # noqa: F401
from typing import Dict, List  # noqa: F401

from workspaces import util
from workspaces.models.base_model_ import Model
from workspaces.models.resource_base import ResourceBase  # noqa: E501


class DownloadResource(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, path=None):  # noqa: E501
        """DownloadResource - a model defined in OpenAPI

        :param path: The path of this DownloadResource.  # noqa: E501
        :type path: str
        """
        self.openapi_types = {"path": str}

        self.attribute_map = {"path": "path"}

        self._path = path

    @classmethod
    def from_dict(cls, dikt) -> "DownloadResource":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DownloadResource of this DownloadResource.  # noqa: E501
        :rtype: DownloadResource
        """
        return util.deserialize_model(dikt, cls)

    @property
    def path(self):
        """Gets the path of this DownloadResource.

        Download URL of the Resource  # noqa: E501

        :return: The path of this DownloadResource.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this DownloadResource.

        Download URL of the Resource  # noqa: E501

        :param path: The path of this DownloadResource.
        :type path: str
        """

        self._path = path
