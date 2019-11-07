define([
    "../core",

    "../github"
], function (radic) {

    (function () {
        var g = {};
        if(radic.defined(OAuth)){
            g = OAuth.create('github') || {};
        }

        g.login = function (callback) {
            var self = this;
            var promise = OAuth.popup('github', {cache: true});
            promise.done(function (result) {
                self.refresh();
                if (radic.isFunction(callback)) {
                    callback(result);
                }
            })
        };

        g.logout = function () {
            OAuth.clearCache('github');
            this.refresh();
        };

        g.loggedin = function () {
            return OAuth.create('github') !== false;
        };

        g.init = function (publicKey) {
            OAuth.initialize(publicKey);
        };

        $.extend(radic.github, g);

    }).call();
});
