var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { Component, Input } from '@angular/core';
import { Orientation } from '../../../../objects/enums/orientation';
var StackPanelComponent = /** @class */ (function () {
    function StackPanelComponent() {
        this.Orientation = Orientation.Horizontal;
        this.HorizontalAlignment = "Left";
    }
    Object.defineProperty(StackPanelComponent.prototype, "StackPanelOrientation", {
        get: function () {
            switch (this.Orientation) {
                case Orientation.Vertical: return "stack-panel-vertical";
                case Orientation.Horizontal: return "stack-panel-horizontal";
            }
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(StackPanelComponent.prototype, "StackPanelHorizontalAlignment", {
        get: function () {
            switch (this.HorizontalAlignment.toLowerCase()) {
                case 'left': return;
                case 'right': return "stack-panel-horizontal-alignment-right";
            }
        },
        enumerable: true,
        configurable: true
    });
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], StackPanelComponent.prototype, "Orientation", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], StackPanelComponent.prototype, "HorizontalAlignment", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], StackPanelComponent.prototype, "Padding", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], StackPanelComponent.prototype, "BackgroundClass", void 0);
    StackPanelComponent = __decorate([
        Component({
            selector: 'pm-stack-panel',
            //templateUrl: './app/controls/components/panels/stack-panel/stack-panel.html',  
            templateUrl: './stack-panel.html'
        })
    ], StackPanelComponent);
    return StackPanelComponent;
}());
export { StackPanelComponent };
