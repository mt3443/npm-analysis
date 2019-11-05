var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { Component, ChangeDetectorRef, ChangeDetectionStrategy, Input, } from '@angular/core';
import { DialogService } from '../../../../controls/services/dialog/dialog-service';
import { GridComponent } from '../../../../controls/components/grid/grid-component';
import { GridSelectionMode } from '../../../../objects/enums/grid-selection-mode';
import { ColumnFilterPopup } from '../../../../controls/components/grid/filters/column-filter-popup';
var GridColumnHeaderComponent = /** @class */ (function () {
    function GridColumnHeaderComponent(dialog, changeDetectorRef) {
        this.dialog = dialog;
        this.changeDetectorRef = changeDetectorRef;
        this.Columns = [];
        changeDetectorRef.detach();
    }
    GridColumnHeaderComponent.prototype.ngOnChanges = function (changes) {
        if (changes['Columns']) {
            this.changeDetectorRef.detectChanges();
        }
    };
    GridColumnHeaderComponent.prototype.ColumnHeaderAlignmentClass = function (column) {
        if (column.HeaderTextAlign) {
            if (column.HeaderTextAlign.toLowerCase() == "left")
                return "column-alignment-left";
            if (column.HeaderTextAlign.toLowerCase() == "right")
                return "column-alignment-right";
            if (column.HeaderTextAlign.toLowerCase() == "center")
                return "column-alignment-center";
        }
        return;
    };
    GridColumnHeaderComponent.prototype.isColumnSelected = function (column) {
        if (this.Grid.GridSelectionMode == GridSelectionMode.Row)
            return false;
        if (this.ColumnFocus && column) {
            return this.ColumnFocus[column.Key];
        }
        return false;
    };
    // OnColumnHeaderMouseOver(column: Column) {
    //     column['_isMouseOver'] = true;
    //     //this.changeDetectorRef.detectChanges();
    // }
    // OnColumnHeaderMouseOut(column: Column) {
    //     column['_isMouseOver'] = false;
    //     //this.changeDetectorRef.detectChanges();
    // }
    GridColumnHeaderComponent.prototype.OnColumnHeaderClick = function (event, column) {
        if (column.HideFilter === undefined || column.HideFilter === false)
            this.Grid.ToggleSort(column);
    };
    GridColumnHeaderComponent.prototype.OnColumnResize = function (size, column) {
        if (size < 0)
            size = 0;
        column.Width.Value = size;
        this.Grid.ResizeColumn(column);
    };
    GridColumnHeaderComponent.prototype.OnColumnFilterOpen = function (event, column) {
        var body = document.querySelector('body');
        if (body)
            body.click(); // closes currently opened dropdowns
        ColumnFilterPopup.Show(event, this.Grid, column);
        event.preventDefault();
        event.stopPropagation();
    };
    GridColumnHeaderComponent.prototype.ColumnSortDirection = function (column) {
        if (column && this.Grid.Sorts.containsKey(column.Key)) {
            var sort = this.Grid.Sorts[column.Key];
            return sort.Direction;
        }
    };
    GridColumnHeaderComponent.prototype.GridColumnHeaderClass = function (column) {
        if (column.Type.IsFill)
            return "";
        return "grid-table-column-cell";
    };
    __decorate([
        Input(),
        __metadata("design:type", Array)
    ], GridColumnHeaderComponent.prototype, "Columns", void 0);
    __decorate([
        Input(),
        __metadata("design:type", GridComponent)
    ], GridColumnHeaderComponent.prototype, "Grid", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], GridColumnHeaderComponent.prototype, "Row", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], GridColumnHeaderComponent.prototype, "ColumnFocus", void 0);
    GridColumnHeaderComponent = __decorate([
        Component({
            selector: 'pm-grid-column-header',
            //templateUrl: './app/controls/components/grid/grid-columns/grid-column-header.html',
            templateUrl: './grid-column-header.html',
            changeDetection: ChangeDetectionStrategy.OnPush
        }),
        __metadata("design:paramtypes", [DialogService,
            ChangeDetectorRef])
    ], GridColumnHeaderComponent);
    return GridColumnHeaderComponent;
}());
export { GridColumnHeaderComponent };
