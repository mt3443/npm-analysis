'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.targetMetadata = undefined;

var _keys = require('babel-runtime/core-js/object/keys');

var _keys2 = _interopRequireDefault(_keys);

exports.getUnsupportedTargets = getUnsupportedTargets;

var _data = require('caniuse-db/fulldata-json/data-2.0.json');

var _data2 = _interopRequireDefault(_data);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

// HACK: modern targets should be determined once at runtime
// eslint-disable-line
var targetMetadata = exports.targetMetadata = {
  targets: ['chrome', 'firefox', 'opera', 'safari', 'ie', 'edge', 'ios_saf', 'op_mini', 'android', 'bb', 'op_mob', 'and_chr', 'and_ff', 'ie_mob', 'and_uc', 'samsung', 'baidu']
};
// $FlowFixMe: Flow import error


var targetNameMappings = {
  chrome: 'Chrome',
  firefox: 'Firefox',
  opera: 'Opera',
  baidu: 'Baidu',
  and_qq: 'QQ Browser',
  safari: 'Safari',
  android: 'Android Browser',
  ie: 'IE',
  edge: 'Edge',
  ios_saf: 'iOS Safari',
  op_mini: 'Opera Mini',
  bb: 'Blackberry Browser',
  op_mob: 'Opera Mobile',
  and_chr: 'Android Chrome',
  and_ff: 'Android Firefox',
  ie_mob: 'IE Mobile',
  and_uc: 'Android UC Browser',
  samsung: 'Samsung Browser'
};

/**
 * Take a target's id and return it's full name by using `targetNameMappings`
 * ex. {target: and_ff, version: 40} => 'Android FireFox 40'
 */
function formatTargetNames(target) {
  return `${targetNameMappings[target.target]} ${target.version}`;
}

/**
 * Check version for the range format.
 * ex. 10.0-10.2
 */
function versionIsRange(version) {
  return version.includes('-');
}

/**
 * Parse version from caniuse and compare with parsed version from browserslist.
 */
function compareRanges(targetVersion, statsVersion) {
  return targetVersion === parseFloat(statsVersion);
}

/**
 * Return an array of all unsupported targets
 */
function getUnsupportedTargets(node, targets) {
  // Check the CanIUse database to see if targets are supported
  var stats = _data2.default.data[node.id].stats;


  return targets.filter(function (target) {
    var version = target.version;

    var targetStats = stats[target.target];

    return versionIsRange(version) ? (0, _keys2.default)(targetStats).some(function (statsVersion) {
      return versionIsRange(statsVersion) && compareRanges(target.parsedVersion, statsVersion) ? !targetStats[statsVersion].includes('y') : false;
    }) : targetStats[version] && !targetStats[version].includes('y');
  }).map(formatTargetNames);
}

function isValid(node, eslintNode, targets) {
  // Filter non-matching objects and properties
  switch (eslintNode.type) {
    case 'CallExpression':
      if (!eslintNode.callee) return true;
      if (eslintNode.callee.name !== node.object) return true;
      break;
    case 'NewExpression':
      if (!eslintNode.callee) return true;
      if (eslintNode.callee.name !== node.object) return true;
      break;
    case 'MemberExpression':
      // Pass tests if non-matching object or property
      if (!eslintNode.object || !eslintNode.property) return true;
      if (eslintNode.object.name !== node.object) return true;

      // If the property is missing from the rule, it means that only the
      // object is required to determine compatibility
      if (!node.property) break;

      if (eslintNode.property.name !== node.property) return true;
      break;
    default:
      return true;
  }

  return getUnsupportedTargets(node, targets).length === 0;
}

//
// TODO: Migrate to compat-db
// TODO: Refactor isValid(), remove from rules
//

var CanIUseProvider = [
// new ServiceWorker()
{
  id: 'serviceworkers',
  ASTNodeType: 'NewExpression',
  object: 'ServiceWorker',
  isValid,
  getUnsupportedTargets
}, {
  id: 'serviceworkers',
  ASTNodeType: 'MemberExpression',
  object: 'navigator',
  property: 'serviceWorker',
  isValid,
  getUnsupportedTargets
},
// document.querySelector()
{
  id: 'queryselector',
  ASTNodeType: 'MemberExpression',
  object: 'document',
  property: 'querySelector',
  isValid,
  getUnsupportedTargets
},
// WebAssembly
{
  id: 'wasm',
  ASTNodeType: 'MemberExpression',
  object: 'WebAssembly',
  isValid,
  getUnsupportedTargets
},
// IntersectionObserver
{
  id: 'intersectionobserver',
  ASTNodeType: 'NewExpression',
  object: 'IntersectionObserver',
  isValid,
  getUnsupportedTargets
},
// PaymentRequest
{
  id: 'payment-request',
  ASTNodeType: 'NewExpression',
  object: 'PaymentRequest',
  isValid,
  getUnsupportedTargets
},
// Promises
{
  id: 'promises',
  ASTNodeType: 'NewExpression',
  object: 'Promise',
  isValid,
  getUnsupportedTargets
}, {
  id: 'promises',
  ASTNodeType: 'MemberExpression',
  object: 'Promise',
  property: 'resolve',
  isValid,
  getUnsupportedTargets
}, {
  id: 'promises',
  ASTNodeType: 'MemberExpression',
  object: 'Promise',
  property: 'all',
  isValid,
  getUnsupportedTargets
}, {
  id: 'promises',
  ASTNodeType: 'MemberExpression',
  object: 'Promise',
  property: 'race',
  isValid,
  getUnsupportedTargets
}, {
  id: 'promises',
  ASTNodeType: 'MemberExpression',
  object: 'Promise',
  property: 'reject',
  isValid,
  getUnsupportedTargets
},
// fetch
{
  id: 'fetch',
  ASTNodeType: 'CallExpression',
  object: 'fetch',
  isValid,
  getUnsupportedTargets
},
// document.currentScript()
{
  id: 'document-currentscript',
  ASTNodeType: 'MemberExpression',
  object: 'document',
  property: 'currentScript',
  isValid,
  getUnsupportedTargets
}];

exports.default = CanIUseProvider;