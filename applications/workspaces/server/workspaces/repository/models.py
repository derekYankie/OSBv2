"""Autogenerated SQLAlchemy models based on OpenAlchemy models."""
# pylint: disable=no-member,super-init-not-called,unused-argument

import datetime
import typing

import sqlalchemy
import typing_extensions
from sqlalchemy import orm

from open_alchemy import models

Base = models.Base  # type: ignore


class _WorkspaceEntityDictBase(typing_extensions.TypedDict, total=True):
    """TypedDict for properties that are required."""

    name: str
    description: str


class WorkspaceEntityDict(_WorkspaceEntityDictBase, total=False):
    """TypedDict for properties that are not required."""

    resources: typing.Sequence["WorkspaceResourceEntityDict"]
    id: int
    timestamp_created: typing.Optional[str]
    timestamp_updated: typing.Optional[str]
    last_opened_resource_id: typing.Optional[int]
    thumbnail: typing.Optional[str]
    gallery: typing.Sequence["WorkspaceImageDict"]
    user_id: typing.Optional[str]
    publicable: bool
    featured: bool
    license: typing.Optional[str]
    collaborators: typing.Sequence["WorkspaceCollaboratorDict"]
    storage: typing.Optional["VolumeStorageDict"]
    tags: typing.Sequence["TagDict"]


