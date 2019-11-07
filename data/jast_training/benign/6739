var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { Component, ChangeDetectorRef, ChangeDetectionStrategy, Input, ViewChild, ViewContainerRef } from '@angular/core';
import { Column } from '../../../../objects/request/column';
var GridCellTemplateComponent = /** @class */ (function () {
    function GridCellTemplateComponent(
        //private viewContainer: ViewContainerRef,
        changeDetectorRef) {
        this.changeDetectorRef = changeDetectorRef;
        changeDetectorRef.detach();
    }
    GridCellTemplateComponent.prototype.ngOnInit = function () {
        if (this.Column.CellTemplateComponent) {
            var container = this.viewContainer.createComponent(this.Column.CellTemplateComponent);
            container.instance.Column = this.Column;
            container.instance.Row = this.Row;
            container.changeDetectorRef.detectChanges();
        }
    };
    __decorate([
        Input(),
        __metadata("design:type", Column)
    ], GridCellTemplateComponent.prototype, "Column", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], GridCellTemplateComponent.prototype, "Row", void 0);
    __decorate([
        ViewChild('container', { read: ViewContainerRef }),
        __metadata("design:type", ViewContainerRef)
    ], GridCellTemplateComponent.prototype, "viewContainer", void 0);
    GridCellTemplateComponent = __decorate([
        Component({
            selector: 'pm-grid-cell-template',
            template: '<ng-template #container></ng-template>',
            changeDetection: ChangeDetectionStrategy.OnPush,
            styles: ["\n    :host { \n        width: 100%;\n    }\n    "]
        }),
        __metadata("design:paramtypes", [ChangeDetectorRef])
    ], GridCellTemplateComponent);
    return GridCellTemplateComponent;
}());
export { GridCellTemplateComponent };
