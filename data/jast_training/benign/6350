/**
 * Copyright (C) 2016 Swift Navigation Inc.
 * Contact: Joshua Gross <josh@swift-nav.com>
 * This source is subject to the license found in the file 'LICENSE' which must
 * be distributed together with this source. All other rights reserved.
 *
 * THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
 * EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED
 * WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE.
 */

import assert from 'assert';
import geohash from 'latlon-geohash';
import zipObject from 'lodash.zipobject';
import rangeRight from 'lodash.rangeright';

export default class GeohashHeatmap {
  /**
   * If heatmap parameter is passed, this becomes a copy constructor.
   */
  constructor (otherHeatmap = null) {
    if (otherHeatmap !== null) {
      assert(otherHeatmap instanceof GeohashHeatmap,
             'when constructor is used as copy constructor, you must pass a valid GeohashHeatmap object');
      this.heatmap = Object.assign({}, otherHeatmap.heatmap);
    } else {
      this.heatmap = {};
    }
  }

  /**
   * Add a latlong point to the heatmap.
   *
   * Expects latlongs to be decimal degrees, floating-point format:
   * https://www.maptools.com/tutorials/lat_lon/formats
   * where positive latitude is North, negative is South.
   * Longitude: negative is west, positive is east.
   *
   * @param {Number} lat Latitude in floating-point format.
   * @param {Number} lon Longitude in floating-point format.
   */
  addLatLong (lat, lon) {
    // All hashes are precision 12.
    return this.addGeohash(geohash.encode(lat, lon, 12));
  }

  /**
   * Add geohash to map.
   *
   * @param {String} hash A geohash encoding of a position, between 1 and 12 characters inclusive.
   */
  addGeohash (hash) {
    assert(typeof hash === 'string', 'geohash must be string');
    assert(hash.length > 0 && hash.length <= 12, 'geohash length must be between 0 and 12, inclusive');

    this.heatmap.count = (this.heatmap.count || 0) + 1;

    const now = Date.now();

    // Neighbors looks like:
    // {
    //   NE: hash0,
    //   NW: hash1,
    //   N: hash2,
    //   W: hash3,
    //   ...
    // }
    const neighbors = geohash.neighbours(hash);
    const neighborKeys = Object.keys(neighbors); // N, S, E, W, NW, NE, SW, SE
    const directionWeights = neighborKeys.map(k => 0.5 / k.length);
    const directionalAmender = zipObject(Object.values(neighbors), directionWeights);

    // This hashmap is added to the global map
    // This hashmap looks something like:
    // {
    //   [hash]: 1
    //   [NE/SE/NW/SW hash]: 0.25
    //   [N/S/E/W hash]: 0.5
    // }
    const amender = Object.assign({
      [hash]: 1
    }, directionalAmender);

    // Construct a dictionary with one character stripped off the end of each key,
    // repeatedly, such that:
    // input:
    // 'abcdefghijkX' = 1
    // 'abcdefghijkY' = 0.5
    // output:
    // 'abcdefghijk' = 1
    // 'abcdefghij' = 1
    // 'abcdefghi' = 1
    // 'abcdefgh' = 1
    // 'abcdefg' = 1
    // 'abcdef' = 1
    // 'abcde' = 1
    // 'abcd' = 1
    // 'abc' = 1
    // 'ab' = 1
    // 'a' = 1
    const reducedAmender = Object.keys(amender).reduce((amenderAcc, key) => {
      const value = amender[key];
      const choppedKeys = chop(key);
      return choppedKeys.reduce((prev, choppedKey) => {
        if (prev[choppedKey] >= value) {
          return prev;
        }
        return Object.assign(prev, {
          [choppedKey]: value
        });
      }, amenderAcc);
    }, amender);

    // Modify heatmap and return
    const reducedAmenderKeys = Object.keys(reducedAmender);
    const assigner = zipObject(reducedAmenderKeys, reducedAmenderKeys.map((k) => {
      return {
        weight: ((this.heatmap[k] || {}).weight || 0) + reducedAmender[k],
        last: now
      };
    }));

    Object.assign(this.heatmap, assigner);

    return true;
  }

  /**
   * Get heat of a particular latlong at all precisions.
   *
   * @param {Number} lat Latitude in floating-point format.
   * @param {Number} lon Longitude in floating-point format.
   */
  getLatLongHeatAll (lat, lon) {
    const hash = geohash.encode(lat, lon, 12);
    const hashes = [hash].concat(chop(hash));
    return zipObject(rangeRight(1, 13), hashes.map(h => this.getGeohashHeat(h)));
  }

  /**
   * Get heat of a particular latlong at a precision. Refer to readme to
   * select the right precision.
   *
   * @param {Number} lat Latitude in floating-point format.
   * @param {Number} lon Longitude in floating-point format.
   * @param {Number} precision Precision between 0 and 12 inclusive
   */
  getLatLongHeat (lat, lon, precision) {
    assert(precision > 0 && precision <= 12, 'geohash precision must be between 0 and 12, inclusive');
    return this.getGeohashHeat(geohash.encode(lat, lon, precision));
  }

  /**
   * Get heat of a particular geohash.
   *
   * @param {String} hash A geohash encoding of a position, between 1 and 12 characters inclusive.
   */
  getGeohashHeat (hash) {
    assert(typeof hash === 'string', 'geohash must be string');
    assert(hash.length > 0 && hash.length <= 12, 'geohash length must be between 0 and 12, inclusive');

    return (this.heatmap[hash] || { weight: 0, last: undefined });
  }
}

// Return `k.length - 1` elements, the string `k` with the final character
// repeatedly removed until the last element is just a single character.
function chop (k) {
  const result = [];
  for (let i = k.length; i > 0; i -= 1) {
    result.push(k.slice(0, i));
  }
  return result;
}
