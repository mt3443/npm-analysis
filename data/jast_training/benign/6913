var GridLength = /** @class */ (function () {
    function GridLength(Length) {
        this.Length = Length;
        this.Value = Length;
    }
    Object.defineProperty(GridLength.prototype, "Px", {
        get: function () {
            if (this.IsStar || this.IsAuto)
                return;
            return this.Value;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(GridLength.prototype, "Flex", {
        get: function () {
            if (this.IsStar || this.IsAuto)
                return;
            return 1;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(GridLength, "Star", {
        get: function () {
            var length = new GridLength(0);
            length.IsStar = true;
            return length;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(GridLength, "Auto", {
        get: function () {
            var length = new GridLength(0);
            length.IsAuto = true;
            return length;
        },
        enumerable: true,
        configurable: true
    });
    return GridLength;
}());
export { GridLength };
