"use strict";
/**
 * Round a value to a precision
 * @param value
 * @param places
 * @returns {number}
 */
function round(value, places) {
    var multiplier = Math.pow(10, places);
    return (Math.round(value * multiplier) / multiplier);
}
exports.round = round;
/**
 * Create a string from an object
 *
 * @param object
 * @returns {any}
 */
function makeString(object) {
    if (object == null)
        return '';
    return '' + object;
}
exports.makeString = makeString;
function defaultToWhiteSpace(characters) {
    if (characters == null)
        return '\\s';
    else if (characters.source)
        return characters.source;
    else
        return '[' + _.escapeRegExp(characters) + ']';
}
exports.defaultToWhiteSpace = defaultToWhiteSpace;
var kindsOf = {};
'Number String Boolean Function RegExp Array Date Error'.split(' ').forEach(function (k) {
    kindsOf['[object ' + k + ']'] = k.toLowerCase();
});
var nativeTrim = String.prototype.trim;
var entityMap = {
    "&": "&amp;",
    "<": "&lt;",
    ">": "&gt;",
    '"': '&quot;',
    "'": '&#39;',
    "/": '&#x2F;'
};
/**
 * Returns the method of a variablse
 *
 * @param value
 * @returns {any}
 */
function kindOf(value) {
    // Null or undefined.
    if (value == null) {
        return String(value);
    }
    // Everything else.
    return kindsOf[kindsOf.toString.call(value)] || 'object';
}
exports.kindOf = kindOf;
/**
 * If val is not defined, return def as default
 * @param val
 * @param def
 * @returns {any}
 */
function def(val, def) {
    return defined(val) ? val : def;
}
exports.def = def;
/**
 * Checks wether the passed variable is defined
 *
 * @param obj
 * @returns {boolean}
 */
function defined(obj) {
    return !_.isUndefined(obj);
}
exports.defined = defined;
/**
 * Get a random generated id string
 *
 * @param length
 * @returns {string}
 */
function getRandomId(length) {
    if (!_.isNumber(length)) {
        length = 15;
    }
    var text = "";
    var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
    for (var i = 0; i < length; i++) {
        text += possible.charAt(Math.floor(Math.random() * possible.length));
    }
    return text;
}
exports.getRandomId = getRandomId;
function guid() {
    return s4() + s4() + '-' + s4() + '-' + s4() + '-' +
        s4() + '-' + s4() + s4() + s4();
}
exports.guid = guid;
function s4() {
    return Math.floor((1 + Math.random()) * 0x10000)
        .toString(16)
        .substring(1);
}
//# sourceMappingURL=general.js.map