/**
 * Copyright (C) 2016 Swift Navigation Inc.
 * Copyright (C) 2016 u-blox AG
 * Contact: Swift Navigation <dev@swiftnav.com>
 *
 * This source is subject to the license found in the file 'LICENSE' which must
 * be distributed together with this source. All other rights reserved.
 *
 * THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
 * EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED
 * WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE.
 */

var UBX = require('./ubx');
var Parser = require('binary-parser').Parser;

/**
 * Package description:
 *
 * UBX navigation messages.
 */

/**
 * UBX class for message NAV_POS_ECEF (0x01 0x01).
 *
 * The position solution message reports absolute Earth Centered Earth Fixed
 * (ECEF) coordinates.
 *
 * Fields in the UBX payload (`ubx.fields`):
 * @field {number} iTOW (unsigned 32-bit int, 4 bytes) GPS Time of Week
 * @field {number} ecefX (float, 8 bytes) ECEF X coordinate
 * @field {number} ecefY (float, 8 bytes) ECEF Y coordinate
 * @field {number} ecefZ (float, 8 bytes) ECEF Z coordinate
 *
 * @param ubx An UBX object with a payload to be decoded.
 */
var NAV_POS_ECEF = 0x01;

var NavPosEcef = function (ubx) {
  UBX.call(this, ubx);
  this.messageType = "NAV-POSECEF";
  this.fields = this.parser.parse(ubx.payload);
  return this;
};

NavPosEcef.prototype = Object.create(UBX.prototype);
NavPosEcef.prototype.constructor = NavPosEcef;
NavPosEcef.prototype.parser = new Parser()
  .uint32le('iTOW')
  .int32le('ecefX')
  .int32le('ecefY')
  .int32le('ecefZ')
  .uint32le('pAcc');
NavPosEcef.prototype.fieldSpec = [];
NavPosEcef.prototype.fieldSpec.push(['iTOW', 'writeUInt32LE', 4]);
NavPosEcef.prototype.fieldSpec.push(['ecefX', 'writeFloatLE', 4]);
NavPosEcef.prototype.fieldSpec.push(['ecefY', 'writeFloatLE', 4]);
NavPosEcef.prototype.fieldSpec.push(['ecefZ', 'writeFloatLE', 4]);
NavPosEcef.prototype.fieldSpec.push(['pAcc', 'writeUInt32LE', 4]);

/**
 * UBX class for message NAV_POS_LLH (0x01 0x02).
 *
 * This message outputs the Geodetic position in the currently selected
 * Ellipsoid. The default is the WGS84 Ellipsoid.
 *
 * Fields in the UBX payload (`ubx.fields`):
 * @field {number} iTOW (unsigned 32-bit int, 4 bytes) GPS Time of Week
 * @field {number} lon (float, 8 bytes) Longitude in degrees. Scaling 1e-7
 * @field {number} lat (float, 8 bytes) Latitude in degrees. Scaling 1e-7
 * @field {number} height (float, 8 bytes) Height above ellipsoid [mm]
 * @field {number} heightMeanSeaLevel (float, 8 bytes) Height above mean sea level [mm]
 * @field {number} hAcc (float, 8 bytes) Horizontal accuracy estimate [mm]
 * @field {number} vAcc (float, 8 bytes) Vertical accuracy estimate [mm]
 *
 * @param ubx An UBX object with a payload to be decoded.
 */
var NAV_POS_LLH = 0x02;

var NavPosLlh = function (ubx) {
  UBX.call(this, ubx);
  this.messageType = "NAV-POSLLH";
  this.fields = this.parser.parse(ubx.payload);
  return this;
};

NavPosLlh.prototype = Object.create(UBX.prototype);
NavPosLlh.prototype.constructor = NavPosLlh;
NavPosLlh.prototype.parser = new Parser()
  .uint32le('iTOW')
  .int32le('lon')
  .int32le('lat')
  .int32le('height')
  .int32le('heightMSL')
  .uint32le('hAcc')
  .uint32le('vAcc');
