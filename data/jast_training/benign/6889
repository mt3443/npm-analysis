var Dictionary = /** @class */ (function () {
    function Dictionary(init) {
        this.keys = [];
        this.values = [];
        if (!init || init.length == 0)
            return;
        for (var x = 0; x < init.length; x++) {
            this[init[x].key] = init[x].value;
            this.keys.push(init[x].key);
            this.values.push(init[x].value);
        }
    }
    Dictionary.prototype.any = function () {
        return this.values ? this.values.length > 0 : false;
    };
    Object.defineProperty(Dictionary.prototype, "length", {
        get: function () {
            return this.values.length;
        },
        enumerable: true,
        configurable: true
    });
    Dictionary.prototype.add = function (key, value) {
        this[key] = value;
        this.keys.push(key);
        this.values.push(value);
    };
    Dictionary.prototype.remove = function (key) {
        var index = this.keys.indexOf(key, 0);
        this.keys.splice(index, 1);
        this.values.splice(index, 1);
        delete this[key];
    };
    Object.defineProperty(Dictionary.prototype, "Keys", {
        get: function () {
            return this.keys;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(Dictionary.prototype, "Values", {
        get: function () {
            return this.values;
        },
        enumerable: true,
        configurable: true
    });
    Dictionary.prototype.containsKey = function (key) {
        if (typeof this[key] === "undefined") {
            return false;
        }
        return true;
    };
    Dictionary.prototype.toLookup = function () {
        return this;
    };
    return Dictionary;
}());
export { Dictionary };
