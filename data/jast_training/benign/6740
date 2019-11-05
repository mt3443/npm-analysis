import { NumberExtensions } from "../../../../objects/extensions/number-extensions";
import { DateExtensions } from "../../../../objects/extensions/date-extensions";
var GridCell = /** @class */ (function () {
    function GridCell(row, column) {
        this.Row = row;
        this.Column = column;
    }
    GridCell.GetProperty = function (column, row) {
        if (!row)
            return "";
        if (!column)
            return row;
        if (column.Type.IsFill)
            return "";
        var property = GridCell.GetPropertyByPath(column.Property, row);
        if (column.Type.IsNumber)
            return property ? property.toLocaleString() : column.DefaultValue;
        if (column.Type.IsString)
            return property ? property : column.DefaultValue;
        if (column.Type.IsCurrency)
            return property ? NumberExtensions.GetCurrency(property) : column.DefaultValue;
        if (column.Type.IsDate) {
            if (column.Format)
                return property ? DateExtensions.GetDate(property, column.Format) : column.DefaultValue;
            return property ? DateExtensions.GetUtcDate(property) : column.DefaultValue;
        }
        if (column.Type.IsDateTime) {
            if (column.Format)
                return property ? DateExtensions.GetDateTime(property, column.Format) : column.DefaultValue;
            return property ? DateExtensions.GetUtcDateTime(property) : column.DefaultValue;
        }
        return property;
    };
    GridCell.GetPropertyByPath = function (path, row) {
        var property = row;
        if (!path)
            return property;
        var paths = path.split(".");
        for (var i = 0; i < paths.length; i++) {
            var value = paths[i];
            if (property && (property.hasOwnProperty(value) || property.__proto__.hasOwnProperty(value)))
                property = property[value];
            else
                return;
        }
        return property;
    };
    return GridCell;
}());
export { GridCell };
