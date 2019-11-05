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
var ToastComponent = /** @class */ (function () {
    function ToastComponent() {
        this.OnClosed = new EventEmitter();
        this.Bottom = "20px";
        this.Left = "20px";
        this.Position = "absolute";
    }
    ToastComponent.prototype.Show = function () {
        this.ShowToast = true;
    };
    ToastComponent.prototype.Close = function (result) {
        this.OnClosed.emit(result);
        this.ShowToast = false;
    };
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], ToastComponent.prototype, "ShowToast", void 0);
    __decorate([
        Output(),
        __metadata("design:type", EventEmitter)
    ], ToastComponent.prototype, "OnClosed", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], ToastComponent.prototype, "Bottom", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], ToastComponent.prototype, "Left", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], ToastComponent.prototype, "Position", void 0);
    ToastComponent = __decorate([
        Component({
            selector: 'pm-toast',
            //templateUrl: './app/controls/components/toast/toast.html',
            templateUrl: './toast.html',
            styles: ["\n  :host {   \n    position: relative;\n  }\n"]
        })
    ], ToastComponent);
    return ToastComponent;
}());
export { ToastComponent };
