define([
    "../core",
    "./var/only_once",
    "./var/_each",

    "../async"
], function (radic, only_once, _each) {

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

    return radic;
});
