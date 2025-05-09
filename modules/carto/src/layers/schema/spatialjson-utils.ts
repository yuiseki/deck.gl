// deck.gl
// SPDX-License-Identifier: MIT
// Copyright (c) vis.gl contributors

import {bigIntToHex} from 'quadbin';
import {BinaryPointFeature} from '@loaders.gl/schema';

export type IndexScheme = 'h3' | 'quadbin';
type TypedArray = Float32Array | Float64Array;

export type Indices = {value: BigUint64Array};
export type NumericProps = BinaryPointFeature['numericProps'];
export type Properties = BinaryPointFeature['properties'];
export type Cells = {
  indices: Indices;
  numericProps: NumericProps;
  properties: Properties;
};
export type SpatialBinary = {scheme?: IndexScheme; cells: Cells};
export type SpatialJson = {
  id: string | bigint;
  properties: Properties;
}[];

export function binaryToSpatialjson(binary: SpatialBinary): SpatialJson {
  const {cells, scheme} = binary;
  const count = cells.indices.value.length;
  const spatial: any[] = [];
  for (let i = 0; i < count; i++) {
    const id = scheme === 'h3' ? bigIntToHex(cells.indices.value[i]) : cells.indices.value[i];

    const properties = {...cells.properties[i]};
    for (const key of Object.keys(cells.numericProps)) {
      properties[key] = cells.numericProps[key].value[i];
    }
    spatial.push({id, properties});
  }

  return spatial;
}
