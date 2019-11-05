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
var TextareaComponent = /** @class */ (function () {
    function TextareaComponent() {
        this.TextareaClass = "textarea-input";
        this.TextChange = new EventEmitter();
        this.BlurChange = new EventEmitter();
        this.FocusChange = new EventEmitter();
        this.KeyUp = new EventEmitter();
        this.KeyDown = new EventEmitter();
    }
    TextareaComponent.prototype.onChange = function (newValue) {
        this.Text = newValue;
        this.TextChange.emit(this.Text);
    };
    TextareaComponent.prototype.onBlur = function (value) {
        this.BlurChange.emit(value);
    };
    TextareaComponent.prototype.onFocus = function (value) {
        this.FocusChange.emit(value);
    };
    TextareaComponent.prototype.onKeyUp = function (event) {
        this.KeyUp.emit(event);
    };
    TextareaComponent.prototype.onKeyDown = function (event) {
        this.KeyDown.emit(event);
    };
    TextareaComponent.prototype.Focus = function () {
        this.textarea.nativeElement.focus();
    };
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], TextareaComponent.prototype, "Text", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], TextareaComponent.prototype, "Watermark", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], TextareaComponent.prototype, "TextareaClass", void 0);
    __decorate([
        HostBinding('style.width'),
        Input(),
        __metadata("design:type", String)
    ], TextareaComponent.prototype, "Width", void 0);
    __decorate([
        HostBinding('style.max-width'),
        Input(),
        __metadata("design:type", String)
    ], TextareaComponent.prototype, "MaxWidth", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], TextareaComponent.prototype, "IsDisabled", void 0);
    __decorate([
        Output(),
        __metadata("design:type", EventEmitter)
    ], TextareaComponent.prototype, "TextChange", void 0);
    __decorate([
        Output(),
        __metadata("design:type", EventEmitter)
    ], TextareaComponent.prototype, "BlurChange", void 0);
    __decorate([
        Output(),
        __metadata("design:type", EventEmitter)
    ], TextareaComponent.prototype, "FocusChange", void 0);
    __decorate([
        Output(),
        __metadata("design:type", EventEmitter)
    ], TextareaComponent.prototype, "KeyUp", void 0);
    __decorate([
        Output(),
        __metadata("design:type", EventEmitter)
    ], TextareaComponent.prototype, "KeyDown", void 0);
    __decorate([
        ViewChild('textarea'),
        __metadata("design:type", ElementRef)
    ], TextareaComponent.prototype, "textarea", void 0);
    TextareaComponent = __decorate([
        Component({
            selector: 'pm-textarea',
            //templateUrl: './app/controls/components/textarea/textarea.html',
            templateUrl: './textarea.html'
        }),
        __metadata("design:paramtypes", [])
    ], TextareaComponent);
    return TextareaComponent;
}());
export { TextareaComponent };
