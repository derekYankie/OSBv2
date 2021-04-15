import json

from workspaces.repository.models import WorkspaceEntity, WorkspaceResourceEntity

from ..base_model_view import BaseModelView
from workspaces.repository import WorkspaceRepository, OSBRepositoryRepository, \
    VolumeStorageRepository, WorkspaceResourceRepository
from workspaces.models import OSBRepository, OSBRepository, OSBRepositoryEntity, Workspace


class WorkspaceView(BaseModelView):
    repository = WorkspaceRepository()

    def post(self, body):
        for r in body.get("resources", []):
            r.update({"origin": json.dumps(r.get("origin"))})
        return super().post(body)

    def get(self, id_):
        workspace = super().get(id_)
        for r in workspace.get("resources", []):
            r.update({"origin": json.loads(r.get("origin"))})
        return workspace

class OsbrepositoryView(BaseModelView):
    repository = OSBRepositoryRepository()

    def post(self, body):
        content_types = ""
        # convert the content types list to a content type comma separated string
        for ct in body["content_types_list"]:
            content_types += f",{ct}"
        body.update({"content_types": content_types.strip(",")})
        body = OSBRepositoryEntity().from_dict(OSBRepository.from_dict(body).to_dict()).to_dict()
        return super().post(body)

class VolumestorageView(BaseModelView):
    repository = VolumeStorageRepository()

class WorkspaceresourceView(BaseModelView):
    repository = WorkspaceResourceRepository()

    def post(self, body):
        body.update({"origin": json.dumps(body.get("origin"))})
        return super().post(body)

    def get(self, id_):
        workspace_resource = super().get(id_)
        workspace_resource.update({"origin": json.loads(workspace_resource.get("origin"))})
        return workspace_resource