NavPosLlh.prototype.fieldSpec = [];
NavPosLlh.prototype.fieldSpec.push(['iTOW', 'writeUInt32LE', 4]);
NavPosLlh.prototype.fieldSpec.push(['lon', 'writeFloatLE', 4]);
NavPosLlh.prototype.fieldSpec.push(['lat', 'writeFloatLE', 4]);
NavPosLlh.prototype.fieldSpec.push(['height', 'writeFloatLE', 4]);
NavPosLlh.prototype.fieldSpec.push(['heightMSL', 'writeFloatLE', 4]);
NavPosLlh.prototype.fieldSpec.push(['hAcc', 'writeUInt32LE', 4]);
NavPosLlh.prototype.fieldSpec.push(['vAcc', 'writeUInt32LE', 4]);

/**
 * UBX class for message NAV_POS_PVT (0x01 0x07).
 *
 * Navigation position velocity time Solution
 *
 * Fields in the UBX payload (`ubx.fields`):
 * @field iTOW number (unsigned 32-bit int, 4 bytes) GPS Time of Week
 * @field {number} year      Year (UTC)
 * @field {number} month     Month, range 1..12 (UTC)
 * @field {number} day       Day of month, range 1..31 (UTC)
 * @field {number} hour      Hour of day, range 0..23 (UTC)
 * @field {number} min       Minute of hour, range 0..59 (UTC)
 * @field {number} sec       Seconds of minute, range 0..60 (UTC)
 * @field {number} valid     Validity Flags (see graphic below)
 * @field {number} tAcc      Time accuracy estimate (UTC)
 * @field {number} nano      Fraction of second, range -1e9 .. 1e9 (UTC)
 * @field {number} fixType   GNSSfix Type, range 0..5
 *                            0x00 = No Fix
 *                            0x01 = Dead Reckoning only
 *                            0x02 = 2D-Fix
 *                            0x03 = 3D-Fix
 *                            0x04 = GNSS + dead reckoning combined
 *                            0x05 = Time only fix
 *                            0x06..0xff: reserved
 * @field {number} flags     Fix Status Flags (see graphic below)
 * @field {number} reserved1 Reserved
 * @field {number} numSV     Number of satellites used in Nav Solution
 * @field {number} lon       Longitude
 * @field {number} lat       Latitude
 * @field {number} height    Height above ellipsoid
 * @field {number} hMSL      Height above mean sea level
 * @field {number} hAcc      Horizontal accuracy estimate
 * @field {number} vAcc      Vertical accuracy estimate
 * @field {number} velN      NED north velocity
 * @field {number} velE      NED east velocity
 * @field {number} velD      NED down velocity
 * @field {number} gSpeed    Ground Speed (2-D)
 * @field {number} headMot   Heading of motion (2-D)
 * @field {number} sAcc      Speed accuracy estimate
 * @field {number} headAcc   Heading accuracy estimate (both motion and vehicle)
 * @field {number} pDOP      Position DOP
 * @field {number} reserved2a     Reserved
 * @field {number} reserved2b     Reserved
 * @field {number} reserved2c     Reserved
 * @field {number} reserved2d     Reserved
 * @field {number} reserved2e     Reserved
 * @field {number} reserved2f     Reserved
 * @field {number} headVeh        Heading of vehicle (2-D)
 * @field {number} reserved3a     Reserved
 * @field {number} reserved3b     Reserved
 * @field {number} reserved3c     Reserved
 * @field {number} reserved3d     Reserved
 *
 * @param ubx An UBX object with a payload to be decoded.
 */
var NAV_PVT = 0x07;

var NavPVT = function (ubx) {
  UBX.call(this, ubx);
  this.messageType = "NAV-PVT";
  this.fields = this.parser.parse(ubx.payload);
  return this;
};

NavPVT.prototype = Object.create(UBX.prototype);
NavPVT.prototype.constructor = NavPVT;
NavPVT.prototype.parser = new Parser()
  .uint32le('iTOW')
  .uint16le('year')
  .uint8('month')
  .uint8('day')
  .uint8('hour')
  .uint8('min')
  .uint8('sec')
  .uint8('valid')
  .uint32le('tAcc')
  .int32le('nano')
  .uint8('fixType')
  .uint8('flags')
  .uint8('reserved1')
  .uint8('numSV')
  .int32le('lon')
  .int32le('lat')
  .int32le('height')
  .int32le('hMSL')
  .uint32le('hAcc')
  .uint32le('vAcc')
  .int32le('velN')
  .int32le('velE')
  .int32le('velD')
  .int32le('gSpeed')
  .int32le('headMot')
  .uint32le('sAcc')
  .uint32le('headAcc')
  .uint16le('pDOP')
  .uint8('reserved2a')
  .uint8('reserved2b')
  .uint8('reserved2c')
  .uint8('reserved2d')
  .uint8('reserved2e')
  .uint8('reserved2f')
  .int32le('headVeh')
  .uint8('reserved3a')
  .uint8('reserved3b')
  .uint8('reserved3c')
  .uint8('reserved3d');

