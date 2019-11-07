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
var SwitchComponent = /** @class */ (function () {
    function SwitchComponent(changeDetectorRef) {
        this.changeDetectorRef = changeDetectorRef;
        this.IsCheckedChange = new EventEmitter();
        this.SwitchTheme = "default";
        this.SwitchButtonClass = "switch-thumb-is-unchecked-default";
        this.SwitchBarClass = "switch-bar-is-unchecked";
    }
    SwitchComponent.prototype.ngOnInit = function () {
        this.changeDetectorRef.detectChanges();
        this.OnSetState();
    };
    SwitchComponent.prototype.OnClick = function () {
        if (this.IsDisabled)
            return;
        this.IsChecked = !this.IsChecked;
        this.IsCheckedChange.emit(this.IsChecked);
        this.changeDetectorRef.detectChanges();
    };
    SwitchComponent.prototype.OnSetState = function () {
        if (!this.IsDisabled) {
            this.SwitchButtonClass = this.IsChecked ? "switch-thumb-is-checked-" + this.SwitchTheme : "switch-thumb-is-unchecked";
            this.SwitchBarClass = this.IsChecked ? "switch-bar-is-checked-" + this.SwitchTheme : "switch-bar-is-unchecked";
        }
        else {
            this.SwitchButtonClass = this.IsChecked ? "switch-thumb-is-checked-disabled" : "switch-thumb-is-unchecked-disabled";
            this.SwitchBarClass = "switch-bar-is-unchecked-disabled";
        }
    };
    Object.defineProperty(SwitchComponent.prototype, "IsChecked", {
        get: function () {
            return this.isChecked;
        },
        set: function (value) {
            this.isChecked = value;
            this.OnSetState();
        },
        enumerable: true,
        configurable: true
    });
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], SwitchComponent.prototype, "IsDisabled", void 0);
    __decorate([
        Output(),
        __metadata("design:type", EventEmitter)
    ], SwitchComponent.prototype, "IsCheckedChange", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], SwitchComponent.prototype, "SwitchTheme", void 0);
    __decorate([
        Input('IsChecked'),
        __metadata("design:type", Boolean),
        __metadata("design:paramtypes", [Boolean])
    ], SwitchComponent.prototype, "IsChecked", null);
    SwitchComponent = __decorate([
        Component({
            selector: 'pm-switch',
            //templateUrl: './app/controls/components/switch/switch.html'
            templateUrl: './switch.html'
        }),
        __metadata("design:paramtypes", [ChangeDetectorRef])
    ], SwitchComponent);
    return SwitchComponent;
}());
export { SwitchComponent };
