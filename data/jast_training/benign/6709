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
var ButtonComponent = /** @class */ (function () {
    function ButtonComponent() {
        this.Click = new EventEmitter();
        this.ButtonClass = "button-primary";
    }
    ButtonComponent.prototype.OnClick = function () {
        if (this.IsDisabled)
            return;
        this.Click.emit();
    };
    __decorate([
        Output(),
        __metadata("design:type", Object)
    ], ButtonComponent.prototype, "Click", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], ButtonComponent.prototype, "IsDisabled", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], ButtonComponent.prototype, "ButtonClass", void 0);
    ButtonComponent = __decorate([
        Component({
            selector: 'pm-button',
            //templateUrl: './app/controls/components/buttons/button/button.html',
            templateUrl: './button.html',
            styles: ["\n    :host { \n      margin-top: 6px;\n      margin-bottom: 6px;\n    }\n  "]
        })
    ], ButtonComponent);
    return ButtonComponent;
}());
export { ButtonComponent };