class TWorkspaceEntity(typing_extensions.Protocol):
    """
    SQLAlchemy model protocol.

    Workspace item

    Attrs:
        resources: Resources of the workspace
        id: The id of the WorkspaceEntity.
        name: Workspace name.
        description: Workspace description.
        timestamp_created: Date/time the Workspace is created
        timestamp_updated: Date/time the Workspace is last updated
        last_opened_resource_id: The workspace resource id the workspace is
            opened last with
        thumbnail: The thumbnail of the WorkspaceEntity.
        gallery: Gallery with images of the workspace
        user_id: Workspace keycloak user id, will be automatically be set to
            the logged in user
        publicable: Is this a public workspace? Default false
        featured: Is this a featured workspace? Default false
        license: Workspace license
        collaborators: Collaborators who work on the workspace
        storage: Storage of the workspace
        tags: The tags of the WorkspaceEntity.

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    resources: 'sqlalchemy.Column[typing.Sequence["TWorkspaceResourceEntity"]]'
    id: 'sqlalchemy.Column[int]'
    name: 'sqlalchemy.Column[str]'
    description: 'sqlalchemy.Column[str]'
    timestamp_created: 'sqlalchemy.Column[typing.Optional[datetime.datetime]]'
    timestamp_updated: 'sqlalchemy.Column[typing.Optional[datetime.datetime]]'
    last_opened_resource_id: 'sqlalchemy.Column[typing.Optional[int]]'
    thumbnail: 'sqlalchemy.Column[typing.Optional[str]]'
    gallery: 'sqlalchemy.Column[typing.Sequence["TWorkspaceImage"]]'
    user_id: 'sqlalchemy.Column[typing.Optional[str]]'
    publicable: 'sqlalchemy.Column[bool]'
    featured: 'sqlalchemy.Column[bool]'
    license: 'sqlalchemy.Column[typing.Optional[str]]'
    collaborators: 'sqlalchemy.Column[typing.Sequence["TWorkspaceCollaborator"]]'
    storage: 'sqlalchemy.Column[typing.Optional["TVolumeStorage"]]'
    tags: 'sqlalchemy.Column[typing.Sequence["TTag"]]'

    def __init__(self, name: str, description: str, resources: typing.Optional[typing.Sequence["TWorkspaceResourceEntity"]] = None, id: typing.Optional[int] = None, timestamp_created: typing.Optional[datetime.datetime] = None, timestamp_updated: typing.Optional[datetime.datetime] = None, last_opened_resource_id: typing.Optional[int] = None, thumbnail: typing.Optional[str] = None, gallery: typing.Optional[typing.Sequence["TWorkspaceImage"]] = None, user_id: typing.Optional[str] = None, publicable: bool = False, featured: bool = False, license: typing.Optional[str] = None, collaborators: typing.Optional[typing.Sequence["TWorkspaceCollaborator"]] = None, storage: typing.Optional["TVolumeStorage"] = None, tags: typing.Optional[typing.Sequence["TTag"]] = None) -> None:
        """
        Construct.

        Args:
            resources: Resources of the workspace
            id: The id of the WorkspaceEntity.
            name: Workspace name.
            description: Workspace description.
            timestamp_created: Date/time the Workspace is created
            timestamp_updated: Date/time the Workspace is last updated
            last_opened_resource_id: The workspace resource id the workspace is
                opened last with
            thumbnail: The thumbnail of the WorkspaceEntity.
            gallery: Gallery with images of the workspace
            user_id: Workspace keycloak user id, will be automatically be set
                to the logged in user
            publicable: Is this a public workspace? Default false
            featured: Is this a featured workspace? Default false
            license: Workspace license
            collaborators: Collaborators who work on the workspace
            storage: Storage of the workspace
            tags: The tags of the WorkspaceEntity.

        """
        ...

    @classmethod
    def from_dict(cls, name: str, description: str, resources: typing.Optional[typing.Sequence["WorkspaceResourceEntityDict"]] = None, id: typing.Optional[int] = None, timestamp_created: typing.Optional[datetime.datetime] = None, timestamp_updated: typing.Optional[datetime.datetime] = None, last_opened_resource_id: typing.Optional[int] = None, thumbnail: typing.Optional[str] = None, gallery: typing.Optional[typing.Sequence["WorkspaceImageDict"]] = None, user_id: typing.Optional[str] = None, publicable: bool = False, featured: bool = False, license: typing.Optional[str] = None, collaborators: typing.Optional[typing.Sequence["WorkspaceCollaboratorDict"]] = None, storage: typing.Optional["VolumeStorageDict"] = None, tags: typing.Optional[typing.Sequence["TagDict"]] = None) -> "TWorkspaceEntity":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            resources: Resources of the workspace
            id: The id of the WorkspaceEntity.
            name: Workspace name.
            description: Workspace description.
            timestamp_created: Date/time the Workspace is created
            timestamp_updated: Date/time the Workspace is last updated
            last_opened_resource_id: The workspace resource id the workspace is
                opened last with
            thumbnail: The thumbnail of the WorkspaceEntity.
            gallery: Gallery with images of the workspace
            user_id: Workspace keycloak user id, will be automatically be set
                to the logged in user
            publicable: Is this a public workspace? Default false
            featured: Is this a featured workspace? Default false
            license: Workspace license
            collaborators: Collaborators who work on the workspace
            storage: Storage of the workspace
            tags: The tags of the WorkspaceEntity.

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TWorkspaceEntity":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> WorkspaceEntityDict:
        """
        Convert to a dictionary (eg. to send back for a GET request).

        Returns:
            Dictionary based on the model instance.

        """
        ...

    def to_str(self) -> str:
        """
        Convert to a JSON string (eg. to send back for a GET request).

        Returns:
            JSON string based on the model instance.

        """
        ...


WorkspaceEntity: typing.Type[TWorkspaceEntity] = models.WorkspaceEntity  # type: ignore


class _WorkspaceCollaboratorDictBase(typing_extensions.TypedDict, total=True):
    """TypedDict for properties that are required."""

    user_id: str


class WorkspaceCollaboratorDict(_WorkspaceCollaboratorDictBase, total=False):
    """TypedDict for properties that are not required."""

    id: int


class TWorkspaceCollaborator(typing_extensions.Protocol):
    """
    SQLAlchemy model protocol.

    Workspace Collaborator of a workspace

    Attrs:
        id: The id of the WorkspaceCollaborator.
        user_id: Workspace Collaborator keycloak user id

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    id: 'sqlalchemy.Column[int]'
    user_id: 'sqlalchemy.Column[str]'

    def __init__(self, user_id: str, id: typing.Optional[int] = None) -> None:
        """
        Construct.

        Args:
            id: The id of the WorkspaceCollaborator.
            user_id: Workspace Collaborator keycloak user id

        """
        ...

    @classmethod
    def from_dict(cls, user_id: str, id: typing.Optional[int] = None) -> "TWorkspaceCollaborator":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            id: The id of the WorkspaceCollaborator.
            user_id: Workspace Collaborator keycloak user id

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TWorkspaceCollaborator":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> WorkspaceCollaboratorDict:
        """
        Convert to a dictionary (eg. to send back for a GET request).

        Returns:
            Dictionary based on the model instance.

        """
        ...

    def to_str(self) -> str:
        """
        Convert to a JSON string (eg. to send back for a GET request).

        Returns:
            JSON string based on the model instance.

        """
        ...


