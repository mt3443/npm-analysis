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
import { GridComponent } from '../../../../../controls/components/grid/grid-component';
var GridColumnGroupingComponent = /** @class */ (function () {
    function GridColumnGroupingComponent(changeDetectorRef) {
        this.changeDetectorRef = changeDetectorRef;
        this.ColumnGroups = [];
        changeDetectorRef.detach();
    }
    GridColumnGroupingComponent.prototype.ngOnChanges = function (changes) {
        if (changes['Columns']) {
            this.changeDetectorRef.detectChanges();
        }
        if (changes['ColumnGroups']) {
            this.changeDetectorRef.detectChanges();
        }
    };
    GridColumnGroupingComponent.prototype.ColumnHeaderAlignmentClass = function (column) {
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
    __decorate([
        Input(),
        __metadata("design:type", Array)
    ], GridColumnGroupingComponent.prototype, "ColumnGroups", void 0);
    __decorate([
        Input(),
        __metadata("design:type", GridComponent)
    ], GridColumnGroupingComponent.prototype, "Grid", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], GridColumnGroupingComponent.prototype, "Row", void 0);
    GridColumnGroupingComponent = __decorate([
        Component({
            selector: 'pm-grid-column-group',
            //templateUrl: './app/controls/components/grid/grid-columns/grid-column-grouping.html',
            templateUrl: './grid-column-group.html',
            changeDetection: ChangeDetectionStrategy.OnPush
        }),
        __metadata("design:paramtypes", [ChangeDetectorRef])
    ], GridColumnGroupingComponent);
    return GridColumnGroupingComponent;
}());
export { GridColumnGroupingComponent };
