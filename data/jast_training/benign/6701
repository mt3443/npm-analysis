var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { Component, Input, Output, ElementRef, EventEmitter, HostBinding, ViewChild } from '@angular/core';
var TextBoxComponent = /** @class */ (function () {
    function TextBoxComponent() {
        this.TextBoxClass = "text-box-input";
        this.TextChange = new EventEmitter();
        this.BlurChange = new EventEmitter();
        this.FocusChange = new EventEmitter();
        this.KeyUp = new EventEmitter();
        this.KeyDown = new EventEmitter();
    }
    TextBoxComponent.prototype.onChange = function (newValue) {
        this.Text = newValue;
        this.TextChange.emit(this.Text);
    };
    TextBoxComponent.prototype.onBlur = function (value) {
        this.BlurChange.emit(value);
    };
    TextBoxComponent.prototype.onFocus = function (value) {
        this.FocusChange.emit(value);
    };
    TextBoxComponent.prototype.onKeyUp = function (event) {
        this.KeyUp.emit(event);
    };
    TextBoxComponent.prototype.onKeyDown = function (event) {
        this.KeyDown.emit(event);
    };
    TextBoxComponent.prototype.Focus = function () {
        this.textBox.nativeElement.focus();
    };
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], TextBoxComponent.prototype, "Text", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], TextBoxComponent.prototype, "Watermark", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], TextBoxComponent.prototype, "TextBoxClass", void 0);
    __decorate([
        HostBinding('style.width'),
        Input(),
        __metadata("design:type", String)
    ], TextBoxComponent.prototype, "Width", void 0);
    __decorate([
        HostBinding('style.max-width'),
        Input(),
        __metadata("design:type", String)
    ], TextBoxComponent.prototype, "MaxWidth", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], TextBoxComponent.prototype, "IsDisabled", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], TextBoxComponent.prototype, "IsReadOnly", void 0);
    __decorate([
        Output(),
        __metadata("design:type", EventEmitter)
    ], TextBoxComponent.prototype, "TextChange", void 0);
    __decorate([
        Output(),
        __metadata("design:type", EventEmitter)
    ], TextBoxComponent.prototype, "BlurChange", void 0);
    __decorate([
        Output(),
        __metadata("design:type", EventEmitter)
    ], TextBoxComponent.prototype, "FocusChange", void 0);
    __decorate([
        Output(),
        __metadata("design:type", EventEmitter)
    ], TextBoxComponent.prototype, "KeyUp", void 0);
    __decorate([
        Output(),
        __metadata("design:type", EventEmitter)
    ], TextBoxComponent.prototype, "KeyDown", void 0);
    __decorate([
        ViewChild('input'),
        __metadata("design:type", ElementRef)
    ], TextBoxComponent.prototype, "textBox", void 0);
    TextBoxComponent = __decorate([
        Component({
            selector: 'pm-text-box',
            //templateUrl: './app/controls/components/boxes/text-box/text-box.html',
            templateUrl: './text-box.html',
        }),
        __metadata("design:paramtypes", [])
    ], TextBoxComponent);
    return TextBoxComponent;
}());
export { TextBoxComponent };
