"""Autogenerated SQLAlchemy models based on OpenAlchemy models."""
# pylint: disable=no-member,super-init-not-called,unused-argument

import datetime
import typing

import sqlalchemy
import typing_extensions
from sqlalchemy import orm

from open_alchemy import models


class UserDict(typing_extensions.TypedDict, total=False):
    """TypedDict for properties that are not required."""

    id: int
    keycloak_id: typing.Optional[str]
    firstname: typing.Optional[str]
    lastname: typing.Optional[str]
    email: typing.Optional[str]


class TUser(typing_extensions.Protocol):
    """
    SQLAlchemy model protocol.

    key cloak User

    Attrs:
        id: The id of the User.
        keycloak_id: Keycloak user id
        firstname: First name of the user (derived from Keycload)
        lastname: Last name of the user (derived from Keycload)
        email: Email address of the user (derived from Keycloak)

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    id: int
    keycloak_id: typing.Optional[str]
    firstname: typing.Optional[str]
    lastname: typing.Optional[str]
    email: typing.Optional[str]

    def __init__(
        self,
        id: typing.Optional[int] = None,
        keycloak_id: typing.Optional[str] = None,
        firstname: typing.Optional[str] = None,
        lastname: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
    ) -> None:
        """
        Construct.

        Args:
            id: The id of the User.
            keycloak_id: Keycloak user id
            firstname: First name of the user (derived from Keycload)
            lastname: Last name of the user (derived from Keycload)
            email: Email address of the user (derived from Keycloak)

        """
        ...

    @classmethod
    def from_dict(
        cls,
        id: typing.Optional[int] = None,
        keycloak_id: typing.Optional[str] = None,
        firstname: typing.Optional[str] = None,
        lastname: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
    ) -> "TUser":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            id: The id of the User.
            keycloak_id: Keycloak user id
            firstname: First name of the user (derived from Keycload)
            lastname: Last name of the user (derived from Keycload)
            email: Email address of the user (derived from Keycloak)

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TUser":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> UserDict:
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


User: TUser = models.User  # type: ignore


class _WorkspaceDictBase(typing_extensions.TypedDict, total=True):
    """TypedDict for properties that are required."""

    name: str
    description: str


class WorkspaceDict(_WorkspaceDictBase, total=False):
    """TypedDict for properties that are not required."""

    id: int
    timestamp_created: typing.Optional[datetime.datetime]
    timestamp_updated: typing.Optional[datetime.datetime]
    tags: typing.Sequence["WorkspaceTagDict"]
    last_opened_resource_id: typing.Optional[int]
    thumbnail: typing.Optional[str]
    gallery: typing.Sequence["WorkspaceImageDict"]
    owner: typing.Optional["UserDict"]
    publicable: bool
    license: typing.Optional[str]
    collaborators: typing.Sequence["UserDict"]
    resources: typing.Sequence["WorkspaceResourceDict"]
    storage: typing.Optional["VolumeStorageDict"]


class TWorkspace(typing_extensions.Protocol):
    """
    SQLAlchemy model protocol.

    Workspace item

    Attrs:
        id: The id of the Workspace.
        name: Workspace name.
        description: Workspace description.
        timestamp_created: Date/time the Workspace is created
        timestamp_updated: Date/time the Workspace is last updated
        tags: Workspace tags
        last_opened_resource_id: The workspace resource id the workspace is
            opened last with
        thumbnail: The thumbnail of the Workspace.
        gallery: Gallery with images of the workspace
        owner: The owner of the Workspace.
        publicable: Is the workspace available for non collaborators? Default
            false
        license: Workspace license
        collaborators: Collaborators who work on the workspace
        resources: Resources of the workspace
        storage: The storage of the Workspace.

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    id: int
    name: str
    description: str
    timestamp_created: typing.Optional[datetime.datetime]
    timestamp_updated: typing.Optional[datetime.datetime]
    tags: typing.Sequence["TWorkspaceTag"]
    last_opened_resource_id: typing.Optional[int]
    thumbnail: typing.Optional[str]
    gallery: typing.Sequence["TWorkspaceImage"]
    owner: typing.Optional["TUser"]
    publicable: bool
    license: typing.Optional[str]
    collaborators: typing.Sequence["TUser"]
    resources: typing.Sequence["TWorkspaceResource"]
    storage: typing.Optional["TVolumeStorage"]

    def __init__(
        self,
        name: str,
        description: str,
        id: typing.Optional[int] = None,
        timestamp_created: typing.Optional[datetime.datetime] = None,
        timestamp_updated: typing.Optional[datetime.datetime] = None,
        tags: typing.Optional[typing.Sequence["TWorkspaceTag"]] = None,
        last_opened_resource_id: typing.Optional[int] = None,
        thumbnail: typing.Optional[str] = None,
        gallery: typing.Optional[typing.Sequence["TWorkspaceImage"]] = None,
        owner: typing.Optional["TUser"] = None,
        publicable: bool = False,
        license: typing.Optional[str] = None,
        collaborators: typing.Optional[typing.Sequence["TUser"]] = None,
        resources: typing.Optional[typing.Sequence["TWorkspaceResource"]] = None,
        storage: typing.Optional["TVolumeStorage"] = None,
    ) -> None:
        """
        Construct.

        Args:
            id: The id of the Workspace.
            name: Workspace name.
            description: Workspace description.
            timestamp_created: Date/time the Workspace is created
            timestamp_updated: Date/time the Workspace is last updated
            tags: Workspace tags
            last_opened_resource_id: The workspace resource id the workspace is
                opened last with
            thumbnail: The thumbnail of the Workspace.
            gallery: Gallery with images of the workspace
            owner: The owner of the Workspace.
            publicable: Is the workspace available for non collaborators?
                Default false
            license: Workspace license
            collaborators: Collaborators who work on the workspace
            resources: Resources of the workspace
            storage: The storage of the Workspace.

        """
        ...

    @classmethod
    def from_dict(
        cls,
        name: str,
        description: str,
        id: typing.Optional[int] = None,
        timestamp_created: typing.Optional[datetime.datetime] = None,
        timestamp_updated: typing.Optional[datetime.datetime] = None,
        tags: typing.Optional[typing.Sequence["WorkspaceTagDict"]] = None,
        last_opened_resource_id: typing.Optional[int] = None,
        thumbnail: typing.Optional[str] = None,
        gallery: typing.Optional[typing.Sequence["WorkspaceImageDict"]] = None,
        owner: typing.Optional["UserDict"] = None,
        publicable: bool = False,
        license: typing.Optional[str] = None,
        collaborators: typing.Optional[typing.Sequence["UserDict"]] = None,
        resources: typing.Optional[typing.Sequence["WorkspaceResourceDict"]] = None,
        storage: typing.Optional["VolumeStorageDict"] = None,
    ) -> "TWorkspace":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            id: The id of the Workspace.
            name: Workspace name.
            description: Workspace description.
            timestamp_created: Date/time the Workspace is created
            timestamp_updated: Date/time the Workspace is last updated
            tags: Workspace tags
            last_opened_resource_id: The workspace resource id the workspace is
                opened last with
            thumbnail: The thumbnail of the Workspace.
            gallery: Gallery with images of the workspace
            owner: The owner of the Workspace.
            publicable: Is the workspace available for non collaborators?
                Default false
            license: Workspace license
            collaborators: Collaborators who work on the workspace
            resources: Resources of the workspace
            storage: The storage of the Workspace.

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TWorkspace":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> WorkspaceDict:
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


