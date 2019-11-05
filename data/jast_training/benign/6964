define([
    "./core",
    "./core/getlodash"
], function (radic, getlodash) {

    radic.extend(getlodash());

    radic.defined = radic.isDefined = function(val){
        return radic.isUndefined(val) === false;
    };

    return radic;
});
