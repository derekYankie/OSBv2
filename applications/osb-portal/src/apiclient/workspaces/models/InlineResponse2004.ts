/* tslint:disable */
/* eslint-disable */
/**
 * Workspaces manager API
 * Opensource Brain Platform - Reference Workspaces manager API
 *
 * The version of the OpenAPI document: 0.1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { exists, mapValues } from '../runtime';
import {
    Pagination,
    PaginationFromJSON,
    PaginationFromJSONTyped,
    PaginationToJSON,
    VolumeStorage,
    VolumeStorageFromJSON,
    VolumeStorageFromJSONTyped,
    VolumeStorageToJSON,
} from './';

/**
 * 
 * @export
 * @interface InlineResponse2004
 */
export interface InlineResponse2004 {
    /**
     * 
     * @type {Pagination}
     * @memberof InlineResponse2004
     */
    pagination?: Pagination;
    /**
     * 
     * @type {Array<VolumeStorage>}
     * @memberof InlineResponse2004
     */
    volumestorages?: Array<VolumeStorage>;
}

export function InlineResponse2004FromJSON(json: any): InlineResponse2004 {
    return InlineResponse2004FromJSONTyped(json, false);
}

export function InlineResponse2004FromJSONTyped(json: any, ignoreDiscriminator: boolean): InlineResponse2004 {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'pagination': !exists(json, 'pagination') ? undefined : PaginationFromJSON(json['pagination']),
        'volumestorages': !exists(json, 'volumestorages') ? undefined : ((json['volumestorages'] as Array<any>).map(VolumeStorageFromJSON)),
    };
}

export function InlineResponse2004ToJSON(value?: InlineResponse2004 | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'pagination': PaginationToJSON(value.pagination),
        'volumestorages': value.volumestorages === undefined ? undefined : ((value.volumestorages as Array<any>).map(VolumeStorageToJSON)),
    };
}

