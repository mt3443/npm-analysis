define(function(){

    /** Used for native method references */
    var objectProto = Object.prototype;

    /** Used to resolve the internal [[Class]] of values */
    var toString = objectProto.toString;




    function toArray(collection) {
        if (isArray(collection)) {
            return slice(collection);
        }
        if (collection && typeof collection.length == 'number') {
            return map(collection);
        }
        return values(collection);
    }
})