WorkspaceCollaborator: typing.Type[TWorkspaceCollaborator] = models.WorkspaceCollaborator  # type: ignore


class _WorkspaceImageDictBase(typing_extensions.TypedDict, total=True):
    """TypedDict for properties that are required."""

    image: str


class WorkspaceImageDict(_WorkspaceImageDictBase, total=False):
    """TypedDict for properties that are not required."""

    id: int


class TWorkspaceImage(typing_extensions.Protocol):
    """
    SQLAlchemy model protocol.

    Workspace images of a workspace

    Attrs:
        id: The id of the WorkspaceImage.
        image: The image of the WorkspaceImage.

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    id: 'sqlalchemy.Column[int]'
    image: 'sqlalchemy.Column[str]'

    def __init__(self, image: str, id: typing.Optional[int] = None) -> None:
        """
        Construct.

        Args:
            id: The id of the WorkspaceImage.
            image: The image of the WorkspaceImage.

        """
        ...

    @classmethod
    def from_dict(cls, image: str, id: typing.Optional[int] = None) -> "TWorkspaceImage":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            id: The id of the WorkspaceImage.
            image: The image of the WorkspaceImage.

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TWorkspaceImage":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> WorkspaceImageDict:
        """
        Convert to a dictionary (eg. to send back for a GET request).

        Returns:
            Dictionary based on the model instance.

        """
        ...

    def to_str(self) -> str:
        """
        Convert to a JSON string (eg. to send back for a GET request).

        Returns:
            JSON string based on the model instance.

        """
        ...


WorkspaceImage: typing.Type[TWorkspaceImage] = models.WorkspaceImage  # type: ignore


class _WorkspaceResourceEntityDictBase(typing_extensions.TypedDict, total=True):
    """TypedDict for properties that are required."""

    name: str
    resource_type: str


class WorkspaceResourceEntityDict(_WorkspaceResourceEntityDictBase, total=False):
    """TypedDict for properties that are not required."""

    origin: typing.Optional[str]
    workspace_id: typing.Optional[int]
    id: int
    folder: typing.Optional[str]
    status: str
    timestamp_created: typing.Optional[str]
    timestamp_updated: typing.Optional[str]
    timestamp_last_opened: typing.Optional[str]


class TWorkspaceResourceEntity(typing_extensions.Protocol):
    """
    SQLAlchemy model protocol.

    Attrs:
        origin: Origin data JSON formatted of the WorkspaceResource
        workspace_id: workspace_id
        id: The id of the WorkspaceResourceEntity.
        name: WorkspaceResource name
        folder: WorkspaceResource folder where the resource will stored in the
            pvc
        status: Resource status:  * a - Available  * e - Error, not available
            * p - Pending
        timestamp_created: Date/time of creation of the WorkspaceResource
        timestamp_updated: Date/time of last updating of the WorkspaceResource
        timestamp_last_opened: Date/time of last opening of the
            WorkspaceResource
        resource_type: Resource type:  * e - Experimental  * m - Model  * g -
            Generic  * u - Unknown (to be defined)

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    origin: 'sqlalchemy.Column[typing.Optional[str]]'
    workspace_id: 'sqlalchemy.Column[typing.Optional[int]]'
    id: 'sqlalchemy.Column[int]'
    name: 'sqlalchemy.Column[str]'
    folder: 'sqlalchemy.Column[typing.Optional[str]]'
    status: 'sqlalchemy.Column[str]'
    timestamp_created: 'sqlalchemy.Column[typing.Optional[datetime.datetime]]'
    timestamp_updated: 'sqlalchemy.Column[typing.Optional[datetime.datetime]]'
    timestamp_last_opened: 'sqlalchemy.Column[typing.Optional[datetime.datetime]]'
    resource_type: 'sqlalchemy.Column[str]'

    def __init__(self, name: str, resource_type: str, origin: typing.Optional[str] = None, workspace_id: typing.Optional[int] = None, id: typing.Optional[int] = None, folder: typing.Optional[str] = None, status: str = "p", timestamp_created: typing.Optional[datetime.datetime] = None, timestamp_updated: typing.Optional[datetime.datetime] = None, timestamp_last_opened: typing.Optional[datetime.datetime] = None) -> None:
        """
        Construct.

        Args:
            origin: Origin data JSON formatted of the WorkspaceResource
            workspace_id: workspace_id
            id: The id of the WorkspaceResourceEntity.
            name: WorkspaceResource name
            folder: WorkspaceResource folder where the resource will stored in
                the pvc
            status: Resource status:  * a - Available  * e - Error, not
                available  * p - Pending
            timestamp_created: Date/time of creation of the WorkspaceResource
            timestamp_updated: Date/time of last updating of the
                WorkspaceResource
            timestamp_last_opened: Date/time of last opening of the
                WorkspaceResource
            resource_type: Resource type:  * e - Experimental  * m - Model  * g
                - Generic  * u - Unknown (to be defined)

        """
        ...

    @classmethod
    def from_dict(cls, name: str, resource_type: str, origin: typing.Optional[str] = None, workspace_id: typing.Optional[int] = None, id: typing.Optional[int] = None, folder: typing.Optional[str] = None, status: str = "p", timestamp_created: typing.Optional[datetime.datetime] = None, timestamp_updated: typing.Optional[datetime.datetime] = None, timestamp_last_opened: typing.Optional[datetime.datetime] = None) -> "TWorkspaceResourceEntity":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            origin: Origin data JSON formatted of the WorkspaceResource
            workspace_id: workspace_id
            id: The id of the WorkspaceResourceEntity.
            name: WorkspaceResource name
            folder: WorkspaceResource folder where the resource will stored in
                the pvc
            status: Resource status:  * a - Available  * e - Error, not
                available  * p - Pending
            timestamp_created: Date/time of creation of the WorkspaceResource
            timestamp_updated: Date/time of last updating of the
                WorkspaceResource
            timestamp_last_opened: Date/time of last opening of the
                WorkspaceResource
            resource_type: Resource type:  * e - Experimental  * m - Model  * g
                - Generic  * u - Unknown (to be defined)

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TWorkspaceResourceEntity":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> WorkspaceResourceEntityDict:
        """
        Convert to a dictionary (eg. to send back for a GET request).

        Returns:
            Dictionary based on the model instance.

        """
        ...

    def to_str(self) -> str:
        """
        Convert to a JSON string (eg. to send back for a GET request).

        Returns:
            JSON string based on the model instance.

        """
        ...