Workspace: TWorkspace = models.Workspace  # type: ignore


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
    id: int
    image: str

    def __init__(self, image: str, id: typing.Optional[int] = None) -> None:
        """
        Construct.

        Args:
            id: The id of the WorkspaceImage.
            image: The image of the WorkspaceImage.

        """
        ...

    @classmethod
    def from_dict(
        cls, image: str, id: typing.Optional[int] = None
    ) -> "TWorkspaceImage":
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


WorkspaceImage: TWorkspaceImage = models.WorkspaceImage  # type: ignore


class _WorkspaceTagDictBase(typing_extensions.TypedDict, total=True):
    """TypedDict for properties that are required."""

    tag: str


class WorkspaceTagDict(_WorkspaceTagDictBase, total=False):
    """TypedDict for properties that are not required."""

    id: int


class TWorkspaceTag(typing_extensions.Protocol):
    """
    SQLAlchemy model protocol.

    Workspace tags linking to workspaces

    Attrs:
        id: The id of the WorkspaceTag.
        tag: WorkspaceTag tag

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    id: int
    tag: str

    def __init__(self, tag: str, id: typing.Optional[int] = None) -> None:
        """
        Construct.

        Args:
            id: The id of the WorkspaceTag.
            tag: WorkspaceTag tag

        """
        ...

    @classmethod
    def from_dict(cls, tag: str, id: typing.Optional[int] = None) -> "TWorkspaceTag":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            id: The id of the WorkspaceTag.
            tag: WorkspaceTag tag

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


WorkspaceTag: TWorkspaceTag = models.WorkspaceTag  # type: ignore


class _WorkspaceResourceDictBase(typing_extensions.TypedDict, total=True):
    """TypedDict for properties that are required."""

    name: str
    location: str
    resource_type: str


class WorkspaceResourceDict(_WorkspaceResourceDictBase, total=False):
    """TypedDict for properties that are not required."""

    id: int
    folder: typing.Optional[str]
    status: str
    timestamp_created: typing.Optional[datetime.datetime]
    timestamp_updated: typing.Optional[datetime.datetime]
    timestamp_last_opened: typing.Optional[datetime.datetime]
    workspace_id: typing.Optional[int]


class TWorkspaceResource(typing_extensions.Protocol):
    """
    SQLAlchemy model protocol.

    Workspace Resource item of a Workspace

    Attrs:
        id: The id of the WorkspaceResource.
        name: WorkspaceResource name
        location: WorkspaceResource location original location of the resource
        folder: WorkspaceResource folder where the resource will stored in the
            pvc
        status: Resource status:  * a - Available  * e - Error, not available
            * p - Pending
        timestamp_created: Date/time of creation of the WorkspaceResource
        timestamp_updated: Date/time of last updating of the WorkspaceResource
        timestamp_last_opened: Date/time of last opening of the
            WorkspaceResource
        resource_type: Resource type:  * e - Experimental  * m - Model  * g -
            Generic
        workspace_id: workspace_id

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    id: int
    name: str
    location: str
    folder: typing.Optional[str]
    status: str
    timestamp_created: typing.Optional[datetime.datetime]
    timestamp_updated: typing.Optional[datetime.datetime]
    timestamp_last_opened: typing.Optional[datetime.datetime]
    resource_type: str
    workspace_id: typing.Optional[int]

    def __init__(
        self,
        name: str,
        location: str,
        resource_type: str,
        id: typing.Optional[int] = None,
        folder: typing.Optional[str] = None,
        status: str = "p",
        timestamp_created: typing.Optional[datetime.datetime] = None,
        timestamp_updated: typing.Optional[datetime.datetime] = None,
        timestamp_last_opened: typing.Optional[datetime.datetime] = None,
        workspace_id: typing.Optional[int] = None,
    ) -> None:
        """
        Construct.

        Args:
            id: The id of the WorkspaceResource.
            name: WorkspaceResource name
            location: WorkspaceResource location original location of the
                resource
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
                - Generic
            workspace_id: workspace_id

        """
        ...

    @classmethod
    def from_dict(
        cls,
        name: str,
        location: str,
        resource_type: str,
        id: typing.Optional[int] = None,
        folder: typing.Optional[str] = None,
        status: str = "p",
        timestamp_created: typing.Optional[datetime.datetime] = None,
        timestamp_updated: typing.Optional[datetime.datetime] = None,
        timestamp_last_opened: typing.Optional[datetime.datetime] = None,
        workspace_id: typing.Optional[int] = None,
    ) -> "TWorkspaceResource":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            id: The id of the WorkspaceResource.
            name: WorkspaceResource name
            location: WorkspaceResource location original location of the
                resource
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
                - Generic
            workspace_id: workspace_id

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TWorkspaceResource":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> WorkspaceResourceDict:
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


