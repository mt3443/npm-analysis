var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { Component, ChangeDetectorRef, ChangeDetectionStrategy, Input, Injector, } from '@angular/core';
import { GridComponent } from '../../../../controls/components/grid/grid-component';
import { GridCell } from '../../../../controls/components/grid/grid-cell/grid-cell';
var GridRowComponent = /** @class */ (function () {
    function GridRowComponent(changeDetectorRef, injector) {
        this.changeDetectorRef = changeDetectorRef;
        this.injector = injector;
        this.Columns = [];
        changeDetectorRef.detach();
    }
    GridRowComponent.prototype.ngOnChanges = function (changes) {
        if (changes['Rows']) {
            this.changeDetectorRef.detectChanges();
        }
        if (changes['Row']) {
            this.changeDetectorRef.detectChanges();
        }
        if (changes['Columns']) {
            this.changeDetectorRef.detectChanges();
        }
    };
    GridRowComponent.prototype.getProperty = function (column) {
        return GridCell.GetProperty(column, this.Row);
    };
    GridRowComponent.prototype.onCellSelect = function (column) {
        this.Grid.SelectCell(new GridCell(this.Row, column));
    };
    GridRowComponent.prototype.hasHierarchy = function (column) {
        return this.Grid.HierarchyColumnIndex > 0
            && this.Grid.HierarchyColumnIndex == column['_columnNumber']
            && this.Row[this.Grid.HierarchyColumnProperty]
            && this.Row[this.Grid.HierarchyColumnProperty].length > 0;
    };
    GridRowComponent.prototype.isCellSelected = function (column) {
        if (this.SelectedCells && this.Row && column) {
            return this.SelectedCells[this.Row['_rowNumber'] + column.Key];
        }
        return false;
    };
    GridRowComponent.prototype.isRowSelected = function () {
        if (this.SelectedRows && this.Row) {
            return this.SelectedRows[this.Row['_rowNumber']];
        }
        return false;
    };
    GridRowComponent.prototype.isRowHighlighted = function () {
        if (this.Row) {
            return this.Row['_isHighlighted'];
        }
        return false;
    };
    GridRowComponent.prototype.onToggleExpandCollapse = function (event) {
        this.Grid.ExpandCollapseHierarchyRow(this.Row);
        event.preventDefault();
        event.stopPropagation();
    };
    GridRowComponent.prototype.CellAlignmentClass = function (column) {
        if (column.CellTextAlign) {
            if (column.CellTextAlign.toLowerCase() == "left")
                return "cell-alignment-left";
            if (column.CellTextAlign.toLowerCase() == "right")
                return "cell-alignment-right";
            if (column.CellTextAlign.toLowerCase() == "center")
                return "cell-alignment-center";
        }
        return;
    };
    GridRowComponent.prototype.CellClass = function (column) {
        if (column.Type.IsFill)
            return "";
        return "grid-table-row-cell";
    };
    Object.defineProperty(GridRowComponent.prototype, "RowSelectClass", {
        get: function () {
            if (this.Grid.FrozenColumnCount > 0) {
                if (this.IsFrozen)
                    return "frozen-row-is-selected";
                return "regular-row-is-selected";
            }
            return "row-is-selected";
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(GridRowComponent.prototype, "CellMouseOver", {
        get: function () {
            return this.Grid.CellMouseOver;
        },
        enumerable: true,
        configurable: true
    });
    __decorate([
        Input(),
        __metadata("design:type", Array)
    ], GridRowComponent.prototype, "Columns", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], GridRowComponent.prototype, "Row", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], GridRowComponent.prototype, "SelectedCells", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], GridRowComponent.prototype, "SelectedRows", void 0);
    __decorate([
        Input(),
        __metadata("design:type", GridComponent)
    ], GridRowComponent.prototype, "Grid", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], GridRowComponent.prototype, "IsFrozen", void 0);
    GridRowComponent = __decorate([
        Component({
            selector: 'pm-grid-row',
            //templateUrl: './app/controls/components/grid/grid-rows/grid-row.html',
            templateUrl: './grid-row.html',
            changeDetection: ChangeDetectionStrategy.OnPush
        }),
        __metadata("design:paramtypes", [ChangeDetectorRef,
            Injector])
    ], GridRowComponent);
    return GridRowComponent;
}());
export { GridRowComponent };