WorkspaceResourceEntity: typing.Type[TWorkspaceResourceEntity] = models.WorkspaceResourceEntity  # type: ignore


class _VolumeStorageDictBase(typing_extensions.TypedDict, total=True):
    """TypedDict for properties that are required."""

    name: str


class VolumeStorageDict(_VolumeStorageDictBase, total=False):
    """TypedDict for properties that are not required."""

    id: int


class TVolumeStorage(typing_extensions.Protocol):
    """
    SQLAlchemy model protocol.

    Volume which can be connected to a workspace

    Attrs:
        id: The id of the VolumeStorage.
        name: StorageVolume name

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    id: 'sqlalchemy.Column[int]'
    name: 'sqlalchemy.Column[str]'

    def __init__(self, name: str, id: typing.Optional[int] = None) -> None:
        """
        Construct.

        Args:
            id: The id of the VolumeStorage.
            name: StorageVolume name

        """
        ...

    @classmethod
    def from_dict(cls, name: str, id: typing.Optional[int] = None) -> "TVolumeStorage":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            id: The id of the VolumeStorage.
            name: StorageVolume name

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TVolumeStorage":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> VolumeStorageDict:
        """
        Convert to a dictionary (eg. to send back for a GET request).

        Returns:
            Dictionary based on the model instance.

        """
        ...

    def to_str(self) -> str:
        """
        Convert to a JSON string (eg. to send back for a GET request).

        Returns:
            JSON string based on the model instance.

        """
        ...


VolumeStorage: typing.Type[TVolumeStorage] = models.VolumeStorage  # type: ignore


class _OSBRepositoryEntityDictBase(typing_extensions.TypedDict, total=True):
    """TypedDict for properties that are required."""

    name: str
    repository_type: str
    content_types: str
    uri: str


class OSBRepositoryEntityDict(_OSBRepositoryEntityDictBase, total=False):
    """TypedDict for properties that are not required."""

    id: int
    summary: typing.Optional[str]
    auto_sync: bool
    default_context: typing.Optional[str]
    user_id: typing.Optional[str]
    timestamp_created: typing.Optional[str]
    timestamp_updated: typing.Optional[str]
    tags: typing.Sequence["TagDict"]


class TOSBRepositoryEntity(typing_extensions.Protocol):
    """
    SQLAlchemy model protocol.

    OSB Repository Base model

    Attrs:
        id: The id of the OSBRepositoryEntity.
        name: Repository name.
        summary: Summary describing the OSB Repository
        repository_type: Repository type:   * dandi - DANDI repository   *
            figshare - FigShare repository   * github - Github repository
        content_types: List of Repository Content Types
        auto_sync: Auto sync of the resources
        uri: URI of the repository
        default_context: The default branch to show for this repository
        user_id: OSBRepository keycloak user id, will be automatically be set
            to the logged in user
        timestamp_created: Date/time the Workspace is created
        timestamp_updated: Date/time the Workspace is last updated
        tags: The tags of the OSBRepositoryEntity.

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    id: 'sqlalchemy.Column[int]'
    name: 'sqlalchemy.Column[str]'
    summary: 'sqlalchemy.Column[typing.Optional[str]]'
    repository_type: 'sqlalchemy.Column[str]'
    content_types: 'sqlalchemy.Column[str]'
    auto_sync: 'sqlalchemy.Column[bool]'
    uri: 'sqlalchemy.Column[str]'
    default_context: 'sqlalchemy.Column[typing.Optional[str]]'
    user_id: 'sqlalchemy.Column[typing.Optional[str]]'
    timestamp_created: 'sqlalchemy.Column[typing.Optional[datetime.datetime]]'
    timestamp_updated: 'sqlalchemy.Column[typing.Optional[datetime.datetime]]'
    tags: 'sqlalchemy.Column[typing.Sequence["TTag"]]'

    def __init__(self, name: str, repository_type: str, content_types: str, uri: str, id: typing.Optional[int] = None, summary: typing.Optional[str] = None, auto_sync: bool = True, default_context: typing.Optional[str] = None, user_id: typing.Optional[str] = None, timestamp_created: typing.Optional[datetime.datetime] = None, timestamp_updated: typing.Optional[datetime.datetime] = None, tags: typing.Optional[typing.Sequence["TTag"]] = None) -> None:
        """
        Construct.

        Args:
            id: The id of the OSBRepositoryEntity.
            name: Repository name.
            summary: Summary describing the OSB Repository
            repository_type: Repository type:   * dandi - DANDI repository   *
                figshare - FigShare repository   * github - Github repository
            content_types: List of Repository Content Types
            auto_sync: Auto sync of the resources
            uri: URI of the repository
            default_context: The default branch to show for this repository
            user_id: OSBRepository keycloak user id, will be automatically be
                set to the logged in user
            timestamp_created: Date/time the Workspace is created
            timestamp_updated: Date/time the Workspace is last updated
            tags: The tags of the OSBRepositoryEntity.

        """
        ...

    @classmethod
    def from_dict(cls, name: str, repository_type: str, content_types: str, uri: str, id: typing.Optional[int] = None, summary: typing.Optional[str] = None, auto_sync: bool = True, default_context: typing.Optional[str] = None, user_id: typing.Optional[str] = None, timestamp_created: typing.Optional[datetime.datetime] = None, timestamp_updated: typing.Optional[datetime.datetime] = None, tags: typing.Optional[typing.Sequence["TagDict"]] = None) -> "TOSBRepositoryEntity":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            id: The id of the OSBRepositoryEntity.
            name: Repository name.
            summary: Summary describing the OSB Repository
            repository_type: Repository type:   * dandi - DANDI repository   *
                figshare - FigShare repository   * github - Github repository
            content_types: List of Repository Content Types
            auto_sync: Auto sync of the resources
            uri: URI of the repository
            default_context: The default branch to show for this repository
            user_id: OSBRepository keycloak user id, will be automatically be
                set to the logged in user
            timestamp_created: Date/time the Workspace is created
            timestamp_updated: Date/time the Workspace is last updated
            tags: The tags of the OSBRepositoryEntity.

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TOSBRepositoryEntity":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> OSBRepositoryEntityDict:
        """
        Convert to a dictionary (eg. to send back for a GET request).

        Returns:
            Dictionary based on the model instance.

        """
        ...

    def to_str(self) -> str:
        """
        Convert to a JSON string (eg. to send back for a GET request).

        Returns:
            JSON string based on the model instance.

        """
        ...


