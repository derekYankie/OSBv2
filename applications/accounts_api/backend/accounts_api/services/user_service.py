from datetime import datetime
from keycloak.exceptions import KeycloakGetError, KeycloakError
from accounts_api.models import User
from cloudharness.auth import AuthClient


class UserNotFound(Exception): pass


class UserNotAuthorized(Exception): pass


def get_user(userid: str) -> User:
    try:
        client = AuthClient()
        kc_user = client.get_user(userid)
    except KeycloakGetError as e:
        if e.response_code == 404:
            raise UserNotFound(userid)
        raise Exception("Unhandled Keycloak exception") from e
    except KeycloakError as e:
        raise Exception("Unhandled Keycloak exception") from e

    user = User.from_dict(kc_user)
    user.profiles = {k[len('profile--')::]: kc_user['attributes'][k][0]
                     for k in kc_user['attributes'] if k.startswith('profile--')}
    user.avatar = kc_user['attributes'].get('avatar', [None])[0]
    user.registration_date = datetime.fromtimestamp(kc_user['createdTimestamp'] / 1000)
    user.website = kc_user['attributes'].get('website', [None])[0]
    user.groups = [g['name'] for g in kc_user['userGroups']]
    try:
        current_user = client.get_current_user()
        if current_user['id'] != userid:
            user.email = None
    except:  # user not provided
        user.email = None
    return user


def update_user(userid, user: User):
    client = AuthClient()

    try:
        current_user = client.get_current_user()
        if current_user['id'] != userid != user.id:
            raise UserNotAuthorized
        admin_client = client.get_admin_client()
        admin_client.update_user(userid, {
            'firstName': user.first_name or current_user['firstName'],
            'lastName': user.last_name or current_user['lastName'],
            'attributes': {
                **current_user['attributes'],
                **{('profile--' + k): user.profiles[k] for k in user.profiles},
                'avatar': user.avatar,
                'website': user.website
            }
        })
    except KeycloakError as e:
        if e.response_code == 404:
            raise UserNotFound(userid)
        raise Exception("Unhandled Keycloak exception") from e