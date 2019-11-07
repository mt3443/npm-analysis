import { GridCell } from "../../../../controls/components/grid/grid-cell/grid-cell";
import { DateExtensions } from "../../../../objects/extensions/date-extensions";
var ColumnFilter = /** @class */ (function () {
    function ColumnFilter(Column, FilterText, SearchType, SelectedDistinctValues) {
        this.Column = Column;
        this.FilterText = FilterText;
        this.SearchType = SearchType;
        this.SelectedDistinctValues = SelectedDistinctValues;
    }
    ColumnFilter.prototype.Filter = function (row) {
        var cellValue = GridCell.GetProperty(this.Column, row);
        var isFilterMatch = false;
        if (this.FilterText) {
            if (this.Column.Type.IsNumber) {
                isFilterMatch = this.IsFilterMatchNumber(cellValue);
            }
            else if (this.Column.Type.IsDate || this.Column.Type.IsDateTime) {
                isFilterMatch = this.IsFilterMatchDate(cellValue);
            }
            else if (this.Column.Type.IsString) {
                isFilterMatch = this.IsFilterMatchString(cellValue);
            }
            else {
                isFilterMatch = this.IsFilterMatchString(cellValue);
            }
        }
        if (this.FilterText && this.SelectedDistinctValues != undefined && this.SelectedDistinctValues.length > 0)
            return isFilterMatch && this.IsDistinctMatch(cellValue);
        else if (this.FilterText)
            return isFilterMatch;
        else if (this.SelectedDistinctValues != undefined && this.SelectedDistinctValues.length > 0)
            return this.IsDistinctMatch(cellValue);
        else
            return false;
    };
    ColumnFilter.prototype.IsFilterMatchString = function (cellValue) {
        if (this.FilterText && this.SearchType != undefined) {
            var lowercaseFilterText = this.FilterText.toLowerCase();
            var lowerCaseCellValue = cellValue.toString().toLowerCase();
            switch (this.SearchType) {
                case 0:
                    // Contains
                    return lowerCaseCellValue.indexOf(lowercaseFilterText) !== -1;
                case 1:
                    // Does Not Contain
                    return lowerCaseCellValue.indexOf(lowercaseFilterText) === -1;
                case 2:
                    // Starts With
                    return lowerCaseCellValue.indexOf(lowercaseFilterText) === 0;
                case 3:
                    // Ends With
                    return lowerCaseCellValue.indexOf(lowercaseFilterText, lowerCaseCellValue.length - lowercaseFilterText.length) !== -1;
            }
        }
        return false;
    };
    ColumnFilter.prototype.IsFilterMatchNumber = function (cellValue) {
        if (this.FilterText && this.SearchType != undefined) {
            var filterTextAsNumber = Number(this.FilterText);
            switch (this.SearchType) {
                case 0:
                    // Equals
                    return cellValue == filterTextAsNumber;
                case 1:
                    // Less Than (<)
                    return cellValue < filterTextAsNumber;
                case 2:
                    // Less Than or Equal to (<=)
                    return cellValue <= filterTextAsNumber;
                case 3:
                    // Greater Than (>)
                    return cellValue > filterTextAsNumber;
                case 4:
                    // Greater Than or Equal to (>=)
                    return cellValue >= filterTextAsNumber;
            }
        }
        return false;
    };
    ColumnFilter.prototype.IsFilterMatchDate = function (cellValue) {
        if (this.FilterText && this.SearchType != undefined) {
            var filterTextAsDate = DateExtensions.GetDate(this.FilterText, 'DD-MMM-YYYY');
            var cellValueAsDate = DateExtensions.GetDate(cellValue, 'DD-MMM-YYYY');
            switch (this.SearchType) {
                case 0:
                    // Is After
                    return cellValueAsDate > filterTextAsDate;
                case 1:
                    // Is On or After
                    return cellValueAsDate >= filterTextAsDate;
                case 2:
                    // Is Before
                    return cellValueAsDate < filterTextAsDate;
                case 3:
                    // Is On or Before
                    return cellValueAsDate <= filterTextAsDate;
            }
        }
        return false;
    };
    ColumnFilter.prototype.IsDistinctMatch = function (cellValue) {
        if (this.SelectedDistinctValues != undefined && this.SelectedDistinctValues.length > 0) {
            return this.SelectedDistinctValues.map(function (e) { return e.Name.toLowerCase(); }).indexOf(cellValue.toString().toLowerCase()) !== -1;
        }
        return false;
    };
    return ColumnFilter;
}());
export { ColumnFilter };
