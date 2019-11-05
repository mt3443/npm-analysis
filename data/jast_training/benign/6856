var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { ChangeDetectorRef, Component, EventEmitter, Input, Output } from '@angular/core';
var RadioButtonComponent = /** @class */ (function () {
    function RadioButtonComponent(changeDetectorRef) {
        this.changeDetectorRef = changeDetectorRef;
        this.RadioGroupChange = new EventEmitter();
        this.RadioButtonOuterTheme = "radio-button-default-outer-selected";
        this.RadioButtonInnerTheme = "radio-button-default-inner-selected";
        this.changeDetectorRef.detach();
    }
    RadioButtonComponent.prototype.ngOnInit = function () {
        this.changeDetectorRef.detectChanges();
    };
    RadioButtonComponent.prototype.OnClick = function () {
        if (this.IsChecked || this.IsDisabled)
            return;
        this.IsChecked = true;
        this.RadioGroupChange.emit(this.Value);
        this.changeDetectorRef.detectChanges();
    };
    Object.defineProperty(RadioButtonComponent.prototype, "OuterClass", {
        get: function () {
            if (this.IsChecked) {
                if (this.IsDisabled)
                    return "radio-button-outer-selected-disabled";
                return this.RadioButtonOuterTheme;
            }
            if (this.IsDisabled)
                return "radio-button-outer-not-selected-disabled";
            return "radio-button-outer-not-selected";
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(RadioButtonComponent.prototype, "InnerClass", {
        get: function () {
            if (this.IsChecked) {
                if (this.IsDisabled)
                    return "radio-button-inner-selected-disabled";
                return this.RadioButtonInnerTheme;
            }
            return "radio-button-inner-not-selected";
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(RadioButtonComponent.prototype, "IsChecked", {
        get: function () {
            return this.isChecked;
        },
        set: function (value) {
            this.isChecked = value;
            this.changeDetectorRef.detectChanges();
        },
        enumerable: true,
        configurable: true
    });
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], RadioButtonComponent.prototype, "IsDisabled", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], RadioButtonComponent.prototype, "Label", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], RadioButtonComponent.prototype, "Value", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], RadioButtonComponent.prototype, "RadioGroup", void 0);
    __decorate([
        Output(),
        __metadata("design:type", EventEmitter)
    ], RadioButtonComponent.prototype, "RadioGroupChange", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], RadioButtonComponent.prototype, "RadioButtonOuterTheme", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], RadioButtonComponent.prototype, "RadioButtonInnerTheme", void 0);
    __decorate([
        Input('IsChecked'),
        __metadata("design:type", Boolean),
        __metadata("design:paramtypes", [Boolean])
    ], RadioButtonComponent.prototype, "IsChecked", null);
    RadioButtonComponent = __decorate([
        Component({
            selector: 'pm-radio-button',
            //templateUrl: './app/controls/components/radio/radio-button/radio-button.html',
            templateUrl: './radio-button.html'
        }),
        __metadata("design:paramtypes", [ChangeDetectorRef])
    ], RadioButtonComponent);
    return RadioButtonComponent;
}());
export { RadioButtonComponent };