OSBRepositoryEntity: typing.Type[TOSBRepositoryEntity] = models.OSBRepositoryEntity  # type: ignore


class TagDict(typing_extensions.TypedDict, total=False):
    """TypedDict for properties that are not required."""

    id: int
    tag: typing.Optional[str]


class TTag(typing_extensions.Protocol):
    """
    SQLAlchemy model protocol.

    Tags

    Attrs:
        id: The id of the Tag.
        tag: The tag of the Tag.

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    id: 'sqlalchemy.Column[int]'
    tag: 'sqlalchemy.Column[typing.Optional[str]]'

    def __init__(self, id: typing.Optional[int] = None, tag: typing.Optional[str] = None) -> None:
        """
        Construct.

        Args:
            id: The id of the Tag.
            tag: The tag of the Tag.

        """
        ...

    @classmethod
    def from_dict(cls, id: typing.Optional[int] = None, tag: typing.Optional[str] = None) -> "TTag":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            id: The id of the Tag.
            tag: The tag of the Tag.

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TTag":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> TagDict:
        """
        Convert to a dictionary (eg. to send back for a GET request).

        Returns:
            Dictionary based on the model instance.

        """
        ...

    def to_str(self) -> str:
        """
        Convert to a JSON string (eg. to send back for a GET request).

        Returns:
            JSON string based on the model instance.

        """
        ...


Tag: typing.Type[TTag] = models.Tag  # type: ignore


class WorkspaceTagDict(typing_extensions.TypedDict, total=True):
    """TypedDict for properties that are required."""

    workspace_id: int
    tag_id: int


class TWorkspaceTag(typing_extensions.Protocol):
    """
    SQLAlchemy model protocol.

    Attrs:
        workspace_id: The workspace_id of the WorkspaceTag.
        tag_id: The tag_id of the WorkspaceTag.

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    workspace_id: 'sqlalchemy.Column[int]'
    tag_id: 'sqlalchemy.Column[int]'

    def __init__(self, workspace_id: int, tag_id: int) -> None:
        """
        Construct.

        Args:
            workspace_id: The workspace_id of the WorkspaceTag.
            tag_id: The tag_id of the WorkspaceTag.

        """
        ...

    @classmethod
    def from_dict(cls, workspace_id: int, tag_id: int) -> "TWorkspaceTag":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            workspace_id: The workspace_id of the WorkspaceTag.
            tag_id: The tag_id of the WorkspaceTag.

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TWorkspaceTag":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> WorkspaceTagDict:
        """
        Convert to a dictionary (eg. to send back for a GET request).

        Returns:
            Dictionary based on the model instance.

        """
        ...

    def to_str(self) -> str:
        """
        Convert to a JSON string (eg. to send back for a GET request).

        Returns:
            JSON string based on the model instance.

        """
        ...


