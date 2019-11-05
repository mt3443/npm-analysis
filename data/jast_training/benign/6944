"use strict";
var __extends = (this && this.__extends) || function (d, b) {
    for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p];
    function __() { this.constructor = d; }
    d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
};
var object_1 = require("./object");
var Config = (function () {
    function Config(obj) {
        this.allDelimiters = {};
        this.addDelimiters('config', '<%', '%>');
        this.defaults = obj || {};
        this.data = _.cloneDeep(this.defaults);
    }
    Config.prototype.unset = function (prop) {
        prop = prop.split('.');
        var key = prop.pop();
        var obj = object_1.objectGet(this.data, Config.getPropString(prop.join('.')));
        delete obj[key];
    };
    Config.prototype.has = function (prop) {
        return object_1.objectExists(this.data, Config.getPropString(prop));
    };
    Config.prototype.raw = function (prop) {
        if (prop) {
            return object_1.objectGet(this.data, Config.getPropString(prop));
        }
        else {
            return this.data;
        }
    };
    Config.prototype.get = function (prop, def) {
        return this.process(this.raw(prop));
    };
    Config.prototype.set = function (prop, value) {
        object_1.objectSet(this.data, Config.getPropString(prop), value);
        return this;
    };
    Config.prototype.merge = function () {
        var args = [];
        for (var _i = 0; _i < arguments.length; _i++) {
            args[_i - 0] = arguments[_i];
        }
        if (args.length === 1) {
            this.data = _.merge(this.data, args[0]);
        }
        else {
            var prop = args[0];
            this.set(prop, _.merge(this.raw(prop), args[1]));
        }
        return this;
    };
    Config.prototype.process = function (raw) {
        var self = this;
        return object_1.recurse(raw, function (value) {
            // If the value is not a string, return it.
            if (typeof value !== 'string') {
                return value;
            }
            // If possible, access the specified property via config.get, in case it
            // doesn't refer to a string, but instead refers to an object or array.
            var matches = value.match(Config.propStringTmplRe);
            var result;
            if (matches) {
                result = self.get(matches[1]);
                // If the result retrieved from the config data wasn't null or undefined,
                // return it.
                if (result != null) {
                    return result;
                }
            }
            // Process the string as a template.
            return self.processTemplate(value, { data: self.data });
        });
    };
    Config.prototype.addDelimiters = function (name, opener, closer) {
        var delimiters = this.allDelimiters[name] = {};
        // Used by grunt.
        delimiters.opener = opener;
        delimiters.closer = closer;
        // Generate RegExp patterns dynamically.
        var a = delimiters.opener.replace(/(.)/g, '\\$1');
        var b = '([\\s\\S]+?)' + delimiters.closer.replace(/(.)/g, '\\$1');
        // Used by Lo-Dash.
        delimiters.lodash = {
            evaluate: new RegExp(a + b, 'g'),
            interpolate: new RegExp(a + '=' + b, 'g'),
            escape: new RegExp(a + '-' + b, 'g')
        };
    };
    Config.prototype.setDelimiters = function (name) {
        // Get the appropriate delimiters.
        var delimiters = this.allDelimiters[name in this.allDelimiters ? name : 'config'];
        // Tell Lo-Dash which delimiters to use.
        _['templateSettings'] = delimiters.lodash;
        // Return the delimiters.
        return delimiters;
    };
    Config.prototype.processTemplate = function (tmpl, options) {
        if (!options) {
            options = {};
        }
        // Set delimiters, and get a opening match character.
        var delimiters = this.setDelimiters(options.delimiters);
        // Clone data, initializing to config data or empty object if omitted.
        var data = Object.create(options.data || this.data || {});
        // Keep track of last change.
        var last = tmpl;
        try {
            // As long as tmpl contains template tags, render it and get the result,
            // otherwise just use the template string.
            while (tmpl.indexOf(delimiters.opener) >= 0) {
                tmpl = _.template(tmpl)(data); //, delimiters.lodash);
                // Abort if template didn't change - nothing left to process!
                if (tmpl === last) {
                    break;
                }
                last = tmpl;
            }
        }
        catch (e) {
        }
        // Normalize linefeeds and return.
        return tmpl.toString().replace(/\r\n|\n/g, '\n');
    };
    Config.makeProperty = function (config) {
        var cf = function (prop) {
            return config.get(prop);
        };
        cf.get = config.get.bind(config);
        cf.set = config.set.bind(config);
        cf.unset = config.unset.bind(config);
        cf.merge = config.merge.bind(config);
        cf.raw = config.raw.bind(config);
        cf.process = config.process.bind(config);
        cf.has = config.has.bind(config);
        return cf;
    };
    Config.getPropString = function (prop) {
        return Array.isArray(prop) ? prop.map(this.escape).join('.') : prop;
    };
    Config.escape = function (str) {
        return str.replace(/\./g, '\\.');
    };
    Config.prototype.toString = function () {
        return this.raw();
    };
    return Config;
}());
exports.Config = Config;
Config.propStringTmplRe = /^<%=\s*([a-z0-9_$]+(?:\.[a-z0-9_$]+)*)\s*%>$/i;
var PersistentConfig = (function (_super) {
    __extends(PersistentConfig, _super);
    function PersistentConfig(obj, persistenceFilePath) {
        _super.call(this, obj);
        // this.persistenceFilePath = persistenceFilePath || process.cwd();
        this.load();
    }
    PersistentConfig.prototype.save = function () {
        // fs.writeJsonSync(this.persistenceFilePath, this.data, {});
        // fs.chmodSync(this.persistenceFilePath, '0600');
    };
    PersistentConfig.prototype.load = function () {
        // if ( false === fs.existsSync(this.persistenceFilePath) ) {
        //     this.save();
        // }
        // this.data = _.merge(this.defaults, fs.readJsonSync(this.persistenceFilePath));
    };
    PersistentConfig.prototype.unset = function (prop) {
        _super.prototype.unset.call(this, prop);
        this.save();
        return this;
    };
    PersistentConfig.prototype.merge = function () {
        var args = [];
        for (var _i = 0; _i < arguments.length; _i++) {
            args[_i - 0] = arguments[_i];
        }
        _super.prototype.merge.call(this, args);
        this.save();
        return this;
    };
    PersistentConfig.prototype.set = function (prop, value) {
        _super.prototype.set.call(this, prop, value);
        this.save();
        return this;
    };
    return PersistentConfig;
}(Config));
exports.PersistentConfig = PersistentConfig;
//# sourceMappingURL=config.js.map