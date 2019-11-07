var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { Component, Input, Output, EventEmitter } from '@angular/core';
var BarComponent = /** @class */ (function () {
    function BarComponent() {
        this.Name = '';
        this.onExportToExcel = new EventEmitter();
        this.onTogglePanel = new EventEmitter();
    }
    BarComponent.prototype.exportToExcel = function () {
        this.onExportToExcel.emit({});
    };
    BarComponent.prototype.togglePanel = function () {
        this.onTogglePanel.emit({});
    };
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], BarComponent.prototype, "Name", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], BarComponent.prototype, "Items", void 0);
    __decorate([
        Output(),
        __metadata("design:type", Object)
    ], BarComponent.prototype, "onExportToExcel", void 0);
    __decorate([
        Output(),
        __metadata("design:type", Object)
    ], BarComponent.prototype, "onTogglePanel", void 0);
    BarComponent = __decorate([
        Component({
            selector: 'pm-bar',
            //templateUrl: './app/controls/components/bar/bar.html',
            templateUrl: './bar.html',
        })
    ], BarComponent);
    return BarComponent;
}());
export { BarComponent };