WorkspaceTag: typing.Type[TWorkspaceTag] = models.WorkspaceTag  # type: ignore


class OsbrepositoryTagDict(typing_extensions.TypedDict, total=True):
    """TypedDict for properties that are required."""

    osbrepository_id: int
    tag_id: int


class TOsbrepositoryTag(typing_extensions.Protocol):
    """
    SQLAlchemy model protocol.

    Attrs:
        osbrepository_id: The osbrepository_id of the OsbrepositoryTag.
        tag_id: The tag_id of the OsbrepositoryTag.

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    osbrepository_id: 'sqlalchemy.Column[int]'
    tag_id: 'sqlalchemy.Column[int]'

    def __init__(self, osbrepository_id: int, tag_id: int) -> None:
        """
        Construct.

        Args:
            osbrepository_id: The osbrepository_id of the OsbrepositoryTag.
            tag_id: The tag_id of the OsbrepositoryTag.

        """
        ...

    @classmethod
    def from_dict(cls, osbrepository_id: int, tag_id: int) -> "TOsbrepositoryTag":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            osbrepository_id: The osbrepository_id of the OsbrepositoryTag.
            tag_id: The tag_id of the OsbrepositoryTag.

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TOsbrepositoryTag":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> OsbrepositoryTagDict:
        """
        Convert to a dictionary (eg. to send back for a GET request).

        Returns:
            Dictionary based on the model instance.

        """
        ...

    def to_str(self) -> str:
        """
        Convert to a JSON string (eg. to send back for a GET request).

        Returns:
            JSON string based on the model instance.

        """
        ...


OsbrepositoryTag: typing.Type[TOsbrepositoryTag] = models.OsbrepositoryTag  # type: ignore
