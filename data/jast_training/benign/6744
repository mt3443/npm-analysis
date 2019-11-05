var GridColumnRange = /** @class */ (function () {
    function GridColumnRange(columns, left, right) {
        this.left = left;
        this.right = right;
        this.LeftIndex = this.GetLeftIndex(columns, left);
        this.RightIndex = this.GetRightIndex(columns, right);
    }
    GridColumnRange.prototype.GetLeftIndex = function (columns, left) {
        for (var i = 0; i < columns.length; i++) {
            var column = columns[i];
            if (column['_right'] >= left)
                return i;
        }
        return 0;
    };
    GridColumnRange.prototype.GetRightIndex = function (columns, right) {
        for (var i = 0; i < columns.length; i++) {
            var column = columns[i];
            //if (column['_left'] + column.Width.Value > right)
            if (column['_right'] >= right)
                return i;
        }
        return columns.length - 1;
    };
    GridColumnRange.GetVisibleColumns = function (columns, left, right) {
        var range = new GridColumnRange(columns, left, right);
        return columns.slice(range.LeftIndex, range.RightIndex + 1);
    };
    return GridColumnRange;
}());
export { GridColumnRange };
