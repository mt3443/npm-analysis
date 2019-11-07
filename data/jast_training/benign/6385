/*!

 handlebars v2.0.0

Copyright (C) 2011-2014 by Yehuda Katz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

@license
*/
/* exported Handlebars */
(function (root, factory) {
  if (typeof define === 'function' && define.amd) {
    define([], factory);
  } else if (typeof exports === 'object') {
    module.exports = factory();
  } else {
    root.Handlebars = root.Handlebars || factory();
  }
}(this, function () {
// handlebars/safe-string.js
var __module3__ = (function() {
  "use strict";
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
  "use strict";
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
  "use strict";
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
  "use strict";
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
  "use strict";
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
  "use strict";
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

  return __module0__;
}));

!function a(b,c,d){function e(g,h){if(!c[g]){if(!b[g]){var i="function"==typeof require&&require;if(!h&&i)return i(g,!0);if(f)return f(g,!0);throw new Error("Cannot find module '"+g+"'")}var j=c[g]={exports:{}};b[g][0].call(j.exports,function(a){var c=b[g][1][a];return e(c?c:a)},j,j.exports,a,b,c,d)}return c[g].exports}for(var f="function"==typeof require&&require,g=0;g<d.length;g++)e(d[g]);return e}({1:[function(a,b){b.exports={oauthd_url:"https://oauth.io",oauthd_api:"https://oauth.io/api",version:"web-0.3.0",options:{}}},{}],2:[function(a,b){"use strict";var c,d,e,f,g,h,i;f=a("../config"),g=a("../tools/cookies"),e=a("../tools/cache"),d=a("../tools/url"),i=a("../tools/sha1"),h=a("./oauthio_requests"),c=a("q"),b.exports=function(a,b,c,j){var k,l,m,n,o,p,q;return d=d(b),g.init(f,b),e.init(g,f),q={},p={},o={execProvidersCb:function(a,b,c){var d,e;if(p[a]){d=p[a],delete p[a];for(e in d)d[e](b,c)}},fetchDescription:function(a){q[a]||(q[a]=!0,c.ajax({url:f.oauthd_api+"/providers/"+a,data:{extend:!0},dataType:"json"}).done(function(b){q[a]=b.data,o.execProvidersCb(a,null,b.data)}).always(function(){"object"!=typeof q[a]&&(delete q[a],o.execProvidersCb(a,new Error("Unable to fetch request description")))}))},getDescription:function(a,b,c){return b=b||{},"object"==typeof q[a]?c(null,q[a]):(q[a]||o.fetchDescription(a),b.wait?(p[a]=p[a]||[],void p[a].push(c)):c(null,{}))}},f.oauthd_base=d.getAbsUrl(f.oauthd_url).match(/^.{2,5}:\/\/[^/]+/)[0],k=[],l=void 0,(n=function(){var a,c;c=/[\\#&]oauthio=([^&]*)/.exec(b.location.hash),c&&(b.location.hash=b.location.hash.replace(/&?oauthio=[^&]*/,""),l=decodeURIComponent(c[1].replace(/\+/g," ")),a=g.readCookie("oauthio_state"),a&&(k.push(a),g.eraseCookie("oauthio_state")))})(),a.location_operations={reload:function(){return b.location.reload()},getHash:function(){return b.location.hash},setHash:function(a){return b.location.hash=a},changeHref:function(a){return b.location.href=a}},m={request:h(c,f,k,e,o)},function(h){null==h.OAuth&&(h.OAuth={debug:!1,initialize:function(a,b){var c,d;if(f.key=a,b){d=[];for(c in b)d.push(f.options[c]=b[c]);return d}},setOAuthdURL:function(a){f.oauthd_url=a,f.oauthd_base=d.getAbsUrl(f.oauthd_url).match(/^.{2,5}:\/\/[^/]+/)[0]},getVersion:function(){return f.version},create:function(a,b,c){var d,f,g,i;if(!b)return e.tryCache(h.OAuth,a,!0);"object"!=typeof c&&o.fetchDescription(a),f=function(d){return m.request.mkHttp(a,b,c,d)},g=function(d,e){return m.request.mkHttpEndpoint(a,b,c,d,e)},i={};for(d in b)i[d]=b[d];return i.get=f("GET"),i.post=f("POST"),i.put=f("PUT"),i.patch=f("PATCH"),i.del=f("DELETE"),i.me=m.request.mkHttpMe(a,b,c,"GET"),i},popup:function(g,l,n){var o,p,q,r,s,t,u,v,w,x,y;return r=!1,q=function(a){if(a.origin===f.oauthd_base){try{v.close()}catch(b){}return l.data=a.data,m.request.sendCallback(l,o),r=!0}},v=void 0,p=void 0,w=void 0,o=c.Deferred(),l=l||{},f.key?(2===arguments.length&&"function"==typeof l&&(n=l,l={}),e.cacheEnabled(l.cache)&&(t=e.tryCache(h.OAuth,g,l.cache))?(null!=o&&o.resolve(t),n?n(null,t):o.promise()):(l.state||(l.state=i.create_hash(),l.state_type="client"),k.push(l.state),u=f.oauthd_url+"/auth/"+g+"?k="+f.key,u+="&d="+encodeURIComponent(d.getAbsUrl("/")),l&&(u+="&opts="+encodeURIComponent(JSON.stringify(l))),l.wnd_settings?(y=l.wnd_settings,delete l.wnd_settings):y={width:Math.floor(.8*a.outerWidth),height:Math.floor(.5*a.outerHeight)},null==y.height&&(y.height=y.height<350?350:void 0),null==y.width&&(y.width=y.width<800?800:void 0),null==y.left&&(y.left=a.screenX+(a.outerWidth-y.width)/2),null==y.top&&(y.top=a.screenY+(a.outerHeight-y.height)/8),x="width="+y.width+",height="+y.height,x+=",toolbar=0,scrollbars=1,status=1,resizable=1,location=1,menuBar=0",x+=",left="+y.left+",top="+y.top,l={provider:g,cache:l.cache},l.callback=function(c,d){return a.removeEventListener?a.removeEventListener("message",q,!1):a.detachEvent?a.detachEvent("onmessage",q):b.detachEvent&&b.detachEvent("onmessage",q),l.callback=function(){},w&&(clearTimeout(w),w=void 0),n?n(c,d):void 0},a.attachEvent?a.attachEvent("onmessage",q):b.attachEvent?b.attachEvent("onmessage",q):a.addEventListener&&a.addEventListener("message",q,!1),"undefined"!=typeof chrome&&chrome.runtime&&chrome.runtime.onMessageExternal&&chrome.runtime.onMessageExternal.addListener(function(a,b){return a.origin=b.url.match(/^.{2,5}:\/\/[^/]+/)[0],null!=o&&o.resolve(),q(a)}),!p&&(-1!==j.userAgent.indexOf("MSIE")||j.appVersion.indexOf("Trident/")>0)&&(p=b.createElement("iframe"),p.src=f.oauthd_url+"/auth/iframe?d="+encodeURIComponent(d.getAbsUrl("/")),p.width=0,p.height=0,p.frameBorder=0,p.style.visibility="hidden",b.body.appendChild(p)),w=setTimeout(function(){null!=o&&o.reject(new Error("Authorization timed out")),l.callback&&"function"==typeof l.callback&&l.callback(new Error("Authorization timed out"));try{v.close()}catch(a){}},12e5),v=a.open(u,"Authorization",x),v?(v.focus(),s=a.setInterval(function(){return null!==v&&!v.closed||(a.clearInterval(s),r||(null!=o&&o.reject(new Error("The popup was closed")),!l.callback||"function"!=typeof l.callback))?void 0:l.callback(new Error("The popup was closed"))},500)):(null!=o&&o.reject(new Error("Could not open a popup")),l.callback&&"function"==typeof l.callback&&l.callback(new Error("Could not open a popup"))),null!=o?o.promise():void 0)):(null!=o&&o.reject(new Error("OAuth object must be initialized")),null==n?o.promise():n(new Error("OAuth object must be initialized")))},redirect:function(b,c,j){var k,l;return 2===arguments.length&&(j=c,c={}),e.cacheEnabled(c.cache)&&(l=e.tryCache(h.OAuth,b,c.cache))?(j=d.getAbsUrl(j)+(-1===j.indexOf("#")?"#":"&")+"oauthio=cache",a.location_operations.changeHref(j),void a.location_operations.reload()):(c.state||(c.state=i.create_hash(),c.state_type="client"),g.createCookie("oauthio_state",c.state),k=encodeURIComponent(d.getAbsUrl(j)),j=f.oauthd_url+"/auth/"+b+"?k="+f.key,j+="&redirect_uri="+k,c&&(j+="&opts="+encodeURIComponent(JSON.stringify(c))),void a.location_operations.changeHref(j))},callback:function(a,b,d){var f,g;if(f=c.Deferred(),1===arguments.length&&"function"==typeof a&&(d=a,a=void 0,b={}),1===arguments.length&&"string"==typeof a&&(b={}),2===arguments.length&&"function"==typeof b&&(d=b,b={}),e.cacheEnabled(b.cache)||"cache"===l){if(g=e.tryCache(h.OAuth,a,b.cache),"cache"===l&&("string"!=typeof a||!a))return null!=f&&f.reject(new Error("You must set a provider when using the cache")),d?d(new Error("You must set a provider when using the cache")):null!=f?f.promise():void 0;if(g){if(!d)return null!=f&&f.resolve(g),null!=f?f.promise():void 0;if(g)return d(null,g)}}return l?(m.request.sendCallback({data:l,provider:a,cache:b.cache,callback:d},f),null!=f?f.promise():void 0):void 0},clearCache:function(a){g.eraseCookie("oauthio_provider_"+a)},http_me:function(a){m.request.http_me&&m.request.http_me(a)},http:function(a){m.request.http&&m.request.http(a)},ready:function(){}})}}},{"../config":1,"../tools/cache":5,"../tools/cookies":6,"../tools/sha1":8,"../tools/url":9,"./oauthio_requests":3,q:11}],3:[function(a,b){var c,d,e=[].indexOf||function(a){for(var b=0,c=this.length;c>b;b++)if(b in this&&this[b]===a)return b;return-1};d=a("../tools/url")(),c=a("q"),b.exports=function(a,b,f,g,h){var i;return i=[],{retrieveMethods:function(){var d;return d=c.defer(),a.ajax(b.oauthd_url+"/api/extended-endpoints").then(function(a){return i=a.data,d.resolve()}).fail(function(a){return d.reject(a)}),d.promise},generateMethods:function(a,b,c){var d,e,f,g,h,j,k;if(null!=i){k=[];for(d in i)h=i[d],f=h.name.split("."),g=a,k.push(function(){var a;a=[];for(e in f)j=f[e],e<f.length-1?(null==g[j]&&(g[j]={}),a.push(g=g[j])):a.push(g[j]=this.mkHttpAll(c,b,h,arguments));return a}.apply(this,arguments));return k}},http:function(c){var f,g,i,j,k;i=function(){var c,f,g,h;if(h=k.oauthio.request||{},!h.cors){k.url=encodeURIComponent(k.url),"/"!==k.url[0]&&(k.url="/"+k.url),k.url=b.oauthd_url+"/request/"+k.oauthio.provider+k.url,k.headers=k.headers||{},k.headers.oauthio="k="+b.key,k.oauthio.tokens.oauth_token&&k.oauthio.tokens.oauth_token_secret&&(k.headers.oauthio+="&oauthv=1");for(f in k.oauthio.tokens)k.headers.oauthio+="&"+encodeURIComponent(f)+"="+encodeURIComponent(k.oauthio.tokens[f]);return delete k.oauthio,a.ajax(k)}if(k.oauthio.tokens){if(k.oauthio.tokens.access_token&&(k.oauthio.tokens.token=k.oauthio.tokens.access_token),k.url.match(/^[a-z]{2,16}:\/\//)||("/"!==k.url[0]&&(k.url="/"+k.url),k.url=h.url+k.url),k.url=d.replaceParam(k.url,k.oauthio.tokens,h.parameters),h.query){g=[];for(c in h.query)g.push(encodeURIComponent(c)+"="+encodeURIComponent(d.replaceParam(h.query[c],k.oauthio.tokens,h.parameters)));k.url+=e.call(k.url,"?")>=0?"&"+g:"?"+g}if(h.headers){k.headers=k.headers||{};for(c in h.headers)k.headers[c]=d.replaceParam(h.headers[c],k.oauthio.tokens,h.parameters)}return delete k.oauthio,a.ajax(k)}},k={},j=void 0;for(j in c)k[j]=c[j];return k.oauthio.request&&k.oauthio.request!==!0?i():(g={wait:!!k.oauthio.request},f=a.Deferred(),h.getDescription(k.oauthio.provider,g,function(a,b){return a?f.reject(a):(k.oauthio.request=k.oauthio.tokens.oauth_token&&k.oauthio.tokens.oauth_token_secret?b.oauth1&&b.oauth1.request:b.oauth2&&b.oauth2.request,void f.resolve())}),f.then(i))},http_me:function(c){var d,e,f,g,i;f=function(){var c,d,e,f;c=a.Deferred(),f=i.oauthio.request||{},i.url=b.oauthd_url+"/auth/"+i.oauthio.provider+"/me",i.headers=i.headers||{},i.headers.oauthio="k="+b.key,i.oauthio.tokens.oauth_token&&i.oauthio.tokens.oauth_token_secret&&(i.headers.oauthio+="&oauthv=1");for(d in i.oauthio.tokens)i.headers.oauthio+="&"+encodeURIComponent(d)+"="+encodeURIComponent(i.oauthio.tokens[d]);return delete i.oauthio,e=a.ajax(i),a.when(e).done(function(a){c.resolve(a.data)}).fail(function(a){c.reject(a.responseJSON?a.responseJSON.data:new Error("An error occured while trying to access the resource"))}),c.promise()},i={};for(g in c)i[g]=c[g];return i.oauthio.request&&i.oauthio.request!==!0?f():(e={wait:!!i.oauthio.request},d=a.Deferred(),h.getDescription(i.oauthio.provider,e,function(a,b){return a?d.reject(a):(i.oauthio.request=i.oauthio.tokens.oauth_token&&i.oauthio.tokens.oauth_token_secret?b.oauth1&&b.oauth1.request:b.oauth2&&b.oauth2.request,void d.resolve())}),d.then(f))},http_all:function(c){var d;return(d=function(){var d,e,f,g;d=a.Deferred(),g=c.oauthio.request||{},c.headers=c.headers||{},c.headers.oauthio="k="+b.key,c.oauthio.tokens.oauth_token&&c.oauthio.tokens.oauth_token_secret&&(c.headers.oauthio+="&oauthv=1");for(e in c.oauthio.tokens)c.headers.oauthio+="&"+encodeURIComponent(e)+"="+encodeURIComponent(c.oauthio.tokens[e]);return delete c.oauthio,f=a.ajax(c),a.when(f).done(function(a){var b;if("string"==typeof a.data)try{a.data=JSON.parse(a.data)}catch(c){b=c,a.data=a.data}finally{d.resolve(a.data)}}).fail(function(a){d.reject(a.responseJSON?a.responseJSON.data:new Error("An error occured while trying to access the resource"))}),d.promise()})()},mkHttp:function(a,b,c,d){var e;return e=this,function(f,g){var h,i;if(i={},"string"==typeof f){if("object"==typeof g)for(h in g)i[h]=g[h];i.url=f}else if("object"==typeof f)for(h in f)i[h]=f[h];return i.type=i.type||d,i.oauthio={provider:a,tokens:b,request:c},e.http(i)}},mkHttpMe:function(a,b,c,d){var e;return e=this,function(f){var g;return g={},g.type=g.type||d,g.oauthio={provider:a,tokens:b,request:c},g.data=g.data||{},g.data.filter=f?f.join(","):void 0,e.http_me(g)}},mkHttpAll:function(a,c,d){var e;return e=this,function(){var f,g,h,i;g={},g.type=d.method,g.url=b.oauthd_url+d.endpoint.replace(":provider",a),g.oauthio={provider:a,tokens:c},g.data={};for(f in arguments)i=arguments[f],h=d.params[f],null!=h&&(g.data[h.name]=i);return g.data=g.data||{},e.http_all(g,d,arguments)}},sendCallback:function(a,b){var c,d,e,h,i,j,k,l,m,n,o;c=this,d=void 0,h=void 0;try{d=JSON.parse(a.data)}catch(p){return e=p,b.reject(new Error("Error while parsing result")),a.callback(new Error("Error while parsing result"))}if(d&&d.provider){if(a.provider&&d.provider.toLowerCase()!==a.provider.toLowerCase())return h=new Error("Returned provider name does not match asked provider"),b.reject(h),a.callback&&"function"==typeof a.callback?a.callback(h):void 0;if("error"===d.status||"fail"===d.status)return h=new Error(d.message),h.body=d.data,b.reject(h),a.callback&&"function"==typeof a.callback?a.callback(h):void 0;if("success"!==d.status||!d.data)return h=new Error,h.body=d.data,b.reject(h),a.callback&&"function"==typeof a.callback?a.callback(h):void 0;d.state=d.state.replace(/\s+/g,"");for(j in f)o=f[j],f[j]=o.replace(/\s+/g,"");if(!d.state||-1===f.indexOf(d.state))return b.reject(new Error("State is not matching")),a.callback&&"function"==typeof a.callback?a.callback(new Error("State is not matching")):void 0;if(a.provider||(d.data.provider=d.provider),m=d.data,g.cacheEnabled(a.cache)&&m&&g.storeCache(d.provider,m),l=m.request,delete m.request,n=void 0,m.access_token?n={access_token:m.access_token}:m.oauth_token&&m.oauth_token_secret&&(n={oauth_token:m.oauth_token,oauth_token_secret:m.oauth_token_secret}),!l)return b.resolve(m),a.callback&&"function"==typeof a.callback?a.callback(null,m):void 0;if(l.required)for(i in l.required)n[l.required[i]]=m[l.required[i]];return k=function(a){return c.mkHttp(d.provider,n,l,a)},m.get=k("GET"),m.post=k("POST"),m.put=k("PUT"),m.patch=k("PATCH"),m.del=k("DELETE"),m.me=c.mkHttpMe(d.provider,n,l,"GET"),this.generateMethods(m,n,d.provider),b.resolve(m),a.callback&&"function"==typeof a.callback?a.callback(null,m):void 0}}}}},{"../tools/url":9,q:11}],4:[function(a){var b,c;c=a("./tools/jquery-lite.js"),(b=a("./lib/oauth")(window,document,c,navigator))(window||this)},{"./lib/oauth":2,"./tools/jquery-lite.js":7}],5:[function(a,b){b.exports={init:function(a,b){return this.config=b,this.cookies=a},tryCache:function(a,b,c){var d,e,f;if(this.cacheEnabled(c)){if(c=this.cookies.readCookie("oauthio_provider_"+b),!c)return!1;c=decodeURIComponent(c)}if("string"==typeof c)try{c=JSON.parse(c)}catch(g){return d=g,!1}if("object"==typeof c){f={};for(e in c)"request"!==e&&"function"!=typeof c[e]&&(f[e]=c[e]);return a.create(b,f,c.request)}return!1},storeCache:function(a,b){this.cookies.createCookie("oauthio_provider_"+a,encodeURIComponent(JSON.stringify(b)),b.expires_in-10||3600)},cacheEnabled:function(a){return"undefined"==typeof a?this.config.options.cache:a}}},{}],6:[function(a,b){b.exports={init:function(a,b){return this.config=a,this.document=b},createCookie:function(a,b,c){var d;this.eraseCookie(a),d=new Date,d.setTime(d.getTime()+1e3*(c||1200)),c="; expires="+d.toGMTString(),this.document.cookie=a+"="+b+c+"; path=/"},readCookie:function(a){var b,c,d,e;for(e=a+"=",c=this.document.cookie.split(";"),d=0;d<c.length;){for(b=c[d];" "===b.charAt(0);)b=b.substring(1,b.length);if(0===b.indexOf(e))return b.substring(e.length,b.length);d++}return null},eraseCookie:function(a){var b;b=new Date,b.setTime(b.getTime()-864e5),this.document.cookie=a+"=; expires="+b.toGMTString()+"; path=/"}}},{}],7:[function(a,b){!function(a,c){"object"==typeof b&&"object"==typeof b.exports?b.exports=a.document?c(a,!0):function(a){if(!a.document)throw new Error("jQuery requires a window with a document");return c(a)}:c(a)}("undefined"!=typeof window?window:this,function(a){function b(a){var b=a.length,c=A.type(a);return"function"===c||A.isWindow(a)?!1:1===a.nodeType&&b?!0:"array"===c||0===b||"number"==typeof b&&b>0&&b-1 in a}function c(a){var b=K[a]={};return A.each(a.match(J)||[],function(a,c){b[c]=!0}),b}function d(){y.removeEventListener("DOMContentLoaded",d,!1),a.removeEventListener("load",d,!1),A.ready()}function e(){Object.defineProperty(this.cache={},0,{get:function(){return{}}}),this.expando=A.expando+Math.random()}function f(a,b,c){var d;if(void 0===c&&1===a.nodeType)if(d="data-"+b.replace(P,"-$1").toLowerCase(),c=a.getAttribute(d),"string"==typeof c){try{c="true"===c?!0:"false"===c?!1:"null"===c?null:+c+""===c?+c:O.test(c)?A.parseJSON(c):c}catch(e){}data_user.set(a,b,c)}else c=void 0;return c}function g(){return!0}function h(){return!1}function i(){try{return y.activeElement}catch(a){}}function j(a){return function(b,c){"string"!=typeof b&&(c=b,b="*");var d,e=0,f=b.toLowerCase().match(J)||[];if(A.isFunction(c))for(;d=f[e++];)"+"===d[0]?(d=d.slice(1)||"*",(a[d]=a[d]||[]).unshift(c)):(a[d]=a[d]||[]).push(c)}}function k(a,b,c,d){function e(h){var i;return f[h]=!0,A.each(a[h]||[],function(a,h){var j=h(b,c,d);return"string"!=typeof j||g||f[j]?g?!(i=j):void 0:(b.dataTypes.unshift(j),e(j),!1)}),i}var f={},g=a===fb;return e(b.dataTypes[0])||!f["*"]&&e("*")}function l(a,b){var c,d,e=A.ajaxSettings.flatOptions||{};for(c in b)void 0!==b[c]&&((e[c]?a:d||(d={}))[c]=b[c]);return d&&A.extend(!0,a,d),a}function m(a,b,c){for(var d,e,f,g,h=a.contents,i=a.dataTypes;"*"===i[0];)i.shift(),void 0===d&&(d=a.mimeType||b.getResponseHeader("Content-Type"));if(d)for(e in h)if(h[e]&&h[e].test(d)){i.unshift(e);break}if(i[0]in c)f=i[0];else{for(e in c){if(!i[0]||a.converters[e+" "+i[0]]){f=e;break}g||(g=e)}f=f||g}return f?(f!==i[0]&&i.unshift(f),c[f]):void 0}function n(a,b,c,d){var e,f,g,h,i,j={},k=a.dataTypes.slice();if(k[1])for(g in a.converters)j[g.toLowerCase()]=a.converters[g];for(f=k.shift();f;)if(a.responseFields[f]&&(c[a.responseFields[f]]=b),!i&&d&&a.dataFilter&&(b=a.dataFilter(b,a.dataType)),i=f,f=k.shift())if("*"===f)f=i;else if("*"!==i&&i!==f){if(g=j[i+" "+f]||j["* "+f],!g)for(e in j)if(h=e.split(" "),h[1]===f&&(g=j[i+" "+h[0]]||j["* "+h[0]])){g===!0?g=j[e]:j[e]!==!0&&(f=h[0],k.unshift(h[1]));break}if(g!==!0)if(g&&a["throws"])b=g(b);else try{b=g(b)}catch(l){return{state:"parsererror",error:g?l:"No conversion from "+i+" to "+f}}}return{state:"success",data:b}}function o(a,b,c,d){var e;if(A.isArray(b))A.each(b,function(b,e){c||jb.test(a)?d(a,e):o(a+"["+("object"==typeof e?b:"")+"]",e,c,d)});else if(c||"object"!==A.type(b))d(a,b);else for(e in b)o(a+"["+e+"]",b[e],c,d)}var p=[],q=p.slice,r=p.concat,s=p.push,t=p.indexOf,u={},v=u.toString,w=u.hasOwnProperty,x={},y=a.document,z="2.1.1 -attributes,-attributes/attr,-attributes/classes,-attributes/prop,-attributes/support,-attributes/val,-css/addGetHookIf,-css/curCSS,-css/defaultDisplay,-css/hiddenVisibleSelectors,-css/support,-css/swap,-css/var,-css/var/cssExpand,-css/var/getStyles,-css/var/isHidden,-css/var/rmargin,-css/var/rnumnonpx,-css,-effects,-effects/Tween,-effects/animatedSelector,-dimensions,-offset,-data/var/data_user,-deprecated,-event/alias,-event/support,-intro,-manipulation/_evalUrl,-manipulation/support,-manipulation/var,-manipulation/var/rcheckableType,-manipulation,-outro,-queue,-queue/delay,-selector-native,-selector-sizzle,-sizzle/dist,-sizzle/dist/sizzle,-sizzle/dist/min,-sizzle/test,-sizzle/test/jquery,-traversing,-traversing/findFilter,-traversing/var/rneedsContext,-traversing/var,-wrap,-exports,-exports/amd",A=function(a,b){return new A.fn.init(a,b)},B=/^[\s\uFEFF\xA0]+|[\s\uFEFF\xA0]+$/g,C=/^-ms-/,D=/-([\da-z])/gi,E=function(a,b){return b.toUpperCase()};A.fn=A.prototype={jquery:z,constructor:A,selector:"",length:0,toArray:function(){return q.call(this)},get:function(a){return null!=a?0>a?this[a+this.length]:this[a]:q.call(this)},pushStack:function(a){var b=A.merge(this.constructor(),a);return b.prevObject=this,b.context=this.context,b},each:function(a,b){return A.each(this,a,b)},map:function(a){return this.pushStack(A.map(this,function(b,c){return a.call(b,c,b)}))},slice:function(){return this.pushStack(q.apply(this,arguments))},first:function(){return this.eq(0)},last:function(){return this.eq(-1)},eq:function(a){var b=this.length,c=+a+(0>a?b:0);return this.pushStack(c>=0&&b>c?[this[c]]:[])},end:function(){return this.prevObject||this.constructor(null)},push:s,sort:p.sort,splice:p.splice},A.extend=A.fn.extend=function(){var a,b,c,d,e,f,g=arguments[0]||{},h=1,i=arguments.length,j=!1;for("boolean"==typeof g&&(j=g,g=arguments[h]||{},h++),"object"==typeof g||A.isFunction(g)||(g={}),h===i&&(g=this,h--);i>h;h++)if(null!=(a=arguments[h]))for(b in a)c=g[b],d=a[b],g!==d&&(j&&d&&(A.isPlainObject(d)||(e=A.isArray(d)))?(e?(e=!1,f=c&&A.isArray(c)?c:[]):f=c&&A.isPlainObject(c)?c:{},g[b]=A.extend(j,f,d)):void 0!==d&&(g[b]=d));return g},A.extend({expando:"jQuery"+(z+Math.random()).replace(/\D/g,""),isReady:!0,error:function(a){throw new Error(a)},noop:function(){},isFunction:function(a){return"function"===A.type(a)},isArray:Array.isArray,isWindow:function(a){return null!=a&&a===a.window},isNumeric:function(a){return!A.isArray(a)&&a-parseFloat(a)>=0},isPlainObject:function(a){return"object"!==A.type(a)||a.nodeType||A.isWindow(a)?!1:a.constructor&&!w.call(a.constructor.prototype,"isPrototypeOf")?!1:!0},isEmptyObject:function(a){var b;for(b in a)return!1;return!0},type:function(a){return null==a?a+"":"object"==typeof a||"function"==typeof a?u[v.call(a)]||"object":typeof a},globalEval:function(a){var b,c=eval;a=A.trim(a),a&&(1===a.indexOf("use strict")?(b=y.createElement("script"),b.text=a,y.head.appendChild(b).parentNode.removeChild(b)):c(a))},camelCase:function(a){return a.replace(C,"ms-").replace(D,E)},nodeName:function(a,b){return a.nodeName&&a.nodeName.toLowerCase()===b.toLowerCase()},each:function(a,c,d){var e,f=0,g=a.length,h=b(a);if(d){if(h)for(;g>f&&(e=c.apply(a[f],d),e!==!1);f++);else for(f in a)if(e=c.apply(a[f],d),e===!1)break}else if(h)for(;g>f&&(e=c.call(a[f],f,a[f]),e!==!1);f++);else for(f in a)if(e=c.call(a[f],f,a[f]),e===!1)break;return a},trim:function(a){return null==a?"":(a+"").replace(B,"")},makeArray:function(a,c){var d=c||[];return null!=a&&(b(Object(a))?A.merge(d,"string"==typeof a?[a]:a):s.call(d,a)),d},inArray:function(a,b,c){return null==b?-1:t.call(b,a,c)},merge:function(a,b){for(var c=+b.length,d=0,e=a.length;c>d;d++)a[e++]=b[d];return a.length=e,a},grep:function(a,b,c){for(var d,e=[],f=0,g=a.length,h=!c;g>f;f++)d=!b(a[f],f),d!==h&&e.push(a[f]);return e},map:function(a,c,d){var e,f=0,g=a.length,h=b(a),i=[];if(h)for(;g>f;f++)e=c(a[f],f,d),null!=e&&i.push(e);else for(f in a)e=c(a[f],f,d),null!=e&&i.push(e);return r.apply([],i)},guid:1,proxy:function(a,b){var c,d,e;return"string"==typeof b&&(c=a[b],b=a,a=c),A.isFunction(a)?(d=q.call(arguments,2),e=function(){return a.apply(b||this,d.concat(q.call(arguments)))},e.guid=a.guid=a.guid||A.guid++,e):void 0},now:Date.now,support:x}),A.each("Boolean Number String Function Array Date RegExp Object Error".split(" "),function(a,b){u["[object "+b+"]"]=b.toLowerCase()});var F,G=/^<(\w+)\s*\/?>(?:<\/\1>|)$/,H=/^(?:\s*(<[\w\W]+>)[^>]*|#([\w-]*))$/,I=A.fn.init=function(a,b){var c,d;if(!a)return this;if("string"==typeof a){if(c="<"===a[0]&&">"===a[a.length-1]&&a.length>=3?[null,a,null]:H.exec(a),!c||!c[1]&&b)return!b||b.jquery?(b||F).find(a):this.constructor(b).find(a);if(c[1]){if(b=b instanceof A?b[0]:b,A.merge(this,A.parseHTML(c[1],b&&b.nodeType?b.ownerDocument||b:y,!0)),G.test(c[1])&&A.isPlainObject(b))for(c in b)A.isFunction(this[c])?this[c](b[c]):this.attr(c,b[c]);return this}return d=y.getElementById(c[2]),d&&d.parentNode&&(this.length=1,this[0]=d),this.context=y,this.selector=a,this}return a.nodeType?(this.context=this[0]=a,this.length=1,this):A.isFunction(a)?"undefined"!=typeof F.ready?F.ready(a):a(A):(void 0!==a.selector&&(this.selector=a.selector,this.context=a.context),A.makeArray(a,this))};I.prototype=A.fn,F=A(y);var J=/\S+/g,K={};A.Callbacks=function(a){a="string"==typeof a?K[a]||c(a):A.extend({},a);var b,d,e,f,g,h,i=[],j=!a.once&&[],k=function(c){for(b=a.memory&&c,d=!0,h=f||0,f=0,g=i.length,e=!0;i&&g>h;h++)if(i[h].apply(c[0],c[1])===!1&&a.stopOnFalse){b=!1;break}e=!1,i&&(j?j.length&&k(j.shift()):b?i=[]:l.disable())},l={add:function(){if(i){var c=i.length;!function d(b){A.each(b,function(b,c){var e=A.type(c);"function"===e?a.unique&&l.has(c)||i.push(c):c&&c.length&&"string"!==e&&d(c)})}(arguments),e?g=i.length:b&&(f=c,k(b))}return this},remove:function(){return i&&A.each(arguments,function(a,b){for(var c;(c=A.inArray(b,i,c))>-1;)i.splice(c,1),e&&(g>=c&&g--,h>=c&&h--)}),this},has:function(a){return a?A.inArray(a,i)>-1:!(!i||!i.length)},empty:function(){return i=[],g=0,this},disable:function(){return i=j=b=void 0,this},disabled:function(){return!i},lock:function(){return j=void 0,b||l.disable(),this},locked:function(){return!j},fireWith:function(a,b){return!i||d&&!j||(b=b||[],b=[a,b.slice?b.slice():b],e?j.push(b):k(b)),this},fire:function(){return l.fireWith(this,arguments),this},fired:function(){return!!d}};return l},A.extend({Deferred:function(a){var b=[["resolve","done",A.Callbacks("once memory"),"resolved"],["reject","fail",A.Callbacks("once memory"),"rejected"],["notify","progress",A.Callbacks("memory")]],c="pending",d={state:function(){return c},always:function(){return e.done(arguments).fail(arguments),this},then:function(){var a=arguments;return A.Deferred(function(c){A.each(b,function(b,f){var g=A.isFunction(a[b])&&a[b];e[f[1]](function(){var a=g&&g.apply(this,arguments);a&&A.isFunction(a.promise)?a.promise().done(c.resolve).fail(c.reject).progress(c.notify):c[f[0]+"With"](this===d?c.promise():this,g?[a]:arguments)})}),a=null}).promise()},promise:function(a){return null!=a?A.extend(a,d):d}},e={};return d.pipe=d.then,A.each(b,function(a,f){var g=f[2],h=f[3];d[f[1]]=g.add,h&&g.add(function(){c=h},b[1^a][2].disable,b[2][2].lock),e[f[0]]=function(){return e[f[0]+"With"](this===e?d:this,arguments),this},e[f[0]+"With"]=g.fireWith}),d.promise(e),a&&a.call(e,e),e},when:function(a){var b,c,d,e=0,f=q.call(arguments),g=f.length,h=1!==g||a&&A.isFunction(a.promise)?g:0,i=1===h?a:A.Deferred(),j=function(a,c,d){return function(e){c[a]=this,d[a]=arguments.length>1?q.call(arguments):e,d===b?i.notifyWith(c,d):--h||i.resolveWith(c,d)}};if(g>1)for(b=new Array(g),c=new Array(g),d=new Array(g);g>e;e++)f[e]&&A.isFunction(f[e].promise)?f[e].promise().done(j(e,d,f)).fail(i.reject).progress(j(e,c,b)):--h;return h||i.resolveWith(d,f),i.promise()}});var L;A.fn.ready=function(a){return A.ready.promise().done(a),this},A.extend({isReady:!1,readyWait:1,holdReady:function(a){a?A.readyWait++:A.ready(!0)},ready:function(a){(a===!0?--A.readyWait:A.isReady)||(A.isReady=!0,a!==!0&&--A.readyWait>0||(L.resolveWith(y,[A]),A.fn.triggerHandler&&(A(y).triggerHandler("ready"),A(y).off("ready"))))}}),A.ready.promise=function(b){return L||(L=A.Deferred(),"complete"===y.readyState?setTimeout(A.ready):(y.addEventListener("DOMContentLoaded",d,!1),a.addEventListener("load",d,!1))),L.promise(b)},A.ready.promise();var M=A.access=function(a,b,c,d,e,f,g){var h=0,i=a.length,j=null==c;if("object"===A.type(c)){e=!0;for(h in c)A.access(a,b,h,c[h],!0,f,g)}else if(void 0!==d&&(e=!0,A.isFunction(d)||(g=!0),j&&(g?(b.call(a,d),b=null):(j=b,b=function(a,b,c){return j.call(A(a),c)})),b))for(;i>h;h++)b(a[h],c,g?d:d.call(a[h],h,b(a[h],c)));return e?a:j?b.call(a):i?b(a[0],c):f};A.acceptData=function(a){return 1===a.nodeType||9===a.nodeType||!+a.nodeType},e.uid=1,e.accepts=A.acceptData,e.prototype={key:function(a){if(!e.accepts(a))return 0;var b={},c=a[this.expando];if(!c){c=e.uid++;try{b[this.expando]={value:c},Object.defineProperties(a,b)}catch(d){b[this.expando]=c,A.extend(a,b)}}return this.cache[c]||(this.cache[c]={}),c},set:function(a,b,c){var d,e=this.key(a),f=this.cache[e];if("string"==typeof b)f[b]=c;else if(A.isEmptyObject(f))A.extend(this.cache[e],b);else for(d in b)f[d]=b[d];return f},get:function(a,b){var c=this.cache[this.key(a)];return void 0===b?c:c[b]},access:function(a,b,c){var d;return void 0===b||b&&"string"==typeof b&&void 0===c?(d=this.get(a,b),void 0!==d?d:this.get(a,A.camelCase(b))):(this.set(a,b,c),void 0!==c?c:b)},remove:function(a,b){var c,d,e,f=this.key(a),g=this.cache[f];if(void 0===b)this.cache[f]={};else{A.isArray(b)?d=b.concat(b.map(A.camelCase)):(e=A.camelCase(b),b in g?d=[b,e]:(d=e,d=d in g?[d]:d.match(J)||[])),c=d.length;for(;c--;)delete g[d[c]]}},hasData:function(a){return!A.isEmptyObject(this.cache[a[this.expando]]||{})},discard:function(a){a[this.expando]&&delete this.cache[a[this.expando]]}};var N=new e,O=/^(?:\{[\w\W]*\}|\[[\w\W]*\])$/,P=/([A-Z])/g;A.extend({hasData:function(a){return data_user.hasData(a)||N.hasData(a)},data:function(a,b,c){return data_user.access(a,b,c)},removeData:function(a,b){data_user.remove(a,b)},_data:function(a,b,c){return N.access(a,b,c)},_removeData:function(a,b){N.remove(a,b)}}),A.fn.extend({data:function(a,b){var c,d,e,g=this[0],h=g&&g.attributes;if(void 0===a){if(this.length&&(e=data_user.get(g),1===g.nodeType&&!N.get(g,"hasDataAttrs"))){for(c=h.length;c--;)h[c]&&(d=h[c].name,0===d.indexOf("data-")&&(d=A.camelCase(d.slice(5)),f(g,d,e[d])));N.set(g,"hasDataAttrs",!0)}return e}return"object"==typeof a?this.each(function(){data_user.set(this,a)}):M(this,function(b){var c,d=A.camelCase(a);if(g&&void 0===b){if(c=data_user.get(g,a),void 0!==c)return c;if(c=data_user.get(g,d),void 0!==c)return c;if(c=f(g,d,void 0),void 0!==c)return c}else this.each(function(){var c=data_user.get(this,d);data_user.set(this,d,b),-1!==a.indexOf("-")&&void 0!==c&&data_user.set(this,a,b)})},null,b,arguments.length>1,null,!0)},removeData:function(a){return this.each(function(){data_user.remove(this,a)})}});var Q=(/[+-]?(?:\d*\.|)\d+(?:[eE][+-]?\d+|)/.source,"undefined"),R=/^key/,S=/^(?:mouse|pointer|contextmenu)|click/,T=/^(?:focusinfocus|focusoutblur)$/,U=/^([^.]*)(?:\.(.+)|)$/;A.event={global:{},add:function(a,b,c,d,e){var f,g,h,i,j,k,l,m,n,o,p,q=N.get(a);if(q)for(c.handler&&(f=c,c=f.handler,e=f.selector),c.guid||(c.guid=A.guid++),(i=q.events)||(i=q.events={}),(g=q.handle)||(g=q.handle=function(b){return typeof A!==Q&&A.event.triggered!==b.type?A.event.dispatch.apply(a,arguments):void 0}),b=(b||"").match(J)||[""],j=b.length;j--;)h=U.exec(b[j])||[],n=p=h[1],o=(h[2]||"").split(".").sort(),n&&(l=A.event.special[n]||{},n=(e?l.delegateType:l.bindType)||n,l=A.event.special[n]||{},k=A.extend({type:n,origType:p,data:d,handler:c,guid:c.guid,selector:e,needsContext:e&&A.expr.match.needsContext.test(e),namespace:o.join(".")},f),(m=i[n])||(m=i[n]=[],m.delegateCount=0,l.setup&&l.setup.call(a,d,o,g)!==!1||a.addEventListener&&a.addEventListener(n,g,!1)),l.add&&(l.add.call(a,k),k.handler.guid||(k.handler.guid=c.guid)),e?m.splice(m.delegateCount++,0,k):m.push(k),A.event.global[n]=!0)},remove:function(a,b,c,d,e){var f,g,h,i,j,k,l,m,n,o,p,q=N.hasData(a)&&N.get(a);if(q&&(i=q.events)){for(b=(b||"").match(J)||[""],j=b.length;j--;)if(h=U.exec(b[j])||[],n=p=h[1],o=(h[2]||"").split(".").sort(),n){for(l=A.event.special[n]||{},n=(d?l.delegateType:l.bindType)||n,m=i[n]||[],h=h[2]&&new RegExp("(^|\\.)"+o.join("\\.(?:.*\\.|)")+"(\\.|$)"),g=f=m.length;f--;)k=m[f],!e&&p!==k.origType||c&&c.guid!==k.guid||h&&!h.test(k.namespace)||d&&d!==k.selector&&("**"!==d||!k.selector)||(m.splice(f,1),k.selector&&m.delegateCount--,l.remove&&l.remove.call(a,k));g&&!m.length&&(l.teardown&&l.teardown.call(a,o,q.handle)!==!1||A.removeEvent(a,n,q.handle),delete i[n])}else for(n in i)A.event.remove(a,n+b[j],c,d,!0);A.isEmptyObject(i)&&(delete q.handle,N.remove(a,"events"))}},trigger:function(b,c,d,e){var f,g,h,i,j,k,l,m=[d||y],n=w.call(b,"type")?b.type:b,o=w.call(b,"namespace")?b.namespace.split("."):[];if(g=h=d=d||y,3!==d.nodeType&&8!==d.nodeType&&!T.test(n+A.event.triggered)&&(n.indexOf(".")>=0&&(o=n.split("."),n=o.shift(),o.sort()),j=n.indexOf(":")<0&&"on"+n,b=b[A.expando]?b:new A.Event(n,"object"==typeof b&&b),b.isTrigger=e?2:3,b.namespace=o.join("."),b.namespace_re=b.namespace?new RegExp("(^|\\.)"+o.join("\\.(?:.*\\.|)")+"(\\.|$)"):null,b.result=void 0,b.target||(b.target=d),c=null==c?[b]:A.makeArray(c,[b]),l=A.event.special[n]||{},e||!l.trigger||l.trigger.apply(d,c)!==!1)){if(!e&&!l.noBubble&&!A.isWindow(d)){for(i=l.delegateType||n,T.test(i+n)||(g=g.parentNode);g;g=g.parentNode)m.push(g),h=g;h===(d.ownerDocument||y)&&m.push(h.defaultView||h.parentWindow||a)}for(f=0;(g=m[f++])&&!b.isPropagationStopped();)b.type=f>1?i:l.bindType||n,k=(N.get(g,"events")||{})[b.type]&&N.get(g,"handle"),k&&k.apply(g,c),k=j&&g[j],k&&k.apply&&A.acceptData(g)&&(b.result=k.apply(g,c),b.result===!1&&b.preventDefault());return b.type=n,e||b.isDefaultPrevented()||l._default&&l._default.apply(m.pop(),c)!==!1||!A.acceptData(d)||j&&A.isFunction(d[n])&&!A.isWindow(d)&&(h=d[j],h&&(d[j]=null),A.event.triggered=n,d[n](),A.event.triggered=void 0,h&&(d[j]=h)),b.result
}},dispatch:function(a){a=A.event.fix(a);var b,c,d,e,f,g=[],h=q.call(arguments),i=(N.get(this,"events")||{})[a.type]||[],j=A.event.special[a.type]||{};if(h[0]=a,a.delegateTarget=this,!j.preDispatch||j.preDispatch.call(this,a)!==!1){for(g=A.event.handlers.call(this,a,i),b=0;(e=g[b++])&&!a.isPropagationStopped();)for(a.currentTarget=e.elem,c=0;(f=e.handlers[c++])&&!a.isImmediatePropagationStopped();)(!a.namespace_re||a.namespace_re.test(f.namespace))&&(a.handleObj=f,a.data=f.data,d=((A.event.special[f.origType]||{}).handle||f.handler).apply(e.elem,h),void 0!==d&&(a.result=d)===!1&&(a.preventDefault(),a.stopPropagation()));return j.postDispatch&&j.postDispatch.call(this,a),a.result}},handlers:function(a,b){var c,d,e,f,g=[],h=b.delegateCount,i=a.target;if(h&&i.nodeType&&(!a.button||"click"!==a.type))for(;i!==this;i=i.parentNode||this)if(i.disabled!==!0||"click"!==a.type){for(d=[],c=0;h>c;c++)f=b[c],e=f.selector+" ",void 0===d[e]&&(d[e]=f.needsContext?A(e,this).index(i)>=0:A.find(e,this,null,[i]).length),d[e]&&d.push(f);d.length&&g.push({elem:i,handlers:d})}return h<b.length&&g.push({elem:this,handlers:b.slice(h)}),g},props:"altKey bubbles cancelable ctrlKey currentTarget eventPhase metaKey relatedTarget shiftKey target timeStamp view which".split(" "),fixHooks:{},keyHooks:{props:"char charCode key keyCode".split(" "),filter:function(a,b){return null==a.which&&(a.which=null!=b.charCode?b.charCode:b.keyCode),a}},mouseHooks:{props:"button buttons clientX clientY offsetX offsetY pageX pageY screenX screenY toElement".split(" "),filter:function(a,b){var c,d,e,f=b.button;return null==a.pageX&&null!=b.clientX&&(c=a.target.ownerDocument||y,d=c.documentElement,e=c.body,a.pageX=b.clientX+(d&&d.scrollLeft||e&&e.scrollLeft||0)-(d&&d.clientLeft||e&&e.clientLeft||0),a.pageY=b.clientY+(d&&d.scrollTop||e&&e.scrollTop||0)-(d&&d.clientTop||e&&e.clientTop||0)),a.which||void 0===f||(a.which=1&f?1:2&f?3:4&f?2:0),a}},fix:function(a){if(a[A.expando])return a;var b,c,d,e=a.type,f=a,g=this.fixHooks[e];for(g||(this.fixHooks[e]=g=S.test(e)?this.mouseHooks:R.test(e)?this.keyHooks:{}),d=g.props?this.props.concat(g.props):this.props,a=new A.Event(f),b=d.length;b--;)c=d[b],a[c]=f[c];return a.target||(a.target=y),3===a.target.nodeType&&(a.target=a.target.parentNode),g.filter?g.filter(a,f):a},special:{load:{noBubble:!0},focus:{trigger:function(){return this!==i()&&this.focus?(this.focus(),!1):void 0},delegateType:"focusin"},blur:{trigger:function(){return this===i()&&this.blur?(this.blur(),!1):void 0},delegateType:"focusout"},click:{trigger:function(){return"checkbox"===this.type&&this.click&&A.nodeName(this,"input")?(this.click(),!1):void 0},_default:function(a){return A.nodeName(a.target,"a")}},beforeunload:{postDispatch:function(a){void 0!==a.result&&a.originalEvent&&(a.originalEvent.returnValue=a.result)}}},simulate:function(a,b,c,d){var e=A.extend(new A.Event,c,{type:a,isSimulated:!0,originalEvent:{}});d?A.event.trigger(e,null,b):A.event.dispatch.call(b,e),e.isDefaultPrevented()&&c.preventDefault()}},A.removeEvent=function(a,b,c){a.removeEventListener&&a.removeEventListener(b,c,!1)},A.Event=function(a,b){return this instanceof A.Event?(a&&a.type?(this.originalEvent=a,this.type=a.type,this.isDefaultPrevented=a.defaultPrevented||void 0===a.defaultPrevented&&a.returnValue===!1?g:h):this.type=a,b&&A.extend(this,b),this.timeStamp=a&&a.timeStamp||A.now(),void(this[A.expando]=!0)):new A.Event(a,b)},A.Event.prototype={isDefaultPrevented:h,isPropagationStopped:h,isImmediatePropagationStopped:h,preventDefault:function(){var a=this.originalEvent;this.isDefaultPrevented=g,a&&a.preventDefault&&a.preventDefault()},stopPropagation:function(){var a=this.originalEvent;this.isPropagationStopped=g,a&&a.stopPropagation&&a.stopPropagation()},stopImmediatePropagation:function(){var a=this.originalEvent;this.isImmediatePropagationStopped=g,a&&a.stopImmediatePropagation&&a.stopImmediatePropagation(),this.stopPropagation()}},A.each({mouseenter:"mouseover",mouseleave:"mouseout",pointerenter:"pointerover",pointerleave:"pointerout"},function(a,b){A.event.special[a]={delegateType:b,bindType:b,handle:function(a){var c,d=this,e=a.relatedTarget,f=a.handleObj;return(!e||e!==d&&!A.contains(d,e))&&(a.type=f.origType,c=f.handler.apply(this,arguments),a.type=b),c}}}),x.focusinBubbles||A.each({focus:"focusin",blur:"focusout"},function(a,b){var c=function(a){A.event.simulate(b,a.target,A.event.fix(a),!0)};A.event.special[b]={setup:function(){var d=this.ownerDocument||this,e=N.access(d,b);e||d.addEventListener(a,c,!0),N.access(d,b,(e||0)+1)},teardown:function(){var d=this.ownerDocument||this,e=N.access(d,b)-1;e?N.access(d,b,e):(d.removeEventListener(a,c,!0),N.remove(d,b))}}}),A.fn.extend({on:function(a,b,c,d,e){var f,g;if("object"==typeof a){"string"!=typeof b&&(c=c||b,b=void 0);for(g in a)this.on(g,b,c,a[g],e);return this}if(null==c&&null==d?(d=b,c=b=void 0):null==d&&("string"==typeof b?(d=c,c=void 0):(d=c,c=b,b=void 0)),d===!1)d=h;else if(!d)return this;return 1===e&&(f=d,d=function(a){return A().off(a),f.apply(this,arguments)},d.guid=f.guid||(f.guid=A.guid++)),this.each(function(){A.event.add(this,a,d,c,b)})},one:function(a,b,c,d){return this.on(a,b,c,d,1)},off:function(a,b,c){var d,e;if(a&&a.preventDefault&&a.handleObj)return d=a.handleObj,A(a.delegateTarget).off(d.namespace?d.origType+"."+d.namespace:d.origType,d.selector,d.handler),this;if("object"==typeof a){for(e in a)this.off(e,b,a[e]);return this}return(b===!1||"function"==typeof b)&&(c=b,b=void 0),c===!1&&(c=h),this.each(function(){A.event.remove(this,a,c,b)})},trigger:function(a,b){return this.each(function(){A.event.trigger(a,b,this)})},triggerHandler:function(a,b){var c=this[0];return c?A.event.trigger(a,b,c,!0):void 0}});var V=A.now(),W=/\?/;A.parseJSON=function(a){return JSON.parse(a+"")},A.parseXML=function(a){var b,c;if(!a||"string"!=typeof a)return null;try{c=new DOMParser,b=c.parseFromString(a,"text/xml")}catch(d){b=void 0}return(!b||b.getElementsByTagName("parsererror").length)&&A.error("Invalid XML: "+a),b};var X,Y,Z=/#.*$/,$=/([?&])_=[^&]*/,_=/^(.*?):[ \t]*([^\r\n]*)$/gm,ab=/^(?:about|app|app-storage|.+-extension|file|res|widget):$/,bb=/^(?:GET|HEAD)$/,cb=/^\/\//,db=/^([\w.+-]+:)(?:\/\/(?:[^\/?#]*@|)([^\/?#:]*)(?::(\d+)|)|)/,eb={},fb={},gb="*/".concat("*");try{Y=location.href}catch(hb){Y=y.createElement("a"),Y.href="",Y=Y.href}X=db.exec(Y.toLowerCase())||[],A.extend({active:0,lastModified:{},etag:{},ajaxSettings:{url:Y,type:"GET",isLocal:ab.test(X[1]),global:!0,processData:!0,async:!0,contentType:"application/x-www-form-urlencoded; charset=UTF-8",accepts:{"*":gb,text:"text/plain",html:"text/html",xml:"application/xml, text/xml",json:"application/json, text/javascript"},contents:{xml:/xml/,html:/html/,json:/json/},responseFields:{xml:"responseXML",text:"responseText",json:"responseJSON"},converters:{"* text":String,"text html":!0,"text json":A.parseJSON,"text xml":A.parseXML},flatOptions:{url:!0,context:!0}},ajaxSetup:function(a,b){return b?l(l(a,A.ajaxSettings),b):l(A.ajaxSettings,a)},ajaxPrefilter:j(eb),ajaxTransport:j(fb),ajax:function(a,b){function c(a,b,c,g){var i,k,l,u,v,x=b;2!==w&&(w=2,h&&clearTimeout(h),d=void 0,f=g||"",y.readyState=a>0?4:0,i=a>=200&&300>a||304===a,c&&(u=m(o,y,c)),u=n(o,u,y,i),i?(o.ifModified&&(v=y.getResponseHeader("Last-Modified"),v&&(A.lastModified[e]=v),v=y.getResponseHeader("etag"),v&&(A.etag[e]=v)),204===a||"HEAD"===o.type?x="nocontent":304===a?x="notmodified":(x=u.state,k=u.data,l=u.error,i=!l)):(l=x,(a||!x)&&(x="error",0>a&&(a=0))),y.status=a,y.statusText=(b||x)+"",i?r.resolveWith(p,[k,x,y]):r.rejectWith(p,[y,x,l]),y.statusCode(t),t=void 0,j&&q.trigger(i?"ajaxSuccess":"ajaxError",[y,o,i?k:l]),s.fireWith(p,[y,x]),j&&(q.trigger("ajaxComplete",[y,o]),--A.active||A.event.trigger("ajaxStop")))}"object"==typeof a&&(b=a,a=void 0),b=b||{};var d,e,f,g,h,i,j,l,o=A.ajaxSetup({},b),p=o.context||o,q=o.context&&(p.nodeType||p.jquery)?A(p):A.event,r=A.Deferred(),s=A.Callbacks("once memory"),t=o.statusCode||{},u={},v={},w=0,x="canceled",y={readyState:0,getResponseHeader:function(a){var b;if(2===w){if(!g)for(g={};b=_.exec(f);)g[b[1].toLowerCase()]=b[2];b=g[a.toLowerCase()]}return null==b?null:b},getAllResponseHeaders:function(){return 2===w?f:null},setRequestHeader:function(a,b){var c=a.toLowerCase();return w||(a=v[c]=v[c]||a,u[a]=b),this},overrideMimeType:function(a){return w||(o.mimeType=a),this},statusCode:function(a){var b;if(a)if(2>w)for(b in a)t[b]=[t[b],a[b]];else y.always(a[y.status]);return this},abort:function(a){var b=a||x;return d&&d.abort(b),c(0,b),this}};if(r.promise(y).complete=s.add,y.success=y.done,y.error=y.fail,o.url=((a||o.url||Y)+"").replace(Z,"").replace(cb,X[1]+"//"),o.type=b.method||b.type||o.method||o.type,o.dataTypes=A.trim(o.dataType||"*").toLowerCase().match(J)||[""],null==o.crossDomain&&(i=db.exec(o.url.toLowerCase()),o.crossDomain=!(!i||i[1]===X[1]&&i[2]===X[2]&&(i[3]||("http:"===i[1]?"80":"443"))===(X[3]||("http:"===X[1]?"80":"443")))),o.data&&o.processData&&"string"!=typeof o.data&&(o.data=A.param(o.data,o.traditional)),k(eb,o,b,y),2===w)return y;j=o.global,j&&0===A.active++&&A.event.trigger("ajaxStart"),o.type=o.type.toUpperCase(),o.hasContent=!bb.test(o.type),e=o.url,o.hasContent||(o.data&&(e=o.url+=(W.test(e)?"&":"?")+o.data,delete o.data),o.cache===!1&&(o.url=$.test(e)?e.replace($,"$1_="+V++):e+(W.test(e)?"&":"?")+"_="+V++)),o.ifModified&&(A.lastModified[e]&&y.setRequestHeader("If-Modified-Since",A.lastModified[e]),A.etag[e]&&y.setRequestHeader("If-None-Match",A.etag[e])),(o.data&&o.hasContent&&o.contentType!==!1||b.contentType)&&y.setRequestHeader("Content-Type",o.contentType),y.setRequestHeader("Accept",o.dataTypes[0]&&o.accepts[o.dataTypes[0]]?o.accepts[o.dataTypes[0]]+("*"!==o.dataTypes[0]?", "+gb+"; q=0.01":""):o.accepts["*"]);for(l in o.headers)y.setRequestHeader(l,o.headers[l]);if(o.beforeSend&&(o.beforeSend.call(p,y,o)===!1||2===w))return y.abort();x="abort";for(l in{success:1,error:1,complete:1})y[l](o[l]);if(d=k(fb,o,b,y)){y.readyState=1,j&&q.trigger("ajaxSend",[y,o]),o.async&&o.timeout>0&&(h=setTimeout(function(){y.abort("timeout")},o.timeout));try{w=1,d.send(u,c)}catch(z){if(!(2>w))throw z;c(-1,z)}}else c(-1,"No Transport");return y},getJSON:function(a,b,c){return A.get(a,b,c,"json")},getScript:function(a,b){return A.get(a,void 0,b,"script")}}),A.each(["get","post"],function(a,b){A[b]=function(a,c,d,e){return A.isFunction(c)&&(e=e||d,d=c,c=void 0),A.ajax({url:a,type:b,dataType:e,data:c,success:d})}}),A.each(["ajaxStart","ajaxStop","ajaxComplete","ajaxError","ajaxSuccess","ajaxSend"],function(a,b){A.fn[b]=function(a){return this.on(b,a)}});var ib=/%20/g,jb=/\[\]$/,kb=/\r?\n/g,lb=/^(?:submit|button|image|reset|file)$/i,mb=/^(?:input|select|textarea|keygen)/i;A.param=function(a,b){var c,d=[],e=function(a,b){b=A.isFunction(b)?b():null==b?"":b,d[d.length]=encodeURIComponent(a)+"="+encodeURIComponent(b)};if(void 0===b&&(b=A.ajaxSettings&&A.ajaxSettings.traditional),A.isArray(a)||a.jquery&&!A.isPlainObject(a))A.each(a,function(){e(this.name,this.value)});else for(c in a)o(c,a[c],b,e);return d.join("&").replace(ib,"+")},A.fn.extend({serialize:function(){return A.param(this.serializeArray())},serializeArray:function(){return this.map(function(){var a=A.prop(this,"elements");return a?A.makeArray(a):this}).filter(function(){var a=this.type;return this.name&&!A(this).is(":disabled")&&mb.test(this.nodeName)&&!lb.test(a)&&(this.checked||!rcheckableType.test(a))}).map(function(a,b){var c=A(this).val();return null==c?null:A.isArray(c)?A.map(c,function(a){return{name:b.name,value:a.replace(kb,"\r\n")}}):{name:b.name,value:c.replace(kb,"\r\n")}}).get()}}),A.ajaxSettings.xhr=function(){try{return new XMLHttpRequest}catch(a){}};var nb=0,ob={},pb={0:200,1223:204},qb=A.ajaxSettings.xhr();a.ActiveXObject&&A(a).on("unload",function(){for(var a in ob)ob[a]()}),x.cors=!!qb&&"withCredentials"in qb,x.ajax=qb=!!qb,A.ajaxTransport(function(a){var b;return x.cors||qb&&!a.crossDomain?{send:function(c,d){var e,f=a.xhr(),g=++nb;if(f.open(a.type,a.url,a.async,a.username,a.password),a.xhrFields)for(e in a.xhrFields)f[e]=a.xhrFields[e];a.mimeType&&f.overrideMimeType&&f.overrideMimeType(a.mimeType),a.crossDomain||c["X-Requested-With"]||(c["X-Requested-With"]="XMLHttpRequest");for(e in c)f.setRequestHeader(e,c[e]);b=function(a){return function(){b&&(delete ob[g],b=f.onload=f.onerror=null,"abort"===a?f.abort():"error"===a?d(f.status,f.statusText):d(pb[f.status]||f.status,f.statusText,"string"==typeof f.responseText?{text:f.responseText}:void 0,f.getAllResponseHeaders()))}},f.onload=b(),f.onerror=b("error"),b=ob[g]=b("abort");try{f.send(a.hasContent&&a.data||null)}catch(h){if(b)throw h}},abort:function(){b&&b()}}:void 0}),A.ajaxSetup({accepts:{script:"text/javascript, application/javascript, application/ecmascript, application/x-ecmascript"},contents:{script:/(?:java|ecma)script/},converters:{"text script":function(a){return A.globalEval(a),a}}}),A.ajaxPrefilter("script",function(a){void 0===a.cache&&(a.cache=!1),a.crossDomain&&(a.type="GET")}),A.ajaxTransport("script",function(a){if(a.crossDomain){var b,c;return{send:function(d,e){b=A("<script>").prop({async:!0,charset:a.scriptCharset,src:a.url}).on("load error",c=function(a){b.remove(),c=null,a&&e("error"===a.type?404:200,a.type)}),y.head.appendChild(b[0])},abort:function(){c&&c()}}}});var rb=[],sb=/(=)\?(?=&|$)|\?\?/;A.ajaxSetup({jsonp:"callback",jsonpCallback:function(){var a=rb.pop()||A.expando+"_"+V++;return this[a]=!0,a}}),A.ajaxPrefilter("json jsonp",function(b,c,d){var e,f,g,h=b.jsonp!==!1&&(sb.test(b.url)?"url":"string"==typeof b.data&&!(b.contentType||"").indexOf("application/x-www-form-urlencoded")&&sb.test(b.data)&&"data");return h||"jsonp"===b.dataTypes[0]?(e=b.jsonpCallback=A.isFunction(b.jsonpCallback)?b.jsonpCallback():b.jsonpCallback,h?b[h]=b[h].replace(sb,"$1"+e):b.jsonp!==!1&&(b.url+=(W.test(b.url)?"&":"?")+b.jsonp+"="+e),b.converters["script json"]=function(){return g||A.error(e+" was not called"),g[0]},b.dataTypes[0]="json",f=a[e],a[e]=function(){g=arguments},d.always(function(){a[e]=f,b[e]&&(b.jsonpCallback=c.jsonpCallback,rb.push(e)),g&&A.isFunction(f)&&f(g[0]),g=f=void 0}),"script"):void 0}),A.parseHTML=function(a,b,c){if(!a||"string"!=typeof a)return null;"boolean"==typeof b&&(c=b,b=!1),b=b||y;var d=G.exec(a),e=!c&&[];return d?[b.createElement(d[1])]:(d=A.buildFragment([a],b,e),e&&e.length&&A(e).remove(),A.merge([],d.childNodes))};var tb=A.fn.load;return A.fn.load=function(a,b,c){if("string"!=typeof a&&tb)return tb.apply(this,arguments);var d,e,f,g=this,h=a.indexOf(" ");return h>=0&&(d=A.trim(a.slice(h)),a=a.slice(0,h)),A.isFunction(b)?(c=b,b=void 0):b&&"object"==typeof b&&(e="POST"),g.length>0&&A.ajax({url:a,type:e,dataType:"html",data:b}).done(function(a){f=arguments,g.html(d?A("<div>").append(A.parseHTML(a)).find(d):a)}).complete(c&&function(a,b){g.each(c,f||[a.responseText,b,a])}),this},A.noConflict=function(){},A})},{}],8:[function(a,b){var c,d;d=0,c="",b.exports={hex_sha1:function(a){return this.rstr2hex(this.rstr_sha1(this.str2rstr_utf8(a)))},b64_sha1:function(a){return this.rstr2b64(this.rstr_sha1(this.str2rstr_utf8(a)))},any_sha1:function(a,b){return this.rstr2any(this.rstr_sha1(this.str2rstr_utf8(a)),b)},hex_hmac_sha1:function(a,b){return this.rstr2hex(this.rstr_hmac_sha1(this.str2rstr_utf8(a),this.str2rstr_utf8(b)))},b64_hmac_sha1:function(a,b){return this.rstr2b64(this.rstr_hmac_sha1(this.str2rstr_utf8(a),this.str2rstr_utf8(b)))},any_hmac_sha1:function(a,b,c){return this.rstr2any(this.rstr_hmac_sha1(this.str2rstr_utf8(a),this.str2rstr_utf8(b)),c)},sha1_vm_test:function(){return"a9993e364706816aba3e25717850c26c9cd0d89d"===thishex_sha1("abc").toLowerCase()},rstr_sha1:function(a){return this.binb2rstr(this.binb_sha1(this.rstr2binb(a),8*a.length))},rstr_hmac_sha1:function(a,b){var c,d,e,f,g;for(c=this.rstr2binb(a),c.length>16&&(c=this.binb_sha1(c,8*a.length)),f=Array(16),g=Array(16),e=0;16>e;)f[e]=909522486^c[e],g[e]=1549556828^c[e],e++;return d=this.binb_sha1(f.concat(this.rstr2binb(b)),512+8*b.length),this.binb2rstr(this.binb_sha1(g.concat(d),672))},rstr2hex:function(a){var b,c,e,f,g;try{}catch(h){b=h,d=0}for(c=d?"0123456789ABCDEF":"0123456789abcdef",f="",g=void 0,e=0;e<a.length;)g=a.charCodeAt(e),f+=c.charAt(g>>>4&15)+c.charAt(15&g),e++;return f},rstr2b64:function(a){var b,d,e,f,g,h,i;try{}catch(j){b=j,c=""}for(h="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/",g="",f=a.length,d=0;f>d;){for(i=a.charCodeAt(d)<<16|(f>d+1?a.charCodeAt(d+1)<<8:0)|(f>d+2?a.charCodeAt(d+2):0),e=0;4>e;)g+=8*d+6*e>8*a.length?c:h.charAt(i>>>6*(3-e)&63),e++;d+=3}return g},rstr2any:function(a,b){var c,d,e,f,g,h,i,j,k;for(d=b.length,j=Array(),f=void 0,h=void 0,k=void 0,i=void 0,c=Array(Math.ceil(a.length/2)),f=0;f<c.length;)c[f]=a.charCodeAt(2*f)<<8|a.charCodeAt(2*f+1),f++;for(;c.length>0;){for(i=Array(),k=0,f=0;f<c.length;)k=(k<<16)+c[f],h=Math.floor(k/d),k-=h*d,(i.length>0||h>0)&&(i[i.length]=h),f++;j[j.length]=k,c=i}for(g="",f=j.length-1;f>=0;)g+=b.charAt(j[f]),f--;for(e=Math.ceil(8*a.length/(Math.log(b.length)/Math.log(2))),f=g.length;e>f;)g=b[0]+g,f++;return g},str2rstr_utf8:function(a){var b,c,d,e;for(c="",b=-1,d=void 0,e=void 0;++b<a.length;)d=a.charCodeAt(b),e=b+1<a.length?a.charCodeAt(b+1):0,d>=55296&&56319>=d&&e>=56320&&57343>=e&&(d=65536+((1023&d)<<10)+(1023&e),b++),127>=d?c+=String.fromCharCode(d):2047>=d?c+=String.fromCharCode(192|d>>>6&31,128|63&d):65535>=d?c+=String.fromCharCode(224|d>>>12&15,128|d>>>6&63,128|63&d):2097151>=d&&(c+=String.fromCharCode(240|d>>>18&7,128|d>>>12&63,128|d>>>6&63,128|63&d));return c},str2rstr_utf16le:function(a){var b,c;for(c="",b=0;b<a.length;)c+=String.fromCharCode(255&a.charCodeAt(b),a.charCodeAt(b)>>>8&255),b++;return c},str2rstr_utf16be:function(a){var b,c;for(c="",b=0;b<a.length;)c+=String.fromCharCode(a.charCodeAt(b)>>>8&255,255&a.charCodeAt(b)),b++;return c},rstr2binb:function(a){var b,c;for(c=Array(a.length>>2),b=0;b<c.length;)c[b]=0,b++;for(b=0;b<8*a.length;)c[b>>5]|=(255&a.charCodeAt(b/8))<<24-b%32,b+=8;return c},binb2rstr:function(a){var b,c;for(c="",b=0;b<32*a.length;)c+=String.fromCharCode(a[b>>5]>>>24-b%32&255),b+=8;return c},binb_sha1:function(a,b){var c,d,e,f,g,h,i,j,k,l,m,n,o,p;for(a[b>>5]|=128<<24-b%32,a[(b+64>>9<<4)+15]=b,p=Array(80),c=1732584193,d=-271733879,e=-1732584194,f=271733878,g=-1009589776,h=0;h<a.length;){for(j=c,k=d,l=e,m=f,n=g,i=0;80>i;)p[i]=16>i?a[h+i]:this.bit_rol(p[i-3]^p[i-8]^p[i-14]^p[i-16],1),o=this.safe_add(this.safe_add(this.bit_rol(c,5),this.sha1_ft(i,d,e,f)),this.safe_add(this.safe_add(g,p[i]),this.sha1_kt(i))),g=f,f=e,e=this.bit_rol(d,30),d=c,c=o,i++;c=this.safe_add(c,j),d=this.safe_add(d,k),e=this.safe_add(e,l),f=this.safe_add(f,m),g=this.safe_add(g,n),h+=16}return Array(c,d,e,f,g)},sha1_ft:function(a,b,c,d){return 20>a?b&c|~b&d:40>a?b^c^d:60>a?b&c|b&d|c&d:b^c^d},sha1_kt:function(a){return 20>a?1518500249:40>a?1859775393:60>a?-1894007588:-899497514},safe_add:function(a,b){var c,d;return c=(65535&a)+(65535&b),d=(a>>16)+(b>>16)+(c>>16),d<<16|65535&c},bit_rol:function(a,b){return a<<b|a>>>32-b},create_hash:function(){var a;return a=this.b64_sha1((new Date).getTime()+":"+Math.floor(9999999*Math.random())),a.replace(/\+/g,"-").replace(/\//g,"_").replace(/\=+$/,"")}}},{}],9:[function(a,b){b.exports=function(a){return{getAbsUrl:function(b){var c;return b.match(/^.{2,5}:\/\//)?b:"/"===b[0]?a.location.protocol+"//"+a.location.host+b:(c=a.location.protocol+"//"+a.location.host+a.location.pathname,"/"!==c[c.length-1]&&"#"!==b[0]?c+"/"+b:c+b)},replaceParam:function(a,b,c){return a=a.replace(/\{\{(.*?)\}\}/g,function(a,c){return b[c]||""}),c&&(a=a.replace(/\{(.*?)\}/g,function(a,b){return c[b]||""})),a}}}},{}],10:[function(a,b){var c=b.exports={};c.nextTick=function(){var a="undefined"!=typeof window&&window.setImmediate,b="undefined"!=typeof window&&window.postMessage&&window.addEventListener;if(a)return function(a){return window.setImmediate(a)};if(b){var c=[];return window.addEventListener("message",function(a){var b=a.source;if((b===window||null===b)&&"process-tick"===a.data&&(a.stopPropagation(),c.length>0)){var d=c.shift();d()}},!0),function(a){c.push(a),window.postMessage("process-tick","*")}}return function(a){setTimeout(a,0)}}(),c.title="browser",c.browser=!0,c.env={},c.argv=[],c.binding=function(){throw new Error("process.binding is not supported")},c.cwd=function(){return"/"},c.chdir=function(){throw new Error("process.chdir is not supported")}},{}],11:[function(a,b,c){(function(a){!function(a){if("function"==typeof bootstrap)bootstrap("promise",a);else if("object"==typeof c)b.exports=a();else if("function"==typeof define&&define.amd)define(a);else if("undefined"!=typeof ses){if(!ses.ok())return;ses.makeQ=a}else Q=a()}(function(){"use strict";function b(a){return function(){return W.apply(a,arguments)}}function c(a){return a===Object(a)}function d(a){return"[object StopIteration]"===cb(a)||a instanceof S}function e(a,b){if(P&&b.stack&&"object"==typeof a&&null!==a&&a.stack&&-1===a.stack.indexOf(db)){for(var c=[],d=b;d;d=d.source)d.stack&&c.unshift(d.stack);c.unshift(a.stack);var e=c.join("\n"+db+"\n");a.stack=f(e)}}function f(a){for(var b=a.split("\n"),c=[],d=0;d<b.length;++d){var e=b[d];i(e)||g(e)||!e||c.push(e)}return c.join("\n")}function g(a){return-1!==a.indexOf("(module.js:")||-1!==a.indexOf("(node.js:")}function h(a){var b=/at .+ \((.+):(\d+):(?:\d+)\)$/.exec(a);if(b)return[b[1],Number(b[2])];var c=/at ([^ ]+):(\d+):(?:\d+)$/.exec(a);if(c)return[c[1],Number(c[2])];var d=/.*@(.+):(\d+)$/.exec(a);return d?[d[1],Number(d[2])]:void 0}function i(a){var b=h(a);if(!b)return!1;var c=b[0],d=b[1];return c===R&&d>=T&&hb>=d}function j(){if(P)try{throw new Error}catch(a){var b=a.stack.split("\n"),c=b[0].indexOf("@")>0?b[1]:b[2],d=h(c);if(!d)return;return R=d[0],d[1]}}function k(a,b,c){return function(){return"undefined"!=typeof console&&"function"==typeof console.warn&&console.warn(b+" is deprecated, use "+c+" instead.",new Error("").stack),a.apply(a,arguments)}}function l(a){return s(a)?a:t(a)?C(a):B(a)}function m(){function a(a){b=a,f.source=a,Y(c,function(b,c){V(function(){a.promiseDispatch.apply(a,c)})},void 0),c=void 0,d=void 0}var b,c=[],d=[],e=_(m.prototype),f=_(p.prototype);if(f.promiseDispatch=function(a,e,f){var g=X(arguments);c?(c.push(g),"when"===e&&f[1]&&d.push(f[1])):V(function(){b.promiseDispatch.apply(b,g)})},f.valueOf=function(){if(c)return f;var a=r(b);return s(a)&&(b=a),a},f.inspect=function(){return b?b.inspect():{state:"pending"}},l.longStackSupport&&P)try{throw new Error}catch(g){f.stack=g.stack.substring(g.stack.indexOf("\n")+1)}return e.promise=f,e.resolve=function(c){b||a(l(c))},e.fulfill=function(c){b||a(B(c))},e.reject=function(c){b||a(A(c))},e.notify=function(a){b||Y(d,function(b,c){V(function(){c(a)})},void 0)},e}function n(a){if("function"!=typeof a)throw new TypeError("resolver must be a function.");var b=m();try{a(b.resolve,b.reject,b.notify)}catch(c){b.reject(c)}return b.promise}function o(a){return n(function(b,c){for(var d=0,e=a.length;e>d;d++)l(a[d]).then(b,c)})}function p(a,b,c){void 0===b&&(b=function(a){return A(new Error("Promise does not support operation: "+a))}),void 0===c&&(c=function(){return{state:"unknown"}});var d=_(p.prototype);if(d.promiseDispatch=function(c,e,f){var g;try{g=a[e]?a[e].apply(d,f):b.call(d,e,f)}catch(h){g=A(h)}c&&c(g)},d.inspect=c,c){var e=c();"rejected"===e.state&&(d.exception=e.reason),d.valueOf=function(){var a=c();return"pending"===a.state||"rejected"===a.state?d:a.value}}return d}function q(a,b,c,d){return l(a).then(b,c,d)}function r(a){if(s(a)){var b=a.inspect();if("fulfilled"===b.state)return b.value}return a}function s(a){return c(a)&&"function"==typeof a.promiseDispatch&&"function"==typeof a.inspect}function t(a){return c(a)&&"function"==typeof a.then}function u(a){return s(a)&&"pending"===a.inspect().state}function v(a){return!s(a)||"fulfilled"===a.inspect().state}function w(a){return s(a)&&"rejected"===a.inspect().state}function x(){eb.length=0,fb.length=0,gb||(gb=!0)}function y(a,b){gb&&(fb.push(a),eb.push(b&&"undefined"!=typeof b.stack?b.stack:"(no stack) "+b))}function z(a){if(gb){var b=Z(fb,a);-1!==b&&(fb.splice(b,1),eb.splice(b,1))}}function A(a){var b=p({when:function(b){return b&&z(this),b?b(a):this}},function(){return this},function(){return{state:"rejected",reason:a}});return y(b,a),b}function B(a){return p({when:function(){return a},get:function(b){return a[b]},set:function(b,c){a[b]=c},"delete":function(b){delete a[b]},post:function(b,c){return null===b||void 0===b?a.apply(void 0,c):a[b].apply(a,c)},apply:function(b,c){return a.apply(b,c)},keys:function(){return bb(a)}},void 0,function(){return{state:"fulfilled",value:a}})}function C(a){var b=m();return V(function(){try{a.then(b.resolve,b.reject,b.notify)}catch(c){b.reject(c)}}),b.promise}function D(a){return p({isDef:function(){}},function(b,c){return J(a,b,c)},function(){return l(a).inspect()})}function E(a,b,c){return l(a).spread(b,c)}function F(a){return function(){function b(a,b){var g;if("undefined"==typeof StopIteration){try{g=c[a](b)}catch(h){return A(h)}return g.done?g.value:q(g.value,e,f)}try{g=c[a](b)}catch(h){return d(h)?h.value:A(h)}return q(g,e,f)}var c=a.apply(this,arguments),e=b.bind(b,"next"),f=b.bind(b,"throw");return e()}}function G(a){l.done(l.async(a)())}function H(a){throw new S(a)}function I(a){return function(){return E([this,K(arguments)],function(b,c){return a.apply(b,c)})}}function J(a,b,c){return l(a).dispatch(b,c)}function K(a){return q(a,function(a){var b=0,c=m();return Y(a,function(d,e,f){var g;s(e)&&"fulfilled"===(g=e.inspect()).state?a[f]=g.value:(++b,q(e,function(d){a[f]=d,0===--b&&c.resolve(a)},c.reject,function(a){c.notify({index:f,value:a})}))},void 0),0===b&&c.resolve(a),c.promise})}function L(a){return q(a,function(a){return a=$(a,l),q(K($(a,function(a){return q(a,U,U)})),function(){return a})})}function M(a){return l(a).allSettled()}function N(a,b){return l(a).then(void 0,void 0,b)}function O(a,b){return l(a).nodeify(b)}var P=!1;try{throw new Error}catch(Q){P=!!Q.stack}var R,S,T=j(),U=function(){},V=function(){function b(){for(;c.next;){c=c.next;var a=c.task;c.task=void 0;var d=c.domain;d&&(c.domain=void 0,d.enter());try{a()}catch(f){if(g)throw d&&d.exit(),setTimeout(b,0),d&&d.enter(),f;setTimeout(function(){throw f},0)}d&&d.exit()}e=!1}var c={task:void 0,next:null},d=c,e=!1,f=void 0,g=!1;if(V=function(b){d=d.next={task:b,domain:g&&a.domain,next:null},e||(e=!0,f())},"undefined"!=typeof a&&a.nextTick)g=!0,f=function(){a.nextTick(b)};else if("function"==typeof setImmediate)f="undefined"!=typeof window?setImmediate.bind(window,b):function(){setImmediate(b)};else if("undefined"!=typeof MessageChannel){var h=new MessageChannel;h.port1.onmessage=function(){f=i,h.port1.onmessage=b,b()};var i=function(){h.port2.postMessage(0)};f=function(){setTimeout(b,0),i()}}else f=function(){setTimeout(b,0)};return V}(),W=Function.call,X=b(Array.prototype.slice),Y=b(Array.prototype.reduce||function(a,b){var c=0,d=this.length;if(1===arguments.length)for(;;){if(c in this){b=this[c++];break}if(++c>=d)throw new TypeError}for(;d>c;c++)c in this&&(b=a(b,this[c],c));return b}),Z=b(Array.prototype.indexOf||function(a){for(var b=0;b<this.length;b++)if(this[b]===a)return b;return-1}),$=b(Array.prototype.map||function(a,b){var c=this,d=[];return Y(c,function(e,f,g){d.push(a.call(b,f,g,c))},void 0),d}),_=Object.create||function(a){function b(){}return b.prototype=a,new b},ab=b(Object.prototype.hasOwnProperty),bb=Object.keys||function(a){var b=[];for(var c in a)ab(a,c)&&b.push(c);return b},cb=b(Object.prototype.toString);S="undefined"!=typeof ReturnValue?ReturnValue:function(a){this.value=a};var db="From previous event:";l.resolve=l,l.nextTick=V,l.longStackSupport=!1,l.defer=m,m.prototype.makeNodeResolver=function(){var a=this;return function(b,c){b?a.reject(b):a.resolve(arguments.length>2?X(arguments,1):c)}},l.Promise=n,l.promise=n,n.race=o,n.all=K,n.reject=A,n.resolve=l,l.passByCopy=function(a){return a},p.prototype.passByCopy=function(){return this},l.join=function(a,b){return l(a).join(b)},p.prototype.join=function(a){return l([this,a]).spread(function(a,b){if(a===b)return a;throw new Error("Can't join: not the same: "+a+" "+b)})},l.race=o,p.prototype.race=function(){return this.then(l.race)},l.makePromise=p,p.prototype.toString=function(){return"[object Promise]"},p.prototype.then=function(a,b,c){function d(b){try{return"function"==typeof a?a(b):b}catch(c){return A(c)}}function f(a){if("function"==typeof b){e(a,h);try{return b(a)}catch(c){return A(c)}}return A(a)}function g(a){return"function"==typeof c?c(a):a}var h=this,i=m(),j=!1;return V(function(){h.promiseDispatch(function(a){j||(j=!0,i.resolve(d(a)))},"when",[function(a){j||(j=!0,i.resolve(f(a)))}])}),h.promiseDispatch(void 0,"when",[void 0,function(a){var b,c=!1;try{b=g(a)}catch(d){if(c=!0,!l.onerror)throw d;l.onerror(d)}c||i.notify(b)}]),i.promise},l.when=q,p.prototype.thenResolve=function(a){return this.then(function(){return a})},l.thenResolve=function(a,b){return l(a).thenResolve(b)},p.prototype.thenReject=function(a){return this.then(function(){throw a})},l.thenReject=function(a,b){return l(a).thenReject(b)},l.nearer=r,l.isPromise=s,l.isPromiseAlike=t,l.isPending=u,p.prototype.isPending=function(){return"pending"===this.inspect().state},l.isFulfilled=v,p.prototype.isFulfilled=function(){return"fulfilled"===this.inspect().state},l.isRejected=w,p.prototype.isRejected=function(){return"rejected"===this.inspect().state};var eb=[],fb=[],gb=!0;l.resetUnhandledRejections=x,l.getUnhandledReasons=function(){return eb.slice()},l.stopUnhandledRejectionTracking=function(){x(),gb=!1},x(),l.reject=A,l.fulfill=B,l.master=D,l.spread=E,p.prototype.spread=function(a,b){return this.all().then(function(b){return a.apply(void 0,b)},b)},l.async=F,l.spawn=G,l["return"]=H,l.promised=I,l.dispatch=J,p.prototype.dispatch=function(a,b){var c=this,d=m();return V(function(){c.promiseDispatch(d.resolve,a,b)}),d.promise},l.get=function(a,b){return l(a).dispatch("get",[b])},p.prototype.get=function(a){return this.dispatch("get",[a])},l.set=function(a,b,c){return l(a).dispatch("set",[b,c])},p.prototype.set=function(a,b){return this.dispatch("set",[a,b])},l.del=l["delete"]=function(a,b){return l(a).dispatch("delete",[b])},p.prototype.del=p.prototype["delete"]=function(a){return this.dispatch("delete",[a])},l.mapply=l.post=function(a,b,c){return l(a).dispatch("post",[b,c])},p.prototype.mapply=p.prototype.post=function(a,b){return this.dispatch("post",[a,b])},l.send=l.mcall=l.invoke=function(a,b){return l(a).dispatch("post",[b,X(arguments,2)])},p.prototype.send=p.prototype.mcall=p.prototype.invoke=function(a){return this.dispatch("post",[a,X(arguments,1)])},l.fapply=function(a,b){return l(a).dispatch("apply",[void 0,b])},p.prototype.fapply=function(a){return this.dispatch("apply",[void 0,a])},l["try"]=l.fcall=function(a){return l(a).dispatch("apply",[void 0,X(arguments,1)])},p.prototype.fcall=function(){return this.dispatch("apply",[void 0,X(arguments)])},l.fbind=function(a){var b=l(a),c=X(arguments,1);return function(){return b.dispatch("apply",[this,c.concat(X(arguments))])}},p.prototype.fbind=function(){var a=this,b=X(arguments);return function(){return a.dispatch("apply",[this,b.concat(X(arguments))])}},l.keys=function(a){return l(a).dispatch("keys",[])},p.prototype.keys=function(){return this.dispatch("keys",[])},l.all=K,p.prototype.all=function(){return K(this)},l.allResolved=k(L,"allResolved","allSettled"),p.prototype.allResolved=function(){return L(this)},l.allSettled=M,p.prototype.allSettled=function(){return this.then(function(a){return K($(a,function(a){function b(){return a.inspect()}return a=l(a),a.then(b,b)}))})},l.fail=l["catch"]=function(a,b){return l(a).then(void 0,b)},p.prototype.fail=p.prototype["catch"]=function(a){return this.then(void 0,a)},l.progress=N,p.prototype.progress=function(a){return this.then(void 0,void 0,a)},l.fin=l["finally"]=function(a,b){return l(a)["finally"](b)},p.prototype.fin=p.prototype["finally"]=function(a){return a=l(a),this.then(function(b){return a.fcall().then(function(){return b
})},function(b){return a.fcall().then(function(){throw b})})},l.done=function(a,b,c,d){return l(a).done(b,c,d)},p.prototype.done=function(b,c,d){var f=function(a){V(function(){if(e(a,g),!l.onerror)throw a;l.onerror(a)})},g=b||c||d?this.then(b,c,d):this;"object"==typeof a&&a&&a.domain&&(f=a.domain.bind(f)),g.then(void 0,f)},l.timeout=function(a,b,c){return l(a).timeout(b,c)},p.prototype.timeout=function(a,b){var c=m(),d=setTimeout(function(){c.reject(new Error(b||"Timed out after "+a+" ms"))},a);return this.then(function(a){clearTimeout(d),c.resolve(a)},function(a){clearTimeout(d),c.reject(a)},c.notify),c.promise},l.delay=function(a,b){return void 0===b&&(b=a,a=void 0),l(a).delay(b)},p.prototype.delay=function(a){return this.then(function(b){var c=m();return setTimeout(function(){c.resolve(b)},a),c.promise})},l.nfapply=function(a,b){return l(a).nfapply(b)},p.prototype.nfapply=function(a){var b=m(),c=X(a);return c.push(b.makeNodeResolver()),this.fapply(c).fail(b.reject),b.promise},l.nfcall=function(a){var b=X(arguments,1);return l(a).nfapply(b)},p.prototype.nfcall=function(){var a=X(arguments),b=m();return a.push(b.makeNodeResolver()),this.fapply(a).fail(b.reject),b.promise},l.nfbind=l.denodeify=function(a){var b=X(arguments,1);return function(){var c=b.concat(X(arguments)),d=m();return c.push(d.makeNodeResolver()),l(a).fapply(c).fail(d.reject),d.promise}},p.prototype.nfbind=p.prototype.denodeify=function(){var a=X(arguments);return a.unshift(this),l.denodeify.apply(void 0,a)},l.nbind=function(a,b){var c=X(arguments,2);return function(){function d(){return a.apply(b,arguments)}var e=c.concat(X(arguments)),f=m();return e.push(f.makeNodeResolver()),l(d).fapply(e).fail(f.reject),f.promise}},p.prototype.nbind=function(){var a=X(arguments,0);return a.unshift(this),l.nbind.apply(void 0,a)},l.nmapply=l.npost=function(a,b,c){return l(a).npost(b,c)},p.prototype.nmapply=p.prototype.npost=function(a,b){var c=X(b||[]),d=m();return c.push(d.makeNodeResolver()),this.dispatch("post",[a,c]).fail(d.reject),d.promise},l.nsend=l.nmcall=l.ninvoke=function(a,b){var c=X(arguments,2),d=m();return c.push(d.makeNodeResolver()),l(a).dispatch("post",[b,c]).fail(d.reject),d.promise},p.prototype.nsend=p.prototype.nmcall=p.prototype.ninvoke=function(a){var b=X(arguments,1),c=m();return b.push(c.makeNodeResolver()),this.dispatch("post",[a,b]).fail(c.reject),c.promise},l.nodeify=O,p.prototype.nodeify=function(a){return a?void this.then(function(b){V(function(){a(null,b)})},function(b){V(function(){a(b)})}):this};var hb=j();return l})}).call(this,a("/Users/antoine/projects/oauth-js/node_modules/browserify/node_modules/insert-module-globals/node_modules/process/browser.js"))},{"/Users/antoine/projects/oauth-js/node_modules/browserify/node_modules/insert-module-globals/node_modules/process/browser.js":10}]},{},[4]);
/**
 * Copyright (c) 2011-2014 Felix Gnass
 * Licensed under the MIT license
 */
