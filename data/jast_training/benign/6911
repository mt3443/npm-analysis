var ColumnType = /** @class */ (function () {
    function ColumnType() {
    }
    Object.defineProperty(ColumnType, "Date", {
        get: function () {
            var type = new ColumnType();
            type.IsDate = true;
            return type;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(ColumnType, "DateTime", {
        get: function () {
            var type = new ColumnType();
            type.IsDateTime = true;
            return type;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(ColumnType, "Number", {
        get: function () {
            var type = new ColumnType();
            type.IsNumber = true;
            return type;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(ColumnType, "String", {
        get: function () {
            var type = new ColumnType();
            type.IsString = true;
            return type;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(ColumnType, "Boolean", {
        get: function () {
            var type = new ColumnType();
            type.IsBoolean = true;
            return type;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(ColumnType, "Currency", {
        get: function () {
            var type = new ColumnType();
            type.IsCurrency = true;
            return type;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(ColumnType, "Fill", {
        get: function () {
            var type = new ColumnType();
            type.IsFill = true;
            return type;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(ColumnType.prototype, "Name", {
        get: function () {
            if (this.IsNumber)
                return "Number";
            if (this.IsDate)
                return "Date";
            if (this.IsDateTime)
                return "DateTime";
            if (this.IsString)
                return "String";
            if (this.IsBoolean)
                return "Boolean";
            if (this.IsCurrency)
                return "Currency";
            if (this.IsFill)
                return "Fill";
            return "";
        },
        enumerable: true,
        configurable: true
    });
    return ColumnType;
}());
export { ColumnType };
