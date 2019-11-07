define([
    "../core",
    "../template"
], function (radic) {

    radic.template.registerHelper('default', function (value, defaultValue) {
        return value != null ? value : defaultValue;
    });

    radic.template.registerHelper('arrayIndex', function (context, ndx) {
        return context[ndx];
    });

});
