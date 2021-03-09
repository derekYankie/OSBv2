import sys

import yaml
from jupyterhub.user import User
from kubespawner.spawner import KubeSpawner

from cloudharness.auth import AuthClient
from cloudharness import log
from pprint import pprint


def change_pod_manifest(self: KubeSpawner):
    """
    Application Hook to change the manifest of the notebook image
    before spawning it.

    Args:
        self (KubeSpawner): the spawner

    Returns:
        -
    """

    # get the workspace cookie to determine the workspace id

    def get_from_cookie(cookie_name):
        cookie = self.handler.request.cookies.get(cookie_name, None)
        if cookie is None:
            raise Exception(
                "Required cookie not found. Check that the cookie named '%s' is set.", cookie_name)
        return cookie.value

    try:
        workspace_id = get_from_cookie('workspaceId')
        volume_name = f'workspace-{workspace_id}'
        log.info('Mapping to volume %s', volume_name)

        # We found the workspace id and now we try to mount the
        # workspace persistent volume claim

        ws_pvc = {
            'name': volume_name,
            'persistentVolumeClaim': {
                'claimName': volume_name,
                'spec': {
                    'accessModes': ['ReadWriteOnce', 'ReadOnlyMany']
                }
            }
        }

        self.extra_labels['workspace'] = str(workspace_id)

        # add the volume to the pod
        self.volumes.append(ws_pvc)

        workspace_owner = get_from_cookie('workspaceOwner')

        # mount the workspace volume in the pod
        write_access = has_user_write_access(
            workspace_id, self.user, workspace_owner)

        if write_access:
            # Pods with write access must be on the same node
            affinity_spec = {
                'labelSelector':
                    {
                        'matchExpressions': [
                            {
                                'key': 'workspace',
                                'operator': 'In',
                                'values': [str(workspace_id)]
                            },
                        ]
                    },
                    'topologyKey': 'topology.kubernetes.io/zone'
            }

            self.pod_affinity_required.append(affinity_spec)

        self.volume_mounts.append({
            'name': volume_name,
            'mountPath': '/opt/workspace',
            'readOnly': not write_access
        })
        print(self.__dict__)
    except Exception as e:
        log.error('Change pod manifest failed due to an error.', exc_info=True)


def has_user_write_access(workspace_id, user: User, workspace_owner: str):
    print('name:', user.name, workspace_owner)
    if workspace_owner == user.name:
        return True
    auth_client = AuthClient()
    return auth_client.user_has_realm_role(user.name, 'administrator')