NavPVT.prototype.fieldSpec = [];
NavPVT.prototype.fieldSpec.push(['iTOW', 'writeUInt32LE', 4]);
NavPVT.prototype.fieldSpec.push(['year', 'writeUInt16', 2]);
NavPVT.prototype.fieldSpec.push(['month', 'writeUInt8', 1]);
NavPVT.prototype.fieldSpec.push(['day', 'writeUInt8', 1]);
NavPVT.prototype.fieldSpec.push(['hour', 'writeUInt8', 1]);
NavPVT.prototype.fieldSpec.push(['min', 'writeUInt8', 1]);
NavPVT.prototype.fieldSpec.push(['sec', 'writeUInt8', 1]);
NavPVT.prototype.fieldSpec.push(['valid', 'writeUInt8', 1]);
NavPVT.prototype.fieldSpec.push(['tAcc', 'writeFloatLE', 4]);
NavPVT.prototype.fieldSpec.push(['nano', 'writeFloatLE', 4]);
NavPVT.prototype.fieldSpec.push(['fixType', 'writeUInt8', 1]);
NavPVT.prototype.fieldSpec.push(['flags', 'writeUInt8', 1]);
NavPVT.prototype.fieldSpec.push(['reserved1', 'writeUInt8', 1]);
NavPVT.prototype.fieldSpec.push(['numSV', 'writeUInt8', 1]);
NavPVT.prototype.fieldSpec.push(['lon', 'writeFloatLE', 4]);
NavPVT.prototype.fieldSpec.push(['lat', 'writeFloatLE', 4]);
NavPVT.prototype.fieldSpec.push(['height', 'writeFloatLE', 4]);
NavPVT.prototype.fieldSpec.push(['hMSL', 'writeFloatLE', 4]);
NavPVT.prototype.fieldSpec.push(['hAcc', 'writeFloatLE', 4]);
NavPVT.prototype.fieldSpec.push(['vAcc', 'writeFloatLE', 4]);
NavPVT.prototype.fieldSpec.push(['velN', 'writeFloatLE', 4]);
NavPVT.prototype.fieldSpec.push(['velE', 'writeFloatLE', 4]);
NavPVT.prototype.fieldSpec.push(['velD', 'writeFloatLE', 4]);
NavPVT.prototype.fieldSpec.push(['gSpeed', 'writeFloatLE', 4]);
NavPVT.prototype.fieldSpec.push(['headMot', 'writeFloatLE', 4]);
NavPVT.prototype.fieldSpec.push(['sAcc', 'writeFloatLE', 4]);
NavPVT.prototype.fieldSpec.push(['headAcc', 'writeFloatLE', 4]);
NavPVT.prototype.fieldSpec.push(['pDOP', 'writeFloatLE', 2]);
NavPVT.prototype.fieldSpec.push(['reserved2a', 'writeUInt8', 1]);
NavPVT.prototype.fieldSpec.push(['reserved2b', 'writeUInt8', 1]);
NavPVT.prototype.fieldSpec.push(['reserved2c', 'writeUInt8', 1]);
NavPVT.prototype.fieldSpec.push(['reserved2d', 'writeUInt8', 1]);
NavPVT.prototype.fieldSpec.push(['reserved2e', 'writeUInt8', 1]);
NavPVT.prototype.fieldSpec.push(['reserved2f', 'writeUInt8', 1]);
NavPVT.prototype.fieldSpec.push(['headVeh', 'writeFloatLE', 4]);
NavPVT.prototype.fieldSpec.push(['reserved3a', 'writeUInt8', 1]);
NavPVT.prototype.fieldSpec.push(['reserved3b', 'writeUInt8', 1]);
NavPVT.prototype.fieldSpec.push(['reserved3c', 'writeUInt8', 1]);
NavPVT.prototype.fieldSpec.push(['reserved3d', 'writeUInt8', 1]);

// Mapping of message class to messages, and the exported messages.
module.exports = {
  0x01: {
    0x01: NavPosEcef,
    0x02: NavPosLlh,
    0x07: NavPVT
  }
};
