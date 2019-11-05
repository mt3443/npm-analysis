define(function() {

    return function (fn) {
        var called = false;
        return function () {
            if (called) throw new Error("Callback was already called.");
            called = true;
            fn.apply(window, arguments);
        }
    }
});