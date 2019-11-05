var ColumnAggregate = /** @class */ (function () {
    function ColumnAggregate() {
    }
    Object.defineProperty(ColumnAggregate, "Sum", {
        get: function () {
            var type = new ColumnAggregate();
            type.IsSum = true;
            return type;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(ColumnAggregate.prototype, "Name", {
        get: function () {
            if (this.IsSum)
                return "Sum";
            return;
        },
        enumerable: true,
        configurable: true
    });
    return ColumnAggregate;
}());
export { ColumnAggregate };
