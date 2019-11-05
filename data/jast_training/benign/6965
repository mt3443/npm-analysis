define([
    "./core"
], function(radic) {

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
    return radic;
});
