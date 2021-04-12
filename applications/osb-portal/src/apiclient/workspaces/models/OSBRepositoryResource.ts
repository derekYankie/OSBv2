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
    OSBRepositoryResourceAllOf,
    OSBRepositoryResourceAllOfFromJSON,
    OSBRepositoryResourceAllOfFromJSONTyped,
    OSBRepositoryResourceAllOfToJSON,
    RepositoryResource,
    RepositoryResourceFromJSON,
    RepositoryResourceFromJSONTyped,
    RepositoryResourceToJSON,
} from './';

/**
 * 
 * @export
 * @interface OSBRepositoryResource
 */
export interface OSBRepositoryResource {
    /**
     * folder/file name
     * @type {string}
     * @memberof OSBRepositoryResource
     */
    name?: string;
    /**
     * unique identifier for the resource in the (external) repository
     * @type {string}
     * @memberof OSBRepositoryResource
     */
    uid?: string;
    /**
     * 
     * @type {number}
     * @memberof OSBRepositoryResource
     */
    id?: number;
}

export function OSBRepositoryResourceFromJSON(json: any): OSBRepositoryResource {
    return OSBRepositoryResourceFromJSONTyped(json, false);
}

export function OSBRepositoryResourceFromJSONTyped(json: any, ignoreDiscriminator: boolean): OSBRepositoryResource {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'name': !exists(json, 'name') ? undefined : json['name'],
        'uid': !exists(json, 'uid') ? undefined : json['uid'],
        'id': !exists(json, 'id') ? undefined : json['id'],
    };
}

export function OSBRepositoryResourceToJSON(value?: OSBRepositoryResource | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'name': value.name,
        'uid': value.uid,
        'id': value.id,
    };
}


