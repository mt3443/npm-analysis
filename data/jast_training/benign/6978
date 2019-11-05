define([
    "./core"
], function( radic ) {

    function wordwrap(str, width, spaceReplacer) {
        if (str.length>width) {
            str = str.substr(0, width) + spaceReplacer;
        }
        return str;
    }

    radic.extend({ wordwrap: wordwrap })

    return radic;
});
