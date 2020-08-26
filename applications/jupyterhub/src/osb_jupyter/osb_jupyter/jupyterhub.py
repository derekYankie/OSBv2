import logging
import sys

from kubespawner.spawner import KubeSpawner


def change_pod_manifest(self: KubeSpawner):
    """
    Application Hook to change the manifest of the notebook image
    before spawning it.

    Args:
        self (KubeSpawner): the spawner

    Returns:
        -
    """
    logging.info(f"OSB Jupyter changing pod manifest")
    # get the workspace cookie to determine the workspace id
    workspace_cookie = self.handler.request.cookies.get('workspaceId', None)

    if workspace_cookie:
        workspace_id = workspace_cookie.value
        logging.info(f"Workspace cookie set for workspace {workspace_id}")
        volume_name = f'workspace-{workspace_id}'
        logging.info(f"Mounting volume {volume_name}")
        # We found the workspace id and now we try to mount the
        # workspace persistent volume claim

        # ToDo: get pvc from kubernetes!
        ws_pvc = {'name': volume_name,
                  'persistentVolumeClaim': {
                      'claimName': volume_name,
                      'spec': {
                          'accessModes': ['ReadWriteOne']
                      }
                  }
                  }

        # add the volume to the pod
        self.volumes.append(ws_pvc)
        # mount the workspace volume in the pod
        self.volume_mounts.append({'name': volume_name, 'mountPath': '/home/jovyan/work/workspace'})
    else:
        logging.error("Workspace cookie was not set")
