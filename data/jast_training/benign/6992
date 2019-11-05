define([
    "../core",

    "../github",
    "../storage"
], function (radic) {

    // @todo depracteed delete

    radic.github.syncRequest = function (uri) {

        radic.github.transport.async = false;
        var base = radic.github.transport.base;
        radic.github.transport.base = base + uri;
        var responseText = radic.github.transport.send();
        radic.github.transport.async = true;
        radic.github.transport.base = base;
        return responseText;
    };


    radic.github.sync = function (uri, options) {
        options = $.extend({expires: 60, force: false}, options);

        if (options.force === false) {
            var val = radic.storage.get(uri, {
                json: true
            });
            if (val !== null) {
                return val;
            }
        }

        var response = JSON.parse(radic.github.syncRequest(uri));

        radic.storage.set(uri, response, {
            json: true,
            expires: options.expires
        });

        return response;
    };
});
