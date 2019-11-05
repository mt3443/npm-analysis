var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { Component, ChangeDetectorRef, ChangeDetectionStrategy, Input } from '@angular/core';
import { GridComponent } from '../../../../controls/components/grid/grid-component';
var GridRowsCountComponent = /** @class */ (function () {
    function GridRowsCountComponent(changeDetectorRef) {
        this.changeDetectorRef = changeDetectorRef;
        this.Rows = [];
        changeDetectorRef.detach();
    }
    GridRowsCountComponent.prototype.ngOnChanges = function (changes) {
        if (changes['Rows']) {
            this.changeDetectorRef.detectChanges();
        }
        if (changes['RowFocus']) {
            this.changeDetectorRef.detectChanges();
        }
    };
    GridRowsCountComponent.prototype.IsRowFocused = function (row) {
        if (this.RowFocus) {
            return this.RowFocus[row['_rowNumber']];
        }
        return false;
    };
    GridRowsCountComponent.prototype.OnCellSelect = function (row) {
        this.Grid.SelectRow(row);
    };
    GridRowsCountComponent.prototype.OnRowResize = function (size, row) {
        if (size < 0)
            size = 0;
        row['_rowResizeHeight'] = size;
        this.Grid.ResizeRow(row);
    };
    __decorate([
        Input(),
        __metadata("design:type", Array)
    ], GridRowsCountComponent.prototype, "Rows", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], GridRowsCountComponent.prototype, "RowFocus", void 0);
    __decorate([
        Input(),
        __metadata("design:type", GridComponent)
    ], GridRowsCountComponent.prototype, "Grid", void 0);
    GridRowsCountComponent = __decorate([
        Component({
            selector: 'pm-grid-rows-count',
            //templateUrl: './app/controls/components/grid/grid-rows-count.html',
            templateUrl: './grid-rows-count.html',
            changeDetection: ChangeDetectionStrategy.OnPush
        }),
        __metadata("design:paramtypes", [ChangeDetectorRef])
    ], GridRowsCountComponent);
    return GridRowsCountComponent;
}());
export { GridRowsCountComponent };
