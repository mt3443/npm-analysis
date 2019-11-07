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
import { ErrorHandler, Injectable } from '@angular/core';
import { ErrorToast } from '../../../controls/services/logging/error-toast';
import { ControlsModule } from '../../../controls/controls-module';
var GlobalErrorHandler = /** @class */ (function (_super) {
    __extends(GlobalErrorHandler, _super);
    function GlobalErrorHandler() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    GlobalErrorHandler.prototype.handleError = function (error) {
        var errorToast = ControlsModule.toast.Show(ErrorToast);
        if (!errorToast) {
            console.log(error);
            return;
        }
        var item = error;
        if (error instanceof Error) {
            errorToast.Name = item.name;
            errorToast.Message = item.message;
            errorToast.Stack = item.stack;
        }
        else {
            errorToast.Name = error;
        }
        errorToast.RaiseChange();
        _super.prototype.handleError.call(this, error);
    };
    GlobalErrorHandler = __decorate([
        Injectable()
    ], GlobalErrorHandler);
    return GlobalErrorHandler;
}(ErrorHandler));
export { GlobalErrorHandler };
