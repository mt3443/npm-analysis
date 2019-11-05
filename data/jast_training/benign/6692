var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { ChangeDetectorRef, Component, Input, Output, EventEmitter, } from '@angular/core';
var CheckBoxComponent = /** @class */ (function () {
    function CheckBoxComponent(changeDetectorRef) {
        this.changeDetectorRef = changeDetectorRef;
        this.CheckBoxTheme = "check-box-default";
        this.IsAnimated = true;
        this.IsCheckedChange = new EventEmitter();
    }
    CheckBoxComponent.prototype.OnClick = function () {
        if (this.IsReadOnly || this.IsDisabled)
            return;
        this.CheckBoxStateClass = "check-box-click-animate";
        this.IsChecked = !this.IsChecked;
        this.IsCheckedChange.emit(this.IsChecked);
        this.changeDetectorRef.detectChanges();
    };
    Object.defineProperty(CheckBoxComponent.prototype, "CheckBoxClass", {
        get: function () {
            if (this.IsChecked) {
                if (this.IsDisabled)
                    return "is-checked-disabled";
                return this.CheckBoxTheme;
            }
            else {
                if (this.IsDisabled)
                    return "is-unchecked-disabled";
                return "is-unchecked";
            }
        },
        enumerable: true,
        configurable: true
    });
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], CheckBoxComponent.prototype, "Label", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], CheckBoxComponent.prototype, "CheckBoxTheme", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], CheckBoxComponent.prototype, "IsAnimated", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], CheckBoxComponent.prototype, "IsReadOnly", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], CheckBoxComponent.prototype, "IsChecked", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], CheckBoxComponent.prototype, "IsDisabled", void 0);
    __decorate([
        Output(),
        __metadata("design:type", EventEmitter)
    ], CheckBoxComponent.prototype, "IsCheckedChange", void 0);
    CheckBoxComponent = __decorate([
        Component({
            selector: 'pm-check-box',
            //templateUrl: './app/controls/components/boxes/check-box/check-box.html',
            templateUrl: './check-box.html',
        }),
        __metadata("design:paramtypes", [ChangeDetectorRef])
    ], CheckBoxComponent);
    return CheckBoxComponent;
}());
export { CheckBoxComponent };
