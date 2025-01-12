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

/**
 * Resource type:
 *  * e - Experimental
 *  * m - Model
 *  * g - Generic
 *  * u - Unknown (to be defined)
 * @export
 * @enum {string}
 */
export enum ResourceType {
    E = 'e',
    M = 'm',
    G = 'g',
    U = 'u'
}

export function ResourceTypeFromJSON(json: any): ResourceType {
    return ResourceTypeFromJSONTyped(json, false);
}

export function ResourceTypeFromJSONTyped(json: any, ignoreDiscriminator: boolean): ResourceType {
    return json as ResourceType;
}

export function ResourceTypeToJSON(value?: ResourceType | null): any {
    return value as any;
}

