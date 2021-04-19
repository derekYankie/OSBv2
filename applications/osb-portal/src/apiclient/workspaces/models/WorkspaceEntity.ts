/* tslint:disable */
/* eslint-disable */
/**
 * Workspaces manager API
 * Opensource Brain Platform - Reference Workspaces manager API
 *
 * The version of the OpenAPI document: 0.2.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { exists, mapValues } from '../runtime';
import {
    VolumeStorage,
    VolumeStorageFromJSON,
    VolumeStorageFromJSONTyped,
    VolumeStorageToJSON,
    WorkspaceBase,
    WorkspaceBaseFromJSON,
    WorkspaceBaseFromJSONTyped,
    WorkspaceBaseToJSON,
    WorkspaceCollaborator,
    WorkspaceCollaboratorFromJSON,
    WorkspaceCollaboratorFromJSONTyped,
    WorkspaceCollaboratorToJSON,
    WorkspaceEntityAllOf,
    WorkspaceEntityAllOfFromJSON,
    WorkspaceEntityAllOfFromJSONTyped,
    WorkspaceEntityAllOfToJSON,
    WorkspaceImage,
    WorkspaceImageFromJSON,
    WorkspaceImageFromJSONTyped,
    WorkspaceImageToJSON,
    WorkspaceResourceEntity,
    WorkspaceResourceEntityFromJSON,
    WorkspaceResourceEntityFromJSONTyped,
    WorkspaceResourceEntityToJSON,
    WorkspaceTag,
    WorkspaceTagFromJSON,
    WorkspaceTagFromJSONTyped,
    WorkspaceTagToJSON,
} from './';

/**
 * Workspace model
 * @export
 * @interface WorkspaceEntity
 */
export interface WorkspaceEntity {
    /**
     * 
     * @type {number}
     * @memberof WorkspaceEntity
     */
    id?: number;
    /**
     * Workspace name.
     * @type {string}
     * @memberof WorkspaceEntity
     */
    name: string;
    /**
     * Workspace description.
     * @type {string}
     * @memberof WorkspaceEntity
     */
    description: string;
    /**
     * Date/time the Workspace is created
     * @type {Date}
     * @memberof WorkspaceEntity
     */
    timestampCreated?: Date;
    /**
     * Date/time the Workspace is last updated
     * @type {Date}
     * @memberof WorkspaceEntity
     */
    timestampUpdated?: Date;
    /**
     * Workspace tags
     * @type {Array<WorkspaceTag>}
     * @memberof WorkspaceEntity
     */
    tags?: Array<WorkspaceTag>;
    /**
     * The workspace resource id the workspace is opened last with
     * @type {number}
     * @memberof WorkspaceEntity
     */
    lastOpenedResourceId?: number;
    /**
     * 
     * @type {string}
     * @memberof WorkspaceEntity
     */
    thumbnail?: string;
    /**
     * Gallery with images of the workspace
     * @type {Array<WorkspaceImage>}
     * @memberof WorkspaceEntity
     */
    gallery?: Array<WorkspaceImage>;
    /**
     * Workspace keycloak user id, will be automatically be set to the logged in user
     * @type {string}
     * @memberof WorkspaceEntity
     */
    userId?: string;
    /**
     * Is the workspace available for non collaborators? Default false
     * @type {boolean}
     * @memberof WorkspaceEntity
     */
    publicable?: boolean;
    /**
     * Workspace license
     * @type {string}
     * @memberof WorkspaceEntity
     */
    license?: string;
    /**
     * Collaborators who work on the workspace
     * @type {Array<WorkspaceCollaborator>}
     * @memberof WorkspaceEntity
     */
    collaborators?: Array<WorkspaceCollaborator>;
    /**
     * 
     * @type {VolumeStorage}
     * @memberof WorkspaceEntity
     */
    storage?: VolumeStorage;
    /**
     * Resources of the workspace
     * @type {Array<WorkspaceResourceEntity>}
     * @memberof WorkspaceEntity
     */
    resources?: Array<WorkspaceResourceEntity>;
}

export function WorkspaceEntityFromJSON(json: any): WorkspaceEntity {
    return WorkspaceEntityFromJSONTyped(json, false);
}

export function WorkspaceEntityFromJSONTyped(json: any, ignoreDiscriminator: boolean): WorkspaceEntity {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'id': !exists(json, 'id') ? undefined : json['id'],
        'name': json['name'],
        'description': json['description'],
        'timestampCreated': !exists(json, 'timestamp_created') ? undefined : (new Date(json['timestamp_created'])),
        'timestampUpdated': !exists(json, 'timestamp_updated') ? undefined : (new Date(json['timestamp_updated'])),
        'tags': !exists(json, 'tags') ? undefined : ((json['tags'] as Array<any>).map(WorkspaceTagFromJSON)),
        'lastOpenedResourceId': !exists(json, 'last_opened_resource_id') ? undefined : json['last_opened_resource_id'],
        'thumbnail': !exists(json, 'thumbnail') ? undefined : json['thumbnail'],
        'gallery': !exists(json, 'gallery') ? undefined : ((json['gallery'] as Array<any>).map(WorkspaceImageFromJSON)),
        'userId': !exists(json, 'user_id') ? undefined : json['user_id'],
        'publicable': !exists(json, 'publicable') ? undefined : json['publicable'],
        'license': !exists(json, 'license') ? undefined : json['license'],
        'collaborators': !exists(json, 'collaborators') ? undefined : ((json['collaborators'] as Array<any>).map(WorkspaceCollaboratorFromJSON)),
        'storage': !exists(json, 'storage') ? undefined : VolumeStorageFromJSON(json['storage']),
        'resources': !exists(json, 'resources') ? undefined : ((json['resources'] as Array<any>).map(WorkspaceResourceEntityFromJSON)),
    };
}

export function WorkspaceEntityToJSON(value?: WorkspaceEntity | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'id': value.id,
        'name': value.name,
        'description': value.description,
        'timestamp_created': value.timestampCreated === undefined ? undefined : (value.timestampCreated.toISOString()),
        'timestamp_updated': value.timestampUpdated === undefined ? undefined : (value.timestampUpdated.toISOString()),
        'tags': value.tags === undefined ? undefined : ((value.tags as Array<any>).map(WorkspaceTagToJSON)),
        'last_opened_resource_id': value.lastOpenedResourceId,
        'thumbnail': value.thumbnail,
        'gallery': value.gallery === undefined ? undefined : ((value.gallery as Array<any>).map(WorkspaceImageToJSON)),
        'user_id': value.userId,
        'publicable': value.publicable,
        'license': value.license,
        'collaborators': value.collaborators === undefined ? undefined : ((value.collaborators as Array<any>).map(WorkspaceCollaboratorToJSON)),
        'storage': VolumeStorageToJSON(value.storage),
        'resources': value.resources === undefined ? undefined : ((value.resources as Array<any>).map(WorkspaceResourceEntityToJSON)),
    };
}

