/*
 * Copyright (C) 2016 Swift Navigation Inc.
 * Contact: Swift Navigation <dev@swiftnav.com>
 *
 * This source is subject to the license found in the file 'LICENSE' which must
 * be be distributed together with this source. All other rights reserved.
 *
 * THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
 * EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED
 * WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE.
 */

const fs = require('fs');
const ubx = require('./../src/msg');
const t = require('chai');

describe('Check parsing of navigation message', function () {
  describe('Decoding file sanity check', function () {
    var binaryStream = fs.createReadStream('../fixtures/m8t/rover.ubx');
    it('should parse binary ubx and payload', function () {
      ubx.dispatch(binaryStream, function (err, decoded, raw) {
        if (decoded.ubx.msgId === 0x01) {
          const fields = decoded.fields;
          t.assert(fields.ecefX < 0);
          t.assert(fields.ecefY < 0);
          t.assert(fields.ecefZ > 0);
          t.assert(fields.pAcc > 0);
        }
      });
    });
  });
});