(function(root, factory) {

  /* CommonJS */
  if (typeof exports == 'object')  module.exports = factory()

  /* AMD module */
  else if (typeof define == 'function' && define.amd) define(factory)

  /* Browser global */
  else root.Spinner = factory()
}
(this, function() {
  "use strict";

  var prefixes = ['webkit', 'Moz', 'ms', 'O'] /* Vendor prefixes */
    , animations = {} /* Animation rules keyed by their name */
    , useCssAnimations /* Whether to use CSS animations or setTimeout */

  /**
   * Utility function to create elements. If no tag name is given,
   * a DIV is created. Optionally properties can be passed.
   */
  function createEl(tag, prop) {
    var el = document.createElement(tag || 'div')
      , n

    for(n in prop) el[n] = prop[n]
    return el
  }

  /**
   * Appends children and returns the parent.
   */
  function ins(parent /* child1, child2, ...*/) {
    for (var i=1, n=arguments.length; i<n; i++)
      parent.appendChild(arguments[i])

    return parent
  }

  /**
   * Insert a new stylesheet to hold the @keyframe or VML rules.
   */
  var sheet = (function() {
    var el = createEl('style', {type : 'text/css'})
    ins(document.getElementsByTagName('head')[0], el)
    return el.sheet || el.styleSheet
  }())

  /**
   * Creates an opacity keyframe animation rule and returns its name.
   * Since most mobile Webkits have timing issues with animation-delay,
   * we create separate rules for each line/segment.
   */
  function addAnimation(alpha, trail, i, lines) {
    var name = ['opacity', trail, ~~(alpha*100), i, lines].join('-')
      , start = 0.01 + i/lines * 100
      , z = Math.max(1 - (1-alpha) / trail * (100-start), alpha)
      , prefix = useCssAnimations.substring(0, useCssAnimations.indexOf('Animation')).toLowerCase()
      , pre = prefix && '-' + prefix + '-' || ''

    if (!animations[name]) {
      sheet.insertRule(
        '@' + pre + 'keyframes ' + name + '{' +
        '0%{opacity:' + z + '}' +
        start + '%{opacity:' + alpha + '}' +
        (start+0.01) + '%{opacity:1}' +
        (start+trail) % 100 + '%{opacity:' + alpha + '}' +
        '100%{opacity:' + z + '}' +
        '}', sheet.cssRules.length)

      animations[name] = 1
    }

    return name
  }

  /**
   * Tries various vendor prefixes and returns the first supported property.
   */
  function vendor(el, prop) {
    var s = el.style
      , pp
      , i

    prop = prop.charAt(0).toUpperCase() + prop.slice(1)
    for(i=0; i<prefixes.length; i++) {
      pp = prefixes[i]+prop
      if(s[pp] !== undefined) return pp
    }
    if(s[prop] !== undefined) return prop
  }

  /**
   * Sets multiple style properties at once.
   */
  function css(el, prop) {
    for (var n in prop)
      el.style[vendor(el, n)||n] = prop[n]

    return el
  }

  /**
   * Fills in default values.
   */
  function merge(obj) {
    for (var i=1; i < arguments.length; i++) {
      var def = arguments[i]
      for (var n in def)
        if (obj[n] === undefined) obj[n] = def[n]
    }
    return obj
  }

  /**
   * Returns the absolute page-offset of the given element.
   */
  function pos(el) {
    var o = { x:el.offsetLeft, y:el.offsetTop }
    while((el = el.offsetParent))
      o.x+=el.offsetLeft, o.y+=el.offsetTop

    return o
  }

  /**
   * Returns the line color from the given string or array.
   */
  function getColor(color, idx) {
    return typeof color == 'string' ? color : color[idx % color.length]
  }

  // Built-in defaults

  var defaults = {
    lines: 12,            // The number of lines to draw
    length: 7,            // The length of each line
    width: 5,             // The line thickness
    radius: 10,           // The radius of the inner circle
    rotate: 0,            // Rotation offset
    corners: 1,           // Roundness (0..1)
    color: '#000',        // #rgb or #rrggbb
    direction: 1,         // 1: clockwise, -1: counterclockwise
    speed: 1,             // Rounds per second
    trail: 100,           // Afterglow percentage
    opacity: 1/4,         // Opacity of the lines
    fps: 20,              // Frames per second when using setTimeout()
    zIndex: 2e9,          // Use a high z-index by default
    className: 'spinner', // CSS class to assign to the element
    top: '50%',           // center vertically
    left: '50%',          // center horizontally
    position: 'absolute'  // element position
  }

  /** The constructor */
  function Spinner(o) {
    this.opts = merge(o || {}, Spinner.defaults, defaults)
  }

  // Global defaults that override the built-ins:
  Spinner.defaults = {}

  merge(Spinner.prototype, {

    /**
     * Adds the spinner to the given target element. If this instance is already
     * spinning, it is automatically removed from its previous target b calling
     * stop() internally.
     */
    spin: function(target) {
      this.stop()

      var self = this
        , o = self.opts
        , el = self.el = css(createEl(0, {className: o.className}), {position: o.position, width: 0, zIndex: o.zIndex})
        , mid = o.radius+o.length+o.width

      css(el, {
        left: o.left,
        top: o.top
      })

      if (target) {
        target.insertBefore(el, target.firstChild||null)
      }

      el.setAttribute('role', 'progressbar')
      self.lines(el, self.opts)

      if (!useCssAnimations) {
        // No CSS animation support, use setTimeout() instead
        var i = 0
          , start = (o.lines - 1) * (1 - o.direction) / 2
          , alpha
          , fps = o.fps
          , f = fps/o.speed
          , ostep = (1-o.opacity) / (f*o.trail / 100)
          , astep = f/o.lines

        ;(function anim() {
          i++;
          for (var j = 0; j < o.lines; j++) {
            alpha = Math.max(1 - (i + (o.lines - j) * astep) % f * ostep, o.opacity)

            self.opacity(el, j * o.direction + start, alpha, o)
          }
          self.timeout = self.el && setTimeout(anim, ~~(1000/fps))
        })()
      }
      return self
    },

    /**
     * Stops and removes the Spinner.
     */
    stop: function() {
      var el = this.el
      if (el) {
        clearTimeout(this.timeout)
        if (el.parentNode) el.parentNode.removeChild(el)
        this.el = undefined
      }
      return this
    },

    /**
     * Internal method that draws the individual lines. Will be overwritten
     * in VML fallback mode below.
     */
    lines: function(el, o) {
      var i = 0
        , start = (o.lines - 1) * (1 - o.direction) / 2
        , seg

      function fill(color, shadow) {
        return css(createEl(), {
          position: 'absolute',
          width: (o.length+o.width) + 'px',
          height: o.width + 'px',
          background: color,
          boxShadow: shadow,
          transformOrigin: 'left',
          transform: 'rotate(' + ~~(360/o.lines*i+o.rotate) + 'deg) translate(' + o.radius+'px' +',0)',
          borderRadius: (o.corners * o.width>>1) + 'px'
        })
      }

      for (; i < o.lines; i++) {
        seg = css(createEl(), {
          position: 'absolute',
          top: 1+~(o.width/2) + 'px',
          transform: o.hwaccel ? 'translate3d(0,0,0)' : '',
          opacity: o.opacity,
          animation: useCssAnimations && addAnimation(o.opacity, o.trail, start + i * o.direction, o.lines) + ' ' + 1/o.speed + 's linear infinite'
        })

        if (o.shadow) ins(seg, css(fill('#000', '0 0 4px ' + '#000'), {top: 2+'px'}))
        ins(el, ins(seg, fill(getColor(o.color, i), '0 0 1px rgba(0,0,0,.1)')))
      }
      return el
    },

    /**
     * Internal method that adjusts the opacity of a single line.
     * Will be overwritten in VML fallback mode below.
     */
    opacity: function(el, i, val) {
      if (i < el.childNodes.length) el.childNodes[i].style.opacity = val
    }

  })


  function initVML() {

    /* Utility function to create a VML tag */
    function vml(tag, attr) {
      return createEl('<' + tag + ' xmlns="urn:schemas-microsoft.com:vml" class="spin-vml">', attr)
    }

    // No CSS transforms but VML support, add a CSS rule for VML elements:
    sheet.addRule('.spin-vml', 'behavior:url(#default#VML)')

    Spinner.prototype.lines = function(el, o) {
      var r = o.length+o.width
        , s = 2*r

      function grp() {
        return css(
          vml('group', {
            coordsize: s + ' ' + s,
            coordorigin: -r + ' ' + -r
          }),
          { width: s, height: s }
        )
      }

      var margin = -(o.width+o.length)*2 + 'px'
        , g = css(grp(), {position: 'absolute', top: margin, left: margin})
        , i

      function seg(i, dx, filter) {
        ins(g,
          ins(css(grp(), {rotation: 360 / o.lines * i + 'deg', left: ~~dx}),
            ins(css(vml('roundrect', {arcsize: o.corners}), {
                width: r,
                height: o.width,
                left: o.radius,
                top: -o.width>>1,
                filter: filter
              }),
              vml('fill', {color: getColor(o.color, i), opacity: o.opacity}),
              vml('stroke', {opacity: 0}) // transparent stroke to fix color bleeding upon opacity change
            )
          )
        )
      }

      if (o.shadow)
        for (i = 1; i <= o.lines; i++)
          seg(i, -2, 'progid:DXImageTransform.Microsoft.Blur(pixelradius=2,makeshadow=1,shadowopacity=.3)')

      for (i = 1; i <= o.lines; i++) seg(i)
      return ins(el, g)
    }

    Spinner.prototype.opacity = function(el, i, val, o) {
      var c = el.firstChild
      o = o.shadow && o.lines || 0
      if (c && i+o < c.childNodes.length) {
        c = c.childNodes[i+o]; c = c && c.firstChild; c = c && c.firstChild
        if (c) c.opacity = val
      }
    }
  }

  var probe = css(createEl('group'), {behavior: 'url(#default#VML)'})

  if (!vendor(probe, 'transform') && probe.adj) initVML()
  else useCssAnimations = vendor(probe, 'animation')

  return Spinner

}));

