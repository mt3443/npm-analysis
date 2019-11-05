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
var GridRowsComponent = /** @class */ (function () {
    function GridRowsComponent(changeDetectorRef) {
        this.changeDetectorRef = changeDetectorRef;
        this.Columns = [];
        this.Rows = [];
        changeDetectorRef.detach();
    }
    GridRowsComponent.prototype.ngOnChanges = function (changes) {
        if (changes['Columns']) {
            this.changeDetectorRef.detectChanges();
        }
        if (changes['Rows']) {
            this.changeDetectorRef.detectChanges();
        }
    };
    Object.defineProperty(GridRowsComponent.prototype, "RowMouseOver", {
        get: function () {
            return this.Grid.RowMouseOver;
        },
        enumerable: true,
        configurable: true
    });
    __decorate([
        Input(),
        __metadata("design:type", Array)
    ], GridRowsComponent.prototype, "Columns", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Array)
    ], GridRowsComponent.prototype, "Rows", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], GridRowsComponent.prototype, "SelectedCells", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], GridRowsComponent.prototype, "SelectedRows", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], GridRowsComponent.prototype, "IsFrozen", void 0);
    __decorate([
        Input(),
        __metadata("design:type", GridComponent)
    ], GridRowsComponent.prototype, "Grid", void 0);
    GridRowsComponent = __decorate([
        Component({
            selector: 'pm-grid-rows',
            //templateUrl: './app/controls/components/grid/grid-rows.html',
            templateUrl: './grid-rows.html',
            changeDetection: ChangeDetectionStrategy.OnPush
        }),
        __metadata("design:paramtypes", [ChangeDetectorRef])
    ], GridRowsComponent);
    return GridRowsComponent;
}());
export { GridRowsComponent };