WorkspaceResource: TWorkspaceResource = models.WorkspaceResource  # type: ignore


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
    id: int
    name: str

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


VolumeStorage: TVolumeStorage = models.VolumeStorage  # type: ignore


class _OSBRepositoryDictBase(typing_extensions.TypedDict, total=True):
    """TypedDict for properties that are required."""

    uuid: str
    name: str
    storage: "VolumeStorageDict"


class OSBRepositoryDict(_OSBRepositoryDictBase, total=False):
    """TypedDict for properties that are not required."""

    id: int
    resources: typing.Sequence["WorkspaceResourceDict"]


class TOSBRepository(typing_extensions.Protocol):
    """
    SQLAlchemy model protocol.

    Opensource brain repository

    Attrs:
        id: The id of the OSBRepository.
        uuid: Universally unique identifier of the OSB repository
        name: OSB repository name
        storage: The storage of the OSBRepository.
        resources: The resources of the OSBRepository.

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    id: int
    uuid: str
    name: str
    storage: "TVolumeStorage"
    resources: typing.Sequence["TWorkspaceResource"]

    def __init__(
        self,
        uuid: str,
        name: str,
        storage: "TVolumeStorage",
        id: typing.Optional[int] = None,
        resources: typing.Optional[typing.Sequence["TWorkspaceResource"]] = None,
    ) -> None:
        """
        Construct.

        Args:
            id: The id of the OSBRepository.
            uuid: Universally unique identifier of the OSB repository
            name: OSB repository name
            storage: The storage of the OSBRepository.
            resources: The resources of the OSBRepository.

        """
        ...

    @classmethod
    def from_dict(
        cls,
        uuid: str,
        name: str,
        storage: "VolumeStorageDict",
        id: typing.Optional[int] = None,
        resources: typing.Optional[typing.Sequence["WorkspaceResourceDict"]] = None,
    ) -> "TOSBRepository":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            id: The id of the OSBRepository.
            uuid: Universally unique identifier of the OSB repository
            name: OSB repository name
            storage: The storage of the OSBRepository.
            resources: The resources of the OSBRepository.

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TOSBRepository":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> OSBRepositoryDict:
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


OSBRepository: TOSBRepository = models.OSBRepository  # type: ignore


class _GITRepositoryDictBase(typing_extensions.TypedDict, total=True):
    """TypedDict for properties that are required."""

    public_key: str
    private_key: str
    url: str


class GITRepositoryDict(_GITRepositoryDictBase, total=False):
    """TypedDict for properties that are not required."""

    id: int


class TGITRepository(typing_extensions.Protocol):
    """
    SQLAlchemy model protocol.

    GIT repository

    Attrs:
        id: The id of the GITRepository.
        public_key: Public key of the git repository
        private_key: Public key of the git repository
        url: URL of the git repository

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    id: int
    public_key: str
    private_key: str
    url: str

    def __init__(
        self,
        public_key: str,
        private_key: str,
        url: str,
        id: typing.Optional[int] = None,
    ) -> None:
        """
        Construct.

        Args:
            id: The id of the GITRepository.
            public_key: Public key of the git repository
            private_key: Public key of the git repository
            url: URL of the git repository

        """
        ...

    @classmethod
    def from_dict(
        cls,
        public_key: str,
        private_key: str,
        url: str,
        id: typing.Optional[int] = None,
    ) -> "TGITRepository":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            id: The id of the GITRepository.
            public_key: Public key of the git repository
            private_key: Public key of the git repository
            url: URL of the git repository

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TGITRepository":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> GITRepositoryDict:
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


