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
         * Build: `lodash underscore include="omit,pick,values,keys,where,cloneDeep,isUndefined,isNumber,isBoolean,isNull,isDate,toArray" exports="none" -o src/tpl/_lodash.js`
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
           * Checks if `value` is a boolean value.
           *
           * @static
           * @memberOf _
           * @category Objects
           * @param {*} value The value to check.
           * @returns {boolean} Returns `true` if the `value` is a boolean value, else `false`.
           * @example
           *
           * _.isBoolean(null);
           * // => false
           */
          function isBoolean(value) {
            return value === true || value === false ||
              value && typeof value == 'object' && toString.call(value) == boolClass || false;
          }
        
          /**
           * Checks if `value` is a date.
           *
           * @static
           * @memberOf _
           * @category Objects
           * @param {*} value The value to check.
           * @returns {boolean} Returns `true` if the `value` is a date, else `false`.
           * @example
           *
           * _.isDate(new Date);
           * // => true
           */
          function isDate(value) {
            return value && typeof value == 'object' && toString.call(value) == dateClass || false;
          }
        
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
           * Checks if `value` is `null`.
           *
           * @static
           * @memberOf _
           * @category Objects
           * @param {*} value The value to check.
           * @returns {boolean} Returns `true` if the `value` is `null`, else `false`.
           * @example
           *
           * _.isNull(null);
           * // => true
           *
           * _.isNull(undefined);
           * // => false
           */
          function isNull(value) {
            return value === null;
          }
        
          /**
           * Checks if `value` is a number.
           *
           * Note: `NaN` is considered a number. See http://es5.github.io/#x8.5.
           *
           * @static
           * @memberOf _
           * @category Objects
           * @param {*} value The value to check.
           * @returns {boolean} Returns `true` if the `value` is a number, else `false`.
           * @example
           *
           * _.isNumber(8.4 * 5);
           * // => true
           */
          function isNumber(value) {
            return typeof value == 'number' ||
              value && typeof value == 'object' && toString.call(value) == numberClass || false;
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
           * Checks if `value` is `undefined`.
           *
           * @static
           * @memberOf _
           * @category Objects
           * @param {*} value The value to check.
           * @returns {boolean} Returns `true` if the `value` is `undefined`, else `false`.
           * @example
           *
           * _.isUndefined(void 0);
           * // => true
           */
          function isUndefined(value) {
            return typeof value == 'undefined';
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
          lodash.isBoolean = isBoolean;
          lodash.isDate = isDate;
          lodash.isEmpty = isEmpty;
          lodash.isFunction = isFunction;
          lodash.isNull = isNull;
          lodash.isNumber = isNumber;
          lodash.isObject = isObject;
          lodash.isString = isString;
          lodash.isUndefined = isUndefined;
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


    /**
     * @namespace radic
     */
}));
