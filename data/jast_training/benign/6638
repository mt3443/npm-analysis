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

var Parser = require('binary-parser').Parser;
var path = require('path');
var streams = require('stream');
var UBX = require('./ubx');

var UBX_SYNC1 = 0xB5;
var UBX_SYNC2 = 0x62;

var mergeDict = function (dest, src) {
  for (var prop in src) {
    if (src.hasOwnProperty(prop)) {
      dest[prop] = src[prop];
    }
  }
  return dest;
};

function BufferTooShortError (message) {
  this.name = 'BufferTooShortError';
  this.message = message;
  this.stack = (new Error()).stack;
}
BufferTooShortError.prototype = Object.create(Error.prototype);
BufferTooShortError.prototype.constructor = BufferTooShortError;

function BufferCorruptError (message) {
  this.name = 'BufferCorruptError';
  this.message = message;
  this.stack = (new Error()).stack;
}
BufferCorruptError.prototype = Object.create(Error.prototype);
BufferCorruptError.prototype.constructor = BufferCorruptError;

var packages = ['position'];

var ubxTable = packages.map(function (pkg) {
  return require("./" + pkg + ".js");
}).reduce(function (prev, curr) {
  var numericKeysDict = {};
  Object.keys(curr).map(function (key) {
    if (parseInt(key) == key) {
      numericKeysDict[key] = curr[key];
    }
  });
  return mergeDict(prev, numericKeysDict);
}, {});

var parser = new Parser()
  .uint8('sync1')
  .uint8('sync2')
  .uint8('msgClass')
  .uint8('msgId')
  .uint16le('len')
  .buffer('payload', { length: 'len' })
  .uint8('ckA')
  .uint8('ckB');

/**
 * Calculate checksum A/B of the UBX message.
 * These are uint8s, so we truncate at each step.
 */
function ubxCrc (msgClass, msgId, msgLen, payload) {
  var ckA = 0;
  var ckB = 0;
  ckA = (ckA + msgClass) & 0xFF;
  ckB = (ckA + ckB) & 0xFF;
  ckA = (ckA + msgId) & 0xFF;
  ckB = (ckA + ckB) & 0xFF;
  ckA = (ckA + (msgLen & 0xFF)) & 0xFF;
  ckB = (ckA + ckB) & 0xFF;
  ckA = (ckA + (msgLen >> 8)) & 0xFF;
  ckB = (ckA + ckB) & 0xFF;
  for (var i = 0; i < payload.length; i++) {
    ckA = (ckA + payload[i]) & 0xFF;
    ckB = (ckA + ckB) & 0xFF;
  }
  return [ckA, ckB];
}

module.exports = {
  decode: function decode (msg) {
    var ubx = parser.parse(msg);
    var msgTypeDecoderClass = ubxTable[ubx['msgClass']];
    var msgTypeDecoder = msgTypeDecoderClass && msgTypeDecoderClass[ubx['msgId']];
    if (typeof msgTypeDecoder === 'undefined') {
      return new UBX(ubx);
    }
    return new msgTypeDecoder(ubx);
  },
  /**
   * Look for the beginning of a framed message in a stream, and parse it until
   *  the end. Verify that the CRC matches the message. If the framed message is
   *  good, invoke callback. Otherwise throw message away.  Repeats until the
   *  stream has ended.
   *
   * Callback will be called with valid framed messages. Will not currently be
   * called with errors.
   *
   * This corresponds to the logic in libsbp `framer.py`.
   *
   * @param stream: A Readable stream of bytes.
   * @param callback: a callback function invoked when a framed message is found
   * and decoded in the stream.
   * @returns [parsed UBX object, Buffer]
   */
  dispatch: function dispatch (stream, callback) {
    var offset = 0;
    var streamBuffer = new Buffer(0);
    var getFramedMessage = function () {
      var headerBuf, payloadBuf;
      var sync1, sync2, msgType, sender, msgLen, ckA, ckB;
      var payloadCrc;
      // Find sync1 byte
      var sync1pos;
      for (sync1pos = 0; sync1pos < streamBuffer.length; sync1pos++) {
        sync1 = streamBuffer.readUInt8(sync1pos);
        if (sync1 == UBX_SYNC1) {
          break;
        }
      }
      if (sync1 != UBX_SYNC1) {
        throw new BufferTooShortError();
      }
      // Find sync2 byte
      var sync2pos;
      for (sync2pos = 0; sync2pos < streamBuffer.length; sync2pos++) {
        sync2 = streamBuffer.readUInt8(sync2pos);
        if (sync2 == UBX_SYNC2) {
          break;
        }
      }
      if (sync2 != UBX_SYNC2) {
        throw new BufferTooShortError();
      }
      // Get msg_type, sender, length next
      if (sync2pos+5 > streamBuffer.length) {
        throw new BufferTooShortError();
      }
      msgClass = streamBuffer.readUInt8(sync1pos+2);
      msgId = streamBuffer.readUInt8(sync1pos+3);
      msgLen = streamBuffer.readUInt16LE(sync1pos+4);
      // Get full payload
      // First, check payload length + CRC
      if (sync2pos+5+msgLen > streamBuffer.length) {
        throw new BufferTooShortError();
      }
      payloadBuf = streamBuffer.slice(sync1pos+6, sync1pos+6+msgLen);
      payloadCrc = ubxCrc(msgClass, msgId, msgLen, payloadBuf);
      // Finally, get and verify CRC
      ckA = streamBuffer.readUInt8(sync1pos+6+msgLen+0);
      ckB = streamBuffer.readUInt8(sync1pos+6+msgLen+1);
      // Pull out full buffer
      var fullBuffer = streamBuffer.slice(sync1pos, sync1pos+6+msgLen+2);
      // If the CRC looks correct, decode the full payload
      if (ckA === payloadCrc[0] && ckB == payloadCrc[1]) {
        // remove this chunk from the stream buffer
        streamBuffer = streamBuffer.slice(sync1pos+6+msgLen+2);
        return [module.exports.decode(fullBuffer), fullBuffer];
      } else {
        // remove bad sync1 byte from the stream buffer
        streamBuffer = streamBuffer.slice(sync1pos+1);
        throw new BufferCorruptError();
      }
    };

    var processData = function (data) {
      stream.pause();
      try {
        streamBuffer = Buffer.concat([streamBuffer, data]);
        if (streamBuffer.length < 2) {
          return;
        }
        var pair = getFramedMessage();
        var framedMessage = pair[0];
        var fullBuffer = pair[1];
        // If there is data left to process after a successful parse, process
        // again
        if (streamBuffer.length > 0) {
          setTimeout(function () {
            processData(new Buffer(0));
          }, 0);
        }
        callback(null, framedMessage, fullBuffer);
      } catch (e) {
        // If the buffer was corrupt but there's more in the stream, try again
        // immediately
        if (e instanceof BufferCorruptError && streamBuffer.length > 0) {
          setTimeout(function () {
            processData(new Buffer(0));
          }, 0);
        }
      } finally {
        offset = 0;
        stream.resume();
      }
    };
    stream.on('data', processData);
  }
};
