var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { Component, EventEmitter, TemplateRef, Input, Output } from '@angular/core';
import { BaseRequest } from '../../../objects/request/base-request';
import { HorizontalAlignment } from '../../../objects/enums/horizontal-alignment';
var FormComponent = /** @class */ (function () {
    function FormComponent() {
        this.onSubmit = new EventEmitter();
        this.onClear = new EventEmitter();
        this.onCancel = new EventEmitter();
        this.Request = new BaseRequest();
        this.CanClear = false;
        this.ButtonClearLabel = "Clear";
        this.CanCancel = false;
        this.ButtonCancelLabel = "Cancel";
        this.ButtonLabel = "Submit";
        this.ButtonHorizontalAlignment = HorizontalAlignment.Left;
    }
    FormComponent.prototype.Submit = function () {
        if (this.Request.Validate())
            this.onSubmit.emit({});
    };
    FormComponent.prototype.Clear = function () {
        this.onClear.emit({});
    };
    FormComponent.prototype.Cancel = function () {
        this.onCancel.emit({});
    };
    FormComponent.prototype.ShowSettings = function () {
    };
    Object.defineProperty(FormComponent.prototype, "ButtonClass", {
        get: function () {
            if (this.ButtonHorizontalAlignment == HorizontalAlignment.Right)
                return "form-button-right";
        },
        enumerable: true,
        configurable: true
    });
    __decorate([
        Output(),
        __metadata("design:type", Object)
    ], FormComponent.prototype, "onSubmit", void 0);
    __decorate([
        Output(),
        __metadata("design:type", Object)
    ], FormComponent.prototype, "onClear", void 0);
    __decorate([
        Output(),
        __metadata("design:type", Object)
    ], FormComponent.prototype, "onCancel", void 0);
    __decorate([
        Input(),
        __metadata("design:type", BaseRequest)
    ], FormComponent.prototype, "Request", void 0);
    __decorate([
        Input(),
        __metadata("design:type", TemplateRef)
    ], FormComponent.prototype, "ButtonTemplate", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], FormComponent.prototype, "Header", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], FormComponent.prototype, "ActivityTypes", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], FormComponent.prototype, "IsBusy", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], FormComponent.prototype, "CanClear", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], FormComponent.prototype, "ButtonClearLabel", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], FormComponent.prototype, "CanCancel", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], FormComponent.prototype, "ButtonCancelLabel", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], FormComponent.prototype, "ButtonLabel", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], FormComponent.prototype, "ButtonHorizontalAlignment", void 0);
    FormComponent = __decorate([
        Component({
            selector: 'pm-form',
            //templateUrl: './app/controls/components/form/form.html'
            templateUrl: './form.html'
        })
    ], FormComponent);
    return FormComponent;
}());
export { FormComponent };
