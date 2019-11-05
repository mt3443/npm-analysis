var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { Component, Input, EventEmitter, Output } from '@angular/core';
var ButtonBlockComponent = /** @class */ (function () {
    function ButtonBlockComponent() {
        this.Click = new EventEmitter();
        this.ButtonClass = "button-block";
    }
    ButtonBlockComponent.prototype.OnClick = function () {
        if (this.IsDisabled)
            return;
        this.Click.emit();
    };
    __decorate([
        Output(),
        __metadata("design:type", Object)
    ], ButtonBlockComponent.prototype, "Click", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], ButtonBlockComponent.prototype, "ButtonClass", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], ButtonBlockComponent.prototype, "IsDisabled", void 0);
    ButtonBlockComponent = __decorate([
        Component({
            selector: 'pm-button-block',
            //templateUrl: './app/controls/components/buttons/button-block/button-block.html',
            templateUrl: './button-block.html',
            styles: ["\n    :host {\n      display: flex;\n    }\n  "],
        })
    ], ButtonBlockComponent);
    return ButtonBlockComponent;
}());
export { ButtonBlockComponent };
