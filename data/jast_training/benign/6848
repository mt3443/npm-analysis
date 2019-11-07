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
// This is the "standard" Resize-Panel. For more control over styling, use pm-thumb.
var ResizePanelComponent = /** @class */ (function () {
    function ResizePanelComponent() {
        this.HeightPx = "100%";
        this.Orientation = Orientation.Vertical;
        this.FirstElementFlexGrow = .5;
        this.SecondElementFlexGrow = .5;
        this.CustomThumbClass = "";
    }
    Object.defineProperty(ResizePanelComponent.prototype, "Height", {
        get: function () {
            if (this.HeightPx)
                return this.HeightPx + 'px';
            return "100%";
        },
        enumerable: true,
        configurable: true
    });
    ResizePanelComponent.prototype.flexDirection = function () {
        return this.isHorizontal() ? "row" : "column";
    };
    ResizePanelComponent.prototype.isHorizontal = function () {
        return this.Orientation == Orientation.Horizontal;
    };
    ResizePanelComponent.prototype.logDragStart = function ($event) {
        console.log("drag start" + $event);
    };
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], ResizePanelComponent.prototype, "HeightPx", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], ResizePanelComponent.prototype, "Orientation", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Number)
    ], ResizePanelComponent.prototype, "FirstElementFlexGrow", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Number)
    ], ResizePanelComponent.prototype, "SecondElementFlexGrow", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], ResizePanelComponent.prototype, "CustomThumbClass", void 0);
    ResizePanelComponent = __decorate([
        Component({
            selector: 'pm-resize-panel',
            //templateUrl: './app/controls/components/panels/resize-panel/resize-panel.html',
            templateUrl: './resize-panel.html',
            styles: ["\n    :host { \n      width: 100%;\n    }\n    "],
        })
    ], ResizePanelComponent);
    return ResizePanelComponent;
}());
export { ResizePanelComponent };
