define([
    "./core",
    "./json"
], function(radic, json) {

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
    return radic;
});