GITRepository: TGITRepository = models.GITRepository  # type: ignore


class _FigshareRepositoryDictBase(typing_extensions.TypedDict, total=True):
    """TypedDict for properties that are required."""

    url: str


class FigshareRepositoryDict(_FigshareRepositoryDictBase, total=False):
    """TypedDict for properties that are not required."""

    id: int


class TFigshareRepository(typing_extensions.Protocol):
    """
    SQLAlchemy model protocol.

    Figshare repository

    Attrs:
        id: The id of the FigshareRepository.
        url: URL of the figshare repository

    """

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    id: int
    url: str

    def __init__(self, url: str, id: typing.Optional[int] = None) -> None:
        """
        Construct.

        Args:
            id: The id of the FigshareRepository.
            url: URL of the figshare repository

        """
        ...

    @classmethod
    def from_dict(
        cls, url: str, id: typing.Optional[int] = None
    ) -> "TFigshareRepository":
        """
        Construct from a dictionary (eg. a POST payload).

        Args:
            id: The id of the FigshareRepository.
            url: URL of the figshare repository

        Returns:
            Model instance based on the dictionary.

        """
        ...

    @classmethod
    def from_str(cls, value: str) -> "TFigshareRepository":
        """
        Construct from a JSON string (eg. a POST payload).

        Returns:
            Model instance based on the JSON string.

        """
        ...

    def to_dict(self) -> FigshareRepositoryDict:
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


FigshareRepository: TFigshareRepository = models.FigshareRepository  # type: ignore
