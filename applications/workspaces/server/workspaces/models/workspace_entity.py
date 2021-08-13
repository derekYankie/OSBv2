# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from workspaces.models.base_model_ import Model
from workspaces.models.volume_storage import VolumeStorage
from workspaces.models.workspace_base import WorkspaceBase
from workspaces.models.workspace_collaborator import WorkspaceCollaborator
from workspaces.models.workspace_entity_all_of import WorkspaceEntityAllOf
from workspaces.models.workspace_image import WorkspaceImage
from workspaces.models.workspace_resource_entity import WorkspaceResourceEntity
from workspaces.models.workspace_tag import WorkspaceTag
from workspaces import util

from workspaces.models.volume_storage import VolumeStorage  # noqa: E501
from workspaces.models.workspace_base import WorkspaceBase  # noqa: E501
from workspaces.models.workspace_collaborator import WorkspaceCollaborator  # noqa: E501
from workspaces.models.workspace_entity_all_of import WorkspaceEntityAllOf  # noqa: E501
from workspaces.models.workspace_image import WorkspaceImage  # noqa: E501
from workspaces.models.workspace_resource_entity import WorkspaceResourceEntity  # noqa: E501
from workspaces.models.workspace_tag import WorkspaceTag  # noqa: E501

class WorkspaceEntity(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, name=None, description=None, timestamp_created=None, timestamp_updated=None, tags=None, last_opened_resource_id=None, thumbnail=None, gallery=None, user_id=None, publicable=False, featured=False, license=None, collaborators=None, storage=None, resources=None):  # noqa: E501
        """WorkspaceEntity - a model defined in OpenAPI

        :param id: The id of this WorkspaceEntity.  # noqa: E501
        :type id: int
        :param name: The name of this WorkspaceEntity.  # noqa: E501
        :type name: str
        :param description: The description of this WorkspaceEntity.  # noqa: E501
        :type description: str
        :param timestamp_created: The timestamp_created of this WorkspaceEntity.  # noqa: E501
        :type timestamp_created: datetime
        :param timestamp_updated: The timestamp_updated of this WorkspaceEntity.  # noqa: E501
        :type timestamp_updated: datetime
        :param tags: The tags of this WorkspaceEntity.  # noqa: E501
        :type tags: List[WorkspaceTag]
        :param last_opened_resource_id: The last_opened_resource_id of this WorkspaceEntity.  # noqa: E501
        :type last_opened_resource_id: int
        :param thumbnail: The thumbnail of this WorkspaceEntity.  # noqa: E501
        :type thumbnail: str
        :param gallery: The gallery of this WorkspaceEntity.  # noqa: E501
        :type gallery: List[WorkspaceImage]
        :param user_id: The user_id of this WorkspaceEntity.  # noqa: E501
        :type user_id: str
        :param publicable: The publicable of this WorkspaceEntity.  # noqa: E501
        :type publicable: bool
        :param featured: The featured of this WorkspaceEntity.  # noqa: E501
        :type featured: bool
        :param license: The license of this WorkspaceEntity.  # noqa: E501
        :type license: str
        :param collaborators: The collaborators of this WorkspaceEntity.  # noqa: E501
        :type collaborators: List[WorkspaceCollaborator]
        :param storage: The storage of this WorkspaceEntity.  # noqa: E501
        :type storage: VolumeStorage
        :param resources: The resources of this WorkspaceEntity.  # noqa: E501
        :type resources: List[WorkspaceResourceEntity]
        """
        self.openapi_types = {
            'id': int,
            'name': str,
            'description': str,
            'timestamp_created': datetime,
            'timestamp_updated': datetime,
            'tags': List[WorkspaceTag],
            'last_opened_resource_id': int,
            'thumbnail': str,
            'gallery': List[WorkspaceImage],
            'user_id': str,
            'publicable': bool,
            'featured': bool,
            'license': str,
            'collaborators': List[WorkspaceCollaborator],
            'storage': VolumeStorage,
            'resources': List[WorkspaceResourceEntity]
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'description': 'description',
            'timestamp_created': 'timestamp_created',
            'timestamp_updated': 'timestamp_updated',
            'tags': 'tags',
            'last_opened_resource_id': 'last_opened_resource_id',
            'thumbnail': 'thumbnail',
            'gallery': 'gallery',
            'user_id': 'user_id',
            'publicable': 'publicable',
            'featured': 'featured',
            'license': 'license',
            'collaborators': 'collaborators',
            'storage': 'storage',
            'resources': 'resources'
        }

        self._id = id
        self._name = name
        self._description = description
        self._timestamp_created = timestamp_created
        self._timestamp_updated = timestamp_updated
        self._tags = tags
        self._last_opened_resource_id = last_opened_resource_id
        self._thumbnail = thumbnail
        self._gallery = gallery
        self._user_id = user_id
        self._publicable = publicable
        self._featured = featured
        self._license = license
        self._collaborators = collaborators
        self._storage = storage
        self._resources = resources

    @classmethod
    def from_dict(cls, dikt) -> 'WorkspaceEntity':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The WorkspaceEntity of this WorkspaceEntity.  # noqa: E501
        :rtype: WorkspaceEntity
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this WorkspaceEntity.


        :return: The id of this WorkspaceEntity.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WorkspaceEntity.


        :param id: The id of this WorkspaceEntity.
        :type id: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this WorkspaceEntity.

        Workspace name.  # noqa: E501

        :return: The name of this WorkspaceEntity.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WorkspaceEntity.

        Workspace name.  # noqa: E501

        :param name: The name of this WorkspaceEntity.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this WorkspaceEntity.

        Workspace description.  # noqa: E501

        :return: The description of this WorkspaceEntity.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this WorkspaceEntity.

        Workspace description.  # noqa: E501

        :param description: The description of this WorkspaceEntity.
        :type description: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def timestamp_created(self):
        """Gets the timestamp_created of this WorkspaceEntity.

        Date/time the Workspace is created  # noqa: E501

        :return: The timestamp_created of this WorkspaceEntity.
        :rtype: datetime
        """
        return self._timestamp_created

    @timestamp_created.setter
    def timestamp_created(self, timestamp_created):
        """Sets the timestamp_created of this WorkspaceEntity.

        Date/time the Workspace is created  # noqa: E501

        :param timestamp_created: The timestamp_created of this WorkspaceEntity.
        :type timestamp_created: datetime
        """

        self._timestamp_created = timestamp_created

    @property
    def timestamp_updated(self):
        """Gets the timestamp_updated of this WorkspaceEntity.

        Date/time the Workspace is last updated  # noqa: E501

        :return: The timestamp_updated of this WorkspaceEntity.
        :rtype: datetime
        """
        return self._timestamp_updated

    @timestamp_updated.setter
    def timestamp_updated(self, timestamp_updated):
        """Sets the timestamp_updated of this WorkspaceEntity.

        Date/time the Workspace is last updated  # noqa: E501

        :param timestamp_updated: The timestamp_updated of this WorkspaceEntity.
        :type timestamp_updated: datetime
        """

        self._timestamp_updated = timestamp_updated

    @property
    def tags(self):
        """Gets the tags of this WorkspaceEntity.

        Workspace tags  # noqa: E501

        :return: The tags of this WorkspaceEntity.
        :rtype: List[WorkspaceTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this WorkspaceEntity.

        Workspace tags  # noqa: E501

        :param tags: The tags of this WorkspaceEntity.
        :type tags: List[WorkspaceTag]
        """

        self._tags = tags

    @property
    def last_opened_resource_id(self):
        """Gets the last_opened_resource_id of this WorkspaceEntity.

        The workspace resource id the workspace is opened last with  # noqa: E501

        :return: The last_opened_resource_id of this WorkspaceEntity.
        :rtype: int
        """
        return self._last_opened_resource_id

    @last_opened_resource_id.setter
    def last_opened_resource_id(self, last_opened_resource_id):
        """Sets the last_opened_resource_id of this WorkspaceEntity.

        The workspace resource id the workspace is opened last with  # noqa: E501

        :param last_opened_resource_id: The last_opened_resource_id of this WorkspaceEntity.
        :type last_opened_resource_id: int
        """

        self._last_opened_resource_id = last_opened_resource_id

    @property
    def thumbnail(self):
        """Gets the thumbnail of this WorkspaceEntity.


        :return: The thumbnail of this WorkspaceEntity.
        :rtype: str
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        """Sets the thumbnail of this WorkspaceEntity.


        :param thumbnail: The thumbnail of this WorkspaceEntity.
        :type thumbnail: str
        """

        self._thumbnail = thumbnail

    @property
    def gallery(self):
        """Gets the gallery of this WorkspaceEntity.

        Gallery with images of the workspace  # noqa: E501

        :return: The gallery of this WorkspaceEntity.
        :rtype: List[WorkspaceImage]
        """
        return self._gallery

    @gallery.setter
    def gallery(self, gallery):
        """Sets the gallery of this WorkspaceEntity.

        Gallery with images of the workspace  # noqa: E501

        :param gallery: The gallery of this WorkspaceEntity.
        :type gallery: List[WorkspaceImage]
        """

        self._gallery = gallery

    @property
    def user_id(self):
        """Gets the user_id of this WorkspaceEntity.

        Workspace keycloak user id, will be automatically be set to the logged in user  # noqa: E501

        :return: The user_id of this WorkspaceEntity.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this WorkspaceEntity.

        Workspace keycloak user id, will be automatically be set to the logged in user  # noqa: E501

        :param user_id: The user_id of this WorkspaceEntity.
        :type user_id: str
        """

        self._user_id = user_id

    @property
    def publicable(self):
        """Gets the publicable of this WorkspaceEntity.

        Is this a public workspace? Default false  # noqa: E501

        :return: The publicable of this WorkspaceEntity.
        :rtype: bool
        """
        return self._publicable

    @publicable.setter
    def publicable(self, publicable):
        """Sets the publicable of this WorkspaceEntity.

        Is this a public workspace? Default false  # noqa: E501

        :param publicable: The publicable of this WorkspaceEntity.
        :type publicable: bool
        """

        self._publicable = publicable

    @property
    def featured(self):
        """Gets the featured of this WorkspaceEntity.

        Is this a featured workspace? Default false  # noqa: E501

        :return: The featured of this WorkspaceEntity.
        :rtype: bool
        """
        return self._featured

    @featured.setter
    def featured(self, featured):
        """Sets the featured of this WorkspaceEntity.

        Is this a featured workspace? Default false  # noqa: E501

        :param featured: The featured of this WorkspaceEntity.
        :type featured: bool
        """

        self._featured = featured

    @property
    def license(self):
        """Gets the license of this WorkspaceEntity.

        Workspace license  # noqa: E501

        :return: The license of this WorkspaceEntity.
        :rtype: str
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this WorkspaceEntity.

        Workspace license  # noqa: E501

        :param license: The license of this WorkspaceEntity.
        :type license: str
        """

        self._license = license

    @property
    def collaborators(self):
        """Gets the collaborators of this WorkspaceEntity.

        Collaborators who work on the workspace  # noqa: E501

        :return: The collaborators of this WorkspaceEntity.
        :rtype: List[WorkspaceCollaborator]
        """
        return self._collaborators

    @collaborators.setter
    def collaborators(self, collaborators):
        """Sets the collaborators of this WorkspaceEntity.

        Collaborators who work on the workspace  # noqa: E501

        :param collaborators: The collaborators of this WorkspaceEntity.
        :type collaborators: List[WorkspaceCollaborator]
        """

        self._collaborators = collaborators

    @property
    def storage(self):
        """Gets the storage of this WorkspaceEntity.


        :return: The storage of this WorkspaceEntity.
        :rtype: VolumeStorage
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        """Sets the storage of this WorkspaceEntity.


        :param storage: The storage of this WorkspaceEntity.
        :type storage: VolumeStorage
        """

        self._storage = storage

    @property
    def resources(self):
        """Gets the resources of this WorkspaceEntity.

        Resources of the workspace  # noqa: E501

        :return: The resources of this WorkspaceEntity.
        :rtype: List[WorkspaceResourceEntity]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this WorkspaceEntity.

        Resources of the workspace  # noqa: E501

        :param resources: The resources of this WorkspaceEntity.
        :type resources: List[WorkspaceResourceEntity]
        """

        self._resources = resources
