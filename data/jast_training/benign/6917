var __extends = (this && this.__extends) || (function () {
    var extendStatics = Object.setPrototypeOf ||
        ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
        function (d, b) { for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p]; };
    return function (d, b) {
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { Input } from '@angular/core';
import { Property } from '../../../objects/request/properties/property';
var CheckBoxProperty = /** @class */ (function (_super) {
    __extends(CheckBoxProperty, _super);
    function CheckBoxProperty(Label, item, display, orientation, isHidden, isDisabled) {
        var _this = _super.call(this, Label, orientation, isHidden, isDisabled) || this;
        _this.Label = Label;
        _this.IsCheckBox = true;
        _this.Item = item;
        _this.Display = display;
        return _this;
    }
    Object.defineProperty(CheckBoxProperty.prototype, "HasValue", {
        get: function () {
            return true;
        },
        enumerable: true,
        configurable: true
    });
    CheckBoxProperty.prototype.Clear = function () {
        if (this.Item)
            this.Item = false;
    };
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], CheckBoxProperty.prototype, "Item", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], CheckBoxProperty.prototype, "Display", void 0);
    return CheckBoxProperty;
}(Property));
export { CheckBoxProperty };
