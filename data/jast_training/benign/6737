var __extends = (this && this.__extends) || (function () {
    var extendStatics = Object.setPrototypeOf ||
        ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
        function (d, b) { for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p]; };
    return function (d, b) {
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { Component, forwardRef, HostListener, Input, ViewChild } from '@angular/core';
import { ModalDialog } from '../../../../controls/components/modal/modal-dialog';
import { ContextMenuComponent } from '../../../../controls/components/context-menu/context-menu-component';
import { ListBoxComponent } from '../../../../controls/components/boxes/list-box/list-box-component';
import { Column } from '../../../../objects/request/column';
import { SortDirection } from '../../../../objects/enums/sort-direction';
import { GridCell } from '../../../../controls/components/grid/grid-cell/grid-cell';
import { DateExtensions } from '../../../../objects/extensions/date-extensions';
import { ControlsModule } from '../../../../controls/controls-module';
var ColumnFilterPopup = /** @class */ (function (_super) {
    __extends(ColumnFilterPopup, _super);
    function ColumnFilterPopup() {
        var _this = _super.call(this) || this;
        _this.ColumnFilterSearchOptions = [];
        _this.columnFilterDistinctItems = [];
        _this.selectedColumnFilterDistinctItems = [];
        return _this;
    }
    ColumnFilterPopup_1 = ColumnFilterPopup;
    Object.defineProperty(ColumnFilterPopup.prototype, "ColumnFilterDistinctItems", {
        get: function () {
            return this.columnFilterDistinctItems;
        },
        set: function (value) {
            this.columnFilterDistinctItems = value;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(ColumnFilterPopup.prototype, "SelectedColumnFilterDistinctItems", {
        get: function () {
            return this.selectedColumnFilterDistinctItems;
        },
        set: function (value) {
            this.selectedColumnFilterDistinctItems = value;
            this.Grid.SetFilter(this.Column, this.ColumnFilter, this.SelectedColumnFilterSearchOption ? this.SelectedColumnFilterSearchOption.Value : null, this.SelectedColumnFilterDistinctItems);
        },
        enumerable: true,
        configurable: true
    });
    ColumnFilterPopup.prototype.onClick = function (event) {
        event.stopPropagation();
    };
    ColumnFilterPopup.prototype.InitializeFilters = function () {
        var _this = this;
        // Set the filter options based on the data type of the column.
        this.SetFilterOptions();
        if (this.Grid.Filters.containsKey(this.Column.Key)) {
            this.ColumnFilter = this.Grid.Filters[this.Column.Key].FilterText;
            this.SelectedColumnFilterSearchOption = this.ColumnFilterSearchOptions.find(function (x) { return x.Value == _this.Grid.Filters[_this.Column.Key].SearchType; });
        }
        else {
            this.ColumnFilter = undefined;
        }
        if (this.Column['_hasFilter'] === undefined || this.Column['_hasFilter'] === false) {
            // Since no filter haa been set we need to store these distinct values.
            this.Column['_distinctValues'] = this.GetDistinctItems(this.Column);
        }
        this.SetDistinctItems(this.Column);
    };
    ColumnFilterPopup.prototype.OnHideColumn = function () {
        this.Grid.ShowHideColumn(this.Column);
    };
    ColumnFilterPopup.prototype.OnSortAscendingColumn = function () {
        this.Grid.SetSort(this.Column, SortDirection.Ascending);
    };
    ColumnFilterPopup.prototype.OnSortDescendingColumn = function () {
        this.Grid.SetSort(this.Column, SortDirection.Descending);
    };
    ColumnFilterPopup.prototype.OnClearFilter = function () {
        this.Column['_hasFilter'] = false;
        this.Column['_selectedDistinctValues'] = undefined;
        this.Column['_distinctValues'] = undefined;
        this.Grid.ClearFilter(this.Column);
        this.SelectedColumnFilterSearchOption = undefined;
        this.ColumnFilter = "";
        this.SelectedColumnFilterDistinctItems.length = 0;
        this.ColumnFilterDistinctItems.length = 0;
        this.Column['_distinctValues'] = this.GetDistinctItems(this.Column);
        this.SetDistinctItems(this.Column);
    };
    ColumnFilterPopup.prototype.OnSetFilter = function () {
        if (this.ColumnFilter && this.SelectedColumnFilterSearchOption) {
            this.Grid.SetFilter(this.Column, this.ColumnFilter, this.SelectedColumnFilterSearchOption.Value, this.SelectedColumnFilterDistinctItems);
        }
        else {
            // User either did not specify filter criteria or removed the filter text and/or search type.
            this.SelectedColumnFilterSearchOption = undefined;
            this.ColumnFilter = "";
            this.Grid.SetFilter(this.Column, undefined, undefined, this.SelectedColumnFilterDistinctItems);
        }
    };
    ColumnFilterPopup.prototype.OnColumnSetSize = function (column) {
    };
    ColumnFilterPopup.prototype.OnDistinctColumnFilter = function (column) {
        if (this.SelectedColumnFilterDistinctItems === undefined || this.SelectedColumnFilterDistinctItems.length === 0) {
            // The user deselected all of the column filters. For now we will reset everything to get all distinct values back.
            this.OnClearFilter();
        }
        else {
            this.Grid.SetFilter(column, this.ColumnFilter, this.SelectedColumnFilterSearchOption ? this.SelectedColumnFilterSearchOption.Value : null, this.SelectedColumnFilterDistinctItems);
        }
    };
    ColumnFilterPopup.prototype.SetFilterOptions = function () {
        if (this.Column.Type.IsNumber) {
            this.ColumnFilterSearchOptions = [
                { Name: 'Equals (=)', Value: 0 },
                { Name: 'Is Less Than (<)', Value: 1 },
                { Name: 'Is Less Than or Equal to (<=)', Value: 2 },
                { Name: 'Is Greater Than (>)', Value: 3 },
                { Name: 'Is Greater Than or Equal to (>=)', Value: 4 },
            ];
        }
        else if (this.Column.Type.IsDate || this.Column.Type.IsDateTime) {
            this.ColumnFilterSearchOptions = [
                { Name: 'Is After', Value: 0 },
                { Name: 'Is On or After', Value: 1 },
                { Name: 'Is Before', Value: 2 },
                { Name: 'Is On or Before', Value: 3 },
            ];
        }
        else {
            this.ColumnFilterSearchOptions = [
                { Name: 'Contains', Value: 0 },
                { Name: 'Does not contain', Value: 1 },
                { Name: 'Starts with', Value: 2 },
                { Name: 'Ends with', Value: 3 },
            ];
        }
    };
    ColumnFilterPopup.prototype.IsChecked = function (item) {
        if (this.listBox.SelectedItems && this.listBox.SelectedItems.includes(item))
            return true;
        return false;
    };
    ColumnFilterPopup.prototype.GetDistinctItems = function (column) {
        var distinctItems = [];
        var unique = {};
        // Identify all unique values.
        for (var i = 0; i < this.Grid.Rows.length; i++) {
            var cellValue = GridCell.GetProperty(column, this.Grid.Rows[i]);
            if (typeof (unique[cellValue]) == "undefined") {
                distinctItems.push(cellValue);
            }
            unique[cellValue] = 0;
        }
        // Return the unique values sorted by data type.
        return this.GetItemsSortedByDataType(distinctItems);
    };
    ColumnFilterPopup.prototype.GetItemsSortedByDataType = function (items) {
        if (this.Column.Type.IsNumber) {
            return items.sort(this.SortByNumber);
        }
        else if (this.Column.Type.IsDate || this.Column.Type.IsDateTime) {
            return items.sort(this.SortByDateAscending);
        }
        else {
            return items.sort();
        }
    };
    ColumnFilterPopup.prototype.SetDistinctItems = function (column) {
        var isChecked = false;
        var selectedItems = column['_selectedDistinctValues'];
        var distinctItems = column['_distinctValues'];
        var itemsSource = [];
        var maxDistinctItems = 10000 < distinctItems.length ? 10000 : distinctItems.length;
        // Construct ItemsSource. Set to "Checked" all previously selected values.
        for (var i = 0; i < maxDistinctItems; i++) {
            var value = distinctItems[i];
            var item = { Name: value, IsChecked: false };
            if (selectedItems != undefined) {
                if (selectedItems.map(function (e) { return e.Name; }).indexOf(value) !== -1) {
                    item.IsChecked = true;
                    this.selectedColumnFilterDistinctItems.push(item);
                }
            }
            itemsSource.push(item);
        }
        this.ColumnFilterDistinctItems = itemsSource;
    };
    ColumnFilterPopup.prototype.SortByNumber = function (a, b) {
        return a - b;
    };
    ColumnFilterPopup.prototype.SortByDateAscending = function (a, b) {
        return (DateExtensions.GetDate(b, 'DD-MMM-YYYY') - DateExtensions.GetDate(a, 'DD-MMM-YYYY')) * -1;
    };
    ColumnFilterPopup.Show = function (event, grid, column) {
        var popup = ControlsModule.dialog.Show(ColumnFilterPopup_1);
        popup.Column = column;
        popup.Grid = grid;
        popup.InitializeFilters();
        popup.ContextMenu.Open.subscribe(function (value) {
            if (!value)
                popup.Close(value);
        });
        popup.ContextMenu.Show(event.clientX, event.clientY);
    };
    __decorate([
        ViewChild('contextMenu'),
        __metadata("design:type", ContextMenuComponent)
    ], ColumnFilterPopup.prototype, "ContextMenu", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], ColumnFilterPopup.prototype, "ColumnFilter", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], ColumnFilterPopup.prototype, "SelectedColumnFilterSearchOption", void 0);
    __decorate([
        ViewChild(forwardRef(function () { return ListBoxComponent; })),
        __metadata("design:type", ListBoxComponent)
    ], ColumnFilterPopup.prototype, "listBox", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Column)
    ], ColumnFilterPopup.prototype, "Column", void 0);
    __decorate([
        HostListener("click", ["$event"]),
        __metadata("design:type", Function),
        __metadata("design:paramtypes", [Object]),
        __metadata("design:returntype", void 0)
    ], ColumnFilterPopup.prototype, "onClick", null);
    ColumnFilterPopup = ColumnFilterPopup_1 = __decorate([
        Component({
            //templateUrl: './app/controls/components/grid/filters/column-filter-popup.html',
            templateUrl: './column-filter-popup.html',
            styles: ["\n    :host {   \n      position: absolute;\n      height: 100%;\n      width: 100%;\n      top: 0px;\n      z-index: 1000;\n      pointer-events: none;\n    }\n  "]
        }),
        __metadata("design:paramtypes", [])
    ], ColumnFilterPopup);
    return ColumnFilterPopup;
    var ColumnFilterPopup_1;
}(ModalDialog));
export { ColumnFilterPopup };
