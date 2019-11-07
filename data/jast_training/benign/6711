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
var ButtonDropdownComponent = /** @class */ (function () {
    function ButtonDropdownComponent() {
        this.ButtonClass = "button-primary";
    }
    ButtonDropdownComponent.prototype.OnClick = function () {
        if (this.IsDisabled)
            return;
        this.IsDropDownOpen = !this.IsDropDownOpen;
    };
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], ButtonDropdownComponent.prototype, "ButtonClass", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], ButtonDropdownComponent.prototype, "DropDownClass", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], ButtonDropdownComponent.prototype, "IsDisabled", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], ButtonDropdownComponent.prototype, "HorizontalAlignment", void 0);
    ButtonDropdownComponent = __decorate([
        Component({
            selector: 'pm-button-dropdown',
            //templateUrl: './app/controls/components/buttons/button-dropdown/button-dropdown.html',
            templateUrl: './button-dropdown.html',
            styles: ["\n        :host {\n            display: flex;\n            margin-top: 6px;\n            margin-bottom: 6px;\n        }\n    "],
        })
    ], ButtonDropdownComponent);
    return ButtonDropdownComponent;
}());
export { ButtonDropdownComponent };
