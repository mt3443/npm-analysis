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
import { Component, ChangeDetectorRef, Input, } from '@angular/core';
import { Toast } from '../../../controls/components/toast/toast';
var ErrorToast = /** @class */ (function (_super) {
    __extends(ErrorToast, _super);
    function ErrorToast(changeDetectorRef) {
        var _this = _super.call(this) || this;
        _this.changeDetectorRef = changeDetectorRef;
        return _this;
    }
    ErrorToast.prototype.CopyToClipBoard = function (e) {
        var t = document.createElement("textarea");
        t.style.position = 'fixed';
        t.style.top = '0';
        t.style.left = '0';
        t.style.opacity = '0';
        t.value = this.Name + "\n" + this.Message + "\n" + this.Stack;
        document.body.appendChild(t);
        t.select();
        try {
            document.execCommand('copy');
        }
        catch (_a) { }
        document.body.removeChild(t);
    };
    ErrorToast.prototype.RaiseChange = function () {
        this.changeDetectorRef.detectChanges();
    };
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], ErrorToast.prototype, "Name", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], ErrorToast.prototype, "Message", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], ErrorToast.prototype, "Stack", void 0);
    ErrorToast = __decorate([
        Component({
            //templateUrl: './app/controls/services/logging/error-toast.html',
            templateUrl: './error-toast.html',
            styles: ["\n    :host {\n      pointer-events: none;\n      position: absolute;\n      height: 100%;\n      width: 100%;\n      top: 0px;\n      z-index: 1000;\n    }\n  "]
        }),
        __metadata("design:paramtypes", [ChangeDetectorRef])
    ], ErrorToast);
    return ErrorToast;
}(Toast));
export { ErrorToast };
