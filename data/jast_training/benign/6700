var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { Component, Input, Output, EventEmitter, ChangeDetectorRef } from '@angular/core';
var NumericBoxComponent = /** @class */ (function () {
    function NumericBoxComponent(changeDetectorRef) {
        this.changeDetectorRef = changeDetectorRef;
        this.ValueChange = new EventEmitter();
        this.TextChange = new EventEmitter();
        this.changeDetectorRef.detach();
    }
    NumericBoxComponent.prototype.ngOnInit = function () {
        if (this.Value) {
            this.Text = this.Value.toString();
        }
    };
    NumericBoxComponent.prototype.onKeyPress = function (e) {
        var key = e.key;
        if (isNaN(+key) || key == " ")
            e.preventDefault();
    };
    NumericBoxComponent.prototype.onPaste = function (e) {
        var pastedText = undefined;
        if (window.clipboardData && window.clipboardData.getData) {
            pastedText = window.clipboardData.getData('Text');
        }
        else if (e.clipboardData && e.clipboardData.getData) {
            pastedText = e.clipboardData.getData('text/plain');
        }
        // Prevent the default handler from running.
        if (isNaN(pastedText))
            return false;
        if (this.MinValue && pastedText < this.MinValue)
            return false;
        if (this.MaxValue && pastedText > this.MaxValue)
            return false;
        if (pastedText != Math.floor(pastedText))
            return false;
    };
    NumericBoxComponent.prototype.incrementUp = function () {
        if (!isNaN(+this.Text)) {
            var value = +this.Text;
            value++;
            if (this.MaxValue && value > this.MaxValue)
                return;
            this.SetValue(String(value));
        }
        else
            this.SetValue("1");
    };
    NumericBoxComponent.prototype.incrementDown = function () {
        if (!isNaN(+this.Text)) {
            var value = +this.Text;
            value--;
            if (this.MinValue && value < this.MinValue)
                return;
            this.SetValue(String(value));
        }
        else
            this.SetValue("0");
    };
    NumericBoxComponent.prototype.onTextChange = function (newValue) {
        this.SetValue(newValue);
    };
    NumericBoxComponent.prototype.SetValue = function (newValue) {
        this.Text = newValue;
        this.Value = this.Text && !isNaN(+this.Text) ? +this.Text : undefined;
        this.ValueChange.emit(this.Value);
    };
    Object.defineProperty(NumericBoxComponent.prototype, "Text", {
        get: function () {
            return this.text;
        },
        set: function (value) {
            this.text = value;
            this.TextChange.emit(value);
            this.changeDetectorRef.detectChanges();
        },
        enumerable: true,
        configurable: true
    });
    __decorate([
        Input(),
        __metadata("design:type", Number)
    ], NumericBoxComponent.prototype, "Value", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], NumericBoxComponent.prototype, "IsDisabled", void 0);
    __decorate([
        Output(),
        __metadata("design:type", EventEmitter)
    ], NumericBoxComponent.prototype, "ValueChange", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], NumericBoxComponent.prototype, "Watermark", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Number)
    ], NumericBoxComponent.prototype, "MaxValue", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Number)
    ], NumericBoxComponent.prototype, "MinValue", void 0);
    __decorate([
        Output(),
        __metadata("design:type", EventEmitter)
    ], NumericBoxComponent.prototype, "TextChange", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String),
        __metadata("design:paramtypes", [String])
    ], NumericBoxComponent.prototype, "Text", null);
    NumericBoxComponent = __decorate([
        Component({
            selector: 'pm-numeric-box',
            //templateUrl: './app/controls/components/boxes/numeric-box/numeric-box.html',
            templateUrl: './numeric-box.html',
        }),
        __metadata("design:paramtypes", [ChangeDetectorRef])
    ], NumericBoxComponent);
    return NumericBoxComponent;
}());
export { NumericBoxComponent };
