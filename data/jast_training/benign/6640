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

/**
 * Parent prototypal class for all UBX message objects.
 */
function UBX (ubx) {
  this.messageType = "raw";
  this.ubx = ubx;
  this.fields = {};
  return this;
}

UBX.prototype.fieldSpec = [];

/**
 * Convert a payload to its binary representation, based on this object's
 * fieldSpec.
 */
UBX.prototype.payloadToBuffer = function payloadToBuffer (fieldSpec, data) {
  var buffers = [];
  fieldSpec = fieldSpec || this.fieldSpec;
  data = data || this.fields;
  for (var k in fieldSpec) {
    var field = fieldSpec[k];
    var fieldName = field[0];
    var dataType = field[1];
    var fieldSize = function (sz) {
      return typeof sz === 'function' ? sz.apply(this) : sz;
    }.bind(this);
    if (typeof dataType === 'string' && dataType.indexOf('write') === 0) {
      var dataSize = fieldSize(field[2]);
      var b = new Buffer(dataSize);
      b[dataType](data[fieldName], 0);
      buffers.push(b);
    } else if (dataType === 'string') {
      var b = new Buffer(data[fieldName].length);
      b.write(data[fieldName]);
      buffers.push(b);
    } else if (dataType === 'array') {
      var dataFill = field[2];
      for (var i in data[fieldName]) {
        var iData = data[fieldName][i];
        if (Array.isArray(dataFill)) {
          // Nested type
          buffers = buffers.concat(this.payloadToBuffer(dataFill, iData));
        } else {
          // Built-in type
          var b = new Buffer(fieldSize(field[3]));
          b[dataFill](iData, 0);
          buffers.push(b);
        }
      }
    } else {
      // Nested type
      buffers = buffers.concat(this.payloadToBuffer(dataType, data[fieldName]));
    }
  }
  return Buffer.concat(buffers);
};

/**
 * Convert a message to its binary representation.
 */
UBX.prototype.toBuffer = function toBuffer () {
  var payload = this.payloadToBuffer();
  var buffers = [];
  var b;
  b = new Buffer(1);
  b.writeUInt8(this.sbp.preamble, 0);
  buffers.push(b);
  b = new Buffer(2);
  b.writeUInt16LE(this.sbp.msg_type, 0);
  buffers.push(b);
  b = new Buffer(2);
  b.writeUInt16LE(this.sbp.sender, 0);
  buffers.push(b);
  b = new Buffer(1);
  b.writeUInt8(this.sbp.length, 0);
  buffers.push(b);
  b = new Buffer(2);
  b.writeUInt16LE(this.sbp.crc, 0);
  return Buffer.concat(buffers.concat(payload).concat(b));
};

/**
 * Convert a message to JSON by iterating through `UBX` and `fields`.
 */
UBX.prototype.toJSON = function toJSON () {
  var dict = {};
  Object.keys(this.ubx).map(function (k) {
    if (this.ubx[k] instanceof Buffer) {
      dict[k] = this.ubx[k].toString('base64');
    } else {
      dict[k] = this.ubx[k];
    }
  }.bind(this));
  Object.keys(this.fields).map(function (k) {
    dict[k] = this.fields[k];
  }.bind(this));
  return JSON.stringify(dict);
};

/**
 * Serialize a message into base64. Note that this will convert the entire
 *  message - UBX fields and payload/fields, not just the payload.
 */
UBX.prototype.toBase64 = function toBase64 () {
  return this.toBuffer().toString('base64');
};

module.exports = UBX;
