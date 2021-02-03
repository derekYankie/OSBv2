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

import { RequestFile } from '../api';
import { ResourceStatus } from './resourceStatus';
import { ResourceType } from './resourceType';

/**
* Workspace Resource item of a Workspace
*/
export class WorkspaceResource {
    'id'?: number;
    /**
    * WorkspaceResource name
    */
    'name': string;
    /**
    * WorkspaceResource location original location of the resource
    */
    'location': string;
    /**
    * WorkspaceResource folder where the resource will stored in the pvc
    */
    'folder'?: string;
    'status'?: ResourceStatus;
    /**
    * Date/time of creation of the WorkspaceResource
    */
    'timestampCreated'?: Date;
    /**
    * Date/time of last updating of the WorkspaceResource
    */
    'timestampUpdated'?: Date;
    /**
    * Date/time of last opening of the WorkspaceResource
    */
    'timestampLastOpened'?: Date;
    'resourceType': ResourceType;
    /**
    * The id of the Workspace this Workspace Resource belongs to
    */
    'workspaceId': number;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "id",
            "baseName": "id",
            "type": "number"
        },
        {
            "name": "name",
            "baseName": "name",
            "type": "string"
        },
        {
            "name": "location",
            "baseName": "location",
            "type": "string"
        },
        {
            "name": "folder",
            "baseName": "folder",
            "type": "string"
        },
        {
            "name": "status",
            "baseName": "status",
            "type": "ResourceStatus"
        },
        {
            "name": "timestampCreated",
            "baseName": "timestamp_created",
            "type": "Date"
        },
        {
            "name": "timestampUpdated",
            "baseName": "timestamp_updated",
            "type": "Date"
        },
        {
            "name": "timestampLastOpened",
            "baseName": "timestamp_last_opened",
            "type": "Date"
        },
        {
            "name": "resourceType",
            "baseName": "resource_type",
            "type": "ResourceType"
        },
        {
            "name": "workspaceId",
            "baseName": "workspace_id",
            "type": "number"
        }    ];

    static getAttributeTypeMap() {
        return WorkspaceResource.attributeTypeMap;
    }
}

