// @include ../externals/spinjs/spin.js

(function (factory) {
	factory(jQuery);
}(function ($) {
//


    var radic = {},

        version = "undefined";

    radic.extend = function(arg){
        $.extend(radic, arg);
    };


    function getlodash() {

        /**
         * @license
         * Lo-Dash 2.4.1 (Custom Build) <http://lodash.com/>
         * Build: `lodash underscore include="omit,pick,values,keys,where,cloneDeep,sortBy,toArray" exports="none" -o src/tpl/_lodash.js`
         * Copyright 2012-2013 The Dojo Foundation <http://dojofoundation.org/>
         * Based on Underscore.js 1.5.2 <http://underscorejs.org/LICENSE>
         * Copyright 2009-2013 Jeremy Ashkenas, DocumentCloud and Investigative Reporters & Editors
         * Available under MIT license <http://lodash.com/license>
         */
        
        
          /** Used as a safe reference for `undefined` in pre ES5 environments */
          var undefined;
        
          /** Used to pool arrays and objects used internally */
          var arrayPool = [];
        
          /** Used internally to indicate various things */
          var indicatorObject = {};
        
          /** Used as the max size of the `arrayPool` and `objectPool` */
          var maxPoolSize = 40;
        
          /** Used to match regexp flags from their coerced string values */
          var reFlags = /\w*$/;
        
          /** `Object#toString` result shortcuts */
          var argsClass = '[object Arguments]',
              arrayClass = '[object Array]',
              boolClass = '[object Boolean]',
              dateClass = '[object Date]',
              funcClass = '[object Function]',
              numberClass = '[object Number]',
              objectClass = '[object Object]',
              regexpClass = '[object RegExp]',
              stringClass = '[object String]';
        
          /** Used to identify object classifications that `_.clone` supports */
          var cloneableClasses = {};
          cloneableClasses[funcClass] = false;
          cloneableClasses[argsClass] = cloneableClasses[arrayClass] =
          cloneableClasses[boolClass] = cloneableClasses[dateClass] =
          cloneableClasses[numberClass] = cloneableClasses[objectClass] =
          cloneableClasses[regexpClass] = cloneableClasses[stringClass] = true;
        
          /** Used to determine if values are of the language type Object */
          var objectTypes = {
            'boolean': false,
            'function': true,
            'object': true,
            'number': false,
            'string': false,
            'undefined': false
          };
        
          /** Used as a reference to the global object */
          var root = (objectTypes[typeof window] && window) || this;
        
          /** Detect free variable `global` from Node.js or Browserified code and use it as `root` */
          var freeGlobal = objectTypes[typeof global] && global;
          if (freeGlobal && (freeGlobal.global === freeGlobal || freeGlobal.window === freeGlobal)) {
            root = freeGlobal;
          }
        
          /*--------------------------------------------------------------------------*/
        
          /**
           * The base implementation of `_.indexOf` without support for binary searches
           * or `fromIndex` constraints.
           *
           * @private
           * @param {Array} array The array to search.
           * @param {*} value The value to search for.
           * @param {number} [fromIndex=0] The index to search from.
           * @returns {number} Returns the index of the matched value or `-1`.
           */
          function baseIndexOf(array, value, fromIndex) {
            var index = (fromIndex || 0) - 1,
                length = array ? array.length : 0;
        
            while (++index < length) {
              if (array[index] === value) {
                return index;
              }
            }
            return -1;
          }
        
          /**
           * Used by `sortBy` to compare transformed `collection` elements, stable sorting
           * them in ascending order.
           *
           * @private
           * @param {Object} a The object to compare to `b`.
           * @param {Object} b The object to compare to `a`.
           * @returns {number} Returns the sort order indicator of `1` or `-1`.
           */
          function compareAscending(a, b) {
            var ac = a.criteria,
                bc = b.criteria,
                index = -1,
                length = ac.length;
        
            while (++index < length) {
              var value = ac[index],
                  other = bc[index];
        
              if (value !== other) {
                if (value > other || typeof value == 'undefined') {
                  return 1;
                }
                if (value < other || typeof other == 'undefined') {
                  return -1;
                }
              }
            }
            // Fixes an `Array#sort` bug in the JS engine embedded in Adobe applications
            // that causes it, under certain circumstances, to return the same value for
            // `a` and `b`. See https://github.com/jashkenas/underscore/pull/1247
            //
            // This also ensures a stable sort in V8 and other engines.
            // See http://code.google.com/p/v8/issues/detail?id=90
            return a.index - b.index;
          }
        
          /**
           * Gets an array from the array pool or creates a new one if the pool is empty.
           *
           * @private
           * @returns {Array} The array from the pool.
           */
          function getArray() {
            return arrayPool.pop() || [];
          }
        
          /**
           * Releases the given array back to the array pool.
           *
           * @private
           * @param {Array} [array] The array to release.
           */
          function releaseArray(array) {
            array.length = 0;
            if (arrayPool.length < maxPoolSize) {
              arrayPool.push(array);
            }
          }
        
          /**
           * Slices the `collection` from the `start` index up to, but not including,
           * the `end` index.
           *
           * Note: This function is used instead of `Array#slice` to support node lists
           * in IE < 9 and to ensure dense arrays are returned.
           *
           * @private
           * @param {Array|Object|string} collection The collection to slice.
           * @param {number} start The start index.
           * @param {number} end The end index.
           * @returns {Array} Returns the new array.
           */
          function slice(array, start, end) {
            start || (start = 0);
            if (typeof end == 'undefined') {
              end = array ? array.length : 0;
            }
            var index = -1,
                length = end - start || 0,
                result = Array(length < 0 ? 0 : length);
        
            while (++index < length) {
              result[index] = array[start + index];
            }
            return result;
          }
        
          /*--------------------------------------------------------------------------*/
        
          /**
           * Used for `Array` method references.
           *
           * Normally `Array.prototype` would suffice, however, using an array literal
           * avoids issues in Narwhal.
           */
          var arrayRef = [];
        
          /** Used for native method references */
          var objectProto = Object.prototype;
        
          /** Used to resolve the internal [[Class]] of values */
          var toString = objectProto.toString;
        
          /** Used to detect if a method is native */
          var reNative = RegExp('^' +
            String(toString)
              .replace(/[.*+?^${}()|[\]\\]/g, '\\$&')
              .replace(/toString| for [^\]]+/g, '.*?') + '$'
          );
        
          /** Native method shortcuts */
          var hasOwnProperty = objectProto.hasOwnProperty,
              push = arrayRef.push,
              propertyIsEnumerable = objectProto.propertyIsEnumerable;
        
          /* Native method shortcuts for methods with the same name as other `lodash` methods */
          var nativeCreate = isNative(nativeCreate = Object.create) && nativeCreate,
              nativeIsArray = isNative(nativeIsArray = Array.isArray) && nativeIsArray,
              nativeKeys = isNative(nativeKeys = Object.keys) && nativeKeys,
              nativeMax = Math.max;
        
          /** Used to lookup a built-in constructor by [[Class]] */
          var ctorByClass = {};
          ctorByClass[arrayClass] = Array;
          ctorByClass[boolClass] = Boolean;
          ctorByClass[dateClass] = Date;
          ctorByClass[funcClass] = Function;
          ctorByClass[objectClass] = Object;
          ctorByClass[numberClass] = Number;
          ctorByClass[regexpClass] = RegExp;
          ctorByClass[stringClass] = String;
        
          /*--------------------------------------------------------------------------*/
        
          /**
           * Creates a `lodash` object which wraps the given value to enable intuitive
           * method chaining.
           *
           * In addition to Lo-Dash methods, wrappers also have the following `Array` methods:
           * `concat`, `join`, `pop`, `push`, `reverse`, `shift`, `slice`, `sort`, `splice`,
           * and `unshift`
           *
           * Chaining is supported in custom builds as long as the `value` method is
           * implicitly or explicitly included in the build.
           *
           * The chainable wrapper functions are:
           * `after`, `assign`, `bind`, `bindAll`, `bindKey`, `chain`, `compact`,
           * `compose`, `concat`, `countBy`, `create`, `createCallback`, `curry`,
           * `debounce`, `defaults`, `defer`, `delay`, `difference`, `filter`, `flatten`,
           * `forEach`, `forEachRight`, `forIn`, `forInRight`, `forOwn`, `forOwnRight`,
           * `functions`, `groupBy`, `indexBy`, `initial`, `intersection`, `invert`,
           * `invoke`, `keys`, `map`, `max`, `memoize`, `merge`, `min`, `object`, `omit`,
           * `once`, `pairs`, `partial`, `partialRight`, `pick`, `pluck`, `pull`, `push`,
           * `range`, `reject`, `remove`, `rest`, `reverse`, `shuffle`, `slice`, `sort`,
           * `sortBy`, `splice`, `tap`, `throttle`, `times`, `toArray`, `transform`,
           * `union`, `uniq`, `unshift`, `unzip`, `values`, `where`, `without`, `wrap`,
           * and `zip`
           *
           * The non-chainable wrapper functions are:
           * `clone`, `cloneDeep`, `contains`, `escape`, `every`, `find`, `findIndex`,
           * `findKey`, `findLast`, `findLastIndex`, `findLastKey`, `has`, `identity`,
           * `indexOf`, `isArguments`, `isArray`, `isBoolean`, `isDate`, `isElement`,
           * `isEmpty`, `isEqual`, `isFinite`, `isFunction`, `isNaN`, `isNull`, `isNumber`,
           * `isObject`, `isPlainObject`, `isRegExp`, `isString`, `isUndefined`, `join`,
           * `lastIndexOf`, `mixin`, `noConflict`, `parseInt`, `pop`, `random`, `reduce`,
           * `reduceRight`, `result`, `shift`, `size`, `some`, `sortedIndex`, `runInContext`,
           * `template`, `unescape`, `uniqueId`, and `value`
           *
           * The wrapper functions `first` and `last` return wrapped values when `n` is
           * provided, otherwise they return unwrapped values.
           *
           * Explicit chaining can be enabled by using the `_.chain` method.
           *
           * @name _
           * @constructor
           * @category Chaining
           * @param {*} value The value to wrap in a `lodash` instance.
           * @returns {Object} Returns a `lodash` instance.
           * @example
           *
           * var wrapped = _([1, 2, 3]);
           *
           * // returns an unwrapped value
           * wrapped.reduce(function(sum, num) {
           *   return sum + num;
           * });
           * // => 6
           *
           * // returns a wrapped value
           * var squares = wrapped.map(function(num) {
           *   return num * num;
           * });
           *
           * _.isArray(squares);
           * // => false
           *
           * _.isArray(squares.value());
           * // => true
           */
          function lodash() {
            // no operation performed
          }
        
          /*--------------------------------------------------------------------------*/
        
          /**
           * The base implementation of `_.bind` that creates the bound function and
           * sets its meta data.
           *
           * @private
           * @param {Array} bindData The bind data array.
           * @returns {Function} Returns the new bound function.
           */
          function baseBind(bindData) {
            var func = bindData[0],
                partialArgs = bindData[2],
                thisArg = bindData[4];
        
            function bound() {
              // `Function#bind` spec
              // http://es5.github.io/#x15.3.4.5
              if (partialArgs) {
                // avoid `arguments` object deoptimizations by using `slice` instead
                // of `Array.prototype.slice.call` and not assigning `arguments` to a
                // variable as a ternary expression
                var args = slice(partialArgs);
                push.apply(args, arguments);
              }
              // mimic the constructor's `return` behavior
              // http://es5.github.io/#x13.2.2
              if (this instanceof bound) {
                // ensure `new bound` is an instance of `func`
                var thisBinding = baseCreate(func.prototype),
                    result = func.apply(thisBinding, args || arguments);
                return isObject(result) ? result : thisBinding;
              }
              return func.apply(thisArg, args || arguments);
            }
            return bound;
          }
        
          /**
           * The base implementation of `_.clone` without argument juggling or support
           * for `thisArg` binding.
           *
           * @private
           * @param {*} value The value to clone.
           * @param {boolean} [isDeep=false] Specify a deep clone.
           * @param {Function} [callback] The function to customize cloning values.
           * @param {Array} [stackA=[]] Tracks traversed source objects.
           * @param {Array} [stackB=[]] Associates clones with source counterparts.
           * @returns {*} Returns the cloned value.
           */
          function baseClone(value, isDeep, callback, stackA, stackB) {
            if (callback) {
              var result = callback(value);
              if (typeof result != 'undefined') {
                return result;
              }
            }
            // inspect [[Class]]
            var isObj = isObject(value);
            if (isObj) {
              var className = toString.call(value);
              if (!cloneableClasses[className]) {
                return value;
              }
              var ctor = ctorByClass[className];
              switch (className) {
                case boolClass:
                case dateClass:
                  return new ctor(+value);
        
                case numberClass:
                case stringClass:
                  return new ctor(value);
        
                case regexpClass:
                  result = ctor(value.source, reFlags.exec(value));
                  result.lastIndex = value.lastIndex;
                  return result;
              }
            } else {
              return value;
            }
            var isArr = isArray(value);
            if (isDeep) {
              // check for circular references and return corresponding clone
              var initedStack = !stackA;
              stackA || (stackA = getArray());
              stackB || (stackB = getArray());
        
              var length = stackA.length;
              while (length--) {
                if (stackA[length] == value) {
                  return stackB[length];
                }
              }
              result = isArr ? ctor(value.length) : {};
            }
            else {
              result = isArr ? slice(value) : assign({}, value);
            }
            // add array properties assigned by `RegExp#exec`
            if (isArr) {
              if (hasOwnProperty.call(value, 'index')) {
                result.index = value.index;
              }
              if (hasOwnProperty.call(value, 'input')) {
                result.input = value.input;
              }
            }
            // exit for shallow clone
            if (!isDeep) {
              return result;
            }
            // add the source value to the stack of traversed objects
            // and associate it with its clone
            stackA.push(value);
            stackB.push(result);
        
            // recursively populate clone (susceptible to call stack limits)
            (isArr ? forEach : forOwn)(value, function(objValue, key) {
              result[key] = baseClone(objValue, isDeep, callback, stackA, stackB);
            });
        
            if (initedStack) {
              releaseArray(stackA);
              releaseArray(stackB);
            }
            return result;
          }
        
          /**
           * The base implementation of `_.create` without support for assigning
           * properties to the created object.
           *
           * @private
           * @param {Object} prototype The object to inherit from.
           * @returns {Object} Returns the new object.
           */
          function baseCreate(prototype, properties) {
            return isObject(prototype) ? nativeCreate(prototype) : {};
          }
          // fallback for browsers without `Object.create`
          if (!nativeCreate) {
            baseCreate = (function() {
              function Object() {}
              return function(prototype) {
                if (isObject(prototype)) {
                  Object.prototype = prototype;
                  var result = new Object;
                  Object.prototype = null;
                }
                return result || root.Object();
              };
            }());
          }
        
          /**
           * The base implementation of `_.createCallback` without support for creating
           * "_.pluck" or "_.where" style callbacks.
           *
           * @private
           * @param {*} [func=identity] The value to convert to a callback.
           * @param {*} [thisArg] The `this` binding of the created callback.
           * @param {number} [argCount] The number of arguments the callback accepts.
           * @returns {Function} Returns a callback function.
           */
          function baseCreateCallback(func, thisArg, argCount) {
            if (typeof func != 'function') {
              return identity;
            }
            // exit early for no `thisArg` or already bound by `Function#bind`
            if (typeof thisArg == 'undefined' || !('prototype' in func)) {
              return func;
            }
            switch (argCount) {
              case 1: return function(value) {
                return func.call(thisArg, value);
              };
              case 2: return function(a, b) {
                return func.call(thisArg, a, b);
              };
              case 3: return function(value, index, collection) {
                return func.call(thisArg, value, index, collection);
              };
              case 4: return function(accumulator, value, index, collection) {
                return func.call(thisArg, accumulator, value, index, collection);
              };
            }
            return bind(func, thisArg);
          }
        
          /**
           * The base implementation of `createWrapper` that creates the wrapper and
           * sets its meta data.
           *
           * @private
           * @param {Array} bindData The bind data array.
           * @returns {Function} Returns the new function.
           */
          function baseCreateWrapper(bindData) {
            var func = bindData[0],
                bitmask = bindData[1],
                partialArgs = bindData[2],
                partialRightArgs = bindData[3],
                thisArg = bindData[4],
                arity = bindData[5];
        
            var isBind = bitmask & 1,
                isBindKey = bitmask & 2,
                isCurry = bitmask & 4,
                isCurryBound = bitmask & 8,
                key = func;
        
            function bound() {
              var thisBinding = isBind ? thisArg : this;
              if (partialArgs) {
                var args = slice(partialArgs);
                push.apply(args, arguments);
              }
              if (partialRightArgs || isCurry) {
                args || (args = slice(arguments));
                if (partialRightArgs) {
                  push.apply(args, partialRightArgs);
                }
                if (isCurry && args.length < arity) {
                  bitmask |= 16 & ~32;
                  return baseCreateWrapper([func, (isCurryBound ? bitmask : bitmask & ~3), args, null, thisArg, arity]);
                }
              }
              args || (args = arguments);
              if (isBindKey) {
                func = thisBinding[key];
              }
              if (this instanceof bound) {
                thisBinding = baseCreate(func.prototype);
                var result = func.apply(thisBinding, args);
                return isObject(result) ? result : thisBinding;
              }
              return func.apply(thisBinding, args);
            }
            return bound;
          }
        
          /**
           * The base implementation of `_.difference` that accepts a single array
           * of values to exclude.
           *
           * @private
           * @param {Array} array The array to process.
           * @param {Array} [values] The array of values to exclude.
           * @returns {Array} Returns a new array of filtered values.
           */
          function baseDifference(array, values) {
            var index = -1,
                indexOf = getIndexOf(),
                length = array ? array.length : 0,
                result = [];
        
            while (++index < length) {
              var value = array[index];
              if (indexOf(values, value) < 0) {
                result.push(value);
              }
            }
            return result;
          }
        
          /**
           * The base implementation of `_.flatten` without support for callback
           * shorthands or `thisArg` binding.
           *
           * @private
           * @param {Array} array The array to flatten.
           * @param {boolean} [isShallow=false] A flag to restrict flattening to a single level.
           * @param {boolean} [isStrict=false] A flag to restrict flattening to arrays and `arguments` objects.
           * @param {number} [fromIndex=0] The index to start from.
           * @returns {Array} Returns a new flattened array.
           */
          function baseFlatten(array, isShallow, isStrict, fromIndex) {
            var index = (fromIndex || 0) - 1,
                length = array ? array.length : 0,
                result = [];
        
            while (++index < length) {
              var value = array[index];
        
              if (value && typeof value == 'object' && typeof value.length == 'number'
                  && (isArray(value) || isArguments(value))) {
                // recursively flatten arrays (susceptible to call stack limits)
                if (!isShallow) {
                  value = baseFlatten(value, isShallow, isStrict);
                }
                var valIndex = -1,
                    valLength = value.length,
                    resIndex = result.length;
        
                result.length += valLength;
                while (++valIndex < valLength) {
                  result[resIndex++] = value[valIndex];
                }
              } else if (!isStrict) {
                result.push(value);
              }
            }
            return result;
          }
        
          /**
           * Creates a function that, when called, either curries or invokes `func`
           * with an optional `this` binding and partially applied arguments.
           *
           * @private
           * @param {Function|string} func The function or method name to reference.
           * @param {number} bitmask The bitmask of method flags to compose.
           *  The bitmask may be composed of the following flags:
           *  1 - `_.bind`
           *  2 - `_.bindKey`
           *  4 - `_.curry`
           *  8 - `_.curry` (bound)
           *  16 - `_.partial`
           *  32 - `_.partialRight`
           * @param {Array} [partialArgs] An array of arguments to prepend to those
           *  provided to the new function.
           * @param {Array} [partialRightArgs] An array of arguments to append to those
           *  provided to the new function.
           * @param {*} [thisArg] The `this` binding of `func`.
           * @param {number} [arity] The arity of `func`.
           * @returns {Function} Returns the new function.
           */
          function createWrapper(func, bitmask, partialArgs, partialRightArgs, thisArg, arity) {
            var isBind = bitmask & 1,
                isBindKey = bitmask & 2,
                isCurry = bitmask & 4,
                isCurryBound = bitmask & 8,
                isPartial = bitmask & 16,
                isPartialRight = bitmask & 32;
        
            if (!isBindKey && !isFunction(func)) {
              throw new TypeError;
            }
            if (isPartial && !partialArgs.length) {
              bitmask &= ~16;
              isPartial = partialArgs = false;
            }
            if (isPartialRight && !partialRightArgs.length) {
              bitmask &= ~32;
              isPartialRight = partialRightArgs = false;
            }
            // fast path for `_.bind`
            var creater = (bitmask == 1 || bitmask === 17) ? baseBind : baseCreateWrapper;
            return creater([func, bitmask, partialArgs, partialRightArgs, thisArg, arity]);
          }
        
          /**
           * Gets the appropriate "indexOf" function. If the `_.indexOf` method is
           * customized, this method returns the custom method, otherwise it returns
           * the `baseIndexOf` function.
           *
           * @private
           * @returns {Function} Returns the "indexOf" function.
           */
          function getIndexOf() {
            var result = (result = lodash.indexOf) === indexOf ? baseIndexOf : result;
            return result;
          }
        
          /**
           * Checks if `value` is a native function.
           *
           * @private
           * @param {*} value The value to check.
           * @returns {boolean} Returns `true` if the `value` is a native function, else `false`.
           */
          function isNative(value) {
            return typeof value == 'function' && reNative.test(value);
          }
        
          /*--------------------------------------------------------------------------*/
        
          /**
           * Checks if `value` is an `arguments` object.
           *
           * @static
           * @memberOf _
           * @category Objects
           * @param {*} value The value to check.
           * @returns {boolean} Returns `true` if the `value` is an `arguments` object, else `false`.
           * @example
           *
           * (function() { return _.isArguments(arguments); })(1, 2, 3);
           * // => true
           *
           * _.isArguments([1, 2, 3]);
           * // => false
           */
          function isArguments(value) {
            return value && typeof value == 'object' && typeof value.length == 'number' &&
              toString.call(value) == argsClass || false;
          }
          // fallback for browsers that can't detect `arguments` objects by [[Class]]
          if (!isArguments(arguments)) {
            isArguments = function(value) {
              return value && typeof value == 'object' && typeof value.length == 'number' &&
                hasOwnProperty.call(value, 'callee') && !propertyIsEnumerable.call(value, 'callee') || false;
            };
          }
        
          /**
           * Checks if `value` is an array.
           *
           * @static
           * @memberOf _
           * @type Function
           * @category Objects
           * @param {*} value The value to check.
           * @returns {boolean} Returns `true` if the `value` is an array, else `false`.
           * @example
           *
           * (function() { return _.isArray(arguments); })();
           * // => false
           *
           * _.isArray([1, 2, 3]);
           * // => true
           */
          var isArray = nativeIsArray || function(value) {
            return value && typeof value == 'object' && typeof value.length == 'number' &&
              toString.call(value) == arrayClass || false;
          };
        
          /**
           * A fallback implementation of `Object.keys` which produces an array of the
           * given object's own enumerable property names.
           *
           * @private
           * @type Function
           * @param {Object} object The object to inspect.
           * @returns {Array} Returns an array of property names.
           */
          var shimKeys = function(object) {
            var index, iterable = object, result = [];
            if (!iterable) return result;
            if (!(objectTypes[typeof object])) return result;
              for (index in iterable) {
                if (hasOwnProperty.call(iterable, index)) {
                  result.push(index);
                }
              }
            return result
          };
        
          /**
           * Creates an array composed of the own enumerable property names of an object.
           *
           * @static
           * @memberOf _
           * @category Objects
           * @param {Object} object The object to inspect.
           * @returns {Array} Returns an array of property names.
           * @example
           *
           * _.keys({ 'one': 1, 'two': 2, 'three': 3 });
           * // => ['one', 'two', 'three'] (property order is not guaranteed across environments)
           */
          var keys = !nativeKeys ? shimKeys : function(object) {
            if (!isObject(object)) {
              return [];
            }
            return nativeKeys(object);
          };
        
          /*--------------------------------------------------------------------------*/
        
          /**
           * Assigns own enumerable properties of source object(s) to the destination
           * object. Subsequent sources will overwrite property assignments of previous
           * sources. If a callback is provided it will be executed to produce the
           * assigned values. The callback is bound to `thisArg` and invoked with two
           * arguments; (objectValue, sourceValue).
           *
           * @static
           * @memberOf _
           * @type Function
           * @alias extend
           * @category Objects
           * @param {Object} object The destination object.
           * @param {...Object} [source] The source objects.
           * @param {Function} [callback] The function to customize assigning values.
           * @param {*} [thisArg] The `this` binding of `callback`.
           * @returns {Object} Returns the destination object.
           * @example
           *
           * _.assign({ 'name': 'fred' }, { 'employer': 'slate' });
           * // => { 'name': 'fred', 'employer': 'slate' }
           *
           * var defaults = _.partialRight(_.assign, function(a, b) {
           *   return typeof a == 'undefined' ? b : a;
           * });
           *
           * var object = { 'name': 'barney' };
           * defaults(object, { 'name': 'fred', 'employer': 'slate' });
           * // => { 'name': 'barney', 'employer': 'slate' }
           */
          function assign(object) {
            if (!object) {
              return object;
            }
            for (var argsIndex = 1, argsLength = arguments.length; argsIndex < argsLength; argsIndex++) {
              var iterable = arguments[argsIndex];
              if (iterable) {
                for (var key in iterable) {
                  object[key] = iterable[key];
                }
              }
            }
            return object;
          }
        
          /**
           * Creates a deep clone of `value`. If a callback is provided it will be
           * executed to produce the cloned values. If the callback returns `undefined`
           * cloning will be handled by the method instead. The callback is bound to
           * `thisArg` and invoked with one argument; (value).
           *
           * Note: This method is loosely based on the structured clone algorithm. Functions
           * and DOM nodes are **not** cloned. The enumerable properties of `arguments` objects and
           * objects created by constructors other than `Object` are cloned to plain `Object` objects.
           * See http://www.w3.org/TR/html5/infrastructure.html#internal-structured-cloning-algorithm.
           *
           * @static
           * @memberOf _
           * @category Objects
           * @param {*} value The value to deep clone.
           * @param {Function} [callback] The function to customize cloning values.
           * @param {*} [thisArg] The `this` binding of `callback`.
           * @returns {*} Returns the deep cloned value.
           * @example
           *
           * var characters = [
           *   { 'name': 'barney', 'age': 36 },
           *   { 'name': 'fred',   'age': 40 }
           * ];
           *
           * var deep = _.cloneDeep(characters);
           * deep[0] === characters[0];
           * // => false
           *
           * var view = {
           *   'label': 'docs',
           *   'node': element
           * };
           *
           * var clone = _.cloneDeep(view, function(value) {
           *   return _.isElement(value) ? value.cloneNode(true) : undefined;
           * });
           *
           * clone.node == view.node;
           * // => false
           */
          function cloneDeep(value, callback, thisArg) {
            return baseClone(value, true, typeof callback == 'function' && baseCreateCallback(callback, thisArg, 1));
          }
        
          /**
           * Iterates over own and inherited enumerable properties of an object,
           * executing the callback for each property. The callback is bound to `thisArg`
           * and invoked with three arguments; (value, key, object). Callbacks may exit
           * iteration early by explicitly returning `false`.
           *
           * @static
           * @memberOf _
           * @type Function
           * @category Objects
           * @param {Object} object The object to iterate over.
           * @param {Function} [callback=identity] The function called per iteration.
           * @param {*} [thisArg] The `this` binding of `callback`.
           * @returns {Object} Returns `object`.
           * @example
           *
           * function Shape() {
           *   this.x = 0;
           *   this.y = 0;
           * }
           *
           * Shape.prototype.move = function(x, y) {
           *   this.x += x;
           *   this.y += y;
           * };
           *
           * _.forIn(new Shape, function(value, key) {
           *   console.log(key);
           * });
           * // => logs 'x', 'y', and 'move' (property order is not guaranteed across environments)
           */
          var forIn = function(collection, callback) {
            var index, iterable = collection, result = iterable;
            if (!iterable) return result;
            if (!objectTypes[typeof iterable]) return result;
              for (index in iterable) {
                if (callback(iterable[index], index, collection) === indicatorObject) return result;
              }
            return result
          };
        
          /**
           * Iterates over own enumerable properties of an object, executing the callback
           * for each property. The callback is bound to `thisArg` and invoked with three
           * arguments; (value, key, object). Callbacks may exit iteration early by
           * explicitly returning `false`.
           *
           * @static
           * @memberOf _
           * @type Function
           * @category Objects
           * @param {Object} object The object to iterate over.
           * @param {Function} [callback=identity] The function called per iteration.
           * @param {*} [thisArg] The `this` binding of `callback`.
           * @returns {Object} Returns `object`.
           * @example
           *
           * _.forOwn({ '0': 'zero', '1': 'one', 'length': 2 }, function(num, key) {
           *   console.log(key);
           * });
           * // => logs '0', '1', and 'length' (property order is not guaranteed across environments)
           */
          var forOwn = function(collection, callback) {
            var index, iterable = collection, result = iterable;
            if (!iterable) return result;
            if (!objectTypes[typeof iterable]) return result;
              for (index in iterable) {
                if (hasOwnProperty.call(iterable, index)) {
                  if (callback(iterable[index], index, collection) === indicatorObject) return result;
                }
              }
            return result
          };
        
          /**
           * Checks if `value` is empty. Arrays, strings, or `arguments` objects with a
           * length of `0` and objects with no own enumerable properties are considered
           * "empty".
           *
           * @static
           * @memberOf _
           * @category Objects
           * @param {Array|Object|string} value The value to inspect.
           * @returns {boolean} Returns `true` if the `value` is empty, else `false`.
           * @example
           *
           * _.isEmpty([1, 2, 3]);
           * // => false
           *
           * _.isEmpty({});
           * // => true
           *
           * _.isEmpty('');
           * // => true
           */
          function isEmpty(value) {
            if (!value) {
              return true;
            }
            if (isArray(value) || isString(value)) {
              return !value.length;
            }
            for (var key in value) {
              if (hasOwnProperty.call(value, key)) {
                return false;
              }
            }
            return true;
          }
        
          /**
           * Checks if `value` is a function.
           *
           * @static
           * @memberOf _
           * @category Objects
           * @param {*} value The value to check.
           * @returns {boolean} Returns `true` if the `value` is a function, else `false`.
           * @example
           *
           * _.isFunction(_);
           * // => true
           */
          function isFunction(value) {
            return typeof value == 'function';
          }
          // fallback for older versions of Chrome and Safari
          if (isFunction(/x/)) {
            isFunction = function(value) {
              return typeof value == 'function' && toString.call(value) == funcClass;
            };
          }
        
          /**
           * Checks if `value` is the language type of Object.
           * (e.g. arrays, functions, objects, regexes, `new Number(0)`, and `new String('')`)
           *
           * @static
           * @memberOf _
           * @category Objects
           * @param {*} value The value to check.
           * @returns {boolean} Returns `true` if the `value` is an object, else `false`.
           * @example
           *
           * _.isObject({});
           * // => true
           *
           * _.isObject([1, 2, 3]);
           * // => true
           *
           * _.isObject(1);
           * // => false
           */
          function isObject(value) {
            // check if the value is the ECMAScript language type of Object
            // http://es5.github.io/#x8
            // and avoid a V8 bug
            // http://code.google.com/p/v8/issues/detail?id=2291
            return !!(value && objectTypes[typeof value]);
          }
        
          /**
           * Checks if `value` is a string.
           *
           * @static
           * @memberOf _
           * @category Objects
           * @param {*} value The value to check.
           * @returns {boolean} Returns `true` if the `value` is a string, else `false`.
           * @example
           *
           * _.isString('fred');
           * // => true
           */
          function isString(value) {
            return typeof value == 'string' ||
              value && typeof value == 'object' && toString.call(value) == stringClass || false;
          }
        
          /**
           * Creates a shallow clone of `object` excluding the specified properties.
           * Property names may be specified as individual arguments or as arrays of
           * property names. If a callback is provided it will be executed for each
           * property of `object` omitting the properties the callback returns truey
           * for. The callback is bound to `thisArg` and invoked with three arguments;
           * (value, key, object).
           *
           * @static
           * @memberOf _
           * @category Objects
           * @param {Object} object The source object.
           * @param {Function|...string|string[]} [callback] The properties to omit or the
           *  function called per iteration.
           * @param {*} [thisArg] The `this` binding of `callback`.
           * @returns {Object} Returns an object without the omitted properties.
           * @example
           *
           * _.omit({ 'name': 'fred', 'age': 40 }, 'age');
           * // => { 'name': 'fred' }
           *
           * _.omit({ 'name': 'fred', 'age': 40 }, function(value) {
           *   return typeof value == 'number';
           * });
           * // => { 'name': 'fred' }
           */
          function omit(object) {
            var props = [];
            forIn(object, function(value, key) {
              props.push(key);
            });
            props = baseDifference(props, baseFlatten(arguments, true, false, 1));
        
            var index = -1,
                length = props.length,
                result = {};
        
            while (++index < length) {
              var key = props[index];
              result[key] = object[key];
            }
            return result;
          }
        
          /**
           * Creates a shallow clone of `object` composed of the specified properties.
           * Property names may be specified as individual arguments or as arrays of
           * property names. If a callback is provided it will be executed for each
           * property of `object` picking the properties the callback returns truey
           * for. The callback is bound to `thisArg` and invoked with three arguments;
           * (value, key, object).
           *
           * @static
           * @memberOf _
           * @category Objects
           * @param {Object} object The source object.
           * @param {Function|...string|string[]} [callback] The function called per
           *  iteration or property names to pick, specified as individual property
           *  names or arrays of property names.
           * @param {*} [thisArg] The `this` binding of `callback`.
           * @returns {Object} Returns an object composed of the picked properties.
           * @example
           *
           * _.pick({ 'name': 'fred', '_userid': 'fred1' }, 'name');
           * // => { 'name': 'fred' }
           *
           * _.pick({ 'name': 'fred', '_userid': 'fred1' }, function(value, key) {
           *   return key.charAt(0) != '_';
           * });
           * // => { 'name': 'fred' }
           */
          function pick(object) {
            var index = -1,
                props = baseFlatten(arguments, true, false, 1),
                length = props.length,
                result = {};
        
            while (++index < length) {
              var key = props[index];
              if (key in object) {
                result[key] = object[key];
              }
            }
            return result;
          }
        
          /**
           * Creates an array composed of the own enumerable property values of `object`.
           *
           * @static
           * @memberOf _
           * @category Objects
           * @param {Object} object The object to inspect.
           * @returns {Array} Returns an array of property values.
           * @example
           *
           * _.values({ 'one': 1, 'two': 2, 'three': 3 });
           * // => [1, 2, 3] (property order is not guaranteed across environments)
           */
          function values(object) {
            var index = -1,
                props = keys(object),
                length = props.length,
                result = Array(length);
        
            while (++index < length) {
              result[index] = object[props[index]];
            }
            return result;
          }
        
          /*--------------------------------------------------------------------------*/
        
          /**
           * Iterates over elements of a collection, returning an array of all elements
           * the callback returns truey for. The callback is bound to `thisArg` and
           * invoked with three arguments; (value, index|key, collection).
           *
           * If a property name is provided for `callback` the created "_.pluck" style
           * callback will return the property value of the given element.
           *
           * If an object is provided for `callback` the created "_.where" style callback
           * will return `true` for elements that have the properties of the given object,
           * else `false`.
           *
           * @static
           * @memberOf _
           * @alias select
           * @category Collections
           * @param {Array|Object|string} collection The collection to iterate over.
           * @param {Function|Object|string} [callback=identity] The function called
           *  per iteration. If a property name or object is provided it will be used
           *  to create a "_.pluck" or "_.where" style callback, respectively.
           * @param {*} [thisArg] The `this` binding of `callback`.
           * @returns {Array} Returns a new array of elements that passed the callback check.
           * @example
           *
           * var evens = _.filter([1, 2, 3, 4, 5, 6], function(num) { return num % 2 == 0; });
           * // => [2, 4, 6]
           *
           * var characters = [
           *   { 'name': 'barney', 'age': 36, 'blocked': false },
           *   { 'name': 'fred',   'age': 40, 'blocked': true }
           * ];
           *
           * // using "_.pluck" callback shorthand
           * _.filter(characters, 'blocked');
           * // => [{ 'name': 'fred', 'age': 40, 'blocked': true }]
           *
           * // using "_.where" callback shorthand
           * _.filter(characters, { 'age': 36 });
           * // => [{ 'name': 'barney', 'age': 36, 'blocked': false }]
           */
          function filter(collection, callback, thisArg) {
            var result = [];
            callback = createCallback(callback, thisArg, 3);
        
            var index = -1,
                length = collection ? collection.length : 0;
        
            if (typeof length == 'number') {
              while (++index < length) {
                var value = collection[index];
                if (callback(value, index, collection)) {
                  result.push(value);
                }
              }
            } else {
              forOwn(collection, function(value, index, collection) {
                if (callback(value, index, collection)) {
                  result.push(value);
                }
              });
            }
            return result;
          }
        
          /**
           * Iterates over elements of a collection, returning the first element that
           * the callback returns truey for. The callback is bound to `thisArg` and
           * invoked with three arguments; (value, index|key, collection).
           *
           * If a property name is provided for `callback` the created "_.pluck" style
           * callback will return the property value of the given element.
           *
           * If an object is provided for `callback` the created "_.where" style callback
           * will return `true` for elements that have the properties of the given object,
           * else `false`.
           *
           * @static
           * @memberOf _
           * @alias detect, findWhere
           * @category Collections
           * @param {Array|Object|string} collection The collection to iterate over.
           * @param {Function|Object|string} [callback=identity] The function called
           *  per iteration. If a property name or object is provided it will be used
           *  to create a "_.pluck" or "_.where" style callback, respectively.
           * @param {*} [thisArg] The `this` binding of `callback`.
           * @returns {*} Returns the found element, else `undefined`.
           * @example
           *
           * var characters = [
           *   { 'name': 'barney',  'age': 36, 'blocked': false },
           *   { 'name': 'fred',    'age': 40, 'blocked': true },
           *   { 'name': 'pebbles', 'age': 1,  'blocked': false }
           * ];
           *
           * _.find(characters, function(chr) {
           *   return chr.age < 40;
           * });
           * // => { 'name': 'barney', 'age': 36, 'blocked': false }
           *
           * // using "_.where" callback shorthand
           * _.find(characters, { 'age': 1 });
           * // =>  { 'name': 'pebbles', 'age': 1, 'blocked': false }
           *
           * // using "_.pluck" callback shorthand
           * _.find(characters, 'blocked');
           * // => { 'name': 'fred', 'age': 40, 'blocked': true }
           */
          function find(collection, callback, thisArg) {
            callback = createCallback(callback, thisArg, 3);
        
            var index = -1,
                length = collection ? collection.length : 0;
        
            if (typeof length == 'number') {
              while (++index < length) {
                var value = collection[index];
                if (callback(value, index, collection)) {
                  return value;
                }
              }
            } else {
              var result;
              forOwn(collection, function(value, index, collection) {
                if (callback(value, index, collection)) {
                  result = value;
                  return indicatorObject;
                }
              });
              return result;
            }
          }
        
          /**
           * Iterates over elements of a collection, executing the callback for each
           * element. The callback is bound to `thisArg` and invoked with three arguments;
           * (value, index|key, collection). Callbacks may exit iteration early by
           * explicitly returning `false`.
           *
           * Note: As with other "Collections" methods, objects with a `length` property
           * are iterated like arrays. To avoid this behavior `_.forIn` or `_.forOwn`
           * may be used for object iteration.
           *
           * @static
           * @memberOf _
           * @alias each
           * @category Collections
           * @param {Array|Object|string} collection The collection to iterate over.
           * @param {Function} [callback=identity] The function called per iteration.
           * @param {*} [thisArg] The `this` binding of `callback`.
           * @returns {Array|Object|string} Returns `collection`.
           * @example
           *
           * _([1, 2, 3]).forEach(function(num) { console.log(num); }).join(',');
           * // => logs each number and returns '1,2,3'
           *
           * _.forEach({ 'one': 1, 'two': 2, 'three': 3 }, function(num) { console.log(num); });
           * // => logs each number and returns the object (property order is not guaranteed across environments)
           */
          function forEach(collection, callback, thisArg) {
            var index = -1,
                length = collection ? collection.length : 0;
        
            callback = callback && typeof thisArg == 'undefined' ? callback : baseCreateCallback(callback, thisArg, 3);
            if (typeof length == 'number') {
              while (++index < length) {
                if (callback(collection[index], index, collection) === indicatorObject) {
                  break;
                }
              }
            } else {
              forOwn(collection, callback);
            }
          }
        
          /**
           * Creates an array of values by running each element in the collection
           * through the callback. The callback is bound to `thisArg` and invoked with
           * three arguments; (value, index|key, collection).
           *
           * If a property name is provided for `callback` the created "_.pluck" style
           * callback will return the property value of the given element.
           *
           * If an object is provided for `callback` the created "_.where" style callback
           * will return `true` for elements that have the properties of the given object,
           * else `false`.
           *
           * @static
           * @memberOf _
           * @alias collect
           * @category Collections
           * @param {Array|Object|string} collection The collection to iterate over.
           * @param {Function|Object|string} [callback=identity] The function called
           *  per iteration. If a property name or object is provided it will be used
           *  to create a "_.pluck" or "_.where" style callback, respectively.
           * @param {*} [thisArg] The `this` binding of `callback`.
           * @returns {Array} Returns a new array of the results of each `callback` execution.
           * @example
           *
           * _.map([1, 2, 3], function(num) { return num * 3; });
           * // => [3, 6, 9]
           *
           * _.map({ 'one': 1, 'two': 2, 'three': 3 }, function(num) { return num * 3; });
           * // => [3, 6, 9] (property order is not guaranteed across environments)
           *
           * var characters = [
           *   { 'name': 'barney', 'age': 36 },
           *   { 'name': 'fred',   'age': 40 }
           * ];
           *
           * // using "_.pluck" callback shorthand
           * _.map(characters, 'name');
           * // => ['barney', 'fred']
           */
          function map(collection, callback, thisArg) {
            var index = -1,
                length = collection ? collection.length : 0;
        
            callback = createCallback(callback, thisArg, 3);
            if (typeof length == 'number') {
              var result = Array(length);
              while (++index < length) {
                result[index] = callback(collection[index], index, collection);
              }
            } else {
              result = [];
              forOwn(collection, function(value, key, collection) {
                result[++index] = callback(value, key, collection);
              });
            }
            return result;
          }
        
          /**
           * Creates an array of elements, sorted in ascending order by the results of
           * running each element in a collection through the callback. This method
           * performs a stable sort, that is, it will preserve the original sort order
           * of equal elements. The callback is bound to `thisArg` and invoked with
           * three arguments; (value, index|key, collection).
           *
           * If a property name is provided for `callback` the created "_.pluck" style
           * callback will return the property value of the given element.
           *
           * If an array of property names is provided for `callback` the collection
           * will be sorted by each property value.
           *
           * If an object is provided for `callback` the created "_.where" style callback
           * will return `true` for elements that have the properties of the given object,
           * else `false`.
           *
           * @static
           * @memberOf _
           * @category Collections
           * @param {Array|Object|string} collection The collection to iterate over.
           * @param {Array|Function|Object|string} [callback=identity] The function called
           *  per iteration. If a property name or object is provided it will be used
           *  to create a "_.pluck" or "_.where" style callback, respectively.
           * @param {*} [thisArg] The `this` binding of `callback`.
           * @returns {Array} Returns a new array of sorted elements.
           * @example
           *
           * _.sortBy([1, 2, 3], function(num) { return Math.sin(num); });
           * // => [3, 1, 2]
           *
           * _.sortBy([1, 2, 3], function(num) { return this.sin(num); }, Math);
           * // => [3, 1, 2]
           *
           * var characters = [
           *   { 'name': 'barney',  'age': 36 },
           *   { 'name': 'fred',    'age': 40 },
           *   { 'name': 'barney',  'age': 26 },
           *   { 'name': 'fred',    'age': 30 }
           * ];
           *
           * // using "_.pluck" callback shorthand
           * _.map(_.sortBy(characters, 'age'), _.values);
           * // => [['barney', 26], ['fred', 30], ['barney', 36], ['fred', 40]]
           *
           * // sorting by multiple properties
           * _.map(_.sortBy(characters, ['name', 'age']), _.values);
           * // = > [['barney', 26], ['barney', 36], ['fred', 30], ['fred', 40]]
           */
          function sortBy(collection, callback, thisArg) {
            var index = -1,
                length = collection ? collection.length : 0,
                result = Array(typeof length == 'number' ? length : 0);
        
            callback = createCallback(callback, thisArg, 3);
            forEach(collection, function(value, key, collection) {
              result[++index] = {
                'criteria': [callback(value, key, collection)],
                'index': index,
                'value': value
              };
            });
        
            length = result.length;
            result.sort(compareAscending);
            while (length--) {
              result[length] = result[length].value;
            }
            return result;
          }
        
          /**
           * Converts the `collection` to an array.
           *
           * @static
           * @memberOf _
           * @category Collections
           * @param {Array|Object|string} collection The collection to convert.
           * @returns {Array} Returns the new converted array.
           * @example
           *
           * (function() { return _.toArray(arguments).slice(1); })(1, 2, 3, 4);
           * // => [2, 3, 4]
           */
          function toArray(collection) {
            if (isArray(collection)) {
              return slice(collection);
            }
            if (collection && typeof collection.length == 'number') {
              return map(collection);
            }
            return values(collection);
          }
        
          /**
           * Performs a deep comparison of each element in a `collection` to the given
           * `properties` object, returning an array of all elements that have equivalent
           * property values.
           *
           * @static
           * @memberOf _
           * @type Function
           * @category Collections
           * @param {Array|Object|string} collection The collection to iterate over.
           * @param {Object} props The object of property values to filter by.
           * @returns {Array} Returns a new array of elements that have the given properties.
           * @example
           *
           * var characters = [
           *   { 'name': 'barney', 'age': 36, 'pets': ['hoppy'] },
           *   { 'name': 'fred',   'age': 40, 'pets': ['baby puss', 'dino'] }
           * ];
           *
           * _.where(characters, { 'age': 36 });
           * // => [{ 'name': 'barney', 'age': 36, 'pets': ['hoppy'] }]
           *
           * _.where(characters, { 'pets': ['dino'] });
           * // => [{ 'name': 'fred', 'age': 40, 'pets': ['baby puss', 'dino'] }]
           */
          function where(collection, properties, first) {
            return (first && isEmpty(properties))
              ? undefined
              : (first ? find : filter)(collection, properties);
          }
        
          /*--------------------------------------------------------------------------*/
        
          /**
           * Gets the index at which the first occurrence of `value` is found using
           * strict equality for comparisons, i.e. `===`. If the array is already sorted
           * providing `true` for `fromIndex` will run a faster binary search.
           *
           * @static
           * @memberOf _
           * @category Arrays
           * @param {Array} array The array to search.
           * @param {*} value The value to search for.
           * @param {boolean|number} [fromIndex=0] The index to search from or `true`
           *  to perform a binary search on a sorted array.
           * @returns {number} Returns the index of the matched value or `-1`.
           * @example
           *
           * _.indexOf([1, 2, 3, 1, 2, 3], 2);
           * // => 1
           *
           * _.indexOf([1, 2, 3, 1, 2, 3], 2, 3);
           * // => 4
           *
           * _.indexOf([1, 1, 2, 2, 3, 3], 2, true);
           * // => 2
           */
          function indexOf(array, value, fromIndex) {
            if (typeof fromIndex == 'number') {
              var length = array ? array.length : 0;
              fromIndex = (fromIndex < 0 ? nativeMax(0, length + fromIndex) : fromIndex || 0);
            } else if (fromIndex) {
              var index = sortedIndex(array, value);
              return array[index] === value ? index : -1;
            }
            return baseIndexOf(array, value, fromIndex);
          }
        
          /**
           * Uses a binary search to determine the smallest index at which a value
           * should be inserted into a given sorted array in order to maintain the sort
           * order of the array. If a callback is provided it will be executed for
           * `value` and each element of `array` to compute their sort ranking. The
           * callback is bound to `thisArg` and invoked with one argument; (value).
           *
           * If a property name is provided for `callback` the created "_.pluck" style
           * callback will return the property value of the given element.
           *
           * If an object is provided for `callback` the created "_.where" style callback
           * will return `true` for elements that have the properties of the given object,
           * else `false`.
           *
           * @static
           * @memberOf _
           * @category Arrays
           * @param {Array} array The array to inspect.
           * @param {*} value The value to evaluate.
           * @param {Function|Object|string} [callback=identity] The function called
           *  per iteration. If a property name or object is provided it will be used
           *  to create a "_.pluck" or "_.where" style callback, respectively.
           * @param {*} [thisArg] The `this` binding of `callback`.
           * @returns {number} Returns the index at which `value` should be inserted
           *  into `array`.
           * @example
           *
           * _.sortedIndex([20, 30, 50], 40);
           * // => 2
           *
           * // using "_.pluck" callback shorthand
           * _.sortedIndex([{ 'x': 20 }, { 'x': 30 }, { 'x': 50 }], { 'x': 40 }, 'x');
           * // => 2
           *
           * var dict = {
           *   'wordToNumber': { 'twenty': 20, 'thirty': 30, 'fourty': 40, 'fifty': 50 }
           * };
           *
           * _.sortedIndex(['twenty', 'thirty', 'fifty'], 'fourty', function(word) {
           *   return dict.wordToNumber[word];
           * });
           * // => 2
           *
           * _.sortedIndex(['twenty', 'thirty', 'fifty'], 'fourty', function(word) {
           *   return this.wordToNumber[word];
           * }, dict);
           * // => 2
           */
          function sortedIndex(array, value, callback, thisArg) {
            var low = 0,
                high = array ? array.length : low;
        
            // explicitly reference `identity` for better inlining in Firefox
            callback = callback ? createCallback(callback, thisArg, 1) : identity;
            value = callback(value);
        
            while (low < high) {
              var mid = (low + high) >>> 1;
              (callback(array[mid]) < value)
                ? low = mid + 1
                : high = mid;
            }
            return low;
          }
        
          /*--------------------------------------------------------------------------*/
        
          /**
           * Creates a function that, when called, invokes `func` with the `this`
           * binding of `thisArg` and prepends any additional `bind` arguments to those
           * provided to the bound function.
           *
           * @static
           * @memberOf _
           * @category Functions
           * @param {Function} func The function to bind.
           * @param {*} [thisArg] The `this` binding of `func`.
           * @param {...*} [arg] Arguments to be partially applied.
           * @returns {Function} Returns the new bound function.
           * @example
           *
           * var func = function(greeting) {
           *   return greeting + ' ' + this.name;
           * };
           *
           * func = _.bind(func, { 'name': 'fred' }, 'hi');
           * func();
           * // => 'hi fred'
           */
          function bind(func, thisArg) {
            return arguments.length > 2
              ? createWrapper(func, 17, slice(arguments, 2), null, thisArg)
              : createWrapper(func, 1, null, null, thisArg);
          }
        
          /*--------------------------------------------------------------------------*/
        
          /**
           * Produces a callback bound to an optional `thisArg`. If `func` is a property
           * name the created callback will return the property value for a given element.
           * If `func` is an object the created callback will return `true` for elements
           * that contain the equivalent object properties, otherwise it will return `false`.
           *
           * @static
           * @memberOf _
           * @category Utilities
           * @param {*} [func=identity] The value to convert to a callback.
           * @param {*} [thisArg] The `this` binding of the created callback.
           * @param {number} [argCount] The number of arguments the callback accepts.
           * @returns {Function} Returns a callback function.
           * @example
           *
           * var characters = [
           *   { 'name': 'barney', 'age': 36 },
           *   { 'name': 'fred',   'age': 40 }
           * ];
           *
           * // wrap to create custom callback shorthands
           * _.createCallback = _.wrap(_.createCallback, function(func, callback, thisArg) {
           *   var match = /^(.+?)__([gl]t)(.+)$/.exec(callback);
           *   return !match ? func(callback, thisArg) : function(object) {
           *     return match[2] == 'gt' ? object[match[1]] > match[3] : object[match[1]] < match[3];
           *   };
           * });
           *
           * _.filter(characters, 'age__gt38');
           * // => [{ 'name': 'fred', 'age': 40 }]
           */
          function createCallback(func, thisArg, argCount) {
            var type = typeof func;
            if (func == null || type == 'function') {
              return baseCreateCallback(func, thisArg, argCount);
            }
            // handle "_.pluck" style callback shorthands
            if (type != 'object') {
              return property(func);
            }
            var props = keys(func);
            return function(object) {
              var length = props.length,
                  result = false;
        
              while (length--) {
                if (!(result = object[props[length]] === func[props[length]])) {
                  break;
                }
              }
              return result;
            };
          }
        
          /**
           * This method returns the first argument provided to it.
           *
           * @static
           * @memberOf _
           * @category Utilities
           * @param {*} value Any value.
           * @returns {*} Returns `value`.
           * @example
           *
           * var object = { 'name': 'fred' };
           * _.identity(object) === object;
           * // => true
           */
          function identity(value) {
            return value;
          }
        
          /**
           * A no-operation function.
           *
           * @static
           * @memberOf _
           * @category Utilities
           * @example
           *
           * var object = { 'name': 'fred' };
           * _.noop(object) === undefined;
           * // => true
           */
          function noop() {
            // no operation performed
          }
        
          /**
           * Creates a "_.pluck" style function, which returns the `key` value of a
           * given object.
           *
           * @static
           * @memberOf _
           * @category Utilities
           * @param {string} key The name of the property to retrieve.
           * @returns {Function} Returns the new function.
           * @example
           *
           * var characters = [
           *   { 'name': 'fred',   'age': 40 },
           *   { 'name': 'barney', 'age': 36 }
           * ];
           *
           * var getName = _.property('name');
           *
           * _.map(characters, getName);
           * // => ['barney', 'fred']
           *
           * _.sortBy(characters, getName);
           * // => [{ 'name': 'barney', 'age': 36 }, { 'name': 'fred',   'age': 40 }]
           */
          function property(key) {
            return function(object) {
              return object[key];
            };
          }
        
          /*--------------------------------------------------------------------------*/
        
          lodash.bind = bind;
          lodash.filter = filter;
          lodash.forEach = forEach;
          lodash.keys = keys;
          lodash.map = map;
          lodash.omit = omit;
          lodash.pick = pick;
          lodash.sortBy = sortBy;
          lodash.toArray = toArray;
          lodash.values = values;
          lodash.where = where;
        
          // add aliases
          lodash.collect = map;
          lodash.each = forEach;
          lodash.extend = assign;
          lodash.select = filter;
        
          /*--------------------------------------------------------------------------*/
        
          lodash.cloneDeep = cloneDeep;
          lodash.find = find;
          lodash.identity = identity;
          lodash.indexOf = indexOf;
          lodash.isArguments = isArguments;
          lodash.isArray = isArray;
          lodash.isEmpty = isEmpty;
          lodash.isFunction = isFunction;
          lodash.isObject = isObject;
          lodash.isString = isString;
          lodash.sortedIndex = sortedIndex;
        
          lodash.detect = find;
        
          /*--------------------------------------------------------------------------*/
        
          /**
           * The semantic version number.
           *
           * @static
           * @memberOf _
           * @type string
           */
          lodash.VERSION = '2.4.1';
        
        
        

        delete lodash.VERSION;
        delete lodash.extend;

        return lodash;
    }


    radic.extend(getlodash());

    radic.defined = radic.isDefined = function(val){
        return radic.isUndefined(val) === false;
    };


    var crypt = {};

    radic.extend({
        crypt: {
            md5: function (str) {
                //  discuss at: http://phpjs.org/functions/md5/
                // original by: Webtoolkit.info (http://www.webtoolkit.info/)
                // improved by: Michael White (http://getsprink.com)
                // improved by: Jack
                // improved by: Kevin van Zonneveld (http://kevin.vanzonneveld.net)
                //    input by: Brett Zamir (http://brett-zamir.me)
                // bugfixed by: Kevin van Zonneveld (http://kevin.vanzonneveld.net)
                //  depends on: utf8_encode
                //   example 1: md5('Kevin van Zonneveld');
                //   returns 1: '6e658d4bfcb59cc13f96c14450ac40b9'

                var xl;

                var rotateLeft = function (lValue, iShiftBits) {
                    return (lValue << iShiftBits) | (lValue >>> (32 - iShiftBits));
                };

                var addUnsigned = function (lX, lY) {
                    var lX4, lY4, lX8, lY8, lResult;
                    lX8 = (lX & 0x80000000);
                    lY8 = (lY & 0x80000000);
                    lX4 = (lX & 0x40000000);
                    lY4 = (lY & 0x40000000);
                    lResult = (lX & 0x3FFFFFFF) + (lY & 0x3FFFFFFF);
                    if (lX4 & lY4) {
                        return (lResult ^ 0x80000000 ^ lX8 ^ lY8);
                    }
                    if (lX4 | lY4) {
                        if (lResult & 0x40000000) {
                            return (lResult ^ 0xC0000000 ^ lX8 ^ lY8);
                        } else {
                            return (lResult ^ 0x40000000 ^ lX8 ^ lY8);
                        }
                    } else {
                        return (lResult ^ lX8 ^ lY8);
                    }
                };

                var _F = function (x, y, z) {
                    return (x & y) | ((~x) & z);
                };
                var _G = function (x, y, z) {
                    return (x & z) | (y & (~z));
                };
                var _H = function (x, y, z) {
                    return (x ^ y ^ z);
                };
                var _I = function (x, y, z) {
                    return (y ^ (x | (~z)));
                };

                var _FF = function (a, b, c, d, x, s, ac) {
                    a = addUnsigned(a, addUnsigned(addUnsigned(_F(b, c, d), x), ac));
                    return addUnsigned(rotateLeft(a, s), b);
                };

                var _GG = function (a, b, c, d, x, s, ac) {
                    a = addUnsigned(a, addUnsigned(addUnsigned(_G(b, c, d), x), ac));
                    return addUnsigned(rotateLeft(a, s), b);
                };

                var _HH = function (a, b, c, d, x, s, ac) {
                    a = addUnsigned(a, addUnsigned(addUnsigned(_H(b, c, d), x), ac));
                    return addUnsigned(rotateLeft(a, s), b);
                };

                var _II = function (a, b, c, d, x, s, ac) {
                    a = addUnsigned(a, addUnsigned(addUnsigned(_I(b, c, d), x), ac));
                    return addUnsigned(rotateLeft(a, s), b);
                };

                var convertToWordArray = function (str) {
                    var lWordCount;
                    var lMessageLength = str.length;
                    var lNumberOfWords_temp1 = lMessageLength + 8;
                    var lNumberOfWords_temp2 = (lNumberOfWords_temp1 - (lNumberOfWords_temp1 % 64)) / 64;
                    var lNumberOfWords = (lNumberOfWords_temp2 + 1) * 16;
                    var lWordArray = new Array(lNumberOfWords - 1);
                    var lBytePosition = 0;
                    var lByteCount = 0;
                    while (lByteCount < lMessageLength) {
                        lWordCount = (lByteCount - (lByteCount % 4)) / 4;
                        lBytePosition = (lByteCount % 4) * 8;
                        lWordArray[lWordCount] = (lWordArray[lWordCount] | (str.charCodeAt(lByteCount) << lBytePosition));
                        lByteCount++;
                    }
                    lWordCount = (lByteCount - (lByteCount % 4)) / 4;
                    lBytePosition = (lByteCount % 4) * 8;
                    lWordArray[lWordCount] = lWordArray[lWordCount] | (0x80 << lBytePosition);
                    lWordArray[lNumberOfWords - 2] = lMessageLength << 3;
                    lWordArray[lNumberOfWords - 1] = lMessageLength >>> 29;
                    return lWordArray;
                };

                var wordToHex = function (lValue) {
                    var wordToHexValue = '',
                        wordToHexValue_temp = '',
                        lByte, lCount;
                    for (lCount = 0; lCount <= 3; lCount++) {
                        lByte = (lValue >>> (lCount * 8)) & 255;
                        wordToHexValue_temp = '0' + lByte.toString(16);
                        wordToHexValue = wordToHexValue + wordToHexValue_temp.substr(wordToHexValue_temp.length - 2, 2);
                    }
                    return wordToHexValue;
                };

                var x = [],
                    k, AA, BB, CC, DD, a, b, c, d, S11 = 7,
                    S12 = 12,
                    S13 = 17,
                    S14 = 22,
                    S21 = 5,
                    S22 = 9,
                    S23 = 14,
                    S24 = 20,
                    S31 = 4,
                    S32 = 11,
                    S33 = 16,
                    S34 = 23,
                    S41 = 6,
                    S42 = 10,
                    S43 = 15,
                    S44 = 21;

                str = jQuery.crypt.utf8.encode(str);
                x = convertToWordArray(str);
                a = 0x67452301;
                b = 0xEFCDAB89;
                c = 0x98BADCFE;
                d = 0x10325476;

                xl = x.length;
                for (k = 0; k < xl; k += 16) {
                    AA = a;
                    BB = b;
                    CC = c;
                    DD = d;
                    a = _FF(a, b, c, d, x[k + 0], S11, 0xD76AA478);
                    d = _FF(d, a, b, c, x[k + 1], S12, 0xE8C7B756);
                    c = _FF(c, d, a, b, x[k + 2], S13, 0x242070DB);
                    b = _FF(b, c, d, a, x[k + 3], S14, 0xC1BDCEEE);
                    a = _FF(a, b, c, d, x[k + 4], S11, 0xF57C0FAF);
                    d = _FF(d, a, b, c, x[k + 5], S12, 0x4787C62A);
                    c = _FF(c, d, a, b, x[k + 6], S13, 0xA8304613);
                    b = _FF(b, c, d, a, x[k + 7], S14, 0xFD469501);
                    a = _FF(a, b, c, d, x[k + 8], S11, 0x698098D8);
                    d = _FF(d, a, b, c, x[k + 9], S12, 0x8B44F7AF);
                    c = _FF(c, d, a, b, x[k + 10], S13, 0xFFFF5BB1);
                    b = _FF(b, c, d, a, x[k + 11], S14, 0x895CD7BE);
                    a = _FF(a, b, c, d, x[k + 12], S11, 0x6B901122);
                    d = _FF(d, a, b, c, x[k + 13], S12, 0xFD987193);
                    c = _FF(c, d, a, b, x[k + 14], S13, 0xA679438E);
                    b = _FF(b, c, d, a, x[k + 15], S14, 0x49B40821);
                    a = _GG(a, b, c, d, x[k + 1], S21, 0xF61E2562);
                    d = _GG(d, a, b, c, x[k + 6], S22, 0xC040B340);
                    c = _GG(c, d, a, b, x[k + 11], S23, 0x265E5A51);
                    b = _GG(b, c, d, a, x[k + 0], S24, 0xE9B6C7AA);
                    a = _GG(a, b, c, d, x[k + 5], S21, 0xD62F105D);
                    d = _GG(d, a, b, c, x[k + 10], S22, 0x2441453);
                    c = _GG(c, d, a, b, x[k + 15], S23, 0xD8A1E681);
                    b = _GG(b, c, d, a, x[k + 4], S24, 0xE7D3FBC8);
                    a = _GG(a, b, c, d, x[k + 9], S21, 0x21E1CDE6);
                    d = _GG(d, a, b, c, x[k + 14], S22, 0xC33707D6);
                    c = _GG(c, d, a, b, x[k + 3], S23, 0xF4D50D87);
                    b = _GG(b, c, d, a, x[k + 8], S24, 0x455A14ED);
                    a = _GG(a, b, c, d, x[k + 13], S21, 0xA9E3E905);
                    d = _GG(d, a, b, c, x[k + 2], S22, 0xFCEFA3F8);
                    c = _GG(c, d, a, b, x[k + 7], S23, 0x676F02D9);
                    b = _GG(b, c, d, a, x[k + 12], S24, 0x8D2A4C8A);
                    a = _HH(a, b, c, d, x[k + 5], S31, 0xFFFA3942);
                    d = _HH(d, a, b, c, x[k + 8], S32, 0x8771F681);
                    c = _HH(c, d, a, b, x[k + 11], S33, 0x6D9D6122);
                    b = _HH(b, c, d, a, x[k + 14], S34, 0xFDE5380C);
                    a = _HH(a, b, c, d, x[k + 1], S31, 0xA4BEEA44);
                    d = _HH(d, a, b, c, x[k + 4], S32, 0x4BDECFA9);
                    c = _HH(c, d, a, b, x[k + 7], S33, 0xF6BB4B60);
                    b = _HH(b, c, d, a, x[k + 10], S34, 0xBEBFBC70);
                    a = _HH(a, b, c, d, x[k + 13], S31, 0x289B7EC6);
                    d = _HH(d, a, b, c, x[k + 0], S32, 0xEAA127FA);
                    c = _HH(c, d, a, b, x[k + 3], S33, 0xD4EF3085);
                    b = _HH(b, c, d, a, x[k + 6], S34, 0x4881D05);
                    a = _HH(a, b, c, d, x[k + 9], S31, 0xD9D4D039);
                    d = _HH(d, a, b, c, x[k + 12], S32, 0xE6DB99E5);
                    c = _HH(c, d, a, b, x[k + 15], S33, 0x1FA27CF8);
                    b = _HH(b, c, d, a, x[k + 2], S34, 0xC4AC5665);
                    a = _II(a, b, c, d, x[k + 0], S41, 0xF4292244);
                    d = _II(d, a, b, c, x[k + 7], S42, 0x432AFF97);
                    c = _II(c, d, a, b, x[k + 14], S43, 0xAB9423A7);
                    b = _II(b, c, d, a, x[k + 5], S44, 0xFC93A039);
                    a = _II(a, b, c, d, x[k + 12], S41, 0x655B59C3);
                    d = _II(d, a, b, c, x[k + 3], S42, 0x8F0CCC92);
                    c = _II(c, d, a, b, x[k + 10], S43, 0xFFEFF47D);
                    b = _II(b, c, d, a, x[k + 1], S44, 0x85845DD1);
                    a = _II(a, b, c, d, x[k + 8], S41, 0x6FA87E4F);
                    d = _II(d, a, b, c, x[k + 15], S42, 0xFE2CE6E0);
                    c = _II(c, d, a, b, x[k + 6], S43, 0xA3014314);
                    b = _II(b, c, d, a, x[k + 13], S44, 0x4E0811A1);
                    a = _II(a, b, c, d, x[k + 4], S41, 0xF7537E82);
                    d = _II(d, a, b, c, x[k + 11], S42, 0xBD3AF235);
                    c = _II(c, d, a, b, x[k + 2], S43, 0x2AD7D2BB);
                    b = _II(b, c, d, a, x[k + 9], S44, 0xEB86D391);
                    a = addUnsigned(a, AA);
                    b = addUnsigned(b, BB);
                    c = addUnsigned(c, CC);
                    d = addUnsigned(d, DD);
                }

                var temp = wordToHex(a) + wordToHex(b) + wordToHex(c) + wordToHex(d);

                return temp.toLowerCase();
            },
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
        }
    });




    var sprintf_regex = {
        not_string: /[^s]/,
        number: /[dief]/,
        text: /^[^\x25]+/,
        modulo: /^\x25{2}/,
        placeholder: /^\x25(?:([1-9]\d*)\$|\(([^\)]+)\))?(\+)?(0|'[^$])?(-)?(\d+)?(?:\.(\d+))?([b-fiosuxX])/,
        key: /^([a-z_][a-z_\d]*)/i,
        key_access: /^\.([a-z_][a-z_\d]*)/i,
        index_access: /^\[(\d+)\]/,
        sign: /^[\+\-]/
    }

    function sprintf() {
        var key = arguments[0], cache = sprintf.cache
        if (!(cache[key] && cache.hasOwnProperty(key))) {
            cache[key] = sprintf.parse(key)
        }
        return sprintf.format.call(null, cache[key], arguments)
    }

    sprintf.format = function (parse_tree, argv) {
        var cursor = 1, tree_length = parse_tree.length, node_type = "", arg, output = [], i, k, match, pad, pad_character, pad_length, is_positive = true, sign = ""
        for (i = 0; i < tree_length; i++) {
            node_type = sprintf_get_type(parse_tree[i])
            if (node_type === "string") {
                output[output.length] = parse_tree[i]
            }
            else if (node_type === "array") {
                match = parse_tree[i] // convenience purposes only
                if (match[2]) { // keyword argument
                    arg = argv[cursor]
                    for (k = 0; k < match[2].length; k++) {
                        if (!arg.hasOwnProperty(match[2][k])) {
                            throw new Error(sprintf("[sprintf] property '%s' does not exist", match[2][k]))
                        }
                        arg = arg[match[2][k]]
                    }
                }
                else if (match[1]) { // positional argument (explicit)
                    arg = argv[match[1]]
                }
                else { // positional argument (implicit)
                    arg = argv[cursor++]
                }

                if (sprintf_get_type(arg) == "function") {
                    arg = arg()
                }

                if (sprintf_regex.not_string.test(match[8]) && (sprintf_get_type(arg) != "number" && isNaN(arg))) {
                    throw new TypeError(sprintf("[sprintf] expecting number but found %s", sprintf_get_type(arg)))
                }

                if (sprintf_regex.number.test(match[8])) {
                    is_positive = arg >= 0
                }

                switch (match[8]) {
                    case "b":
                        arg = arg.toString(2)
                        break
                    case "c":
                        arg = String.fromCharCode(arg)
                        break
                    case "d":
                    case "i":
                        arg = parseInt(arg, 10)
                        break
                    case "e":
                        arg = match[7] ? arg.toExponential(match[7]) : arg.toExponential()
                        break
                    case "f":
                        arg = match[7] ? parseFloat(arg).toFixed(match[7]) : parseFloat(arg)
                        break
                    case "o":
                        arg = arg.toString(8)
                        break
                    case "s":
                        arg = ((arg = String(arg)) && match[7] ? arg.substring(0, match[7]) : arg)
                        break
                    case "u":
                        arg = arg >>> 0
                        break
                    case "x":
                        arg = arg.toString(16)
                        break
                    case "X":
                        arg = arg.toString(16).toUpperCase()
                        break
                }
                if (sprintf_regex.number.test(match[8]) && (!is_positive || match[3])) {
                    sign = is_positive ? "+" : "-"
                    arg = arg.toString().replace(sprintf_regex.sign, "")
                }
                else {
                    sign = ""
                }
                pad_character = match[4] ? match[4] === "0" ? "0" : match[4].charAt(1) : " "
                pad_length = match[6] - (sign + arg).length
                pad = match[6] ? (pad_length > 0 ? sprintf_str_repeat(pad_character, pad_length) : "") : ""
                output[output.length] = match[5] ? sign + arg + pad : (pad_character === "0" ? sign + pad + arg : pad + sign + arg)
            }
        }
        return output.join("")
    }

    sprintf.cache = {}

    sprintf.parse = function (fmt) {
        var _fmt = fmt, match = [], parse_tree = [], arg_names = 0
        while (_fmt) {
            if ((match = sprintf_regex.text.exec(_fmt)) !== null) {
                parse_tree[parse_tree.length] = match[0]
            }
            else if ((match = sprintf_regex.modulo.exec(_fmt)) !== null) {
                parse_tree[parse_tree.length] = "%"
            }
            else if ((match = sprintf_regex.placeholder.exec(_fmt)) !== null) {
                if (match[2]) {
                    arg_names |= 1
                    var field_list = [], replacement_field = match[2], field_match = []
                    if ((field_match = sprintf_regex.key.exec(replacement_field)) !== null) {
                        field_list[field_list.length] = field_match[1]
                        while ((replacement_field = replacement_field.substring(field_match[0].length)) !== "") {
                            if ((field_match = sprintf_regex.key_access.exec(replacement_field)) !== null) {
                                field_list[field_list.length] = field_match[1]
                            }
                            else if ((field_match = sprintf_regex.index_access.exec(replacement_field)) !== null) {
                                field_list[field_list.length] = field_match[1]
                            }
                            else {
                                throw new SyntaxError("[sprintf] failed to parse named argument key")
                            }
                        }
                    }
                    else {
                        throw new SyntaxError("[sprintf] failed to parse named argument key")
                    }
                    match[2] = field_list
                }
                else {
                    arg_names |= 2
                }
                if (arg_names === 3) {
                    throw new Error("[sprintf] mixing positional and named placeholders is not (yet) supported")
                }
                parse_tree[parse_tree.length] = match
            }
            else {
                throw new SyntaxError("[sprintf] unexpected placeholder")
            }
            _fmt = _fmt.substring(match[0].length)
        }
        return parse_tree
    }

    var vsprintf = function (fmt, argv, _argv) {
        _argv = (argv || []).slice(0)
        _argv.splice(0, 0, fmt)
        return sprintf.apply(null, _argv)
    }

    function sprintf_get_type(variable) {
        return Object.prototype.toString.call(variable).slice(8, -1).toLowerCase()
    }

    function sprintf_str_repeat(input, multiplier) {
        return Array(multiplier + 1).join(input)
    }

    radic.extend({
        sprintf: sprintf,
        vsprintf: vsprintf
    });


    function wordwrap(str, width, spaceReplacer) {
        if (str.length>width) {
            str = str.substr(0, width) + spaceReplacer;
        }
        return str;
    }

    radic.extend({ wordwrap: wordwrap })


    radic.async = {};
var only_once = function (fn) {
        var called = false;
        return function () {
            if (called) throw new Error("Callback was already called.");
            called = true;
            fn.apply(window, arguments);
        }
    }

var _each = function(arr, iterator) {
        if (arr.forEach) {
            return arr.forEach(iterator);
        }
        for (var i = 0; i < arr.length; i += 1) {
            iterator(arr[i], i, arr);
        }
    }



    var each = function (arr, iterator, callback) {
        callback = callback || function () {
        };

        if (!arr.length) {
            return callback();
        }
        var completed = 0;
        _each(arr, function (x) {
            iterator(x, only_once(done));
        });
        function done(err) {
            if (err) {
                callback(err);
                callback = function () {
                };
            }
            else {
                completed += 1;
                if (completed >= arr.length) {
                    callback();
                }
            }
        }
    };

 //   jQuery.async = {};
    radic.async.each = each;
var makeIterator = function (tasks) {
        var makeCallback = function (index) {
            var fn = function () {
                if (tasks.length) {
                    tasks[index].apply(null, arguments);
                }
                return fn.next();
            };
            fn.next = function () {
                return (index < tasks.length - 1) ? makeCallback(index + 1) : null;
            };
            return fn;
        };
        return makeCallback(0);
    }

var nextTick = function (fn) {
        if (typeof setImmediate === 'function') {
            setImmediate(fn);
        } else if (typeof process !== 'undefined' && process.nextTick) {
            process.nextTick(fn);
        } else {
            setTimeout(fn, 0);
        }
    }





    var waterfall = function (tasks, callback) {
        callback = callback || function () {
        };

        var _isArray = Array.isArray || function (maybeArray) {
                return Object.prototype.toString.call(maybeArray) === '[object Array]';
            };

        if (!_isArray(tasks)) {
            var err = new Error('First argument to waterfall must be an array of functions');
            return callback(err);
        }
        if (!tasks.length) {
            return callback();
        }
        var wrapIterator = function (iterator) {
            return function (err) {
                if (err) {
                    callback.apply(null, arguments);
                    callback = function () {
                    };
                } else {
                    var args = Array.prototype.slice.call(arguments, 1);
                    var next = iterator.next();
                    if (next) {
                        args.push(wrapIterator(next));
                    } else {
                        args.push(callback);
                    }
                    nextTick(function () {
                        iterator.apply(null, args);
                    });
                }
            };
        };
        wrapIterator(makeIterator(tasks))();
    };

    radic.async.waterfall = waterfall;





    var json = {};
    json.stringify = function (obj) {

        return JSON.stringify(obj, function (key, value) {
            if (value instanceof Function || typeof value == 'function') {
                return value.toString();
            }
            if (value instanceof RegExp) {
                return '_PxEgEr_' + value;
            }
            return value;
        });
    };

    json.parse = function (str, date2obj) {

        var iso8061 = date2obj ? /^(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2}(?:\.\d*)?)Z$/ : false;

        return JSON.parse(str, function (key, value) {
            var prefix;

            if (typeof value != 'string') {
                return value;
            }
            if (value.length < 8) {
                return value;
            }

            prefix = value.substring(0, 8);

            if (iso8061 && value.match(iso8061)) {
                return new Date(value);
            }
            if (prefix === 'function') {
                return eval('(' + value + ')');
            }
            if (prefix === '_PxEgEr_') {
                return eval(value.slice(8));
            }

            return value;
        });
    };

    json.clone = function (obj, date2obj) {
        return json.parse(json.stringify(obj), date2obj);
    };

    radic.extend({
        json: json
    });


    function getDomain() {
        var d = document.domain;
        if (d.substring(0, 4) == "www.") d = d.substring(4, d.length);
        var a = d.split(".");
        var len = a.length;
        if (len < 3) return d;
        var e = a[len - 1];
        if (e.length < 3) return d;
        d = a[len - 2] + "." + a[len - 1];
        return d;
    }

    function setExpiration(cookieLife) {
        var today = new Date();
        var expr = new Date(today.getTime() + cookieLife * 24 * 60 * 60 * 1000);
        return expr.toGMTString();
    }

    var cookie = {
            options: {
                expire: 2, // day
                path: '/',
                domain: getDomain(),
                secure: '',
                json: false
            },

            get: function (name, config) {

                var options = radic.cloneDeep(this.options);
                $.extend(options, config);

                var expression = new RegExp('(^|; )' + encodeURIComponent(name) + '=(.*?)($|;)'),
                    matches = document.cookie.match(expression),
                    value = matches ? decodeURIComponent(matches[2]) : null;

                if (options.json === true) {
                    try {
                        value = $.parseJSON(value);
                    }
                    catch (e) {
                        value = $.parseJSON('{ data: ' + value + ' }');
                    }
                }

                return value;
            },
            set: function (name, value, config) {
                var options = radic.cloneDeep(this.options);
                $.extend(options, config);
                // console.log(options);

                // JSON OR NOO JSON
                if (typeof value === 'object' && options.json === true) {
                    value = JSON.stringify(value);
                }

                // SUM IT UP FOR CONCAT
                var data = {
                    name: encodeURIComponent(name),
                    value: encodeURIComponent(value),
                    expire: setExpiration(options.expire),
                    domain: options.domain,
                    path: options.path,
                    secure: options.secure
                };

                // ROCKK AND ROLL
                var cookie = sprintf('%(data.name)s=%(data.value)s; expires=%(data.expire)s; path=%(data.path)s; domain=%(data.domain)s;', {data: data}); // Hello Dolly, Molly and Polly
                // console.log(cookie);
                return document.cookie = cookie;
            }
        };

    radic.extend({
        cookie: cookie
    });


    var storage = {};

    storage.on = function (callback) {
        if (window.addEventListener) {
            window.addEventListener("storage", callback, false);
        } else {
            window.attachEvent("onstorage", callback);
        }
    };

    storage.set = function (key, val, options) {
        options = $.extend({json: false, expires: false}, options);
        if (options.json) {
            val = json.stringify(val);
        }
        if(options.expires){
            var now = Math.floor((Date.now() / 1000) / 60);
            window['localStorage'].setItem(key + ':expire', now + expire);
        }
        window['localStorage'].setItem(key, val);
    };

    storage.get = function (key, options) {
        options = $.extend({json: false, default: null}, options);

        if (radic.isUndefined(key)) {
            return options.default;
        }

        if (radic.isString(window['localStorage'].getItem(key))) {
            if (radic.isString(window['localStorage'].getItem(key + ':expire'))) {
                var now = Math.floor((Date.now() / 1000) / 60);
                var expires = parseInt(window['localStorage'].getItem(key + ':expire'));
                if (now > expires) {
                    storage.del(key);
                    storage.del(key + ':expire');
                }
            }
        }

        var val = window['localStorage'].getItem(key);

        if(radic.isUndefined(val)){
            return options.default;
        }

        if (options.json) {
            return json.parse(val);
        }
        return val;
    };

    storage.del = function (key) {
        window['localStorage'].removeItem(key);
    };

    storage.clear = function () {
        window['localStorage'].clear();
    };


    radic.extend({
        storage: storage
    });


    var github = (function(GithubClient){

        return new GithubClient('06ec61fd2853f215bb01f7c5b2e0f56ff8537838'); //'e243a6a733de08c8dfd37e86abd7d2a3b82784de');

    })(function(global, githubRoutes){
        

        // ###########################
        // ### Helpers and globals ###
        // ###########################

        var FP = Function.prototype,
            AP = Array.prototype,
            OP = Object.prototype;

        var bindbind   = FP.bind.bind(FP.bind),
            callbind   = bindbind(FP.bind),
            applybind  = bindbind(FP.apply);

        var has        = callbind(OP.hasOwnProperty),
            slice      = callbind(AP.slice),
            flatten    = applybind(AP.concat, []);

        var filter_    = AP.filter,
            map_       = AP.map,
            push_      = AP.push,
            slice_     = AP.slice;


        function decorate(o){
            var b, c, d;
            for (var i=1; b = arguments[i]; i++) {
                for (c in b) {
                    if (d = Object.getOwnPropertyDescriptor(b, c)) {
                        if (d.get || d.set) {
                            Object.defineProperty(o, c, d);
                        } else {
                            o[c] = d.value;
                        }
                    }
                }
            }
            return o;
        }

        function isObject(o){
            return o != null && typeof o === 'object' || typeof o === 'function';
        }

        function isIndexed(o){
            return Array.isArray(o) || isObject(o) && has(o, 'length') && has(o, o.length - 1);
        }

        // ############
        // ### Path ###
        // ############

        function Path(a){
            if (isIndexed(a)) {
                push_.apply(this, a);
            }
        }

        Path.prototype.length = 0;

        decorate(Path.prototype, {
            join: Array.prototype.join,
            map: Array.prototype.map,
            concat: function concat(){
                var out = new Path(this);
                push_.apply(out, arguments);
                return out;
            },
            args: function args(){
                return filter_.call(this, function(s){
                    return s[0] === 'Δ';
                }).map(function(s){
                    return s.replace(/Δ/g, '');
                });
            },
            toName: function toName(slice, last){
                var array = map_.call(this, function(s){
                    return s.replace(/Δ/g, '');
                });

                if (last) {
                    array.push(last);
                }

                var out = array.slice(slice || 1).map(function(s){
                    return s[0].toUpperCase() + s.slice(1).toLowerCase();
                });

                if (!out[0]) {
                    return '';
                } else {
                    out[0] = out[0].toLowerCase();
                    return out.join('').replace(/_(.)/g, function(s){
                        return s[1].toUpperCase();
                    });
                }
            },
            slice: function slice(){
                return new Path(slice_.apply(this, arguments));
            }
        });


        // #################
        // ### Transport ###
        // #################

        // superclass for XHR and JSONP

        function Transport(options, callback){
            options = options || {};
            if (typeof options === 'string') {
                options = { url: options };
            }
            if (typeof callback === 'function') {
                options.callback = callback;
            }
            this.data = options.data || {};
            this.path = options.path || [];
            this.base = options.url;
            this.callback = options.callback || function(){};
            this.state = 'idle';
        }

        Transport.transports = {};

        decorate(Transport, {
            register: function register(ctor){
                Transport.transports[ctor.name.toLowerCase()] = ctor;
            },
            lookup: function lookup(name){
                name = name.toLowerCase();
                return name in Transport.transports ? Transport.transports[name] : null;
            },
            create: function create(type, base, dispatcher){
                var T = Transport.lookup(type);
                return new T(base, dispatcher);
            }
        });


        decorate(Transport.prototype, {
            params: function params(){
                var data = Object.keys(this.data).map(function(name){ return [name, this.data[name]] }, this);
                data.push([this.callbackParam, this.callbackName]);
                return data.map(function(item){
                    return encodeURIComponent(item[0]) + '=' + encodeURIComponent(item[1]);
                }).join('&');
            }
        });

        // #######################
        // ### JSONP Transport ###
        // #######################

        function JSONP(options, callback){
            Transport.call(this, options = options || {}, callback);
            this.callbackParam = options.callbackParam || 'callback';
            this.callbackName = options.callbackName || '_'+Math.random().toString(36).slice(2);
        }

        Transport.register(JSONP);

        JSONP.prototype = Object.create(Transport.prototype);
        decorate(JSONP.prototype, {
            constructor: JSONP,
            url: function url(){
                return [this.base].concat(this.path).join('/') + '?' + this.params();
            },
            send: function send(callback){
                var script = document.createElement('script'),
                    completed

                callback = callback || this.callback;

                function complete(state, result){
                    if (!completed) {
                        completed = true;
                        delete window[this.callbackName];
                        document.body.removeChild(script);
                        this.state = state;
                        callback.call(this, result);
                    }
                }

                script.src = this.url();
                script.async = script.defer = true;
                script.onerror = complete.bind(this, 'error');
                window[this.callbackName] = complete.bind(this, 'success');

                document.body.appendChild(script);
                this.state = 'loading';
                return this;
            }
        });

        // ################################
        // ### XMLHttpRequest Transport ###
        // ################################

        function XHR(options, callback){
            this.headers = {};
            options = options || {}

            Transport.call(this, options, callback);

            if (options.headers) {
                Object.keys(options.headers).forEach(function(n){
                    this[n] = options.headers[n];
                }, this.headers);
            }
        }

        Transport.register(XHR);

        XHR.prototype = Object.create(Transport.prototype);
        decorate(XHR.prototype, {
            constructor: XHR,
            async: true,
            url: function url(){
                var params = this.params();
                return [this.base].concat(this.path).join('/') + (this.verb === 'get' && params ? '?' + params : '');
            },
            auth: function auth(user, pass){
                if (!pass && user.length === 40) {
                    this.headers.Authorization = 'token '+user;
                } else {
                    this.headers.Authorization = 'Basic '+btoa(user+':'+pass);
                }
            },
            send: function send(callback, verb){
                var xhr = new XMLHttpRequest,
                    self = this;

                if (typeof callback !== 'function') {
                    verb = callback;
                    callback = this.callback;
                }

                function complete(data){
                    if (xhr.readyState === 4) {
                        self.state = 'complete';
                        callback.call(self, JSON.parse(xhr.responseText));
                    }
                }

                xhr.open(verb || 'GET', this.url(), this.async);
                if (this.headers.Authenticate) {
                    xhr.withCredentials = true;
                }

                Object.keys(this.headers).forEach(function(name){
                    xhr.setRequestHeader(name, self.headers[name]);
                });

                xhr.onerror = complete;
                xhr.onload = complete;

                xhr.send(this.data ||  null);
                this.state = 'loading';
                return this.async === true ?  this : xhr.responseText;
            }
        });


        function makeCtor(args, api){
            var Ctor = function(){
                var self = this instanceof Ctor ? this : Object.create(Ctor.prototype);
                return api.request(arguments, args, self);
            }

            decorate(Ctor, {
                args: Object.freeze(args),
                toString: function toString(){ return '[ '+this.args.join(', ')+' ]' }
            });
            return Ctor;
        }

        // #################
        // ### APIClient ###
        // #################

        // generalized REST API handler that turns routes into functions

        function APIClient(routes, onlyGetters){
            var self = this;
            var slices = {};

            function recurse(o,path){
                Object.keys(o).forEach(function(k){
                    if (k === 'SLICE') {
                        slices[path[0]] = o[k];
                    } else if (k.toUpperCase() === k) {
                        if (onlyGetters) {
                            if (k !== 'GET') return;
                            var name = path.toName(slices[path[0]]);
                        } else {
                            var name = path.toName(slices[path[0]], k);
                        }

                        if (name) {
                            var target = self[path[0]] || (self[path[0]] = {});
                        } else {
                            name = path[0];
                            var target = self;
                        }

                        target[name] = makeCtor(path.args().concat(o[k]), self);

                        Object.defineProperty(target[name].prototype, 'path', {
                            get: function(){
                                return path.map(function(s){
                                    return s[0] === 'Δ' ? this[s.slice(1)] : s;
                                }, this).join('/');
                            }
                        });

                    } else if (isObject(o[k])) {
                        recurse(o[k], path.concat(k));
                    }
                });
            }

            recurse(routes, new Path);
        }

        decorate(APIClient.prototype, {
            request: function request(args, fields, req){
                args = [].slice.call(args);
                var callback = typeof args[args.length-1] === 'function' ? args.pop() : this.callback;
                fields.forEach(function(p,i){
                    if (typeof args[i] != null) {
                        req[p] = args[i];
                    }
                });
                var transport = decorate(Object.create(this.transport), {
                    path: req.path,
                    data: req
                });
                transport.send(callback);
                return transport;
            },
            setTransport: function setTransport(type, base, dispatcher){
                Object.defineProperty(this, 'transport', {
                    value: Transport.create(type, base, dispatcher),
                    configurable: true,
                    writable: true
                });
            }
        });


        // ####################
        // ### GithubClient ###
        // ####################

        // APIClient subclass with routes and utilities for Github

        function GithubClient(user, password){
            var self = this;

            function findRefs(obj){
                isObject(obj) && Object.keys(obj).forEach(function(key){
                    if (key !== 'url') return;

                    var val = obj[key].slice(23).split('/');
                    var fn = self[val[0]];
                    if (!fn) return;
                    if (fn[val[1]]) {
                        fn = fn[val[1]];
                        val = val.slice(2);
                    } else {
                        val = val.slice(1);
                    }

                    obj.resolve = function(cb){
                        if (typeof cb === 'function') val.push(cb);
                        return fn.apply(null, val);
                    }.bind(null);

                    if (isObject(obj[key])) {
                        return findRefs(obj[key]);
                    }
                });
            }

            this.setTransport('xhr', 'https://api.github.com', function(result){
                if (result) {
                    findRefs(result);
                    self.lastResult = result;
                }
                if (self.callback) {
                    self.callback.call(self, result);
                }
            });

            this.transport.headers.Accept = 'application/vnd.github.full+json';
            if (user) {
                this.transport.auth(user, password);
            }

            APIClient.call(this, githubRoutes, true);
            this.users.search = this.legacy.userSearchKeyword;
            this.users.searchEmails = this.legacy.userEmailEmail;
            this.repos.search = this.legacy.reposSearchKeyword;
            this.repos.searchIssues = this.legacy.issuesSearchOwnerRepositoryStateKeyword;
            delete this.legacy;
        }

        GithubClient.createClient = function createClient(user, pass){
            return new GithubClient(user, pass);
        };

        GithubClient.prototype = Object.create(APIClient.prototype)
        decorate(GithubClient.prototype, {
            constructor: GithubClient
        });

        return GithubClient;

// ########################################
// ### Routes for Github V3 API in full ###
// ########################################

    }(new Function('return this')(), {
        legacy:{SLICE:1,issues:{search:{Δowner:{Δrepository:{Δstate:{Δkeyword:{GET:[]}}}}}},repos:{search:{Δkeyword:{GET:['language','start_page']}}},user:{search:{Δkeyword:{GET:[]}},email:{Δemail:{GET:[]}}}},
        gists:{SLICE:1,POST:['description','public','files'],GET:['page','per_page'],public:{GET:[]},starred:{GET:[]},Δid:{GET:[],PATCH:['description','files'],star:{GET:[],DELETE:[],POST:[]},fork:{POST:[]},comments:{GET:[],POST:['input'],Δid:{GET:[],DELETE:[],PATCH:['body']}}}},
        teams:{SLICE:2,Δid:{GET:[],DELETE:[],PATCH:['name','permission'],members:{GET:['page','per_page'],Δuser:{GET:[],DELETE:[],POST:[]}},repos:{GET:['page','per_page'],Δuser:{Δrepo:{GET:[],DELETE:[],POST:[]}}}}},
        orgs:{SLICE:2,Δorg:{GET:['page','per_page'],PATCH:['billing_email','company','email','location','name'],members:{GET:['page','per_page'],Δuser:{GET:[],DELETE:[]}},public_members:{GET:[],Δuser:{GET:[],DELETE:[],POST:[]}},teams:{GET:[],POST:['name','repo_names','permission']},repos:{GET:['type','page','per_page'],POST:['name','description','homepage','private','has_issues','has_wiki','has_downloads','team_id'],Δsha:{GET:[]}}}},
        repos:{SLICE:3,Δuser:{Δrepo:{GET:[],GET2:['page','per_page'],PATCH:['name','description','homepage','private','has_issues','has_wiki','has_downloads'],contributors:{GET:['anon','page','per_page']},languages:{GET:['anon','page','per_page']},teams:{GET:['page','per_page']},tags:{GET:['page','per_page'],Δsha:{POST:['tag','message','object','type','tagger.name','tagger.email','tagger.date']}},git:{refs:{POST:['refs','sha'],GET:['page','per_page'],Δref:{GET:[],PATCH:['sha','force']}},commits:{POST:['message','tree','parents','author','committer'],Δsha:{GET:[]}},blobs:{POST:['content','encoding'],Δsha:{GET:['page','per_page']}}},
            branches:{GET:['page','per_page']},events:{GET:['page','per_page']},issues:{GET:['milestone','state','assignee','mentioned','labels','sort','direction','since','page','per_page'],POST:['title','body','assignee','milestone','labels'],events:{GET:['page','per_page'],GET2:[],Δid:{}},Δnumber:{GET:[],PATCH:['title','body','assignee','milestone','labels'],comments:{GET:['page','per_page'],POST:['body']},events:{GET:['page','per_page']}},comments:{Δid:{GET:[],DELETE:[],PATCH:['body']}},},pulls:{GET:['state','page','per_page'],POST:['title','body','base','head'],POST2:['issue','base','head'],Δnumber:{GET:[],PATCH:['state','title','body'],merge:{GET:['page','per_page'],POST:['commit_message']},files:{GET:['page','per_page']},commits:{GET:['page','per_page']},
                comments:{POST:['body','in_reply_to'],POST2:['body','commit_id','path','position'],GET:['page','per_page'],}},comments:{Δnumber:{GET:[],DELETE:[],PATCH:['body']}}},commits:{GET:['sha','path','page','per_page'],Δsha:{GET:[],comments:{GET:['page','per_page'],POST:['body','commit_id','line','path','position']}},},comments:{Δid:{GET:[],DELETE:[],PATCH:['body']}},compare:{ΔbaseΔhead:{GET:['base','head']}},download:{GET:['page','per_page']},downloads:{Δid:{GET:[],DELETE:[]}},forks:{POST:['org'],GET:['sort','page','per_page']},labels:{GET:[],POST:['name','color'],Δname:{GET:[],POST:['color']}},keys:{GET:['page','per_page'],POST:['title','key'],Δid:{GET:[],DELETE:[],POST:['title','key']}},watchers:{GET:['page','per_page']},
            hooks:{GET:['page','per_page'],POST:['name','config','events','active'],Δid:{GET:[],DELETE:[],PATCH:['name','config','events','add_events','remove_events','active'],test:{POST:[]}}},milestones:{POST:['title','state','description','due_on'],GET:['state','sort','page','per_page'],Δnumber:{DELETE:[],GET:[],PATCH:['title','state','description','due_on']}},trees:{POST:['tree'],Δsha:{GET:['recursive']}},collaborators:{GET:['page','per_page'],Δcollabuser:{GET:[],DELETE:[],POST:[]}}}}},
        authorizations:{SLICE:0,GET:[]},
        user:{SLICE:1,GET:[],PATCH:['name','email','blog','company','location','hireable','bio'],gists:{GET:['page','per_page']},emails:{GET:['page','per_page'],DELETE:[],POST:[]},following:{GET:['page','per_page'],Δuser:{GET:['page','per_page'],DELETE:[],POST:[]}},watched:{GET:['page','per_page'],Δuser:{Δrepo:{GET:['page','per_page'],DELETE:[],POST:[]}}},keys:{GET:['page','per_page'],POST:['title','key'],Δid:{GET:[],DELETE:[],PATCH:['title','key']}},repos:{GET:['type','page','per_page'],POST:['name','description','homepage','private','has_issues','has_wiki','has_downloads']}},
        users:{SLICE:2,Δuser:{GET:[],gists:{GET:['page','per_page']},followers:{GET:['page','per_page']},following:{GET:['page','per_page']},orgs:{GET:['page','per_page']},watched:{GET:['page','per_page']},received_events:{GET:['page','per_page']},events:{GET:['page','per_page']},repos:{GET:['type','page','per_page']}}},
        networks:{SLICE:2,Δuser:{Δrepo:{events:{GET:['page','per_page']}},events:{orgs:{Δorg:{GET:['page','per_page']}}}}},
        events:{SLICE:1,GET:['page','per_page']}
    }));




    radic.extend({
        github: github
    });



// handlebars/safe-string.js
    var __module3__ = (function() {
        
        var __exports__;
        // Build out our basic SafeString type
        function SafeString(string) {
            this.string = string;
        }

        SafeString.prototype.toString = function() {
            return "" + this.string;
        };

        __exports__ = SafeString;
        return __exports__;
    })();

// handlebars/utils.js
    var __module2__ = (function(__dependency1__) {
        
        var __exports__ = {};
        /*jshint -W004 */
        var SafeString = __dependency1__;

        var escape = {
            "&": "&amp;",
            "<": "&lt;",
            ">": "&gt;",
            '"': "&quot;",
            "'": "&#x27;",
            "`": "&#x60;"
        };

        var badChars = /[&<>"'`]/g;
        var possible = /[&<>"'`]/;

        function escapeChar(chr) {
            return escape[chr];
        }

        function extend(obj /* , ...source */) {
            for (var i = 1; i < arguments.length; i++) {
                for (var key in arguments[i]) {
                    if (Object.prototype.hasOwnProperty.call(arguments[i], key)) {
                        obj[key] = arguments[i][key];
                    }
                }
            }

            return obj;
        }

        __exports__.extend = extend;var toString = Object.prototype.toString;
        __exports__.toString = toString;
        // Sourced from lodash
        // https://github.com/bestiejs/lodash/blob/master/LICENSE.txt
        var isFunction = function(value) {
            return typeof value === 'function';
        };
        // fallback for older versions of Chrome and Safari
        /* istanbul ignore next */
        if (isFunction(/x/)) {
            isFunction = function(value) {
                return typeof value === 'function' && toString.call(value) === '[object Function]';
            };
        }
        var isFunction;
        __exports__.isFunction = isFunction;
        /* istanbul ignore next */
        var isArray = Array.isArray || function(value) {
                return (value && typeof value === 'object') ? toString.call(value) === '[object Array]' : false;
            };
        __exports__.isArray = isArray;

        function escapeExpression(string) {
            // don't escape SafeStrings, since they're already safe
            if (string instanceof SafeString) {
                return string.toString();
            } else if (string == null) {
                return "";
            } else if (!string) {
                return string + '';
            }

            // Force a string conversion as this will be done by the append regardless and
            // the regex test will do this transparently behind the scenes, causing issues if
            // an object's to string has escaped characters in it.
            string = "" + string;

            if(!possible.test(string)) { return string; }
            return string.replace(badChars, escapeChar);
        }

        __exports__.escapeExpression = escapeExpression;function isEmpty(value) {
            if (!value && value !== 0) {
                return true;
            } else if (isArray(value) && value.length === 0) {
                return true;
            } else {
                return false;
            }
        }

        __exports__.isEmpty = isEmpty;function appendContextPath(contextPath, id) {
            return (contextPath ? contextPath + '.' : '') + id;
        }

        __exports__.appendContextPath = appendContextPath;
        return __exports__;
    })(__module3__);

// handlebars/exception.js
    var __module4__ = (function() {
        
        var __exports__;

        var errorProps = ['description', 'fileName', 'lineNumber', 'message', 'name', 'number', 'stack'];

        function Exception(message, node) {
            var line;
            if (node && node.firstLine) {
                line = node.firstLine;

                message += ' - ' + line + ':' + node.firstColumn;
            }

            var tmp = Error.prototype.constructor.call(this, message);

            // Unfortunately errors are not enumerable in Chrome (at least), so `for prop in tmp` doesn't work.
            for (var idx = 0; idx < errorProps.length; idx++) {
                this[errorProps[idx]] = tmp[errorProps[idx]];
            }

            if (line) {
                this.lineNumber = line;
                this.column = node.firstColumn;
            }
        }

        Exception.prototype = new Error();

        __exports__ = Exception;
        return __exports__;
    })();

// handlebars/base.js
    var __module1__ = (function(__dependency1__, __dependency2__) {
        
        var __exports__ = {};
        var Utils = __dependency1__;
        var Exception = __dependency2__;

        var VERSION = "2.0.0";
        __exports__.VERSION = VERSION;var COMPILER_REVISION = 6;
        __exports__.COMPILER_REVISION = COMPILER_REVISION;
        var REVISION_CHANGES = {
            1: '<= 1.0.rc.2', // 1.0.rc.2 is actually rev2 but doesn't report it
            2: '== 1.0.0-rc.3',
            3: '== 1.0.0-rc.4',
            4: '== 1.x.x',
            5: '== 2.0.0-alpha.x',
            6: '>= 2.0.0-beta.1'
        };
        __exports__.REVISION_CHANGES = REVISION_CHANGES;
        var isArray = Utils.isArray,
            isFunction = Utils.isFunction,
            toString = Utils.toString,
            objectType = '[object Object]';

        function HandlebarsEnvironment(helpers, partials) {
            this.helpers = helpers || {};
            this.partials = partials || {};

            registerDefaultHelpers(this);
        }

        __exports__.HandlebarsEnvironment = HandlebarsEnvironment;HandlebarsEnvironment.prototype = {
            constructor: HandlebarsEnvironment,

            logger: logger,
            log: log,

            registerHelper: function(name, fn) {
                if (toString.call(name) === objectType) {
                    if (fn) { throw new Exception('Arg not supported with multiple helpers'); }
                    Utils.extend(this.helpers, name);
                } else {
                    this.helpers[name] = fn;
                }
            },
            unregisterHelper: function(name) {
                delete this.helpers[name];
            },

            registerPartial: function(name, partial) {
                if (toString.call(name) === objectType) {
                    Utils.extend(this.partials,  name);
                } else {
                    this.partials[name] = partial;
                }
            },
            unregisterPartial: function(name) {
                delete this.partials[name];
            }
        };

        function registerDefaultHelpers(instance) {
            instance.registerHelper('helperMissing', function(/* [args, ]options */) {
                if(arguments.length === 1) {
                    // A missing field in a {{foo}} constuct.
                    return undefined;
                } else {
                    // Someone is actually trying to call something, blow up.
                    throw new Exception("Missing helper: '" + arguments[arguments.length-1].name + "'");
                }
            });

            instance.registerHelper('blockHelperMissing', function(context, options) {
                var inverse = options.inverse,
                    fn = options.fn;

                if(context === true) {
                    return fn(this);
                } else if(context === false || context == null) {
                    return inverse(this);
                } else if (isArray(context)) {
                    if(context.length > 0) {
                        if (options.ids) {
                            options.ids = [options.name];
                        }

                        return instance.helpers.each(context, options);
                    } else {
                        return inverse(this);
                    }
                } else {
                    if (options.data && options.ids) {
                        var data = createFrame(options.data);
                        data.contextPath = Utils.appendContextPath(options.data.contextPath, options.name);
                        options = {data: data};
                    }

                    return fn(context, options);
                }
            });

            instance.registerHelper('each', function(context, options) {
                if (!options) {
                    throw new Exception('Must pass iterator to #each');
                }

                var fn = options.fn, inverse = options.inverse;
                var i = 0, ret = "", data;

                var contextPath;
                if (options.data && options.ids) {
                    contextPath = Utils.appendContextPath(options.data.contextPath, options.ids[0]) + '.';
                }

                if (isFunction(context)) { context = context.call(this); }

                if (options.data) {
                    data = createFrame(options.data);
                }

                if(context && typeof context === 'object') {
                    if (isArray(context)) {
                        for(var j = context.length; i<j; i++) {
                            if (data) {
                                data.index = i;
                                data.first = (i === 0);
                                data.last  = (i === (context.length-1));

                                if (contextPath) {
                                    data.contextPath = contextPath + i;
                                }
                            }
                            ret = ret + fn(context[i], { data: data });
                        }
                    } else {
                        for(var key in context) {
                            if(context.hasOwnProperty(key)) {
                                if(data) {
                                    data.key = key;
                                    data.index = i;
                                    data.first = (i === 0);

                                    if (contextPath) {
                                        data.contextPath = contextPath + key;
                                    }
                                }
                                ret = ret + fn(context[key], {data: data});
                                i++;
                            }
                        }
                    }
                }

                if(i === 0){
                    ret = inverse(this);
                }

                return ret;
            });

            instance.registerHelper('if', function(conditional, options) {
                if (isFunction(conditional)) { conditional = conditional.call(this); }

                // Default behavior is to render the positive path if the value is truthy and not empty.
                // The `includeZero` option may be set to treat the condtional as purely not empty based on the
                // behavior of isEmpty. Effectively this determines if 0 is handled by the positive path or negative.
                if ((!options.hash.includeZero && !conditional) || Utils.isEmpty(conditional)) {
                    return options.inverse(this);
                } else {
                    return options.fn(this);
                }
            });

            instance.registerHelper('unless', function(conditional, options) {
                return instance.helpers['if'].call(this, conditional, {fn: options.inverse, inverse: options.fn, hash: options.hash});
            });

            instance.registerHelper('with', function(context, options) {
                if (isFunction(context)) { context = context.call(this); }

                var fn = options.fn;

                if (!Utils.isEmpty(context)) {
                    if (options.data && options.ids) {
                        var data = createFrame(options.data);
                        data.contextPath = Utils.appendContextPath(options.data.contextPath, options.ids[0]);
                        options = {data:data};
                    }

                    return fn(context, options);
                } else {
                    return options.inverse(this);
                }
            });

            instance.registerHelper('log', function(message, options) {
                var level = options.data && options.data.level != null ? parseInt(options.data.level, 10) : 1;
                instance.log(level, message);
            });

            instance.registerHelper('lookup', function(obj, field) {
                return obj && obj[field];
            });
        }

        var logger = {
            methodMap: { 0: 'debug', 1: 'info', 2: 'warn', 3: 'error' },

            // State enum
            DEBUG: 0,
            INFO: 1,
            WARN: 2,
            ERROR: 3,
            level: 3,

            // can be overridden in the host environment
            log: function(level, message) {
                if (logger.level <= level) {
                    var method = logger.methodMap[level];
                    if (typeof console !== 'undefined' && console[method]) {
                        console[method].call(console, message);
                    }
                }
            }
        };
        __exports__.logger = logger;
        var log = logger.log;
        __exports__.log = log;
        var createFrame = function(object) {
            var frame = Utils.extend({}, object);
            frame._parent = object;
            return frame;
        };
        __exports__.createFrame = createFrame;
        return __exports__;
    })(__module2__, __module4__);

// handlebars/runtime.js
    var __module5__ = (function(__dependency1__, __dependency2__, __dependency3__) {
        
        var __exports__ = {};
        var Utils = __dependency1__;
        var Exception = __dependency2__;
        var COMPILER_REVISION = __dependency3__.COMPILER_REVISION;
        var REVISION_CHANGES = __dependency3__.REVISION_CHANGES;
        var createFrame = __dependency3__.createFrame;

        function checkRevision(compilerInfo) {
            var compilerRevision = compilerInfo && compilerInfo[0] || 1,
                currentRevision = COMPILER_REVISION;

            if (compilerRevision !== currentRevision) {
                if (compilerRevision < currentRevision) {
                    var runtimeVersions = REVISION_CHANGES[currentRevision],
                        compilerVersions = REVISION_CHANGES[compilerRevision];
                    throw new Exception("Template was precompiled with an older version of Handlebars than the current runtime. "+
                    "Please update your precompiler to a newer version ("+runtimeVersions+") or downgrade your runtime to an older version ("+compilerVersions+").");
                } else {
                    // Use the embedded version info since the runtime doesn't know about this revision yet
                    throw new Exception("Template was precompiled with a newer version of Handlebars than the current runtime. "+
                    "Please update your runtime to a newer version ("+compilerInfo[1]+").");
                }
            }
        }

        __exports__.checkRevision = checkRevision;// TODO: Remove this line and break up compilePartial

        function template(templateSpec, env) {
            /* istanbul ignore next */
            if (!env) {
                throw new Exception("No environment passed to template");
            }
            if (!templateSpec || !templateSpec.main) {
                throw new Exception('Unknown template object: ' + typeof templateSpec);
            }

            // Note: Using env.VM references rather than local var references throughout this section to allow
            // for external users to override these as psuedo-supported APIs.
            env.VM.checkRevision(templateSpec.compiler);

            var invokePartialWrapper = function(partial, indent, name, context, hash, helpers, partials, data, depths) {
                if (hash) {
                    context = Utils.extend({}, context, hash);
                }

                var result = env.VM.invokePartial.call(this, partial, name, context, helpers, partials, data, depths);

                if (result == null && env.compile) {
                    var options = { helpers: helpers, partials: partials, data: data, depths: depths };
                    partials[name] = env.compile(partial, { data: data !== undefined, compat: templateSpec.compat }, env);
                    result = partials[name](context, options);
                }
                if (result != null) {
                    if (indent) {
                        var lines = result.split('\n');
                        for (var i = 0, l = lines.length; i < l; i++) {
                            if (!lines[i] && i + 1 === l) {
                                break;
                            }

                            lines[i] = indent + lines[i];
                        }
                        result = lines.join('\n');
                    }
                    return result;
                } else {
                    throw new Exception("The partial " + name + " could not be compiled when running in runtime-only mode");
                }
            };

            // Just add water
            var container = {
                lookup: function(depths, name) {
                    var len = depths.length;
                    for (var i = 0; i < len; i++) {
                        if (depths[i] && depths[i][name] != null) {
                            return depths[i][name];
                        }
                    }
                },
                lambda: function(current, context) {
                    return typeof current === 'function' ? current.call(context) : current;
                },

                escapeExpression: Utils.escapeExpression,
                invokePartial: invokePartialWrapper,

                fn: function(i) {
                    return templateSpec[i];
                },

                programs: [],
                program: function(i, data, depths) {
                    var programWrapper = this.programs[i],
                        fn = this.fn(i);
                    if (data || depths) {
                        programWrapper = program(this, i, fn, data, depths);
                    } else if (!programWrapper) {
                        programWrapper = this.programs[i] = program(this, i, fn);
                    }
                    return programWrapper;
                },

                data: function(data, depth) {
                    while (data && depth--) {
                        data = data._parent;
                    }
                    return data;
                },
                merge: function(param, common) {
                    var ret = param || common;

                    if (param && common && (param !== common)) {
                        ret = Utils.extend({}, common, param);
                    }

                    return ret;
                },

                noop: env.VM.noop,
                compilerInfo: templateSpec.compiler
            };

            var ret = function(context, options) {
                options = options || {};
                var data = options.data;

                ret._setup(options);
                if (!options.partial && templateSpec.useData) {
                    data = initData(context, data);
                }
                var depths;
                if (templateSpec.useDepths) {
                    depths = options.depths ? [context].concat(options.depths) : [context];
                }

                return templateSpec.main.call(container, context, container.helpers, container.partials, data, depths);
            };
            ret.isTop = true;

            ret._setup = function(options) {
                if (!options.partial) {
                    container.helpers = container.merge(options.helpers, env.helpers);

                    if (templateSpec.usePartial) {
                        container.partials = container.merge(options.partials, env.partials);
                    }
                } else {
                    container.helpers = options.helpers;
                    container.partials = options.partials;
                }
            };

            ret._child = function(i, data, depths) {
                if (templateSpec.useDepths && !depths) {
                    throw new Exception('must pass parent depths');
                }

                return program(container, i, templateSpec[i], data, depths);
            };
            return ret;
        }

        __exports__.template = template;function program(container, i, fn, data, depths) {
            var prog = function(context, options) {
                options = options || {};

                return fn.call(container, context, container.helpers, container.partials, options.data || data, depths && [context].concat(depths));
            };
            prog.program = i;
            prog.depth = depths ? depths.length : 0;
            return prog;
        }

        __exports__.program = program;function invokePartial(partial, name, context, helpers, partials, data, depths) {
            var options = { partial: true, helpers: helpers, partials: partials, data: data, depths: depths };

            if(partial === undefined) {
                throw new Exception("The partial " + name + " could not be found");
            } else if(partial instanceof Function) {
                return partial(context, options);
            }
        }

        __exports__.invokePartial = invokePartial;function noop() { return ""; }

        __exports__.noop = noop;function initData(context, data) {
            if (!data || !('root' in data)) {
                data = data ? createFrame(data) : {};
                data.root = context;
            }
            return data;
        }
        return __exports__;
    })(__module2__, __module4__, __module1__);

// handlebars.runtime.js
    var __module0__ = (function(__dependency1__, __dependency2__, __dependency3__, __dependency4__, __dependency5__) {
        
        var __exports__;
        /*globals Handlebars: true */
        var base = __dependency1__;

        // Each of these augment the Handlebars object. No need to setup here.
        // (This is done to easily share code between commonjs and browse envs)
        var SafeString = __dependency2__;
        var Exception = __dependency3__;
        var Utils = __dependency4__;
        var runtime = __dependency5__;

        // For compatibility and usage outside of module systems, make the Handlebars object a namespace
        var create = function() {
            var hb = new base.HandlebarsEnvironment();

            Utils.extend(hb, base);
            hb.SafeString = SafeString;
            hb.Exception = Exception;
            hb.Utils = Utils;
            hb.escapeExpression = Utils.escapeExpression;

            hb.VM = runtime;
            hb.template = function(spec) {
                return runtime.template(spec, hb);
            };

            return hb;
        };

        var Handlebars = create();
        Handlebars.create = create;

        Handlebars['default'] = Handlebars;

        __exports__ = Handlebars;
        return __exports__;
    })(__module1__, __module3__, __module4__, __module2__, __module5__);

    radic.template = __module0__;
    radic.template.get = function(name, data){
        var template = radic._template.templates[name];
        if(radic.isUndefined(data)){
            return template;
        }
        var html = template(data);
        return $($(html).html().trim());
    };


    radic.template.registerHelper('default', function (value, defaultValue) {
        return value != null ? value : defaultValue;
    });

    radic.template.registerHelper('arrayIndex', function (context, ndx) {
        return context[ndx];
    });




    radic.template.expressionRegistry = function () {
        var isArray = function (value) {
            return Object.prototype.toString.call(value) === '[object Array]';
        }

        var ExpressionRegistry = function () {
            this.expressions = [];
        };

        ExpressionRegistry.prototype.add = function (operator, method) {
            this.expressions[operator] = method;
        };

        ExpressionRegistry.prototype.call = function (operator, left, right) {
            if (!this.expressions.hasOwnProperty(operator)) {
                throw new Error('Unknown operator "' + operator + '"');
            }

            return this.expressions[operator](left, right);
        };

        var eR = new ExpressionRegistry;
        eR.add('not', function (left, right) {
            return left != right;
        });
        eR.add('>', function (left, right) {
            return left > right;
        });
        eR.add('<', function (left, right) {
            return left < right;
        });
        eR.add('>=', function (left, right) {
            return left >= right;
        });
        eR.add('<=', function (left, right) {
            return left <= right;
        });
        eR.add('===', function (left, right) {
            return left === right;
        });
        eR.add('!==', function (left, right) {
            return left !== right;
        });
        eR.add('in', function (left, right) {
            if (!isArray(right)) {
                right = right.split(',');
            }
            return right.indexOf(left) !== -1;
        });

        var isHelper = function () {
            var args = arguments
                , left = args[0]
                , operator = args[1]
                , right = args[2]
                , options = args[3]
                ;

            if (args.length == 2) {
                options = args[1];
                if (left) return options.fn(this);
                return options.inverse(this);
            }

            if (args.length == 3) {
                right = args[1];
                options = args[2];
                if (left == right) return options.fn(this);
                return options.inverse(this);
            }

            if (eR.call(operator, left, right)) {
                return options.fn(this);
            }
            return options.inverse(this);
        };

        radic.template.registerHelper('is', isHelper);

        radic.template.registerHelper('nl2br', function (text) {
            var nl2br = (text + '').replace(/([^>\r\n]?)(\r\n|\n\r|\r|\n)/g, '$1' + '<br>' + '$2');
            return new radic.template.SafeString(nl2br);
        });

        radic.template.registerHelper('log', function () {
            console.log(['Values:'].concat(
                Array.prototype.slice.call(arguments, 0, -1)
            ));
        });

        radic.template.registerHelper('debug', function () {
            console.log('Context:', this);
            console.log(['Values:'].concat(
                Array.prototype.slice.call(arguments, 0, -1)
            ));
        });

        return eR;
    }();

    radic.template.expressionRegistry.add('same', function (left, right) { return left === right; });




    var widget_uuid = 0,
        widget_slice = Array.prototype.slice;

    jQuery.cleanData = (function( orig ) {
        return function( elems ) {
            var events, elem, i;
            for ( i = 0; (elem = elems[i]) != null; i++ ) {
                try {

                    // Only trigger remove when necessary to save time
                    events = jQuery._data( elem, "events" );
                    if ( events && events.remove ) {
                        jQuery( elem ).triggerHandler( "remove" );
                    }

                    // http://bugs.jquery.com/ticket/8235
                } catch ( e ) {}
            }
            orig( elems );
        };
    })( jQuery.cleanData );

    jQuery.widget = function( name, base, prototype ) {
        var fullName, existingConstructor, constructor, basePrototype,
        // proxiedPrototype allows the provided prototype to remain unmodified
        // so that it can be used as a mixin for multiple widgets (#8876)
            proxiedPrototype = {},
            namespace = name.split( "." )[ 0 ];

        name = name.split( "." )[ 1 ];
        fullName = namespace + "-" + name;

        if ( !prototype ) {
            prototype = base;
            base = jQuery.Widget;
        }

        // create selector for plugin
        jQuery.expr[ ":" ][ fullName.toLowerCase() ] = function( elem ) {
            return !!jQuery.data( elem, fullName );
        };

        jQuery[ namespace ] = jQuery[ namespace ] || {};
        existingConstructor = jQuery[ namespace ][ name ];
        constructor = jQuery[ namespace ][ name ] = function( options, element ) {
            // allow instantiation without "new" keyword
            if ( !this._createWidget ) {
                return new constructor( options, element );
            }

            // allow instantiation without initializing for simple inheritance
            // must use "new" keyword (the code above always passes args)
            if ( arguments.length ) {
                this._createWidget( options, element );
            }
        };
        // extend with the existing constructor to carry over any static properties
        radic.extend( constructor, existingConstructor, {
            version: prototype.version,
            // copy the object used to create the prototype in case we need to
            // redefine the widget later
            _proto: radic.extend( {}, prototype ),
            // track widgets that inherit from this widget in case this widget is
            // redefined after a widget inherits from it
            _childConstructors: []
        });

        basePrototype = new base();
        // we need to make the options hash a property directly on the new instance
        // otherwise we'll modify the options hash on the prototype that we're
        // inheriting from
        basePrototype.options = jQuery.widget.extend( {}, basePrototype.options );
        jQuery.each( prototype, function( prop, value ) {
            if ( !jQuery.isFunction( value ) ) {
                proxiedPrototype[ prop ] = value;
                return;
            }
            proxiedPrototype[ prop ] = (function() {
                var _super = function() {
                        return base.prototype[ prop ].apply( this, arguments );
                    },
                    _superApply = function( args ) {
                        return base.prototype[ prop ].apply( this, args );
                    };
                return function() {
                    var __super = this._super,
                        __superApply = this._superApply,
                        returnValue;

                    this._super = _super;
                    this._superApply = _superApply;

                    returnValue = value.apply( this, arguments );

                    this._super = __super;
                    this._superApply = __superApply;

                    return returnValue;
                };
            })();
        });
        constructor.prototype = jQuery.widget.extend( basePrototype, {
            // TODO: remove support for widgetEventPrefix
            // always use the name + a colon as the prefix, e.g., draggable:start
            // don't prefix for widgets that aren't DOM-based
            widgetEventPrefix: existingConstructor ? (basePrototype.widgetEventPrefix || name) : name
        }, proxiedPrototype, {
            constructor: constructor,
            namespace: namespace,
            widgetName: name,
            widgetFullName: fullName
        });

        // If this widget is being redefined then we need to find all widgets that
        // are inheriting from it and redefine all of them so that they inherit from
        // the new version of this widget. We're essentially trying to replace one
        // level in the prototype chain.
        if ( existingConstructor ) {
            jQuery.each( existingConstructor._childConstructors, function( i, child ) {
                var childPrototype = child.prototype;

                // redefine the child widget using the same prototype that was
                // originally used, but inherit from the new version of the base
                jQuery.widget( childPrototype.namespace + "." + childPrototype.widgetName, constructor, child._proto );
            });
            // remove the list of existing child constructors from the old constructor
            // so the old child constructors can be garbage collected
            delete existingConstructor._childConstructors;
        } else {
            base._childConstructors.push( constructor );
        }

        jQuery.widget.bridge( name, constructor );

        return constructor;
    };

    jQuery.widget.extend = function( target ) {
        var input = widget_slice.call( arguments, 1 ),
            inputIndex = 0,
            inputLength = input.length,
            key,
            value;
        for ( ; inputIndex < inputLength; inputIndex++ ) {
            for ( key in input[ inputIndex ] ) {
                value = input[ inputIndex ][ key ];
                if ( input[ inputIndex ].hasOwnProperty( key ) && value !== undefined ) {
                    // Clone objects
                    if ( jQuery.isPlainObject( value ) ) {
                        target[ key ] = jQuery.isPlainObject( target[ key ] ) ?
                            jQuery.widget.extend( {}, target[ key ], value ) :
                            // Don't extend strings, arrays, etc. with objects
                            jQuery.widget.extend( {}, value );
                        // Copy everything else by reference
                    } else {
                        target[ key ] = value;
                    }
                }
            }
        }
        return target;
    };

    jQuery.widget.bridge = function( name, object ) {
        var fullName = object.prototype.widgetFullName || name;
        jQuery.fn[ name ] = function( options ) {
            var isMethodCall = typeof options === "string",
                args = widget_slice.call( arguments, 1 ),
                returnValue = this;

            // allow multiple hashes to be passed on init
            options = !isMethodCall && args.length ?
                jQuery.widget.extend.apply( null, [ options ].concat(args) ) :
                options;

            if ( isMethodCall ) {
                this.each(function() {
                    var methodValue,
                        instance = jQuery.data( this, fullName );
                    if ( options === "instance" ) {
                        returnValue = instance;
                        return false;
                    }
                    if ( !instance ) {
                        return radic.error( "cannot call methods on " + name + " prior to initialization; " +
                        "attempted to call method '" + options + "'" );
                    }
                    if ( !jQuery.isFunction( instance[options] ) || options.charAt( 0 ) === "_" ) {
                        return radic.error( "no such method '" + options + "' for " + name + " widget instance" );
                    }
                    methodValue = instance[ options ].apply( instance, args );
                    if ( methodValue !== instance && methodValue !== undefined ) {
                        returnValue = methodValue && methodValue.jquery ?
                            returnValue.pushStack( methodValue.get() ) :
                            methodValue;
                        return false;
                    }
                });
            } else {
                this.each(function() {
                    var instance = jQuery.data( this, fullName );
                    if ( instance ) {
                        instance.option( options || {} );
                        if ( instance._init ) {
                            instance._init();
                        }
                    } else {
                        jQuery.data( this, fullName, new object( options, this ) );
                    }
                });
            }

            return returnValue;
        };
    };

    jQuery.Widget = function( /* options, element */ ) {};
    jQuery.Widget._childConstructors = [];

    jQuery.Widget.prototype = {
        widgetName: "widget",
        widgetEventPrefix: "",
        defaultElement: "<div>",
        options: {
            disabled: false,

            // callbacks
            create: null
        },
        _createWidget: function( options, element ) {
            element = jQuery( element || this.defaultElement || this )[ 0 ];
            this.element = jQuery( element );
            this.uuid = widget_uuid++;
            this.eventNamespace = "." + this.widgetName + this.uuid;

            this.bindings = jQuery();
            this.hoverable = jQuery();
            this.focusable = jQuery();

            if ( element !== this ) {
                jQuery.data( element, this.widgetFullName, this );
                this._on( true, this.element, {
                    remove: function( event ) {
                        if ( event.target === element ) {
                            this.destroy();
                        }
                    }
                });
                this.document = jQuery( element.style ?
                    // element within the document
                    element.ownerDocument :
                    // element is window or document
                element.document || element );
                this.window = jQuery( this.document[0].defaultView || this.document[0].parentWindow );
            }

            this.options = jQuery.widget.extend( {},
                this.options,
                this._getCreateOptions(),
                options );

            this._create();
            this._trigger( "create", null, this._getCreateEventData() );
            this._init();
        },
        _getCreateOptions: jQuery.noop,
        _getCreateEventData: jQuery.noop,
        _create: jQuery.noop,
        _init: jQuery.noop,

        destroy: function() {
            this._destroy();
            // we can probably remove the unbind calls in 2.0
            // all event bindings should go through this._on()
            this.element
                .unbind( this.eventNamespace )
                .removeData( this.widgetFullName )
                // support: jquery <1.6.3
                // http://bugs.jquery.com/ticket/9413
                .removeData( jQuery.camelCase( this.widgetFullName ) );
            this.widget()
                .unbind( this.eventNamespace )
                .removeAttr( "aria-disabled" )
                .removeClass(
                this.widgetFullName + "-disabled " +
                "ui-state-disabled" );

            // clean up events and states
            this.bindings.unbind( this.eventNamespace );
            this.hoverable.removeClass( "ui-state-hover" );
            this.focusable.removeClass( "ui-state-focus" );
        },
        _destroy: jQuery.noop,

        widget: function() {
            return this.element;
        },

        option: function( key, value ) {
            var options = key,
                parts,
                curOption,
                i;

            if ( arguments.length === 0 ) {
                // don't return a reference to the internal hash
                return radic.widget.extend( {}, this.options );
            }

            if ( typeof key === "string" ) {
                // handle nested keys, e.g., "foo.bar" => { foo: { bar: ___ } }
                options = {};
                parts = key.split( "." );
                key = parts.shift();
                if ( parts.length ) {
                    curOption = options[ key ] = jQuery.widget.extend( {}, this.options[ key ] );
                    for ( i = 0; i < parts.length - 1; i++ ) {
                        curOption[ parts[ i ] ] = curOption[ parts[ i ] ] || {};
                        curOption = curOption[ parts[ i ] ];
                    }
                    key = parts.pop();
                    if ( arguments.length === 1 ) {
                        return curOption[ key ] === undefined ? null : curOption[ key ];
                    }
                    curOption[ key ] = value;
                } else {
                    if ( arguments.length === 1 ) {
                        return this.options[ key ] === undefined ? null : this.options[ key ];
                    }
                    options[ key ] = value;
                }
            }

            this._setOptions( options );

            return this;
        },
        _setOptions: function( options ) {
            var key;

            for ( key in options ) {
                this._setOption( key, options[ key ] );
            }

            return this;
        },
        _setOption: function( key, value ) {
            this.options[ key ] = value;

            if ( key === "disabled" ) {
                this.widget()
                    .toggleClass( this.widgetFullName + "-disabled", !!value );

                // If the widget is becoming disabled, then nothing is interactive
                if ( value ) {
                    this.hoverable.removeClass( "ui-state-hover" );
                    this.focusable.removeClass( "ui-state-focus" );
                }
            }

            return this;
        },

        enable: function() {
            return this._setOptions({ disabled: false });
        },
        disable: function() {
            return this._setOptions({ disabled: true });
        },

        _on: function( suppressDisabledCheck, element, handlers ) {
            var delegateElement,
                instance = this;

            // no suppressDisabledCheck flag, shuffle arguments
            if ( typeof suppressDisabledCheck !== "boolean" ) {
                handlers = element;
                element = suppressDisabledCheck;
                suppressDisabledCheck = false;
            }

            // no element argument, shuffle and use this.element
            if ( !handlers ) {
                handlers = element;
                element = this.element;
                delegateElement = this.widget();
            } else {
                element = delegateElement = jQuery( element );
                this.bindings = this.bindings.add( element );
            }

            jQuery.each( handlers, function( event, handler ) {
                function handlerProxy() {
                    // allow widgets to customize the disabled handling
                    // - disabled as an array instead of boolean
                    // - disabled class as method for disabling individual parts
                    if ( !suppressDisabledCheck &&
                        ( instance.options.disabled === true ||
                        jQuery( this ).hasClass( "ui-state-disabled" ) ) ) {
                        return;
                    }
                    return ( typeof handler === "string" ? instance[ handler ] : handler )
                        .apply( instance, arguments );
                }

                // copy the guid so direct unbinding works
                if ( typeof handler !== "string" ) {
                    handlerProxy.guid = handler.guid =
                        handler.guid || handlerProxy.guid || jQuery.guid++;
                }

                var match = event.match( /^([\w:-]*)\s*(.*)$/ ),
                    eventName = match[1] + instance.eventNamespace,
                    selector = match[2];
                if ( selector ) {
                    delegateElement.delegate( selector, eventName, handlerProxy );
                } else {
                    element.bind( eventName, handlerProxy );
                }
            });
        },

        _off: function( element, eventName ) {
            eventName = (eventName || "").split( " " ).join( this.eventNamespace + " " ) +
            this.eventNamespace;
            element.unbind( eventName ).undelegate( eventName );

            // Clear the stack to avoid memory leaks (#10056)
            this.bindings = jQuery( this.bindings.not( element ).get() );
            this.focusable = jQuery( this.focusable.not( element ).get() );
            this.hoverable = jQuery( this.hoverable.not( element ).get() );
        },

        _delay: function( handler, delay ) {
            function handlerProxy() {
                return ( typeof handler === "string" ? instance[ handler ] : handler )
                    .apply( instance, arguments );
            }
            var instance = this;
            return setTimeout( handlerProxy, delay || 0 );
        },

        _hoverable: function( element ) {
            this.hoverable = this.hoverable.add( element );
            this._on( element, {
                mouseenter: function( event ) {
                    jQuery( event.currentTarget ).addClass( "ui-state-hover" );
                },
                mouseleave: function( event ) {
                    jQuery( event.currentTarget ).removeClass( "ui-state-hover" );
                }
            });
        },

        _focusable: function( element ) {
            this.focusable = this.focusable.add( element );
            this._on( element, {
                focusin: function( event ) {
                    jQuery( event.currentTarget ).addClass( "ui-state-focus" );
                },
                focusout: function( event ) {
                    jQuery( event.currentTarget ).removeClass( "ui-state-focus" );
                }
            });
        },

        _trigger: function( type, event, data ) {
            var prop, orig,
                callback = this.options[ type ];

            data = data || {};
            event = jQuery.Event( event );
            event.type = ( type === this.widgetEventPrefix ?
                type :
            this.widgetEventPrefix + type ).toLowerCase();
            // the original event may come from any element
            // so we need to reset the target on the new event
            event.target = this.element[ 0 ];

            // copy original event properties over to the new event
            orig = event.originalEvent;
            if ( orig ) {
                for ( prop in orig ) {
                    if ( !( prop in event ) ) {
                        event[ prop ] = orig[ prop ];
                    }
                }
            }

            this.element.trigger( event, data );
            return !( jQuery.isFunction( callback ) &&
            callback.apply( this.element[0], [ event ].concat( data ) ) === false ||
            event.isDefaultPrevented() );
        }
    };

    jQuery.each( { show: "fadeIn", hide: "fadeOut" }, function( method, defaultEffect ) {
        jQuery.Widget.prototype[ "_" + method ] = function( element, options, callback ) {
            if ( typeof options === "string" ) {
                options = { effect: options };
            }
            var hasOptions,
                effectName = !options ?
                    method :
                    options === true || typeof options === "number" ?
                        defaultEffect :
                    options.effect || defaultEffect;
            options = options || {};
            if ( typeof options === "number" ) {
                options = { duration: options };
            }
            hasOptions = !jQuery.isEmptyObject( options );
            options.complete = callback;
            if ( options.delay ) {
                element.delay( options.delay );
            }
            if ( hasOptions && jQuery.effects && jQuery.effects.effect[ effectName ] ) {
                element[ method ]( options );
            } else if ( effectName !== method && element[ effectName ] ) {
                element[ effectName ]( options.duration, options.easing, callback );
            } else {
                element.queue(function( next ) {
                    jQuery( this )[ method ]();
                    if ( callback ) {
                        callback.call( element[ 0 ] );
                    }
                    next();
                });
            }
        };
    });

    var widget = jQuery.widget;

    radic.widget = jQuery.widget;

    $.widget("radic.base",  {
        version: '0.0.1',
        options: {

        },
        instance: function(){
            return { el: this.element, defel: this.defaultElement, self: this };
        },
        _compile: function (template, data, options) {
            $.extend(data, {
                options: $.extend({}, this.options, options)
            });
            this._trigger('beforeCompile', null, data);

            return radic.template(template, data);
        },
        _getCreateEventData: function() {
            return this.options;
        },
        _pluginExists: function(plugin){
            return radic.defined($.fn[plugin]);
        }
    });




    jQuery.fn.spin = function(opts, color) {

        return this.each(function() {
            var $this = $(this),
                data = $this.data();

            if (data.spinner) {
                data.spinner.stop();
                delete data.spinner;
            }
            if (opts !== false) {
                opts = $.extend(
                    { color: color || $this.css('color') },
                    $.fn.spin.presets[opts] || opts
                )
                data.spinner = new Spinner(opts).spin(this)
            }
        })
    };

    jQuery.fn.spin.presets = {
        tiny: { lines: 8, length: 2, width: 2, radius: 3 },
        small: { lines: 8, length: 4, width: 3, radius: 5 },
        large: { lines: 10, length: 8, width: 4, radius: 8 }
    };



if ( typeof define === "function" && define.amd ) {
	define( "radic", [], function() {
		return radic;
	});
}


var strundefined = typeof undefined;



var
	// Map over jQuery in case of overwrite
	_radic = window.radic,

	// Map over the $ in case of overwrite
	_R = window.R;

	radic.noConflict = function( deep ) {
	if ( window.r === radic ) {
		window.R = _R;
	}

	if ( deep && window.radic === radic ) {
		window.radic = _radic;
	}

	return radic;
};

// Expose jQuery and $ identifiers, even in
// AMD (#7102#comment:10, https://github.com/jquery/jquery/pull/557)
// and CommonJS for browser emulators (#13566)
if ( typeof noGlobal === strundefined ) {
	window.radic = window.R = radic;
}



}));