if(typeof $.widget === 'undefined') {
/*!
 * jQuery UI Widget 1.11.2
 * http://jqueryui.com
 *
 * Copyright 2014 jQuery Foundation and other contributors
 * Released under the MIT license.
 * http://jquery.org/license
 *
 * http://api.jqueryui.com/jQuery.widget/
 */
(function( factory ) {
	if ( typeof define === "function" && define.amd ) {

		// AMD. Register as an anonymous module.
		define( [ "jquery" ], factory );
	} else {

		// Browser globals
		factory( jQuery );
	}
}(function( $ ) {

var widget_uuid = 0,
	widget_slice = Array.prototype.slice;

$.cleanData = (function( orig ) {
	return function( elems ) {
		var events, elem, i;
		for ( i = 0; (elem = elems[i]) != null; i++ ) {
			try {

				// Only trigger remove when necessary to save time
				events = $._data( elem, "events" );
				if ( events && events.remove ) {
					$( elem ).triggerHandler( "remove" );
				}

			// http://bugs.jquery.com/ticket/8235
			} catch ( e ) {}
		}
		orig( elems );
	};
})( $.cleanData );

$.widget = function( name, base, prototype ) {
	var fullName, existingConstructor, constructor, basePrototype,
		// proxiedPrototype allows the provided prototype to remain unmodified
		// so that it can be used as a mixin for multiple widgets (#8876)
		proxiedPrototype = {},
		namespace = name.split( "." )[ 0 ];

	name = name.split( "." )[ 1 ];
	fullName = namespace + "-" + name;

	if ( !prototype ) {
		prototype = base;
		base = $.Widget;
	}

	// create selector for plugin
	$.expr[ ":" ][ fullName.toLowerCase() ] = function( elem ) {
		return !!$.data( elem, fullName );
	};

	$[ namespace ] = $[ namespace ] || {};
	existingConstructor = $[ namespace ][ name ];
	constructor = $[ namespace ][ name ] = function( options, element ) {
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
	$.extend( constructor, existingConstructor, {
		version: prototype.version,
		// copy the object used to create the prototype in case we need to
		// redefine the widget later
		_proto: $.extend( {}, prototype ),
		// track widgets that inherit from this widget in case this widget is
		// redefined after a widget inherits from it
		_childConstructors: []
	});

	basePrototype = new base();
	// we need to make the options hash a property directly on the new instance
	// otherwise we'll modify the options hash on the prototype that we're
	// inheriting from
	basePrototype.options = $.widget.extend( {}, basePrototype.options );
	$.each( prototype, function( prop, value ) {
		if ( !$.isFunction( value ) ) {
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
	constructor.prototype = $.widget.extend( basePrototype, {
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
		$.each( existingConstructor._childConstructors, function( i, child ) {
			var childPrototype = child.prototype;

			// redefine the child widget using the same prototype that was
			// originally used, but inherit from the new version of the base
			$.widget( childPrototype.namespace + "." + childPrototype.widgetName, constructor, child._proto );
		});
		// remove the list of existing child constructors from the old constructor
		// so the old child constructors can be garbage collected
		delete existingConstructor._childConstructors;
	} else {
		base._childConstructors.push( constructor );
	}

	$.widget.bridge( name, constructor );

	return constructor;
};

$.widget.extend = function( target ) {
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
				if ( $.isPlainObject( value ) ) {
					target[ key ] = $.isPlainObject( target[ key ] ) ?
						$.widget.extend( {}, target[ key ], value ) :
						// Don't extend strings, arrays, etc. with objects
						$.widget.extend( {}, value );
				// Copy everything else by reference
				} else {
					target[ key ] = value;
				}
			}
		}
	}
	return target;
};

$.widget.bridge = function( name, object ) {
	var fullName = object.prototype.widgetFullName || name;
	$.fn[ name ] = function( options ) {
		var isMethodCall = typeof options === "string",
			args = widget_slice.call( arguments, 1 ),
			returnValue = this;

		// allow multiple hashes to be passed on init
		options = !isMethodCall && args.length ?
			$.widget.extend.apply( null, [ options ].concat(args) ) :
			options;

		if ( isMethodCall ) {
			this.each(function() {
				var methodValue,
					instance = $.data( this, fullName );
				if ( options === "instance" ) {
					returnValue = instance;
					return false;
				}
				if ( !instance ) {
					return $.error( "cannot call methods on " + name + " prior to initialization; " +
						"attempted to call method '" + options + "'" );
				}
				if ( !$.isFunction( instance[options] ) || options.charAt( 0 ) === "_" ) {
					return $.error( "no such method '" + options + "' for " + name + " widget instance" );
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
				var instance = $.data( this, fullName );
				if ( instance ) {
					instance.option( options || {} );
					if ( instance._init ) {
						instance._init();
					}
				} else {
					$.data( this, fullName, new object( options, this ) );
				}
			});
		}

		return returnValue;
	};
};

$.Widget = function( /* options, element */ ) {};
$.Widget._childConstructors = [];

$.Widget.prototype = {
	widgetName: "widget",
	widgetEventPrefix: "",
	defaultElement: "<div>",
	options: {
		disabled: false,

		// callbacks
		create: null
	},
	_createWidget: function( options, element ) {
		element = $( element || this.defaultElement || this )[ 0 ];
		this.element = $( element );
		this.uuid = widget_uuid++;
		this.eventNamespace = "." + this.widgetName + this.uuid;

		this.bindings = $();
		this.hoverable = $();
		this.focusable = $();

		if ( element !== this ) {
			$.data( element, this.widgetFullName, this );
			this._on( true, this.element, {
				remove: function( event ) {
					if ( event.target === element ) {
						this.destroy();
					}
				}
			});
			this.document = $( element.style ?
				// element within the document
				element.ownerDocument :
				// element is window or document
				element.document || element );
			this.window = $( this.document[0].defaultView || this.document[0].parentWindow );
		}

		this.options = $.widget.extend( {},
			this.options,
			this._getCreateOptions(),
			options );

		this._create();
		this._trigger( "create", null, this._getCreateEventData() );
		this._init();
	},
	_getCreateOptions: $.noop,
	_getCreateEventData: $.noop,
	_create: $.noop,
	_init: $.noop,

	destroy: function() {
		this._destroy();
		// we can probably remove the unbind calls in 2.0
		// all event bindings should go through this._on()
		this.element
			.unbind( this.eventNamespace )
			.removeData( this.widgetFullName )
			// support: jquery <1.6.3
			// http://bugs.jquery.com/ticket/9413
			.removeData( $.camelCase( this.widgetFullName ) );
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
	_destroy: $.noop,

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
			return $.widget.extend( {}, this.options );
		}

		if ( typeof key === "string" ) {
			// handle nested keys, e.g., "foo.bar" => { foo: { bar: ___ } }
			options = {};
			parts = key.split( "." );
			key = parts.shift();
			if ( parts.length ) {
				curOption = options[ key ] = $.widget.extend( {}, this.options[ key ] );
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
			element = delegateElement = $( element );
			this.bindings = this.bindings.add( element );
		}

		$.each( handlers, function( event, handler ) {
			function handlerProxy() {
				// allow widgets to customize the disabled handling
				// - disabled as an array instead of boolean
				// - disabled class as method for disabling individual parts
				if ( !suppressDisabledCheck &&
						( instance.options.disabled === true ||
							$( this ).hasClass( "ui-state-disabled" ) ) ) {
					return;
				}
				return ( typeof handler === "string" ? instance[ handler ] : handler )
					.apply( instance, arguments );
			}

			// copy the guid so direct unbinding works
			if ( typeof handler !== "string" ) {
				handlerProxy.guid = handler.guid =
					handler.guid || handlerProxy.guid || $.guid++;
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
		this.bindings = $( this.bindings.not( element ).get() );
		this.focusable = $( this.focusable.not( element ).get() );
		this.hoverable = $( this.hoverable.not( element ).get() );
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
				$( event.currentTarget ).addClass( "ui-state-hover" );
			},
			mouseleave: function( event ) {
				$( event.currentTarget ).removeClass( "ui-state-hover" );
			}
		});
	},

	_focusable: function( element ) {
		this.focusable = this.focusable.add( element );
		this._on( element, {
			focusin: function( event ) {
				$( event.currentTarget ).addClass( "ui-state-focus" );
			},
			focusout: function( event ) {
				$( event.currentTarget ).removeClass( "ui-state-focus" );
			}
		});
	},

	_trigger: function( type, event, data ) {
		var prop, orig,
			callback = this.options[ type ];

		data = data || {};
		event = $.Event( event );
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
		return !( $.isFunction( callback ) &&
			callback.apply( this.element[0], [ event ].concat( data ) ) === false ||
			event.isDefaultPrevented() );
	}
};

$.each( { show: "fadeIn", hide: "fadeOut" }, function( method, defaultEffect ) {
	$.Widget.prototype[ "_" + method ] = function( element, options, callback ) {
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
		hasOptions = !$.isEmptyObject( options );
		options.complete = callback;
		if ( options.delay ) {
			element.delay( options.delay );
		}
		if ( hasOptions && $.effects && $.effects.effect[ effectName ] ) {
			element[ method ]( options );
		} else if ( effectName !== method && element[ effectName ] ) {
			element[ effectName ]( options.duration, options.easing, callback );
		} else {
			element.queue(function( next ) {
				$( this )[ method ]();
				if ( callback ) {
					callback.call( element[ 0 ] );
				}
				next();
			});
		}
	};
});

return $.widget;

}));

}

(function (factory) {
	factory(jQuery);
}(function ($) {
//


    var version = "undefined";

    /**
     * @name radic
     * @constructor
     * @mixes radic/storage
     * @mixes radic/template
     * @mixes radic/template/comparisons
     */
    function radic(){

    }


    /**
     * Extends the base radic object
     *
     * @param {Object} obj - The object to extend radic with
     * @example
     * radic.extend({
     *      storage: {
     *          print: function(what){
     *              console.log(what);
     *          }
     *      }
     * });
     */
    radic.extend = function(obj){
        $.extend(radic, obj);
    };


    function getlodash() {

        /**
         * @ignore
         */

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



    radic.async = {};




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




    /**
     * @mixin
     * @alias radic/storage
     */
    var storage = {};


    /**
     * Extends the base radic object
     *
     *
     * @param {Function} callback - The object to extend radic with
     * @example
     * radic.storage.on(function(){
     *      // do something
     * }
     */
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
            window['localStorage'].setItem(key + ':expire', now + options.expires);
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
        window.localStorage.clear();
    };


    radic.extend({
        storage: storage
    });


    radic.extend({
        md5: function (string) {

            function cmn(q, a, b, x, s, t) {
                a = add32(add32(a, q), add32(x, t));
                return add32((a << s) | (a >>> (32 - s)), b);
            }


            function ff(a, b, c, d, x, s, t) {
                return cmn((b & c) | ((~b) & d), a, b, x, s, t);
            }

            function gg(a, b, c, d, x, s, t) {
                return cmn((b & d) | (c & (~d)), a, b, x, s, t);
            }

            function hh(a, b, c, d, x, s, t) {
                return cmn(b ^ c ^ d, a, b, x, s, t);
            }

            function ii(a, b, c, d, x, s, t) {
                return cmn(c ^ (b | (~d)), a, b, x, s, t);
            }


            function md5cycle(x, k) {
                var a = x[0], b = x[1], c = x[2], d = x[3];

                a = ff(a, b, c, d, k[0], 7, -680876936);
                d = ff(d, a, b, c, k[1], 12, -389564586);
                c = ff(c, d, a, b, k[2], 17, 606105819);
                b = ff(b, c, d, a, k[3], 22, -1044525330);
                a = ff(a, b, c, d, k[4], 7, -176418897);
                d = ff(d, a, b, c, k[5], 12, 1200080426);
                c = ff(c, d, a, b, k[6], 17, -1473231341);
                b = ff(b, c, d, a, k[7], 22, -45705983);
                a = ff(a, b, c, d, k[8], 7, 1770035416);
                d = ff(d, a, b, c, k[9], 12, -1958414417);
                c = ff(c, d, a, b, k[10], 17, -42063);
                b = ff(b, c, d, a, k[11], 22, -1990404162);
                a = ff(a, b, c, d, k[12], 7, 1804603682);
                d = ff(d, a, b, c, k[13], 12, -40341101);
                c = ff(c, d, a, b, k[14], 17, -1502002290);
                b = ff(b, c, d, a, k[15], 22, 1236535329);

                a = gg(a, b, c, d, k[1], 5, -165796510);
                d = gg(d, a, b, c, k[6], 9, -1069501632);
                c = gg(c, d, a, b, k[11], 14, 643717713);
                b = gg(b, c, d, a, k[0], 20, -373897302);
                a = gg(a, b, c, d, k[5], 5, -701558691);
                d = gg(d, a, b, c, k[10], 9, 38016083);
                c = gg(c, d, a, b, k[15], 14, -660478335);
                b = gg(b, c, d, a, k[4], 20, -405537848);
                a = gg(a, b, c, d, k[9], 5, 568446438);
                d = gg(d, a, b, c, k[14], 9, -1019803690);
                c = gg(c, d, a, b, k[3], 14, -187363961);
                b = gg(b, c, d, a, k[8], 20, 1163531501);
                a = gg(a, b, c, d, k[13], 5, -1444681467);
                d = gg(d, a, b, c, k[2], 9, -51403784);
                c = gg(c, d, a, b, k[7], 14, 1735328473);
                b = gg(b, c, d, a, k[12], 20, -1926607734);

                a = hh(a, b, c, d, k[5], 4, -378558);
                d = hh(d, a, b, c, k[8], 11, -2022574463);
                c = hh(c, d, a, b, k[11], 16, 1839030562);
                b = hh(b, c, d, a, k[14], 23, -35309556);
                a = hh(a, b, c, d, k[1], 4, -1530992060);
                d = hh(d, a, b, c, k[4], 11, 1272893353);
                c = hh(c, d, a, b, k[7], 16, -155497632);
                b = hh(b, c, d, a, k[10], 23, -1094730640);
                a = hh(a, b, c, d, k[13], 4, 681279174);
                d = hh(d, a, b, c, k[0], 11, -358537222);
                c = hh(c, d, a, b, k[3], 16, -722521979);
                b = hh(b, c, d, a, k[6], 23, 76029189);
                a = hh(a, b, c, d, k[9], 4, -640364487);
                d = hh(d, a, b, c, k[12], 11, -421815835);
                c = hh(c, d, a, b, k[15], 16, 530742520);
                b = hh(b, c, d, a, k[2], 23, -995338651);

                a = ii(a, b, c, d, k[0], 6, -198630844);
                d = ii(d, a, b, c, k[7], 10, 1126891415);
                c = ii(c, d, a, b, k[14], 15, -1416354905);
                b = ii(b, c, d, a, k[5], 21, -57434055);
                a = ii(a, b, c, d, k[12], 6, 1700485571);
                d = ii(d, a, b, c, k[3], 10, -1894986606);
                c = ii(c, d, a, b, k[10], 15, -1051523);
                b = ii(b, c, d, a, k[1], 21, -2054922799);
                a = ii(a, b, c, d, k[8], 6, 1873313359);
                d = ii(d, a, b, c, k[15], 10, -30611744);
                c = ii(c, d, a, b, k[6], 15, -1560198380);
                b = ii(b, c, d, a, k[13], 21, 1309151649);
                a = ii(a, b, c, d, k[4], 6, -145523070);
                d = ii(d, a, b, c, k[11], 10, -1120210379);
                c = ii(c, d, a, b, k[2], 15, 718787259);
                b = ii(b, c, d, a, k[9], 21, -343485551);

                x[0] = add32(a, x[0]);
                x[1] = add32(b, x[1]);
                x[2] = add32(c, x[2]);
                x[3] = add32(d, x[3]);

            }


            function md51(s) {
                txt = '';
                var n = s.length,
                    state = [1732584193, -271733879, -1732584194, 271733878], i;
                for (i = 64; i <= n; i += 64) {
                    md5cycle(state, md5blk(s.substring(i - 64, i)));
                }
                s = s.substring(i - 64);
                var tail = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], sl = s.length;
                for (i = 0; i < sl; i++)    tail[i >> 2] |= s.charCodeAt(i) << ((i % 4) << 3);
                tail[i >> 2] |= 0x80 << ((i % 4) << 3);
                if (i > 55) {
                    md5cycle(state, tail);
                    i = 16;
                    while (i--) {
                        tail[i] = 0
                    }
                    //			for (i=0; i<16; i++) tail[i] = 0;
                }
                tail[14] = n * 8;
                md5cycle(state, tail);
                return state;
            }

            /* there needs to be support for Unicode here,
             * unless we pretend that we can redefine the MD-5
             * algorithm for multi-byte characters (perhaps
             * by adding every four 16-bit characters and
             * shortening the sum to 32 bits). Otherwise
             * I suggest performing MD-5 as if every character
             * was two bytes--e.g., 0040 0025 = @%--but then
             * how will an ordinary MD-5 sum be matched?
             * There is no way to standardize text to something
             * like UTF-8 before transformation; speed cost is
             * utterly prohibitive. The JavaScript standard
             * itself needs to look at this: it should start
             * providing access to strings as preformed UTF-8
             * 8-bit unsigned value arrays.
             */
            function md5blk(s) {        /* I figured global was faster.   */
                var md5blks = [], i;
                /* Andy King said do it this way. */
                for (i = 0; i < 64; i += 4) {
                    md5blks[i >> 2] = s.charCodeAt(i)
                    + (s.charCodeAt(i + 1) << 8)
                    + (s.charCodeAt(i + 2) << 16)
                    + (s.charCodeAt(i + 3) << 24);
                }
                return md5blks;
            }

            var hex_chr = '0123456789abcdef'.split('');

            function rhex(n) {
                var s = '', j = 0;
                for (; j < 4; j++)    s += hex_chr[(n >> (j * 8 + 4)) & 0x0F] + hex_chr[(n >> (j * 8)) & 0x0F];
                return s;
            }

            function hex(x) {
                var l = x.length;
                for (var i = 0; i < l; i++)    x[i] = rhex(x[i]);
                return x.join('');
            }

            /* this function is much faster,
             so if possible we use it. Some IEs
             are the only ones I know of that
             need the idiotic second function,
             generated by an if clause.  */

            function add32(a, b) {
                return (a + b) & 0xFFFFFFFF;
            }

            if (hex(md51("hello")) != "5d41402abc4b2a76b9719d911017c592") {
                function add32(x, y) {
                    var lsw = (x & 0xFFFF) + (y & 0xFFFF),
                        msw = (x >> 16) + (y >> 16) + (lsw >> 16);
                    return (msw << 16) | (lsw & 0xFFFF);
                }
            }

            return hex(md51(string));


        }
    });



    var GithubClient = (function (GithubClient) {

        return GithubClient; //('06ec61fd2853f215bb01f7c5b2e0f56ff8537838'); //'e243a6a733de08c8dfd37e86abd7d2a3b82784de');

    })(function (global, githubRoutes) {


        // ###########################
        // ### Helpers and globals ###
        // ###########################

        var FP = Function.prototype,
            AP = Array.prototype,
            OP = Object.prototype;

        var bindbind = FP.bind.bind(FP.bind),
            callbind = bindbind(FP.bind),
            applybind = bindbind(FP.apply);

        var has = callbind(OP.hasOwnProperty),
            slice = callbind(AP.slice),
            flatten = applybind(AP.concat, []);

        var filter_ = AP.filter,
            map_ = AP.map,
            push_ = AP.push,
            slice_ = AP.slice;


        function decorate(o) {
            var b, c, d;
            for (var i = 1; b = arguments[i]; i++) {
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

        function isObject(o) {
            return o != null && typeof o === 'object' || typeof o === 'function';
        }

        function isIndexed(o) {
            return Array.isArray(o) || isObject(o) && has(o, 'length') && has(o, o.length - 1);
        }

        // ############
        // ### Path ###
        // ############

        function Path(a) {
            if (isIndexed(a)) {
                push_.apply(this, a);
            }
        }

        Path.prototype.length = 0;

        decorate(Path.prototype, {
            join: Array.prototype.join,
            map: Array.prototype.map,
            concat: function concat() {
                var out = new Path(this);
                push_.apply(out, arguments);
                return out;
            },
            args: function args() {
                return filter_.call(this, function (s) {
                    return s[0] === 'Δ';
                }).map(function (s) {
                    return s.replace(/Δ/g, '');
                });
            },
            toName: function toName(slice, last) {
                var array = map_.call(this, function (s) {
                    return s.replace(/Δ/g, '');
                });

                if (last) {
                    array.push(last);
                }

                var out = array.slice(slice || 1).map(function (s) {
                    return s[0].toUpperCase() + s.slice(1).toLowerCase();
                });

                if (!out[0]) {
                    return '';
                } else {
                    out[0] = out[0].toLowerCase();
                    return out.join('').replace(/_(.)/g, function (s) {
                        return s[1].toUpperCase();
                    });
                }
            },
            slice: function slice() {
                return new Path(slice_.apply(this, arguments));
            }
        });


        // #################
        // ### Transport ###
        // #################

        // superclass for XHR and JSONP

        function Transport(options, callback) {
            options = options || {};
            if (typeof options === 'string') {
                options = {url: options};
            }
            if (typeof callback === 'function') {
                options.callback = callback;
            }
            this.data = options.data || {};
            this.path = options.path || [];
            this.base = options.url;
            this.callback = options.callback || function () {
            };
            this.state = 'idle';
        }

        Transport.transports = {};

        decorate(Transport, {
            register: function register(ctor) {
                Transport.transports[ctor.name.toLowerCase()] = ctor;
            },
            lookup: function lookup(name) {
                name = name.toLowerCase();
                return name in Transport.transports ? Transport.transports[name] : null;
            },
            create: function create(type, base, dispatcher) {
                var T = Transport.lookup(type);
                return new T(base, dispatcher);
            }
        });


        decorate(Transport.prototype, {
            async: true,
            cache: true,
            expires: 60, // minutes
            params: function params() {
                var data = Object.keys(this.data).map(function (name) {
                    return [name, this.data[name]]
                }, this);
                data.push([this.callbackParam, this.callbackName]);
                return data.map(function (item) {
                    return encodeURIComponent(item[0]) + '=' + encodeURIComponent(item[1]);
                }).join('&');
            }
        });

        // #######################
        // ### JSONP Transport ###
        // #######################

        function JSONP(options, callback) {
            Transport.call(this, options = options || {}, callback);
            this.callbackParam = options.callbackParam || 'callback';
            this.callbackName = options.callbackName || '_' + Math.random().toString(36).slice(2);
        }

        Transport.register(JSONP);

        JSONP.prototype = Object.create(Transport.prototype);
        decorate(JSONP.prototype, {
            constructor: JSONP,

            url: function url() {
                return [this.base].concat(this.path).join('/') + '?' + this.params();
            },
            send: function send(callback) {
                var cacheKey = radic.md5(JSON.stringify({path: this.path, data: this.data}));

                if (this.cache) {
                    var cache = radic.storage.get(cacheKey, {json: true, force: this.cache !== true});
                    if (radic.defined(cache) && !radic.isNull(cache)) {
                        //this.state = 'success';
                        console.log('cache jsonp', typeof cache);
                        if (this.async === false) {
                            return {data: cache.data, meta: cache.meta};
                        }
                        if (radic.isFunction(callback)) {
                            callback.call(this, cache.data, cache.meta);
                        }
                        return this;
                    }
                }

                var script = document.createElement('script'),
                    completed

                this.callbackName = '_' + Math.random().toString(36).slice(2);

                callback = callback || this.callback;

                function complete(state, result) {
                    if (!completed) {
                        completed = true;
                        delete window[this.callbackName];
                        document.body.removeChild(script);
                        this.state = state;

                        if (this.cache) {
                            radic.storage.set(cacheKey, result, {
                                expires: this.expires,
                                json: true
                            });
                        }

                        this.response = result;
                        callback.call(this, result.data, result.meta);
                    }
                }

                script.src = this.url();
                script.async = script.defer = this.async;
                script.onerror = complete.bind(this, 'error');
                window[this.callbackName] = complete.bind(this, 'success');

                document.body.appendChild(script);
                this.state = 'loading';
                return this.async ? this : this.response;
            }
        });

        // ################################
        // ### XMLHttpRequest Transport ###
        // ################################

        function XHR(options, callback) {
            this.headers = {};
            options = options || {}

            Transport.call(this, options, callback);

            if (options.headers) {
                Object.keys(options.headers).forEach(function (n) {
                    this[n] = options.headers[n];
                }, this.headers);
            }
        }

        Transport.register(XHR);

        XHR.prototype = Object.create(Transport.prototype);
        decorate(XHR.prototype, {
            constructor: XHR,
            url: function url() {
                var params = this.params();
                return [this.base].concat(this.path).join('/') + (this.verb === 'get' && params ? '?' + params : '');
            },
            auth: function auth(user, pass) {
                if (!pass && user.length === 40) {
                    this.headers.Authorization = 'token ' + user;
                } else {
                    this.headers.Authorization = 'Basic ' + btoa(user + ':' + pass);
                }
            },
            send: function send(callback, verb) {


                var cacheKey = radic.md5(JSON.stringify({path: this.path, data: this.data}));
                if (this.cache) {
                    var cache = radic.storage.get(cacheKey, {json: true});
                    if (radic.defined(cache) && !radic.isNull(cache)) {
                        console.log('cache xhr', typeof cache, cache);
                        if (this.async === true) {
                            callback.call(this, cache.data, cache.meta);
                            return this;
                        } else {
                            return {data: cache.data, meta: cache.meta};
                        }
                    }
                }
                if (typeof callback !== 'function') {
                    verb = callback;
                    callback = this.callback;
                }

                var xhr = new XMLHttpRequest,
                    self = this;

                function complete(data) {
                    if (xhr.readyState === 4) {
                        self.state = 'complete';


                        var headerJson = {};
                        xhr.getAllResponseHeaders().split("\n").forEach(function (a) {
                            if (radic.isString(a) && a.length > 0) {
                                var header = a.split(':');
                                headerJson[header[0]] = header[1];
                            }
                        });

                        var responseData = JSON.parse(xhr.responseText);

                        var response = {data: responseData, meta: headerJson}
                        if (self.cache) {
                            radic.storage.set(cacheKey, response, {
                                expires: self.expires,
                                json: true
                            });
                        }

                        callback.call(self, responseData, headerJson, xhr);
                        return response
                    }
                }

                xhr.open(verb || 'GET', this.url(), this.async);
                if (this.headers.Authenticate) {
                    xhr.withCredentials = true;
                }

                Object.keys(this.headers).forEach(function (name) {
                    xhr.setRequestHeader(name, self.headers[name]);
                });

                xhr.onerror = complete;

                xhr.onreadystatechange = function (readyState) {
                    console.log('onreaddy change', readyState);
                };

                xhr.onload = complete;

                xhr.send(this.data || null);
                this.state = 'loading';
                return this.async === true ? this : complete();
            }
        });


        function makeCtor(args, api) {
            var Ctor = function () {
                var self = this instanceof Ctor ? this : Object.create(Ctor.prototype);
                return api.request(arguments, args, self);
            }

            decorate(Ctor, {
                args: Object.freeze(args),
                toString: function toString() {
                    return '[ ' + this.args.join(', ') + ' ]'
                }
            });
            return Ctor;
        }

        // #################
        // ### APIClient ###
        // #################

        // generalized REST API handler that turns routes into functions

        function APIClient(routes, onlyGetters) {
            var self = this;
            var slices = {};

            function recurse(o, path) {
                Object.keys(o).forEach(function (k) {
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
                            get: function () {
                                return path.map(function (s) {
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
            request: function request(args, fields, req) {
                args = [].slice.call(args);
                var callback = typeof args[args.length - 1] === 'function' ? args.pop() : this.callback;
                fields.forEach(function (p, i) {
                    if (typeof args[i] != null) {
                        req[p] = args[i];
                    }
                });
                var transport = decorate(Object.create(this.transport), {
                    path: req.path,
                    data: req
                });

                return transport.send(callback);
            },
            setTransport: function setTransport(type, base, dispatcher) {
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

        function GithubClient(user, password) {
            var self = this;


            function findRefs(obj) {
                isObject(obj) && Object.keys(obj).forEach(function (key) {
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

                    obj.resolve = function (cb) {
                        if (typeof cb === 'function') val.push(cb);
                        return fn.apply(null, val);
                    }.bind(null);

                    if (isObject(obj[key])) {
                        return findRefs(obj[key]);
                    }
                });
            }

            this.setTransport('xhr', 'https://api.github.com', function (result) {
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

        GithubClient.createClient = function createClient(user, pass) {
            return new GithubClient(user, pass);
        };

        GithubClient.prototype = Object.create(APIClient.prototype)
        decorate(GithubClient.prototype, {
            constructor: GithubClient,
            jsonp: function () {
                this.setTransport('jsonp', 'https://api.github.com')
            }
        });

        return GithubClient;

// ########################################
// ### Routes for Github V3 API in full ###
// ########################################

    }(new Function('return this')(), {
        legacy: {SLICE: 1, issues: {search: {Δowner: {Δrepository: {Δstate: {Δkeyword: {GET: []}}}}}}, repos: {search: {Δkeyword: {GET: ['language', 'start_page']}}}, user: {search: {Δkeyword: {GET: []}}, email: {Δemail: {GET: []}}}},
        gists: {
            SLICE: 1,
            POST: ['description', 'public', 'files'],
            GET: ['page', 'per_page'],
            public: {GET: []},
            starred: {GET: []},
            Δid: {GET: [], PATCH: ['description', 'files'], star: {GET: [], DELETE: [], POST: []}, fork: {POST: []}, comments: {GET: [], POST: ['input'], Δid: {GET: [], DELETE: [], PATCH: ['body']}}}
        },
        teams: {SLICE: 2, Δid: {GET: [], DELETE: [], PATCH: ['name', 'permission'], members: {GET: ['page', 'per_page'], Δuser: {GET: [], DELETE: [], POST: []}}, repos: {GET: ['page', 'per_page'], Δuser: {Δrepo: {GET: [], DELETE: [], POST: []}}}}},
        orgs: {
            SLICE: 2,
            Δorg: {
                GET: ['page', 'per_page'],
                PATCH: ['billing_email', 'company', 'email', 'location', 'name'],
                members: {GET: ['page', 'per_page'], Δuser: {GET: [], DELETE: []}},
                public_members: {GET: [], Δuser: {GET: [], DELETE: [], POST: []}},
                teams: {GET: [], POST: ['name', 'repo_names', 'permission']},
                repos: {GET: ['type', 'page', 'per_page'], POST: ['name', 'description', 'homepage', 'private', 'has_issues', 'has_wiki', 'has_downloads', 'team_id'], Δsha: {GET: []}}
            }
        },
        repos: {
            SLICE: 3, Δuser: {
                Δrepo: {
                    GET: [],
                    GET2: ['page', 'per_page'],
                    PATCH: ['name', 'description', 'homepage', 'private', 'has_issues', 'has_wiki', 'has_downloads'],
                    contributors: {GET: ['anon', 'page', 'per_page']},
                    languages: {GET: ['anon', 'page', 'per_page']},
                    teams: {GET: ['page', 'per_page']},
                    tags: {GET: ['page', 'per_page'], Δsha: {POST: ['tag', 'message', 'object', 'type', 'tagger.name', 'tagger.email', 'tagger.date']}},
                    git: {refs: {POST: ['refs', 'sha'], GET: ['page', 'per_page'], Δref: {GET: [], PATCH: ['sha', 'force']}}, commits: {POST: ['message', 'tree', 'parents', 'author', 'committer'], Δsha: {GET: []}}, blobs: {POST: ['content', 'encoding'], Δsha: {GET: ['page', 'per_page']}}},
                    branches: {GET: ['page', 'per_page']},
                    events: {GET: ['page', 'per_page']},
                    issues: {
                        GET: ['milestone', 'state', 'assignee', 'mentioned', 'labels', 'sort', 'direction', 'since', 'page', 'per_page'],
                        POST: ['title', 'body', 'assignee', 'milestone', 'labels'],
                        events: {GET: ['page', 'per_page'], GET2: [], Δid: {}},
                        Δnumber: {GET: [], PATCH: ['title', 'body', 'assignee', 'milestone', 'labels'], comments: {GET: ['page', 'per_page'], POST: ['body']}, events: {GET: ['page', 'per_page']}},
                        comments: {Δid: {GET: [], DELETE: [], PATCH: ['body']}},
                    },
                    pulls: {
                        GET: ['state', 'page', 'per_page'], POST: ['title', 'body', 'base', 'head'], POST2: ['issue', 'base', 'head'], Δnumber: {
                            GET: [], PATCH: ['state', 'title', 'body'], merge: {GET: ['page', 'per_page'], POST: ['commit_message']}, files: {GET: ['page', 'per_page']}, commits: {GET: ['page', 'per_page']},
                            comments: {POST: ['body', 'in_reply_to'], POST2: ['body', 'commit_id', 'path', 'position'], GET: ['page', 'per_page'],}
                        }, comments: {Δnumber: {GET: [], DELETE: [], PATCH: ['body']}}
                    },
                    commits: {GET: ['sha', 'path', 'page', 'per_page'], Δsha: {GET: [], comments: {GET: ['page', 'per_page'], POST: ['body', 'commit_id', 'line', 'path', 'position']}},},
                    comments: {Δid: {GET: [], DELETE: [], PATCH: ['body']}},
                    compare: {ΔbaseΔhead: {GET: ['base', 'head']}},
                    download: {GET: ['page', 'per_page']},
                    downloads: {Δid: {GET: [], DELETE: []}},
                    forks: {POST: ['org'], GET: ['sort', 'page', 'per_page']},
                    labels: {GET: [], POST: ['name', 'color'], Δname: {GET: [], POST: ['color']}},
                    keys: {GET: ['page', 'per_page'], POST: ['title', 'key'], Δid: {GET: [], DELETE: [], POST: ['title', 'key']}},
                    watchers: {GET: ['page', 'per_page']},
                    hooks: {GET: ['page', 'per_page'], POST: ['name', 'config', 'events', 'active'], Δid: {GET: [], DELETE: [], PATCH: ['name', 'config', 'events', 'add_events', 'remove_events', 'active'], test: {POST: []}}},
                    milestones: {POST: ['title', 'state', 'description', 'due_on'], GET: ['state', 'sort', 'page', 'per_page'], Δnumber: {DELETE: [], GET: [], PATCH: ['title', 'state', 'description', 'due_on']}},
                    trees: {POST: ['tree'], Δsha: {GET: ['recursive']}},
                    collaborators: {GET: ['page', 'per_page'], Δcollabuser: {GET: [], DELETE: [], POST: []}}
                }
            }
        },
        authorizations: {SLICE: 0, GET: []},
        user: {
            SLICE: 1,
            GET: [],
            PATCH: ['name', 'email', 'blog', 'company', 'location', 'hireable', 'bio'],
            gists: {GET: ['page', 'per_page']},
            emails: {GET: ['page', 'per_page'], DELETE: [], POST: []},
            following: {GET: ['page', 'per_page'], Δuser: {GET: ['page', 'per_page'], DELETE: [], POST: []}},
            watched: {GET: ['page', 'per_page'], Δuser: {Δrepo: {GET: ['page', 'per_page'], DELETE: [], POST: []}}},
            keys: {GET: ['page', 'per_page'], POST: ['title', 'key'], Δid: {GET: [], DELETE: [], PATCH: ['title', 'key']}},
            repos: {GET: ['type', 'page', 'per_page'], POST: ['name', 'description', 'homepage', 'private', 'has_issues', 'has_wiki', 'has_downloads']}
        },
        users: {
            SLICE: 2,
            Δuser: {
                GET: [],
                gists: {GET: ['page', 'per_page']},
                followers: {GET: ['page', 'per_page']},
                following: {GET: ['page', 'per_page']},
                orgs: {GET: ['page', 'per_page']},
                watched: {GET: ['page', 'per_page']},
                received_events: {GET: ['page', 'per_page']},
                events: {GET: ['page', 'per_page']},
                repos: {GET: ['type', 'page', 'per_page']}
            }
        },
        networks: {SLICE: 2, Δuser: {Δrepo: {events: {GET: ['page', 'per_page']}}, events: {orgs: {Δorg: {GET: ['page', 'per_page']}}}}},
        events: {SLICE: 1, GET: ['page', 'per_page']}
    }));

    radic.githubCredentials = {
        user: null,
        password: null,
        token: null
    };

    var makeGithubClient = function (Client, user, password) {
        console.log('make client', typeof Client, typeof user, typeof password);
        this.github = new Client(user, password);

        this.github.reset = function () {
            this.github = new Client(user, password);
        }.bind(this);

        this.github.authorize = function (user, password, callback) {
            callback = callback || password;
            var self = this;
            var github = new Client(user, password);
            github.user(function (data, xhr) {
                if (xhr.status === 200) {
                    makeGithubClient(user, password);
                    return callback(true, data, xhr);
                }
                callback(false, data, xhr)
            });
        }.bind(this);

        this.github.async = function (enabled) {
            this.github.transport.async = radic.isBoolean(enabled) ? enabled : true;
        }.bind(this);

        this.github.jsonp = function () {
            this.github.setTransport('jsonp', 'https://api.github.com');
        }.bind(this);

        this.github.xhr = function () {
            this.github.setTransport('xhr', 'https://api.github.com');
        }.bind(this);

    }.bind(radic, GithubClient);


    jQuery(document).ready(function () {

        if (radic.githubCredentials.token) {
            makeGithubClient(radic.githubCredentials.token);
        } else if (radic.githubCredentials.password) {
            makeGithubClient(radic.githubCredentials.user, radic.githubCredentials.password);
        } else {
            makeGithubClient();
        }

    });
    /*
     radic.extend({
     _github: makeGithubClient
     });

     radic._github();
     */


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


    /**
     * @mixin
     * @alias radic/template
     */
    var template = Handlebars;

    /**
     * Get a template
     *
     * @param name
     * @param data
     * @returns {*}
     */
    template.get = function(name, data){
        console.log('template get', name, Handlebars.templates);
        var template = Handlebars.templates[name];
        if(radic.isUndefined(data)){
            return template;
        }
        var html = template(data);

        return $($(html).html().trim());
    };


    radic.template = template;




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

    template.expressionRegistry.add('same', function (left, right) { return left === right; });



    radic.time = {};



    radic.time.ago = function (timestamp) {
        if (timestamp instanceof Date) {
            return inWords(timestamp);
        } else if (typeof timestamp === "string") {
            return inWords(radic.time.ago.parse(timestamp));
        } else if (typeof timestamp === "number") {
            return inWords(new Date(timestamp));
        } else {
            return inWords(radic.time.ago.datetime(timestamp));
        }
    };
    var $t = radic.time.ago;

    $.extend(radic.time.ago, {
        settings: {
            refreshMillis: 60000,
            allowPast: true,
            allowFuture: false,
            localeTitle: false,
            cutoff: 0,
            strings: {
                prefixAgo: null,
                prefixFromNow: null,
                suffixAgo: "ago",
                suffixFromNow: "from now",
                inPast: 'any moment now',
                seconds: "%d seconds",
                minute: "1 minute",
                minutes: "%d minutes",
                hour: "1 hour",
                hours: "%d hours",
                day: "1 day",
                days: "%d days",
                month: "1 month",
                months: "%d months",
                year: "1 year",
                years: "%d years",
                wordSeparator: " ",
                numbers: []
            }
        },

        inWords: function (distanceMillis) {
            if (!this.settings.allowPast && !this.settings.allowFuture) {
                throw 'timeago allowPast and allowFuture settings can not both be set to false.';
            }

            var $l = this.settings.strings;
            var prefix = $l.prefixAgo;
            var suffix = $l.suffixAgo;
            if (this.settings.allowFuture) {
                if (distanceMillis < 0) {
                    prefix = $l.prefixFromNow;
                    suffix = $l.suffixFromNow;
                }
            }

            if (!this.settings.allowPast && distanceMillis >= 0) {
                return this.settings.strings.inPast;
            }

            var seconds = Math.abs(distanceMillis) / 1000;
            var minutes = seconds / 60;
            var hours = minutes / 60;
            var days = hours / 24;
            var years = days / 365;

            function substitute(stringOrFunction, number) {
                var string = $.isFunction(stringOrFunction) ? stringOrFunction(number, distanceMillis) : stringOrFunction;
                var value = ($l.numbers && $l.numbers[number]) || number;
                return string.replace(/%d/i, value);
            }

            var words = seconds < 45 && substitute($l.seconds, Math.round(seconds)) ||
                seconds < 90 && substitute($l.minute, 1) ||
                minutes < 45 && substitute($l.minutes, Math.round(minutes)) ||
                minutes < 90 && substitute($l.hour, 1) ||
                hours < 24 && substitute($l.hours, Math.round(hours)) ||
                hours < 42 && substitute($l.day, 1) ||
                days < 30 && substitute($l.days, Math.round(days)) ||
                days < 45 && substitute($l.month, 1) ||
                days < 365 && substitute($l.months, Math.round(days / 30)) ||
                years < 1.5 && substitute($l.year, 1) ||
                substitute($l.years, Math.round(years));

            var separator = $l.wordSeparator || "";
            if ($l.wordSeparator === undefined) {
                separator = " ";
            }
            return $.trim([prefix, words, suffix].join(separator));
        },

        parse: function (iso8601) {
            var s = $.trim(iso8601);
            s = s.replace(/\.\d+/, ""); // remove milliseconds
            s = s.replace(/-/, "/").replace(/-/, "/");
            s = s.replace(/T/, " ").replace(/Z/, " UTC");
            s = s.replace(/([\+\-]\d\d)\:?(\d\d)/, " $1$2"); // -04:00 -> -0400
            s = s.replace(/([\+\-]\d\d)$/, " $100"); // +09 -> +0900
            return new Date(s);
        },
        datetime: function (elem) {
            var iso8601 = $t.isTime(elem) ? $(elem).attr("datetime") : $(elem).attr("title");
            return $t.parse(iso8601);
        },
        isTime: function (elem) {
            // jQuery's `is()` doesn't play well with HTML5 in IE
            return $(elem).get(0).tagName.toLowerCase() === "time"; // $(elem).is("time");
        }
    });

// functions that can be called via $(el).timeago('action')
// init is default when no action is given
// functions are called with context of a single element
    var functions = {
        init: function () {
            var refresh_el = $.proxy(refresh, this);
            refresh_el();
            var $s = $t.settings;
            if ($s.refreshMillis > 0) {
                this._timeagoInterval = setInterval(refresh_el, $s.refreshMillis);
            }
        },
        update: function (time) {
            var parsedTime = $t.parse(time);
            $(this).data('timeago', {datetime: parsedTime});
            if ($t.settings.localeTitle) $(this).attr("title", parsedTime.toLocaleString());
            refresh.apply(this);
        },
        updateFromDOM: function () {
            $(this).data('timeago', {datetime: $t.parse($t.isTime(this) ? $(this).attr("datetime") : $(this).attr("title"))});
            refresh.apply(this);
        },
        dispose: function () {
            if (this._timeagoInterval) {
                window.clearInterval(this._timeagoInterval);
                this._timeagoInterval = null;
            }
        }
    };

    $.fn.timeago = function (action, options) {
        var fn = action ? functions[action] : functions.init;
        if (!fn) {
            throw new Error("Unknown function name '" + action + "' for timeago");
        }
        // each over objects here and call the requested function
        this.each(function () {
            fn.call(this, options);
        });
        return this;
    };

    function refresh() {
        //check if it's still visible
        if (!$.contains(document.documentElement, this)) {
            //stop if it has been removed
            $(this).timeago("dispose");
            return this;
        }

        var data = prepareData(this);
        var $s = $t.settings;

        if (!isNaN(data.datetime)) {
            if ($s.cutoff == 0 || Math.abs(distance(data.datetime)) < $s.cutoff) {
                $(this).text(inWords(data.datetime));
            }
        }
        return this;
    }

    function prepareData(element) {
        element = $(element);
        if (!element.data("timeago")) {
            element.data("timeago", {datetime: $t.datetime(element)});
            var text = $.trim(element.text());
            if ($t.settings.localeTitle) {
                element.attr("title", element.data('timeago').datetime.toLocaleString());
            } else if (text.length > 0 && !($t.isTime(element) && element.attr("title"))) {
                element.attr("title", text);
            }
        }
        return element.data("timeago");
    }

    function inWords(date) {
        return $t.inWords(distance(date));
    }

    function distance(date) {
        return (new Date().getTime() - date.getTime());
    }


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

            return radic.template.get(template, data);
        },
        _getCreateEventData: function() {
            return this.options;
        },
        _pluginExists: function(plugin){
            return radic.defined($.fn[plugin]);
        }
    });





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

