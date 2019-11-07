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
import { GridCell } from '../../../../controls/components/grid/grid-cell/grid-cell';
var GridColumnFooterComponent = /** @class */ (function () {
    function GridColumnFooterComponent(changeDetectorRef) {
        this.changeDetectorRef = changeDetectorRef;
        this.Columns = [];
        changeDetectorRef.detach();
    }
    GridColumnFooterComponent.prototype.ngOnChanges = function (changes) {
        if (changes['Columns']) {
            this.changeDetectorRef.detectChanges();
        }
    };
    GridColumnFooterComponent.GetPropertyByPath = function (path, row) {
        var property = row;
        if (!path)
            return property;
        var paths = path.split(".");
        for (var i = 0; i < paths.length; i++) {
            var value = paths[i];
            if (property.hasOwnProperty(value) || property.__proto__.hasOwnProperty(value))
                property = property[value];
            else
                return;
        }
        return property;
    };
    GridColumnFooterComponent.prototype.getAggregate = function (column) {
        if (this.Grid.Rows && column.Aggregate) {
            var sum = 0;
            for (var i = 0; i < this.Grid.Rows.length; i++) {
                var row = this.Grid.Rows[i];
                var value = GridCell.GetProperty(column, row);
                sum += +value;
            }
            return sum;
        }
    };
    GridColumnFooterComponent.prototype.GridColumnFooterClass = function (column) {
        if (column.Type.IsFill)
            return "";
        return "grid-table-column-cell";
    };
    __decorate([
        Input(),
        __metadata("design:type", Array)
    ], GridColumnFooterComponent.prototype, "Columns", void 0);
    __decorate([
        Input(),
        __metadata("design:type", GridComponent)
    ], GridColumnFooterComponent.prototype, "Grid", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], GridColumnFooterComponent.prototype, "Row", void 0);
    GridColumnFooterComponent = __decorate([
        Component({
            selector: 'pm-grid-column-footer',
            //templateUrl: './app/controls/components/grid/grid-columns/grid-column-footer.html',
            templateUrl: './grid-column-footer.html',
            changeDetection: ChangeDetectionStrategy.OnPush
        }),
        __metadata("design:paramtypes", [ChangeDetectorRef])
    ], GridColumnFooterComponent);
    return GridColumnFooterComponent;
}());
export { GridColumnFooterComponent };
