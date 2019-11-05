import { SortDirection } from "../../../../objects/enums/sort-direction";
import { GridCell } from "../../../../controls/components/grid/grid-cell/grid-cell";
import { DateExtensions } from "../../../../objects/extensions/date-extensions";
var ColumnSort = /** @class */ (function () {
    function ColumnSort(Column, Direction) {
        this.Column = Column;
        this.Direction = Direction;
    }
    ColumnSort.prototype.Sort = function (a, b) {
        var valueA = GridCell.GetProperty(this.Column, a);
        var valueB = GridCell.GetProperty(this.Column, b);
        if (this.Direction == SortDirection.Ascending) {
            if (this.Column.Type.IsNumber) {
                return this.SortByNumberAscending(valueA, valueB);
            }
            else if (this.Column.Type.IsDate || this.Column.Type.IsDateTime) {
                return this.SortByDateAscending(valueA, valueB);
            }
            else {
                return valueA.localeCompare(valueB);
            }
        }
        else if (this.Direction == SortDirection.Descending) {
            if (this.Column.Type.IsNumber) {
                return this.SortByNumberDescending(valueA, valueB);
            }
            else if (this.Column.Type.IsDate || this.Column.Type.IsDateTime) {
                return this.SortByDateDescending(valueA, valueB);
            }
            else {
                return valueB.localeCompare(valueA);
            }
        }
    };
    ColumnSort.prototype.SortByNumberAscending = function (a, b) {
        return a - b;
    };
    ColumnSort.prototype.SortByNumberDescending = function (a, b) {
        return (a - b) * -1;
    };
    ColumnSort.prototype.SortByDateAscending = function (a, b) {
        return (DateExtensions.GetDate(b, 'DD-MMM-YYYY') - DateExtensions.GetDate(a, 'DD-MMM-YYYY')) * -1;
    };
    ColumnSort.prototype.SortByDateDescending = function (a, b) {
        return (DateExtensions.GetDate(b, 'DD-MMM-YYYY') - DateExtensions.GetDate(a, 'DD-MMM-YYYY'));
    };
    return ColumnSort;
}());
export { ColumnSort };
