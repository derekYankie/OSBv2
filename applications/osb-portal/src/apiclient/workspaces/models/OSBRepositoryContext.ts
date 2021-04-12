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
    OSBRepositoryResource,
    OSBRepositoryResourceFromJSON,
    OSBRepositoryResourceFromJSONTyped,
    OSBRepositoryResourceToJSON,
} from './';

/**
 * OSBRepository context
 * @export
 * @interface OSBRepositoryContext
 */
export interface OSBRepositoryContext {
    /**
     * 
     * @type {number}
     * @memberof OSBRepositoryContext
     */
    id?: number;
    /**
     * Name of the repository context
     * @type {string}
     * @memberof OSBRepositoryContext
     */
    name?: string;
    /**
     * List of used/referenced resources in this context
     * @type {Array<OSBRepositoryResource>}
     * @memberof OSBRepositoryContext
     */
    resources?: Array<OSBRepositoryResource>;
}

export function OSBRepositoryContextFromJSON(json: any): OSBRepositoryContext {
    return OSBRepositoryContextFromJSONTyped(json, false);
}

export function OSBRepositoryContextFromJSONTyped(json: any, ignoreDiscriminator: boolean): OSBRepositoryContext {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'id': !exists(json, 'id') ? undefined : json['id'],
        'name': !exists(json, 'name') ? undefined : json['name'],
        'resources': !exists(json, 'resources') ? undefined : ((json['resources'] as Array<any>).map(OSBRepositoryResourceFromJSON)),
    };
}

export function OSBRepositoryContextToJSON(value?: OSBRepositoryContext | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'id': value.id,
        'name': value.name,
        'resources': value.resources === undefined ? undefined : ((value.resources as Array<any>).map(OSBRepositoryResourceToJSON)),
    };
}


