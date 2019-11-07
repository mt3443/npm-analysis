define([
    "../core"
], function (radic) {

    radic.extend({
        utf8: {
            encode: function (argString) {
                //  discuss at: http://phpjs.org/functions/utf8_encode/
                // original by: Webtoolkit.info (http://www.webtoolkit.info/)
                // improved by: Kevin van Zonneveld (http://kevin.vanzonneveld.net)
                // improved by: sowberry
                // improved by: Jack
                // improved by: Yves Sucaet
                // improved by: kirilloid
                // bugfixed by: Onno Marsman
                // bugfixed by: Onno Marsman
                // bugfixed by: Ulrich
                // bugfixed by: Rafal Kukawski
                // bugfixed by: kirilloid
                //   example 1: utf8_encode('Kevin van Zonneveld');
                //   returns 1: 'Kevin van Zonneveld'

                if (argString === null || typeof argString === 'undefined') {
                    return '';
                }

                var string = (argString + ''); // .replace(/\r\n/g, "\n").replace(/\r/g, "\n");
                var utftext = '',
                    start, end, stringl = 0;

                start = end = 0;
                stringl = string.length;
                for (var n = 0; n < stringl; n++) {
                    var c1 = string.charCodeAt(n);
                    var enc = null;

                    if (c1 < 128) {
                        end++;
                    } else if (c1 > 127 && c1 < 2048) {
                        enc = String.fromCharCode(
                            (c1 >> 6) | 192, (c1 & 63) | 128
                        );
                    } else if ((c1 & 0xF800) != 0xD800) {
                        enc = String.fromCharCode(
                            (c1 >> 12) | 224, ((c1 >> 6) & 63) | 128, (c1 & 63) | 128
                        );
                    } else { // surrogate pairs
                        if ((c1 & 0xFC00) != 0xD800) {
                            throw new RangeError('Unmatched trail surrogate at ' + n);
                        }
                        var c2 = string.charCodeAt(++n);
                        if ((c2 & 0xFC00) != 0xDC00) {
                            throw new RangeError('Unmatched lead surrogate at ' + (n - 1));
                        }
                        c1 = ((c1 & 0x3FF) << 10) + (c2 & 0x3FF) + 0x10000;
                        enc = String.fromCharCode(
                            (c1 >> 18) | 240, ((c1 >> 12) & 63) | 128, ((c1 >> 6) & 63) | 128, (c1 & 63) | 128
                        );
                    }
                    if (enc !== null) {
                        if (end > start) {
                            utftext += string.slice(start, end);
                        }
                        utftext += enc;
                        start = end = n + 1;
                    }
                }

                if (end > start) {
                    utftext += string.slice(start, stringl);
                }

                return utftext;
            },
            decode: function (str_data) {
                //  discuss at: http://phpjs.org/functions/utf8_decode/
                // original by: Webtoolkit.info (http://www.webtoolkit.info/)
                //    input by: Aman Gupta
                //    input by: Brett Zamir (http://brett-zamir.me)
                // improved by: Kevin van Zonneveld (http://kevin.vanzonneveld.net)
                // improved by: Norman "zEh" Fuchs
                // bugfixed by: hitwork
                // bugfixed by: Onno Marsman
                // bugfixed by: Kevin van Zonneveld (http://kevin.vanzonneveld.net)
                // bugfixed by: kirilloid
                //   example 1: utf8_decode('Kevin van Zonneveld');
                //   returns 1: 'Kevin van Zonneveld'

                var tmp_arr = [],
                    i = 0,
                    ac = 0,
                    c1 = 0,
                    c2 = 0,
                    c3 = 0,
                    c4 = 0;

                str_data += '';

                while (i < str_data.length) {
                    c1 = str_data.charCodeAt(i);
                    if (c1 <= 191) {
                        tmp_arr[ac++] = String.fromCharCode(c1);
                        i++;
                    } else if (c1 <= 223) {
                        c2 = str_data.charCodeAt(i + 1);
                        tmp_arr[ac++] = String.fromCharCode(((c1 & 31) << 6) | (c2 & 63));
                        i += 2;
                    } else if (c1 <= 239) {
                        // http://en.wikipedia.org/wiki/UTF-8#Codepage_layout
                        c2 = str_data.charCodeAt(i + 1);
                        c3 = str_data.charCodeAt(i + 2);
                        tmp_arr[ac++] = String.fromCharCode(((c1 & 15) << 12) | ((c2 & 63) << 6) | (c3 & 63));
                        i += 3;
                    } else {
                        c2 = str_data.charCodeAt(i + 1);
                        c3 = str_data.charCodeAt(i + 2);
                        c4 = str_data.charCodeAt(i + 3);
                        c1 = ((c1 & 7) << 18) | ((c2 & 63) << 12) | ((c3 & 63) << 6) | (c4 & 63);
                        c1 -= 0x10000;
                        tmp_arr[ac++] = String.fromCharCode(0xD800 | ((c1 >> 10) & 0x3FF));
                        tmp_arr[ac++] = String.fromCharCode(0xDC00 | (c1 & 0x3FF));
                        i += 4;
                    }
                }

                return tmp_arr.join('');
            }
        }
    });

    return radic;
});
