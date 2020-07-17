/* tslint:disable */
/* eslint-disable */
/**
 * Workspaces manager API
 * Opensource Brain Platform - Reference Workspaces manager API
 *
 * The version of the OpenAPI document: 0.1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { exists, mapValues } from '../runtime';
import {
    WorkspaceType,
    WorkspaceTypeFromJSON,
    WorkspaceTypeFromJSONTyped,
    WorkspaceTypeToJSON,
} from './';

/**
 * 
 * @export
 * @interface InlineObject
 */
export interface InlineObject {
    /**
     * 
     * @type {WorkspaceType}
     * @memberof InlineObject
     */
    workspaceType?: WorkspaceType;
}

export function InlineObjectFromJSON(json: any): InlineObject {
    return InlineObjectFromJSONTyped(json, false);
}

export function InlineObjectFromJSONTyped(json: any, ignoreDiscriminator: boolean): InlineObject {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'workspaceType': !exists(json, 'workspaceType') ? undefined : WorkspaceTypeFromJSON(json['workspaceType']),
    };
}

export function InlineObjectToJSON(value?: InlineObject | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'workspaceType': WorkspaceTypeToJSON(value.workspaceType),
    };
}

